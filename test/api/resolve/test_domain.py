from rest_framework.test import APITestCase

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.problem_type import ProblemType
from test.testutils.domain_solved_exercises import DomainExercises
from test.testutils.test_utils import solve_exercise_with_solution_tree

solution_tree_mapper = SolutionTreeMapper()


class SolutionTreeAPITest(APITestCase):

    def test_rational_domain_root_zero(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.rational_domain_root_zero())

    def test_square_root_domain(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.square_root_domain())

    def test_rational_domain_root_moved(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.rational_domain_root_moved())

    def test_domain_as_intersection_of_domains(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.intermediate_results_as_intersection_of_domains())

    def test_domain_as_intersection_of_three_domains(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.intermediate_results_as_intersection_of_three_domains())

    def test_domain_as_intersection_of_domains_with_combinations_inside(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.intermediate_results_as_intersection_of_domains_combined_inside())

    def test_domain_as_intersection_of_domains_from_sum_of_terms(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.intermediate_results_as_intersection_of_domains_in_sum_of_terms())

    def test_domain_as_intersection_of_domains_and_intervals(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.intermediate_results_mixing_domains_and_intervals())

    def test_domain_with_rational_interval_borders(self):
        solve_exercise_with_solution_tree(self, ProblemType.DOMAIN, DomainExercises.domains_with_rational_interval_borders())

