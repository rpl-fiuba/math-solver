from rest_framework.test import APITestCase

from mathlearning.model.problem_type import ProblemType
from test.testutils.test_utils import run_entire_test_list


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

    square_root_domains = [
        {
            'problem_input': {'expression': '\\sqrt{\\left(x\\right)}', 'variables': []},
            'problem_output': '\\left[0, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '\\sqrt{\\left(5-x\\right)}', 'variables': []},
            'problem_output': '\\left(-\\infty, 5\\right]'
        },
        {
            'problem_input': {'expression': '\\sqrt{\\left(x^2\\right)}', 'variables': []},
            'problem_output': '\\left(-\\infty, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '\\sqrt{\\left(1/x\\right)}', 'variables': []},
            'problem_output': '\\left(0, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '\\sqrt{\\left(3-x\\right)}/(x^2-25)', 'variables': []},
            'problem_output': '\\left(-\\infty, -5\\right) \\cup \\left(-5, 3\\right]'
        }
    ]

    factorisable_domains = [
        {
            'problem_input': {'expression': '1/(x^2+2x+1)', 'variables': []},
            'problem_output': '\\left(-\\infty, -1\\right) \\cup \\left(-1, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '1/(x^2-1)', 'variables': []},
            'problem_output': '\\left(-\\infty, -1\\right) \\cup \\left(-1, 1\\right) \\cup \\left(1, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '(x-1)/(x-1)', 'variables': []},
            'problem_output': '\\left(-\\infty, 1\\right) \\cup \\left(1, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '(x-1)/(x^2-1)', 'variables': []},
            'problem_output': '\\left(-\\infty, -1\\right) \\cup \\left(-1, 1\\right) \\cup \\left(1, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '(x-3)/(x^2-1) * (x-1)/(x+3)', 'variables': []},
            'problem_output': '\\left(-\\infty, -3\\right) \\cup \\left(-3, -1\\right) '
                              '\\cup \\left(-1, 1\\right) \\cup \\left(1, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '(x-3)/(x^2-1) + (x-1)/(x+3)', 'variables': []},
            'problem_output': '\\left(-\\infty, -3\\right) \\cup \\left(-3, -1\\right) '
                              '\\cup \\left(-1, 1\\right) \\cup \\left(1, \\infty\\right)'
        }
    ]

    mixed_domains = [
        {
            'problem_input': {'expression': '\\frac{1}{\\sqrt{\\left(x-5\\right)}}', 'variables': []},
            'problem_output': '\\left(5, \\infty\\right)'
        },
        {
            'problem_input': {'expression': '\\sqrt{\\left(7-x\\right)}\\cdot\\sqrt{\\left(x-5\\right)}',
                              'variables': []},
            'problem_output': '\\left[5, 7\\right]'
        },
        {
            'problem_input': {'expression': '\\sqrt{\\left(7-x\\right)}\\sqrt{\\left(x-7\\right)}', 'variables': []},
            'problem_output': '\\left\\{7\\right\\}'
        },
        {
            'problem_input': {'expression': '\\sqrt{\\left(x^2-5\\right)}', 'variables': []},
            'problem_output': '\\left(-\\infty, - \\sqrt{5}\\right] \\cup \\left[\\sqrt{5}, \\infty\\right)'
        }
    ]

    def test_evaluate_rational_domains(self):
        run_entire_test_list(self, test_list=self.rational_domains, exercise_type=ProblemType.DOMAIN.value)

    def test_evaluate_square_root_domains(self):
        run_entire_test_list(self, test_list=self.square_root_domains, exercise_type=ProblemType.DOMAIN.value)

    def test_evaluate_factorisable_domains(self):
        run_entire_test_list(self, test_list=self.factorisable_domains, exercise_type=ProblemType.DOMAIN.value)

    def test_mixed_domains(self):
        run_entire_test_list(self, test_list=self.mixed_domains, exercise_type=ProblemType.DOMAIN.value)
