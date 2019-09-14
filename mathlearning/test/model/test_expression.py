import unittest
from mathlearning.model.expression import Expression

class TestExpression(unittest.TestCase):
    
    def test_is_leaf(self):

        leaf = Expression("x")
        self.assertTrue(leaf.is_leaf())

    def test_solve_derivatives(self):
        exp = Expression("\\frac{d(x)}{dx}")
        exp = exp.solve_derivatives()
        self.assertEqual(exp.to_string(), '1')

    def test_compare(self):
        exp_one = Expression("x + x")
        exp_two = Expression("2 * x")

        self.assertTrue(exp_one.is_equivalent_to(exp_two))
    
    def test_some(self):
        exp_one = Expression("x + x")
        exp_two = Expression("x + x")

        self.assertTrue(exp_one == exp_two)

    def test_get_children(self):
        exp = Expression("x + x^2")
        children = exp.get_children()
        self.assertEqual(2, len(children))

        self.assertTrue(Expression("x") in children)
        self.assertTrue(Expression("x^2") in children)

    def test_get_children_add_three_elements(self):
        exp = Expression("x + x^2 + x^3")
        children = exp.get_children()
        self.assertEqual(3, len(children))

        self.assertTrue(Expression("x") in children)
        self.assertTrue(Expression("x^2") in children)
        self.assertTrue(Expression("x^3") in children)

    def test_get_children_derivative(self):
        exp = Expression("x^3 + \\frac{d(x)}{dx} + \\frac{d(x^2)}{dx}")
        children = exp.get_children()
        self.assertEqual(3, len(children))
        self.assertTrue(Expression("\\frac{d(x^2)}{dx}") in children)
        self.assertTrue(Expression("\\frac{d(x)}{dx}") in children)
        self.assertTrue(Expression("x^3") in children)