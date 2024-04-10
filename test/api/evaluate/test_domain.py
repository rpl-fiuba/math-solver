import json
from rest_framework import status
from rest_framework.test import APITestCase


class APITests(APITestCase):

    rational_domains = [
        {
            'problem_input': {'expression': 'x', 'variables': []},
            'problem_output': '\mathbb{R}'
        },
        {
            'problem_input': {'expression': '1/x', 'variables': []},
            'problem_output': '\\left(-\\infty, 0\\right) \\cup \\left(0, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '1/(x-2)', 'variables': []},
            'problem_output': '\\left(-\\infty, 2\\right) \\cup \\left(2, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '1/(x^2)', 'variables': []},
            'problem_output': '\\left(-\\infty, 0\\right) \\cup \\left(0, \\infty\\right)'
        }
    ]

    def test_evaluate_rational_domains(self):
        for exercise in self.rational_domains:
            data = {
                'problem_input': exercise['problem_input'],
                'type': 'domain'
            }

            response = self.client.post(path='/validations/evaluate', data=data, format='json')

            body = json.loads(response.content)
            self.assertEquals(response.status_code, status.HTTP_200_OK)
            self.assertEquals(body['result']['expression'], exercise['problem_output'])

