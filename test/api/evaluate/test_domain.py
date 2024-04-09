import json
from rest_framework import status
from rest_framework.test import APITestCase


class APITests(APITestCase):

    def test_evaluate_domain_zeroed_root(self):
        data = {
            'problem_input': {'expression': '1/x', 'variables': []},
            'type': 'domain'
        }

        response = self.client.post(path='/validations/evaluate', data=data, format='json')

        body = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(body['result']['expression'], '\\left(-\\infty, 0\\right) \\cup \\left(0, \\infty\\right)')

    def test_evaluate_domain_real_root(self):
        data = {
            'problem_input': {'expression': '1/(x-2)', 'variables': []},
            'type': 'domain'
        }

        response = self.client.post(path='/validations/evaluate', data=data, format='json')

        body = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(body['result']['expression'], '\\left(-\\infty, 2\\right) \\cup \\left(2, \\infty\\right)')

    def test_evaluate_domain_double_zeroed_root(self):
        data = {
            'problem_input': {'expression': '1/(x^2)', 'variables': []},
            'type': 'domain'
        }

        response = self.client.post(path='/validations/evaluate', data=data, format='json')

        body = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(body['result']['expression'], '\\left(-\\infty, 0\\right) \\cup \\left(0, \\infty\\right)')

    def test_evaluate_domain_no_root(self):
        data = {
            'problem_input': {'expression': 'x', 'variables': []},
            'type': 'domain'
        }

        response = self.client.post(path='/validations/evaluate', data=data, format='json')

        body = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(body['result']['expression'], '\mathbb{R}')
