from rest_framework.test import APITestCase

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.problem_type import ProblemType
from test.testutils.intersection_solved_exercises import IntersectionExercises
from test.testutils.test_utils import solve_exercise_with_solution_tree

solution_tree_mapper = SolutionTreeMapper()


class SolutionTreeAPITest(APITestCase):

    def test_lineal_expression(self):
        solve_exercise_with_solution_tree(self, ProblemType.INTERSECTION, IntersectionExercises.lineal_expression())

    def test_sqrt_expression(self):
        solve_exercise_with_solution_tree(self, ProblemType.INTERSECTION, IntersectionExercises.sqrt_expression())

    def test_sqrt_expression_hard(self):
        solve_exercise_with_solution_tree(self, ProblemType.INTERSECTION, IntersectionExercises.sqrt_expression_hard())

    def test_sqrt_expression_with_two_conditions(self):
        solve_exercise_with_solution_tree(self, ProblemType.INTERSECTION, IntersectionExercises.sqrt_expression_with_two_conditions())

    def test_sqrt_expression_with_abs(self):
        solve_exercise_with_solution_tree(self, ProblemType.INTERSECTION, IntersectionExercises.sqrt_expression_with_abs())

    def test_rational_expression(self):
        solve_exercise_with_solution_tree(self, ProblemType.INTERSECTION, IntersectionExercises.rational_expression())

    def test_rational_expression_with_sqrt(self):
        solve_exercise_with_solution_tree(self, ProblemType.INTERSECTION, IntersectionExercises.rational_expression_with_sqrt())

    def test_sqrt_expression_with_constant(self):
        solve_exercise_with_solution_tree(self, ProblemType.INTERSECTION, IntersectionExercises.sqrt_expression_with_constant())

    def test_expression_with_inf_solutions(self):
        solve_exercise_with_solution_tree(self, ProblemType.INTERSECTION, IntersectionExercises.expression_with_inf_solutions())


