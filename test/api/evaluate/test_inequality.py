from rest_framework.test import APITestCase

from mathlearning.model.problem_type import ProblemType
from test.testutils.test_utils import run_entire_test_list


class APITests(APITestCase):
    expressions = [
        {
            'problem_input': {'expression': '(x-1)\\cdot(\\left|x-2\\right|-3)\\ge0', 'variables': []},
            'problem_output': '\\left[-1, 1\\right] \\cup \\left[5, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '|x-1|<2', 'variables': []},
            'problem_output': '\\left(-1, 3\\right)'
        },
        {
            'problem_input': {'expression': '\\left|x-1\\right|<2', 'variables': []},
            'problem_output': '\\left(-1, 3\\right)'
        },
        {
            'problem_input': {'expression': '\\left|x-1\\right|>0', 'variables': []},
            'problem_output': '\\left(-\\infty, 1\\right) \\cup \\left(1, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '\\left|x-1\\right| \\ge 1', 'variables': []},
            'problem_output': '\\left(-\\infty, 0\\right] \\cup \\left[2, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '|x-1|>0 \\wedge |x-1|<2', 'variables': []},
            'problem_output': '\\left(-1, 1\\right) \\cup \\left(1, 3\\right)'
        },

    ]

    def test_evaluate_expressions(self):
        run_entire_test_list(self, test_list=self.expressions, exercise_type=ProblemType.INEQUALITY.value)

