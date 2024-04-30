from rest_framework.test import APITestCase

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.problem_type import ProblemType
from test.testutils.factor_solved_exercises import FactorExercises
from test.testutils.inequality_solved_exercises import InequalityExercises
from test.testutils.test_utils import solve_exercise_with_solution_tree

solution_tree_mapper = SolutionTreeMapper()


class SolutionTreeAPITest(APITestCase):

    def test_sample_exercise(self):
        solve_exercise_with_solution_tree(self, ProblemType.INEQUALITY, InequalityExercises.sample_exercise_with_initial_vee())

    def test_single_abs_greater_than_equal(self):
        solve_exercise_with_solution_tree(self, ProblemType.INEQUALITY, InequalityExercises.single_abs_greater_than_equal())

    def test_single_abs_less_than_without_including_edge(self):
        solve_exercise_with_solution_tree(self, ProblemType.INEQUALITY, InequalityExercises.single_abs_less_than_without_including_edge())

    def test_double_limited_abs_inequality(self):
        solve_exercise_with_solution_tree(self, ProblemType.INEQUALITY, InequalityExercises.double_limited_abs_inequality())

