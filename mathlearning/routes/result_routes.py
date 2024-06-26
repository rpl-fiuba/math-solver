from sympy import S
from sympy.calculus.util import continuous_domain

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.mappers.theorem_mapper import TheoremMapper
from mathlearning.mappers.validate_mapper import ValidateMapper
from mathlearning.model.expression_variable import ExpressionVariable
from mathlearning.model.problem_type import ProblemType
from mathlearning.services.result_service import ResultService
from mathlearning.utils.logger import Logger
from mathlearning.model.expression import Expression
from rest_framework.request import Request

from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

result_service = ResultService()
logger = Logger.getLogger()
validateMapper = ValidateMapper()
theoremMapper = TheoremMapper()
solutionTreeMapper = SolutionTreeMapper()


@api_view(['POST'])
def solve_derivative(request: Request):
    if request.method == 'POST':
        body = json.loads(request.body)
        expression = Expression(body['expression'])
        result = result_service.get_derivative_result(expression)
        logger.info('Returning the following response: {}'.format(result))
        return Response(result.to_latex(), status=status.HTTP_200_OK)


@api_view(['POST'])
def calculate_solution_tree(request: Request):
    if request.method == 'POST':
        body = json.loads(request.body)
        type = body['type']
        if type == ProblemType.TRIGONOMETRY.value:
            expression = Expression.build_area_expression(body['problem_input'])
        else:
            expression = Expression(body['problem_input']['expression'], body['problem_input']['variables'])
        result = result_service.solution_tree(expression, type)
        logger.info(f'tree')
        logger.info(f'{result.print_tree()}')
        result = result.to_json()
        logger.info('Returning the following response: {}'.format(result))

        return Response(json.dumps(result), status=status.HTTP_200_OK, content_type='application/json')


@api_view(['POST'])
def resolve(request: Request):
    if request.method == 'POST':
        logger.info('Received the following request: {}'.format(request.body))
        body = json.loads(request.body)
        problem_type = ProblemType(body["type"])
        expression_unparsed = body['current_expression']['expression']
        if problem_type == ProblemType.TRIGONOMETRY:
            problem_input = Expression("0")
            expression_unparsed = float(expression_unparsed)
        else:
            problem_input = Expression(body['problem_input']['expression'], body['problem_input']['variables'])
        solution_tree = solutionTreeMapper.parse(body['math_tree'])

        step_list = []
        for step in body['step_list']:
            # TODO: I will find a more more pythonable to do that
            step_expr = step['expression']
            variables = step['variables']
            step_vars = list(map(lambda variable:
                                 ExpressionVariable(
                                     variable['tag'],
                                     Expression(
                                         variable['expression']['expression']
                                     )
                                 ),
                                 variables if variables is not None else []))

            step_list.append(Expression(step_expr, step_vars))

        # Current expression
        body_variables = body['current_expression']['variables']
        variables = list(map(lambda variable: ExpressionVariable(variable['tag'],
                                                                 Expression(variable['expression']['expression'])),
                             body_variables if body_variables is not None else []))
        current_expression = Expression(expression_unparsed, variables)
        (result, hints) = result_service.resolve(problem_input, solution_tree, step_list, current_expression, problem_type)
        logger.info('Returning the following response: {} {}'.format(result, json.dumps(hints)))
        response_data = {
            'exerciseStatus': result,
            'hints': hints
        }
        return Response(response_data, status=status.HTTP_200_OK, content_type='application/json')


@api_view(['GET'])
def ping(request: Request):
    if request.method == 'GET':
        return Response("{\"status\": OK}", status=status.HTTP_200_OK, content_type='application/json')


result_paths = [path('results/solve-derivative', solve_derivative)]
result_paths += [path('results/solution-tree', calculate_solution_tree)]
result_paths += [path('resolve', resolve)]
result_paths += [path('ping', ping)]
result_paths += [path('', ping)]

