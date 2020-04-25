const fs = require('fs');
const path = require('path');
const fetch = require('node-fetch');

const mathSolverBasePath = 'http://localhost:5000';

const functions = {
  x: {
    'func': 'a1*x^{b1}',
    'deriv': 'a1*b1*x^{b1-1}'
  },
  cosx: {
    'func': 'a1*\\cos(x)',
    'deriv': '-a1*\\sin{\\left(x \\right)}'
  },
  senx: {
    'func': 'a1*\\sin(x)',
    'deriv': 'a1*\\cos{\\left(x \\right)}'
  },
  tagx: {
    'func': 'a1*\\tan(x)',
    'deriv': 'a1*\\frac{1}{{\\cos(x)}^2}'
  },
  sqrt: {
    'func': 'a1*\\sqrt[b1]{x}',
    'deriv': 'a1*\\frac{1}{b1} * x^{\\frac{1}{b1}-1}'
  },
  // expx: {
  //   'func': 'a1*\\exp(x)',
  //   'deriv': 'a1*\\exp(x)'
  // }
}


const possible_theorems = {
  'f+g': {
    text: 'f+g',
    input: '\\frac{d(f1+g1)}{dx}',
    steps: [
      { expression: '\\frac{d(f1)}{dx} + dg1', status: 'valid' },
      { expression: 'df1 + dg1', status: 'resolved' },
      { expression: 'dg1 + df1', status: 'resolved' },

      { expression: 'df1 - dg1', status: 'invalid' },
      { expression: '\\frac{d(f1)}{dx} + 2*dg1', status: 'invalid' },
      { expression: 'dg1', status: 'invalid' },
      { expression: 'df1', status: 'invalid' },
    ]
  },
  'f-g': {
    text: 'f1-g1',
    input: '\\frac{d(f1-g1)}{dx}',
    steps: [
      { expression: '\\frac{d(f1)}{dx} - dg1', status: 'valid' },
      { expression: 'df1 - dg1', status: 'resolved' },
      { expression: '-dg1 + df1', status: 'resolved' },

      { expression: 'df1 + dg1', status: 'invalid' },
      { expression: '\\frac{d(f1)}{dx} - 2*dg1', status: 'invalid' },
      { expression: 'dg1', status: 'invalid' },
      { expression: 'df1', status: 'invalid' },
    ]
  },
  'f*g': {
    text: 'f*g',
    input: '\\frac{d(f1*g1)}{dx}',
    steps: [
      { expression: '\\frac{d(f1)}{dx}*g1 + f1*\\frac{d(g1)}{dx}', status: 'valid' },
      { expression: 'df1*g1 + f1*\\frac{d(g1)}{dx}', status: 'valid' },
      { expression: '\\frac{d(f1)}{dx}*g1 + f1*dg1', status: 'valid' },
      { expression: 'df1*g1 + f1*dg1', status: 'resolved' },
      { expression: 'f1*dg1 + df1*g1', status: 'resolved' },

      { expression: 'df1*g1 - f1*\\frac{d(g1)}{dx}', status: 'invalid' },
      { expression: 'df1*g1', status: 'invalid' },
      { expression: 'f1*dg1', status: 'invalid' },   
    ]
  },
  'f/g': {
    text: 'f1/g1',
    input: '\\frac{d(\\frac{f1}{g1})}{dx}',
    steps: [
      { expression: '\\frac{\\frac{d(f1)}{dx}*g1 - f1*\\frac{d(g1)}{dx}}{{g1}^{2}}', status: 'valid' },
      { expression: '\\frac{df1*g1 - f1*\\frac{d(g1)}{dx}}{{g1}^{2}}', status: 'valid' },
      { expression: '\\frac{\\frac{d(f1)}{dx}*g1 - f1*dg1}{{g1}^{2}}', status: 'valid' },
      { expression: '\\frac{df1*g1 - f1*dg1}{{g1}^{2}}', status: 'resolved' },

      { expression: '\\frac{df1*g1 + f1*dg1}{{g1}^{2}}', status: 'invalid' },
      { expression: 'df1*g1 - f1*\\frac{d(g1)}{dx}', status: 'invalid' },
      { expression: '2*\\frac{df1*g1 - f1*dg1}{g1^{2}}', status: 'invalid' },   
    ]
  }
}

