import unittest

from mathlearning.model.expression_variable import ExpressionVariable
from mathlearning.model.integral.integrate_theorems import IntegrateTheorems
from test.model.theorems.test_utils import TestUtils
from mathlearning.model.expression import Expression

theorem = IntegrateTheorems.integrate_by_parts()

equivalent_solutions = TestUtils.equivalent_solutions

#Expresion original
#Expression('\\int (x * \\cos(x))')

#Expresiones equivalentes permitidas
#Expression('\\int (u * \\frac{d(v)}{dx})', is_latex=True, u="x", v="sen(x)")

#Expression('u * v - \\int (\\frac{d(u)}{dx} * v)', is_latex=True, u="x", v="sen(x)")

#Expression('x * \\sen(x) - \\int (\\frac{d(x)}{dx} * \\sen(x))', is_latex=True, u="x", v="sen(x)")

#Expression('u * \\sen(x) - \\int (\\frac{d(x)}{dx} * \\sen(x))', is_latex=True, u="x", v="sen(x)")


class TestTheoremIntegrateByParts(unittest.TestCase):

    def test_parts_there_is_a_chance_to_apply_to(self):
        exp = Expression('\\int (x * \\cos(x))')
        self.assertTrue(theorem.there_is_a_chance_to_apply_to(exp))

    def test_parts_there_is_a_chance_to_apply_to_is_false(self):
        exp = Expression('\\int x')
        self.assertFalse(theorem.there_is_a_chance_to_apply_to(exp))

    def test_parts_there_is_a_chance_to_apply_to_is_false_when_is_not_integral(self):
        exp = Expression('x')
        self.assertFalse(theorem.there_is_a_chance_to_apply_to(exp))

    @unittest.skip("Migrating tests")
    def test_parts_replacing_u_v_should_apply(self):
        exp = Expression('\\int (x * \\cos(x))')
        variables = [
            ExpressionVariable('u(x)', Expression("x")),
            ExpressionVariable('v(x)', Expression("sen(x)")),
        ]
        expected_result = [
            Expression('u(x) * v(x) - \\int (\\frac{d(u(x))}{dx} * v(x))', variables),
            Expression('\\int u(x) * \\frac{d(v(x))}{dx}', variables)
        ]
        result = theorem.apply_to(exp)
        self.assertEqual(result, expected_result)
