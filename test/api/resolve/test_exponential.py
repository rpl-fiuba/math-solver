from rest_framework.test import APITestCase

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.problem_type import ProblemType
from test.testutils.exponential_solved_exercises import ExponentialExercises
from test.testutils.test_utils import solve_exercise_with_solution_tree

solution_tree_mapper = SolutionTreeMapper()


class SolutionTreeAPITest(APITestCase):

    def test_ln_expression(self):
        solve_exercise_with_solution_tree(self, ProblemType.EXPONENTIAL, ExponentialExercises.ln_expression())

    def test_exp_expression(self):
        solve_exercise_with_solution_tree(self, ProblemType.EXPONENTIAL, ExponentialExercises.exp_expression())

