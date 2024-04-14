import json
from rest_framework import status
from rest_framework.test import APITestCase

from mathlearning.model.problem_type import ProblemType
from test.testutils.test_utils import run_entire_test_list


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
        run_entire_test_list(self, test_list=self.simple_images, exercise_type=ProblemType.IMAGE.value)

