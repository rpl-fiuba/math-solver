from rest_framework.test import APITestCase

from mathlearning.model.problem_type import ProblemType
from test.testutils.test_utils import run_entire_test_list


class APITests(APITestCase):
    expressions = [
        {
            'problem_input': {'expression': '\\frac{(3x+12)}{(x^2-3x)}\\cdot\\frac{(x-3)^2}{(x^3-16x)}', 'variables': []},
            'problem_output': '3*(x - 3)/(x**2*(x - 4))'
        },
        {
            'problem_input': {'expression': 'x^2-1', 'variables': []},
            'problem_output': '(x - 1)*(x + 1)'
        },
        {
            'problem_input': {'expression': 'x^2+2x+1', 'variables': []},
            'problem_output': '(x + 1)**2'
        }
    ]

    def test_evaluate_expressions(self):
        run_entire_test_list(self, test_list=self.expressions, exercise_type=ProblemType.FACTORISABLE.value)

