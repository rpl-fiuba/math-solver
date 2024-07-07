from mathlearning.model.problem_type import ProblemType
from mathlearning.services.generate_service import GenerateService
from mathlearning.utils.logger import Logger
from rest_framework.request import Request

from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

generate_service = GenerateService()
logger = Logger.getLogger()


@api_view(['POST'])
def generate_problem(request: Request):
    if request.method == 'POST':
        logger.info('Received the following request: {}'.format(request.body))
        body = json.loads(request.body)
        generated_problem_expression = generate_service.generate_problem_input(ProblemType(body["type"]))
        logger.info('Returning the following response: {}'.format(generated_problem_expression))
        response_data = {'problemInput': generated_problem_expression}
        return Response(response_data, status=status.HTTP_200_OK, content_type='application/json')


generate_paths = [path('problems/generate', generate_problem)]

