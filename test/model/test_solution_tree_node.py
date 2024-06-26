import json

import unittest

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.expression import Expression
from test.testutils.derivative_solved_exercises import DerivativeExercises

tree_byte_arr = ''  # TODO
exercise = DerivativeExercises.derivative_e_plus_sin()
#tree = SolutionTreeMapper.parse(json.loads(tree_byte_arr))


@unittest.skip("Migrating tests")
class TestSolutionTree(unittest.TestCase):

    def test_is_a_result(self):
        tree = SolutionTreeMapper.parse(json.loads(tree_byte_arr))
        self.assertTrue(tree.is_a_result(Expression(exercise.result['expression'], exercise.result['variables'])))

    def test_is_a_result_steps_are_not_results(self):
        steps = exercise.get_results_as_expressions()
        non_result_steps = exercise.get_results_as_expressions()[:len(steps) - 1]
        for non_result in non_result_steps:
            step_is_result = tree.is_a_result(non_result)
            self.assertFalse(step_is_result)
            if step_is_result:
                print('Non result step returned is result True: ' + non_result.to_string())

    def test_is_a_result_pre_simplification_steps_are_results(self):
        result = Expression("x**2*cos(x) + x*(2*sin(x)) + (x + 1)*exp(x)", is_latex=False)
        self.assertTrue(tree.is_a_result(result))

    def test_get_subtree_with_root(self):
        pass

    def test_contains(self):
        all_steps_contained = True
        for i in range(0, len(exercise.steps)):
            step = exercise.steps[i]
            expression = Expression(step['expression'], step['variables'])
            all_steps_contained = all_steps_contained and tree.contains(expression)
            if not all_steps_contained:
                print('failed: ' + expression.to_string())
        self.assertTrue(all_steps_contained)

    def test_get_hints_result_step_should_not_return_hints(self):
        resultStep = Expression("x**2*cos(x) + x*(2*sin(x)) + (x + 1)*exp(x)", is_latex=False)
        hints = tree.get_hints(resultStep)
        self.assertEquals(hints, [])

    def test_get_hints_initial_step_should_return_hints(self):
        initialStep = Expression("Derivative(x*exp(x), x) + Derivative(x**2*sin(x), x)", is_latex=False)
        hints = tree.get_hints(initialStep)
        hints = list(set(map(lambda h: h.name, hints)))
        self.assertTrue('derivada del producto' in hints)
        self.assertTrue('resolver derivadas' in hints)
