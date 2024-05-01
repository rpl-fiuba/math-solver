from rest_framework.test import APITestCase

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.problem_type import ProblemType
from test.testutils.factor_solved_exercises import FactorExercises
from test.testutils.test_utils import solve_exercise_with_solution_tree

solution_tree_mapper = SolutionTreeMapper()


class SolutionTreeAPITest(APITestCase):

    def test_rational_expression_with_mult(self):
        solve_exercise_with_solution_tree(self, ProblemType.FACTORISABLE, FactorExercises.rational_expression_with_mult())

    def test_square_dif(self):
        solve_exercise_with_solution_tree(self, ProblemType.FACTORISABLE, FactorExercises.square_dif())

    def test_square_binomial(self):
        solve_exercise_with_solution_tree(self, ProblemType.FACTORISABLE, FactorExercises.square_binomial())

    def test_cube_expression(self):
        solve_exercise_with_solution_tree(self, ProblemType.FACTORISABLE, FactorExercises.cube_expression())

    def test_square_dif_2(self):
        solve_exercise_with_solution_tree(self, ProblemType.FACTORISABLE, FactorExercises.square_dif_2())

    def test_expression_with_x_y(self):
        solve_exercise_with_solution_tree(self, ProblemType.FACTORISABLE, FactorExercises.expression_with_x_y())

