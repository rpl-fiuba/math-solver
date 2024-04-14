import json
from rest_framework import status
from rest_framework.test import APITestCase


class APITests(APITestCase):

    simple_images = [
        {
            'problem_input': {'expression': 'x', 'variables': []},
            'problem_output': '\mathbb{R}'
        },
        {
            'problem_input': {'expression': 'x^2', 'variables': []},
            'problem_output': '\\left[0, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '3+x^2', 'variables': []},
            'problem_output': '\\left[3, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '-x^2', 'variables': []},
            'problem_output': '\\left(-\\infty, 0\\right]'
        },
        {
            'problem_input': {'expression': '5-x^2', 'variables': []},
            'problem_output': '\\left(-\\infty, 5\\right]'
        }
    ]

    def test_evaluate_simple_images(self):
        for exercise in self.simple_images:
            data = {
                'problem_input': exercise['problem_input'],
                'type': 'image'
            }

            response = self.client.post(path='/validations/evaluate', data=data, format='json')

            body = json.loads(response.content)
            self.assertEquals(response.status_code, status.HTTP_200_OK)
            self.assertEquals(body['result']['expression'], exercise['problem_output'])

