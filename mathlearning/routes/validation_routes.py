from mathlearning.mappers.validate_mapper import ValidateMapper, ValidateMapperException
from mathlearning.model.problem_type import ProblemType
from mathlearning.services.step_service import StepService
from mathlearning.services.evaluate_service import EvaluateService
from mathlearning.utils.logger import Logger
from mathlearning.utils.request_decorators import log_request
from mathlearning.model.expression import Expression
from rest_framework.request import Request

from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import SuspiciousOperation
import json

evaluate_service = EvaluateService()
step_service = StepService()
logger = Logger.getLogger()
validateMapper = ValidateMapper()


def bool_to_str(boolean_value: bool) -> str:
    return "true" if boolean_value else "false"


@api_view(['POST'])
def validate_new_step(request: Request):
    if request.method == 'POST':
        body = json.loads(request.body)
        (new_expression, old_expression, theorems) = validateMapper.parse_validate_new_step_input(body)
        result = step_service.is_a_valid_next_step(old_expression, new_expression, theorems)
        logger.info('Returning the following response: {}'.format(result))
        return Response(bool_to_str(result), status=status.HTTP_200_OK)


@api_view(['POST'])
def validate_not_in_history(request: Request):
    if request.method == 'POST':
        body = json.loads(request.body)
        (expr, history) = validateMapper.parse_validate_not_in_history_input(body)
        result = step_service.validate_not_in_history(expr, history)
        logger.info('Returning the following response: {}'.format(result))
        return Response(bool_to_str(result), status=status.HTTP_200_OK)

@api_view(['POST'])
def evaluate(request: Request):
    if request.method == 'POST':
        body = json.loads(request.body)
        (problem_input, problem_type) = validateMapper.parse_evaluate(body)
        try:
            if problem_type == ProblemType.TRIGONOMETRY.value:
                expression = Expression.build_area_expression(problem_input)
            else:
                expression = Expression(problem_input['expression'], problem_input['variables'])
            result = evaluate_service.evaluate_problem_input(expression, problem_type)
            data = { 'result': {'expression': result, 'variables': []}}

            logger.info('Returning the following response: {}'.format(result))
            return Response(data, status=status.HTTP_200_OK)

        except SuspiciousOperation as e:
            data = { 'message': str(e) }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

validation_paths = [
    path('validations/not-in-history', validate_not_in_history),
    path('validations/new-step', validate_new_step),
    path('validations/evaluate', evaluate),
]
