from rest_framework.test import APITestCase

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.problem_type import ProblemType
from test.testutils.image_solved_exercises import ImageExercises
from test.testutils.test_utils import solve_exercise_with_solution_tree

solution_tree_mapper = SolutionTreeMapper()


class SolutionTreeAPITest(APITestCase):

    def test_rational_domain_root_zero(self):
        solve_exercise_with_solution_tree(self, ProblemType.IMAGE, ImageExercises.full_real_image())

    def test_rational_domain_root_moved(self):
        solve_exercise_with_solution_tree(self, ProblemType.IMAGE, ImageExercises.positive_numbers_image())
