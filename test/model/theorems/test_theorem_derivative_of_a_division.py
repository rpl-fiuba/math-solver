import unittest

from mathlearning.model.derivative.derivative_theorems import DerivativeTheorems
from mathlearning.model.expression import Expression
from test.model.theorems.test_utils import TestUtils

theorem = DerivativeTheorems.derivative_of_a_division()

equivalent_solutions = TestUtils.equivalent_solutions

class TestTheorem(unittest.TestCase):

    def test_simple_division_should_apply(self):
        exp = Expression('\\frac{d(\\frac{x}{x+1})}{dx}')
        expected = [Expression('\\frac{ \\frac{ d(x)}{dx} * (x + 1) - \\frac{d(x+1)}{dx} * x }{(x+1)^ 2}')]
        result = theorem.apply_to(exp)
        self.assertEquals(len(result), 1)
        self.assertTrue(equivalent_solutions(result, expected))

    def test_division_that_can_be_simplified_should_apply(self):
        exp = Expression('\\frac{d(\\frac{x}{x})}{dx}')
        expected = [Expression('0')]
        result = theorem.apply_to(exp)
        self.assertEquals(len(result), 1)
        self.assertTrue(equivalent_solutions(result, expected))

    def test_division_that_can_be_simplified_should_apply(self):
        exp = Expression('Derivative(cos(x)/sin(x),x)', is_latex=False)
        expected = [Expression('(- cos(x) * Derivative(sin(x), x)+ sin(x) * Derivative(cos(x), x) )/ (sin(x))**2', is_latex=False)]
        result = theorem.apply_to(exp)
        self.assertEquals(len(result), 1)
        self.assertTrue(equivalent_solutions(result, expected))
