import json

from rest_framework import status

from mathlearning.model.expression import Expression
from mathlearning.model.problem_type import ProblemType
from test.testutils.solved_exercise import SolvedExercise


def run_entire_test_list(self, test_list, exercise_type):
    for exercise in test_list:
        data = {
            'problem_input': exercise['problem_input'],
            'type': exercise_type
        }

        response = self.client.post(path='/validations/evaluate', data=data, format='json')

        body = json.loads(response.content)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(body['result']['expression'], exercise['problem_output'])


def solve_exercise_with_solution_tree(self, kind: ProblemType, exercise: SolvedExercise):
    data = {
        'problem_input': exercise.steps[0],
        'type': kind.value,
    }

    response = self.client.post(path='/results/solution-tree', data=data, format='json')

    tree_str = json.loads(response.content)

    resolve_data = {
        'problem_input': exercise.steps[0],
        'math_tree': tree_str,
        'type': kind.value,
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
            print(str(current_step))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(result['exerciseStatus'], 'valid')

    for invalid_step in exercise.invalid_steps:
        resolve_data['step_list'] = []
        resolve_data['current_expression'] = invalid_step
        response = self.client.post(path='/resolve', data=resolve_data, format='json')
        result = json.loads(response.content)
        if result['exerciseStatus'] == 'resolved':
            print("Expected invalid result but got resolved", Expression(invalid_step).to_string())
        if result['exerciseStatus'] == 'valid':
            print("Expected invalid result but got valid", str(invalid_step))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(result['exerciseStatus'], 'invalid')

    # the result should be resolved
    resolve_data['step_list'] = exercise.steps
    resolve_data['current_expression'] = exercise.steps[-1]

    response = self.client.post(path='/resolve', data=resolve_data, format='json')

    result = json.loads(response.content)
    self.assertEquals(response.status_code, status.HTTP_200_OK)
    self.assertEquals(result['exerciseStatus'], 'resolved')


def load_exercises(exercises_path):
    with open(exercises_path, 'r') as exercises_file:
        exercises_json = json.load(exercises_file)
        exercises = []
        for exercise_json in exercises_json:
            exercise = SolvedExercise(name=exercise_json["name"], steps=exercise_json["steps"],
                                      result=exercise_json["result"])
            exercises.append(exercise)
        return exercises


def load_theorems():
    with open("test/jsons/theorems.json", 'r') as theorems_file:
        return json.load(theorems_file)