const executeExpression = async (theoreme, functions, stepCount) => {
  const { input, steps } = theoreme;

  // making problem input
  const problem_input = replaceFunctions(input, functions);
  console.log('problem_input to analyze:', problem_input);

  // making problem steps
  const problem_steps = steps.map((step) => ({ ...step, expression: replaceFunctions(step.expression, functions) }));

  // getting problem theorems
  const theorems = JSON.parse(fs.readFileSync(path.resolve(__dirname, './derivative-theorems.json')));

  // generating math tree
  const math_tree = await generateMathTree({ problem_input, theorems, type: 'derivative' });

  // testing each step
  for (let pos = 0; pos < problem_steps.length; pos += 1) {
    const current_expression = problem_steps[pos].expression;
    const expected_status = problem_steps[pos].status;
    const step_list = problem_steps.slice(0, pos).filter((ps) => ['valid', 'resolved'].includes(ps.status)).map((ps) => ps.expression);

    // Hitting math solver
    const result = await testStep({ problem_input, math_tree, theorems, current_expression, step_list, type: 'derivative' });

    if (result.exerciseStatus !== expected_status) {
      failedCount += 1;
      console.log(`\x1b[31m[FAIL] ${current_expression}. Result: ${result.exerciseStatus} !== ${expected_status}`);
    } else {
      successCount += 1;
      console.log(`\x1b[32m[OK] ${current_expression}. Result: ${expected_status}`);
    }
  }
  console.log('\x1b[0m');
}

const testStep = async ({ problem_input, math_tree, theorems, current_expression, step_list, type }) => {
  const fullPath = `${mathSolverBasePath}/resolve`;

  const response = await fetch(fullPath, {
    method: 'post',
    body: JSON.stringify({
      type,
      problem_input,
      step_list: JSON.stringify(step_list),
      math_tree,
      theorems,
      current_expression
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  });


  return response.json();
}

const generateMathTree = async ({ problem_input, theorems, type = 'derivative' }) => {
  const fullPath = `${mathSolverBasePath}/results/solution-tree`;

  const response = await fetch(fullPath, {
    method: 'post',
    body: JSON.stringify({ problem_input, type, theorems }),
    headers: {
      'Content-Type': 'application/json'
    }
  });

  return response.json();
}

const replaceFunctions = (expression, functions) => {
  let finalExpression = expression;
  functions.forEach((func) => {
    const regex = new RegExp(func.source, 'g');
    finalExpression = finalExpression.replace(regex, func.target);
  });
  
  return finalExpression;
}

const makeFunctionsToExecute = (f, g, a = 1, b = 1) => {
  const variableA = new RegExp('a1', 'g');
  const variableB = new RegExp('b1', 'g');

  const dfTarget = f['deriv'].replace(variableA, a).replace(variableB, b);
  const dgTarget = g['deriv'].replace(variableA, a).replace(variableB, b);
  const fTarget = f['func'].replace(variableA, a).replace(variableB, b);
  const gTarget = g['func'].replace(variableA, a).replace(variableB, b);


  return [
    { source: 'df1', target: dfTarget },
    { source: 'dg1', target: dgTarget },
    { source: 'f1', target:  fTarget  },
    { source: 'g1', target:  gTarget  },
  ];
}


// Executing the tests
let successCount = 0;
let failedCount = 0;

const theoremesToTest = [
  'f+g',
  'f-g',
  'f*g',
  'f/g'
];
const functionsToTest = [
  'x',
  'cosx',
  'senx',
  'tagx',
  'sqrt'
];

const execute = async () => {
  const a = 2;
  const b = 3;

  for (theoreme of theoremesToTest) {
    console.log(`Executing tests for theoreme: ${theoreme} \n`);

    for (const keyf of functionsToTest) {
      for (const keyg of functionsToTest) {
        const f = functions[keyf];
        const g = functions[keyg];
    
        console.log(`F: ${f.func}`);
        console.log(`G: ${g.func}`);
    
        const functionsToExecute = makeFunctionsToExecute(f, g, a, b);
        await executeExpression(possible_theorems[theoreme], functionsToExecute);
      }
    }
  }

  console.log('Success:', successCount);
  console.log('Failed:', failedCount);
}

execute();
