import json

from rest_framework import status
from rest_framework.test import APITestCase

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.expression import Expression
from mathlearning.model.theorem import Theorem
from test.api.test_api import load_theorems
from test.testutils.solved_exercises import SolvedExercises, SolvedExercise

solution_tree_mapper = SolutionTreeMapper()


def get_solution_tree_broken_nodes(tree_dict):
    result = []
    for branch in tree_dict['branches']:
        try:
            Expression(branch['expression'])
            result += get_solution_tree_broken_nodes(branch)
        except:
            result.append({'before': tree_dict['expression'], 'after': branch['expression'], 'theorem': branch['theorem_applied']})
    return result

def theorem_to_json(theorem: Theorem):
    return theorem.to_json()


class SolutionTreeAPITest(APITestCase):

    def solve_exercise_with_solution_tree(self, exercise: SolvedExercise):
        # get solution tree
        theorems = load_theorems("test/jsons/theorems.json")
        data = {
            'problem_input': exercise.steps[0],
            'theorems': theorems,
        }
        response = self.client.post(path='/results/solution-tree', data=data, format='json')

        tree_str = json.loads(response.content)
        #broken_nodes = get_solution_tree_broken_nodes(tree_dict)

        resolve_data = {
            'problem_input': exercise.steps[0],
            'math_tree': tree_str,
            'type': 'derivative',
            'theorems': theorems
        }

        # all steps should be valid
        for i in range(1, len(exercise.non_result_steps)):
            previous_steps = exercise.non_result_steps[:i]
            # remove problem_input
            previous_steps.pop()
            current_step = exercise.non_result_steps[i]
            resolve_data['step_list'] = json.dumps(previous_steps)
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
        resolve_data['step_list'] = json.dumps(exercise.steps)
        resolve_data['current_expression'] = exercise.steps[-1]

        response = self.client.post(path='/resolve', data=resolve_data, format='json')

        result = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(result['exerciseStatus'], 'resolved')


    def test_only_result(self, exercise: SolvedExercise):
        # get solution tree
        theorems = load_theorems("test/jsons/theorems.json")
        data = {
            'problem_input': exercise.steps[0],
            'theorems': theorems,
        }

        response = self.client.post(path='/results/solution-tree', data=data, format='json')

        tree_str = json.loads(response.content)
        #broken_nodes = get_solution_tree_broken_nodes(tree_dict)

        resolve_data = {'problem_input': exercise.steps[0], 'math_tree': tree_str, 'type': 'derivative',
                        'theorems': theorems, 'step_list': json.dumps(exercise.steps),
                        'current_expression': exercise.steps[-1]}

        # the result should be resolved
        response = self.client.post(path='/resolve', data=resolve_data, format='json')

        result = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(result['exerciseStatus'], 'resolved')



    def test_solution_tree_cases_sum_of_two_derivatives(self):
        self.solve_exercise_with_solution_tree(SolvedExercises.derivative_e_plus_sin())

    def test_solution_tree_cases_derivative_mult_of_three_elem(self):
        self.solve_exercise_with_solution_tree(SolvedExercises.derivative_mult_of_three_elem())

    def test_solution_tree_cases_derivative_sin_divided_by_cos(self):
        self.solve_exercise_with_solution_tree(SolvedExercises.derivative_sin_divided_by_cos())

    def test_solution_tree_cases_sum_derivative_x2_derivative_sum_x_cos(self):
        self.solve_exercise_with_solution_tree(SolvedExercises.sum_derivative_x2_derivative_sum_x_cos())

    def test_integral_solution_sum_of_two(self):
        self.test_only_result(SolvedExercises.integral_add_x_cosx())

    def test_integral_solution_parts(self):
        self.test_only_result(SolvedExercises.integral_parts_mult_x_cosx())

    def test_integral_substitution_division_of_polynomials(self):
        self.test_only_result(SolvedExercises.integral_substitution_division_of_polynomials())

    def test_integral_substitution_sin_with_polynomials(self):
        self.test_only_result(SolvedExercises.integral_substitution_sin_with_polynomials())

    def test_integral_substitution_multiplication(self):
        self.test_only_result(SolvedExercises.integral_substitution_multiplication())

    def test_integral_parts_example_one(self):
        self.test_only_result(SolvedExercises.integral_parts_example_one())

    def test_integral_parts_example_two(self):
        self.test_only_result(SolvedExercises.integral_parts_example_two())

    def test_integral_parts_example_six(self):
        self.test_only_result(SolvedExercises.integral_parts_example_six())
