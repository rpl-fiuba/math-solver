from rest_framework.test import APITestCase

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.problem_type import ProblemType
from mathlearning.model.theorem import Theorem
from test.testutils.domain_solved_exercises import DomainExercises
from test.testutils.test_utils import solve_exercise_with_solution_tree

solution_tree_mapper = SolutionTreeMapper()


def theorem_to_json(theorem: Theorem):
    return theorem.to_json()


class SolutionTreeAPITest(APITestCase):

    def test_rational_domain_root_zero(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.rational_domain_root_zero())

    def test_rational_domain_root_moved(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.rational_domain_root_moved())
