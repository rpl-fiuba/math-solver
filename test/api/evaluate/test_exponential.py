from rest_framework.test import APITestCase

from mathlearning.model.problem_type import ProblemType
from test.testutils.test_utils import run_entire_test_list


class APITests(APITestCase):
    expressions = [
        {
            'problem_input': {'expression': '\\exp\\left(x^2 + 4x + 4\\right) = 1', 'variables': []},
            'problem_output': 'x=-2'
        },
        {
            'problem_input': {'expression': '\\ln\\left(x^2 + 4x + 4\\right) = 0', 'variables': []},
            'problem_output': 'x=-1 \\vee x=-3'
        }
    ]

    def test_evaluate_expressions(self):
        run_entire_test_list(self, test_list=self.expressions, exercise_type=ProblemType.EXPONENTIAL.value)

