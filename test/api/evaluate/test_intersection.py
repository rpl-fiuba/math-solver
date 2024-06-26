from rest_framework.test import APITestCase

from mathlearning.model.problem_type import ProblemType
from test.testutils.test_utils import run_entire_test_list_with_equivalent


class APITests(APITestCase):
    expressions = [
         {
             'problem_input': {'expression': '\\sqrt{\\left(3x-8\\right)} = 4 - \\sqrt{x}', 'variables': []},
             'problem_output': 'x=4'
         },
         {
             'problem_input': {'expression': '\\sqrt{\\left(3x\\right)} - 8 = 4 - \\sqrt{x}', 'variables': []},
             'problem_output': 'x=144 - 72*sqrt(3)'
         },
         {
             'problem_input': {'expression': 'x^2 - 1 = x', 'variables': []},
             'problem_output': 'x=1/2 + sqrt(5)/2 \\vee x=1/2 - sqrt(5)/2'
         },
         {
            'problem_input': {'expression': 'x^2 - 1 = -x^2 + 1', 'variables': []},
            'problem_output': 'x=-1 \\vee x=1'
         },
         {
             'problem_input': {'expression': '2x - 1 = 5x + 4', 'variables': []},
             'problem_output': 'x=-5/3'
         },
         {
             'problem_input': {'expression': '\\sqrt{x} = x', 'variables': []},
             'problem_output': 'x=0 \\vee x=1'
         },
         {
             'problem_input': {'expression': '0.5*x = \\left|x-2\\right|', 'variables': []},
             'problem_output': 'x=1.33333333333333 \\vee x=4.00000000000000'
         },
         {
             'problem_input': {'expression': '-x = \\sqrt{x}', 'variables': []},
             'problem_output': 'x=0'
         }
    ]

    def test_evaluate_expressions(self):
        run_entire_test_list_with_equivalent(self, test_list=self.expressions, exercise_type=ProblemType.INTERSECTION.value)

