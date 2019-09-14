import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SolvedExercise:
    def __init__(self, name, steps: list, result):
        self.name = name
        self.steps= steps
        self.result = result

def load_exercises(exercises_path):
    with open(exercises_path, 'r') as exercises_file:
        exercises_json = json.load(exercises_file)
        exercises = []
        for exercise_json in exercises_json:
            exercise = SolvedExercise(name= exercise_json["name"], steps= exercise_json["steps"], result= exercise_json["result"])
            exercises.append(exercise)
        return exercises

def load_theorems(theorems_path):
    with open(theorems_path, 'r') as theorems_file:
        return json.load(theorems_file)

def validate_step(api_client, theorems, new_expression, old_expression):
    data = {
        'theorems': theorems,
        'new_expression': new_expression,
        'old_expression': old_expression
    }
    return api_client.post(path= "/validations/new-step",data= data, format= 'json')



class APITests(APITestCase):
    def validate_and_assert(self, api_client, theorems, new_expression, old_expression):
        response = validate_step(api_client, theorems, new_expression, old_expression)
        if response.status_code == 200:
            print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        is_valid = json.loads(response.content)
        self.assertTrue(is_valid)

    def test_create_account(self):
        exercises = load_exercises('test/api/jsons/solved_exercises.json')
        theorems = load_theorems("test/api/jsons/theorems.json")

        for solved_exercise in exercises:
            print("Testing " + solved_exercise.name)
            steps = solved_exercise.steps
            for i in range(0, len(steps) - 1):
                old_expression = steps[i]
                new_expression = steps[i+1]
                self.validate_and_assert(api_client= self.client, 
                    theorems= theorems, 
                    new_expression=new_expression, 
                    old_expression= old_expression)
    
            print("Asserting result")
            data = {
                'expression_one': steps[-1],
                'expression_two': solved_exercise.result
            }
            response = self.client.post(path= '/compare', data= data, format='json')
            self.assertEquals(response.status_code, status.HTTP_200_OK)
            self.assertEquals(response.data, 'true')







