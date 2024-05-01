from rest_framework.test import APITestCase

from mathlearning.model.problem_type import ProblemType
from test.testutils.test_utils import run_entire_test_list


class APITests(APITestCase):
    expressions = [
        {
            'problem_input': {'expression': '\\frac{(3x+12)}{(x^2-3x)}\\cdot\\frac{(x-3)^2}{(x^3-16x)}', 'variables': []},
            'problem_output': '\\frac{3 \\left(x - 3\\right)}{x^{2} \\left(x - 4\\right)}'
        },
        {
            'problem_input': {'expression': 'x^2-1', 'variables': []},
            'problem_output': '\\left(x - 1\\right) \\left(x + 1\\right)'
        },
        {
            'problem_input': {'expression': 'x^2+2x+1', 'variables': []},
            'problem_output': '\\left(x + 1\\right)^{2}'
        },
        {
            'problem_input': {'expression': 'x^3+x^2-2x', 'variables': []},
            'problem_output': 'x \\left(x - 1\\right) \\left(x + 2\\right)'
        },
        {
            'problem_input': {'expression': 'x^4-9x^2', 'variables': []},
            'problem_output': 'x^{2} \\left(x - 3\\right) \\left(x + 3\\right)'
        },
        {
            'problem_input': {'expression': '7x^3y^2+28x^2y^3+28xy^4', 'variables': []},
            'problem_output': '7 x y^{2} \\left(x + 2 y\\right)^{2}'
        }
    ]

    def test_evaluate_expressions(self):
        run_entire_test_list(self, test_list=self.expressions, exercise_type=ProblemType.FACTORISABLE.value)

