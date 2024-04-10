from mathlearning.model.expression import Expression
from mathlearning.model.expression_variable import ExpressionVariable
from test.testutils.solved_exercise import SolvedExercise


class IntegralExercises:

    @staticmethod
    def integral_add_x_cosx() -> SolvedExercise:
        name = "sum of two integrals"

        steps = [
            {'expression': '\\int x + \\cos(x) dx', 'variables': []},
            {'expression': '(\\int x dx) + (\\int \\cos(x) dx)', 'variables': []},
            {'expression': 'x^2 / 2 + \\int (\\cos(x)) dx', 'variables': []},
            {'expression': 'x^2 / 2 + \\sin(x)', 'variables': []}
        ]

        result = {'expression': 'x^2 / 2 + sin(x)', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [
            {'expression': 'Integral(x+ cos(x),x)', 'variables': []},
            {'expression': 'Integral(x,x) + Integral(cos(x),x)', 'variables': []},
            {'expression': 'x**2 / 2 + Integral(cos(x),x)', 'variables': []},
            {'expression': 'x**2 / 2 + sin(x)', 'variables': []}
        ]

        result_non_latex = {'expression': 'x**2 / 2 + sin(x)', 'variables': []}
        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    @staticmethod
    def integral_add_x_x2() -> SolvedExercise:
        name = "sum of two integrals"

        steps = [
            {'expression': '\\int x + x^2 dx', 'variables': []},
            {'expression': '(\\int x dx) + (\\int x^2 dx)', 'variables': []},
            {'expression': 'x^2 / 2 + \\int x^2 dx', 'variables': []},
            {'expression': 'x^2 / 2 + x^3/3', 'variables': []}
        ]

        result = {'expression': 'x^2 / 2 + x^3/3', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [
        ]

        result_non_latex = ''
        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    @staticmethod
    def integral_substitution_division_of_polynomials():
        #   TODO check if the steps are the correct ones
        name = "substitution"

        steps = [
            {'expression': '\\int ( x^2 / (\\sqrt[3]{1+2x}) ) dx', 'variables': []}, # 1+2x = u^3 => x = ( u^3 - 1 ) / 2 ; 2dx = 3u^2 du dx = (3u^2 du)/2

            {'expression': '\\int ( \\frac{ (( u^3 - 1 ) / 2)^2}{u} * (3*u^2)/2 ) du', 'variables': [
                {'tag': 'u', 'expression': {'expression': '\\sqrt[3]{1+2x}', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2/(3*(2*x + 1)^(2/3))', 'variables': []}}
            ]},
            {'expression': '(3/2) * \\int ( (u^6-2u^3+1)/4 *u ) du', 'variables': [
                {'tag': 'u', 'expression': {'expression': '\\sqrt[3]{1+2x}', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2/(3*(2*x + 1)^(2/3))', 'variables': []}}
            ]},
            {'expression': '3/8 * (\\int (u^7 - 2u^4 + u) du)', 'variables': [
                {'tag': 'u', 'expression': {'expression': '\\sqrt[3]{1+2x}', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2/(3*(2*x + 1)^(2/3))', 'variables': []}}
            ]},
            {'expression': '3/8 * (\\int (u^7) du - \\int( 2u^4 + u) du)', 'variables': [
                {'tag': 'u', 'expression': {'expression': '\\sqrt[3]{1+2x}', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2/(3*(2*x + 1)^(2/3))', 'variables': []}}
            ]},
            {'expression': '3/8 * (\\int (u^7) du - \\int( 2u^4) du + \\int (u) du)', 'variables': [
                {'tag': 'u', 'expression': {'expression': '\\sqrt[3]{1+2x}', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2/(3*(2*x + 1)^(2/3))', 'variables': []}}
            ]},
            {'expression': '3/8 * (\\int (u^7) du - \\int( 2u^4) du + u^2/2)', 'variables': [
                {'tag': 'u', 'expression': {'expression': '\\sqrt[3]{1+2x}', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2/(3*(2*x + 1)^(2/3))', 'variables': []}}
            ]},
            {'expression': '3/8 * (\\int (u^7) du - 2u^5/5 + u^2/2)', 'variables': [
                {'tag': 'u', 'expression': {'expression': '\\sqrt[3]{1+2x}', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2/(3*(2*x + 1)^(2/3))', 'variables': []}}
            ]},
            {'expression': '3/8 * (u^8/8 - 2u^5/5 + u^2/2)', 'variables': [
                {'tag': 'u', 'expression': {'expression': '\\sqrt[3]{1+2x}', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2/(3*(2*x + 1)^(2/3))', 'variables': []}}
            ]},

            {'expression': '3/8 * ((\\sqrt[3]{1 +2x})^8/8 - 2(\\sqrt[3]{1 +2x})^5/5 + (\\sqrt[3]{1 +2x})^2/2)', 'variables': []},
            {'expression': '3/64 * (\\sqrt[3]{1 +2x})^8 - 6/40 * (\\sqrt[3]{1 +2x})^5 + 3/16 *(\\sqrt[3]{1 +2x})^2', 'variables': []},
            {'expression': '3/64 * (\\sqrt[3]{1 +2x})^8 - 3/20 * (\\sqrt[3]{1 +2x})^5 + 3/16 *(\\sqrt[3]{1 +2x})^2', 'variables': []}
        ]

        result = {'expression': '3/64 * (\\sqrt[3]{1 +2x})^8 - 3/20 * (\\sqrt[3]{1 +2x})^5 + 3/16 *(\\sqrt[3]{1 +2x})^2', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [

        ]

        result_non_latex = ''
        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    @staticmethod
    def integral_substitution_sin_with_polynomials() -> SolvedExercise:
        # TODO check why the result is different
        name = "sin with polynomials"

        steps = [
            {'expression': '\\int(\\sin(3*x + 5))dx', 'variables': []},# u = 3x+5 du=3dx
            {'expression': '1/3 * \\int(\\sin(u)) * du', 'variables': [
                ExpressionVariable('u', Expression('3x+5')).to_json(),
                ExpressionVariable('du', Expression('3')).to_json()
            ]},
            {'expression': '- 1/3 * \\cos(u)', 'variables': [
                ExpressionVariable('u', Expression('3x+5')).to_json(),
                ExpressionVariable('du', Expression('3')).to_json()
            ]},
            {'expression': '- 1/3 * \\cos(3x+5)', 'variables': []}
        ]

        result = {'expression': '- 1/3 * \\cos(3x+5)', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [
        ]

        result_non_latex = ''
        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    @staticmethod
    def integral_substitution_multiplication() -> SolvedExercise:
        name = "substitution multiplication"

        steps = [
            {'expression': '\\int(2 * x \\sqrt[2]{1+x^2}) dx', 'variables': []},  # u = 1+x^2 du=2x dx
            {'expression': '\\int(\\sqrt[2]{u}) du', 'variables': [
                {'tag': 'u', 'expression': {'expression': '1+x^2', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2x', 'variables': []}}
            ]},
            {'expression': '2/3 * u^{3/2}', 'variables': [
                {'tag': 'u', 'expression': {'expression': '1+x^2', 'variables': []}},
                {'tag': 'du', 'expression': {'expression': '2x', 'variables': []}}
            ]},
            {'expression': '2/3 * (1+x^2)^{3/2}', 'variables': []}
        ]

        result = {'expression': '2/3 * (1+x^2)^{3/2}', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [
        ]

        result_non_latex = ''
        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    @staticmethod
    def integral_parts_mult_x_cosx():
        name = "parts rule mult cosx and x"

        # TODO: check again the steps
        steps = [
            {'expression': '\\int (x * \\cos(x)) dx', 'variables': []},
            {'expression': '\\int u(x)*\\frac{d(v(x))}{dx}',
             'variables': [
                 { 'tag': 'u(x)', 'expression': { 'expression': 'x' } },
                 {'tag': 'v(x)', 'expression': {'expression': '\\sin(x)'} }
             ]
             },
            {'expression': 'u(x) * v(x) - \\int (\\frac{d(u(x))}{dx} * v(x)) dx',
             'variables': [
                 {'tag': 'u(x)', 'expression': {'expression': 'x'}},
                 {'tag': 'v(x)', 'expression': {'expression': '\\sin(x)'}}
             ]
             },
            {'expression': 'x * \\sin(x) - \\int (\\frac{d(x)}{dx} * \\sin(x)) dx', 'variables': []},
            {'expression': 'x * \\sin(x) - \\int (1 * \\sin(x)) dx', 'variables': []},
            {'expression': 'x * \\sin(x) - \\int (\\sin(x)) dx', 'variables': []},
            {'expression': 'x*\\sin(x) + \\cos(x)', 'variables': []}
        ]

        result = {'expression': 'x*\\sin(x) + \\cos(x)', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [

        ]

        result_non_latex = ''
        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    # https://www.intmath.com/methods-integration/7-integration-by-parts.php
    @staticmethod
    def integral_parts_example_one():
        name = "parts example one"

        steps = [
            {'expression': '\\int( x * \\sin(2*x)) dx', 'variables': []},  # u = x  dv = sin(2x) dx ; v -cos(2x)/2
            {'expression': '\\int (u(x) * \\frac{d(v(x))}{dx}) dx', 'variables': [
                {'tag': 'u(x)', 'expression': {'expression': 'x'}},
                {'tag': 'v(x)', 'expression': {'expression': '-\\cos(2x)/2'}}
            ]},
            {'expression': 'u(x) * v(x) - \\int (\\frac{d(u(x))}{dx} * v(x)) dx', 'variables': [
                {'tag': 'u(x)', 'expression': {'expression': 'x'}},
                {'tag': 'v(x)', 'expression': {'expression': '-\\cos(2x)/2'}}
            ]},
            {'expression': 'x * (- \\cos(2x)/2) - \\int (\\frac{d(x)}{dx} * (-\\cos(2x)/2) ) dx', 'variables': []},
            {'expression': 'x * (- \\cos(2x)/2) - \\int ( 1 * (-\\cos(2x)/2) ) dx', 'variables': []},
            {'expression': 'x * (- \\cos(2x)/2) - \\int ((-\\cos(2x)/2) ) dx', 'variables': []},
            {'expression': 'x * (- \\cos(2x)/2) + 1/2 * \\int (\\cos(2x) ) dx', 'variables': []},
            {'expression': 'x * (- \\cos(2x)/2) + 1/2 * \\sin(2x)/2', 'variables': []}
        ]

        result = {'expression': 'x * (- \\cos(2x)/2) + 1/2 * \\sin(2x)/2', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [
        ]

        result_non_latex = ''
        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    @staticmethod
    def integral_parts_example_two():
        name = "parts example two"

        steps = [
            {'expression': '\\int ( x * \\sqrt[2]{x+1} ) dx', 'variables': []},
            {'expression': '\\int (u(x) * \\frac{d(v(x))}{dx}) dx', 'variables': [
                {'tag': 'u(x)', 'expression': {'expression': 'x'}},
                {'tag': 'v(x)', 'expression': {'expression': '(2/3 * (x+1)^{3/2})'}}
            ]},  # TODO think if this step should be included
            {'expression': 'u(x) * v(x) - \\int (\\frac{d(u(x))}{dx} * v(x)) dx', 'variables': [
                {'tag': 'u(x)', 'expression': {'expression': 'x'}},
                {'tag': 'v(x)', 'expression': {'expression': '(2/3 * (x+1)^{3/2})'}}
            ]},
            {'expression': 'x * (2/3 * (x+1)^{3/2}) - \\int (2/3 * (x+1)^{3/2}) dx', 'variables': []},
            {'expression': 'x * (2/3 * (x+1)^{3/2}) - 2/3 * \\int ((x+1)^{3/2}) dx', 'variables': []},
            # {'expression': 'x * (2/3 * (x+1)^{3/2}) - 2/3 * 2/5 * (x+1)^{5/2}', 'variables': []},
            {'expression': 'x * (2/3 * (x+1)^{3/2}) - 4/15 * (x+1)^{5/2}', 'variables': []}
        ]

        result = {'expression': 'x * (2/3 * (x+1)^{3/2}) - 4/15 * (x+1)^{5/2}', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [
        ]

        result_non_latex = ''
        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    @staticmethod
    def integral_parts_example_six():
        name = "parts example six"

        steps = [
            {'expression': '\\int (\\ln(x)) dx', 'variables': []},
            {'expression': '\\int (u(x) * \\frac{d(v(x))}{dx}) dx', 'variables': [
                {'tag': 'u(x)', 'expression': {'expression': '\\ln(x)'}},
                {'tag': 'v(x)', 'expression': {'expression': 'x'}}
            ]},  # TODO think if this step should be included
            {'expression': 'u(x) * v(x) - \\int (\\frac{d(u(x))}{dx} * v(x)) dx', 'variables': [
                {'tag': 'u(x)', 'expression': {'expression': '\\ln(x)'}},
                {'tag': 'v(x)', 'expression': {'expression': 'x'}}
            ]},
            {'expression': '\\ln(x) * x - \\int (\\frac{d(\\ln(x))}{dx} * x ) dx', 'variables': []},
            # {'expression': '\\ln(x) * x - \\int (\\frac{1}{x} * x ) dx', 'variables': []},
            {'expression': '\\ln(x) * x - \\int (1) dx', 'variables': []},
            {'expression': '\\ln(x) * x - x', 'variables': []}
        ]

        result = {'expression': '\\ln(x) * x - x', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [
        ]

        result_non_latex = ''
        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)
