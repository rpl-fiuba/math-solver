import json

from rest_framework import status
from rest_framework.test import APITestCase

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.expression import Expression
from mathlearning.model.theorem import Theorem
from test.testutils.domain_solved_exercises import DomainExercises
from test.testutils.solved_exercise import SolvedExercise

solution_tree_mapper = SolutionTreeMapper()


def theorem_to_json(theorem: Theorem):
    return theorem.to_json()


class SolutionTreeAPITest(APITestCase):

    def solve_exercise_with_solution_tree(self, exercise: SolvedExercise):

        data = {
            'problem_input': exercise.steps[0],
            'type': 'domain',
        }

        response = self.client.post(path='/results/solution-tree', data=data, format='json')

        tree_str = json.loads(response.content)

        resolve_data = {
            'problem_input': exercise.steps[0],
            'math_tree': tree_str,
            'type': 'domain',
            'theorems': []
        }

        # all steps should be valid
        for i in range(1, len(exercise.non_result_steps)):
            previous_steps = exercise.non_result_steps[:i]
            # remove problem_input
            previous_steps.pop()
            current_step = exercise.non_result_steps[i]
            resolve_data['step_list'] = previous_steps
            resolve_data['current_expression'] = current_step
            response = self.client.post(path='/resolve', data=resolve_data, format='json')
            result = json.loads(response.content)
            if result['exerciseStatus'] == 'resolved':
                print(Expression(current_step).to_string())
            if result['exerciseStatus'] == 'invalid':
                print(Expression(current_step).to_string())
            self.assertEquals(response.status_code, status.HTTP_200_OK)
            self.assertEquals(result['exerciseStatus'], 'valid')

        # the result should be resolved
        resolve_data['step_list'] = exercise.steps
        resolve_data['current_expression'] = exercise.steps[-1]

        response = self.client.post(path='/resolve', data=resolve_data, format='json')

        result = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(result['exerciseStatus'], 'resolved')

    def test_rational_domain_root_zero(self):
        self.solve_exercise_with_solution_tree(DomainExercises.rational_domain_root_zero())

    def test_rational_domain_root_moved(self):
        self.solve_exercise_with_solution_tree(DomainExercises.rational_domain_root_moved())
