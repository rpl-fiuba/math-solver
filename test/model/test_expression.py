import unittest

import sympy
from sympy import Add, Derivative, Pow, Mul, cos, Interval

from mathlearning.model.expression import Expression


class TestExpression(unittest.TestCase):

    def test_is_leaf(self):
        leaf = Expression("x")
        self.assertTrue(leaf.is_leaf())

    def test_solve_derivatives(self):
        exp = Expression("\\frac{d(x)}{dx}")
        exp = exp.solve_derivatives()
        self.assertEqual(exp.to_expression_string(), '1')

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

    def test_get_operators_by_level(self):
        exp = Expression("x + Derivative(x + x**2, x)", is_latex=False)
        operators = exp.get_operators_by_level()
        expected = {
            0: [Add],
            1: [Derivative],
            2: [Add],
            3: [Pow]
        }
        self.assertEquals(expected, operators)

    @unittest.skip("Migrating tests")
    def test_get_operators_by_level_complex(self):
        exp = Expression("cos(x+Derivative(e**x,x))  + Derivative(x + x**(2*x+3), x)", is_latex=False)
        operators = exp.get_operators_by_level()
        expected = {
            0: [Add],
            1: [cos, Derivative],
            2: [Add, Add],
            3: [Derivative, Pow],
            4: [Pow, Add],
            5: [Mul]
        }
        self.assertEquals(expected, operators)

    def test_get_operators_by_level_one_level(self):
        exp = Expression("x + 2", is_latex=False)
        operators = exp.get_operators_by_level()
        expected = {
            0: [Add]
        }
        self.assertEquals(expected, operators)

    def test_all_operators_and_levels_match(self):
        expression = Expression("x + Derivative(x +  x**2, x)", is_latex=False)
        sub_expression = Expression("Derivative(x +  x**2, x)", is_latex=False)
        self.assertTrue(expression.operators_and_levels_match(sub_expression))

    def test_all_operators_and_levels_match_long_expression(self):
        expression = Expression("Derivative(x +  x**2, x) + Derivative(x +  x**2, x) + Derivative(x +  x**2, x)",
                                is_latex=False)
        sub_expression = Expression("Derivative(x +  x**2, x)", is_latex=False)
        self.assertTrue(expression.operators_and_levels_match(sub_expression))

    def test_all_operators_and_levels_match_non_contained(self):
        expression = Expression("x + Derivative(x +  x**2, x)", is_latex=False)
        sub_expression = Expression("Derivative(x**2)", is_latex=False)
        self.assertFalse(expression.operators_and_levels_match(sub_expression))

    def test_get_depth_with_user_defined_func(self):
        expression = Expression("Derivative(f(x) +  g(x), x)", is_latex=False)
        self.assertEquals(3, expression.get_depth())

    def test_get_simplifications(self):
        exp = Expression('x**2*cos(x) + 2*x*sin(x) + x*Derivative(exp(x), x) + exp(x)', is_latex=False)
        exp.get_simplifications()

    def test_apply_integral(self):
        expression = Expression('Integral(x+x**2,x)', is_latex=False)
        result = expression.apply_integral()
        self.assertEquals(result, Expression('x**2/2 + x**3/3', is_latex=False))

    def test_integrate_is_integral(self):
        expression = Expression('Integral(x+x**2,x)', is_latex=False)
        self.assertTrue(expression.is_integral())

    def test_integrate_is_integral_false(self):
        expression = Expression('Derivative(x+x**2,x)', is_latex=False)
        self.assertFalse(expression.is_integral())

    def test_integrate_solving_possibilities(self):
        expression = Expression('Integral(x,x) + Integral(x**2,x) - Integral(cos(x),x)', is_latex=False)
        result = expression.integrals_solving_possibilities()
        self.assertEquals(len(result), 6)
        self.assertTrue(Expression('x**2/2 + Integral(x**2,x) - Integral(cos(x),x)', is_latex=False) in result)
        self.assertTrue(Expression('Integral(x,x) + x**3/3 - Integral(cos(x),x)', is_latex=False) in result)
        self.assertTrue(Expression('Integral(x,x) + Integral(x**2,x) - sin(x)', is_latex=False) in result)
        self.assertTrue(Expression('x**2/2 + Integral(x**2,x) - Integral(cos(x),x) + c', is_latex=False) in result)
        self.assertTrue(Expression('Integral(x,x) + x**3/3 - Integral(cos(x),x) + c', is_latex=False) in result)
        self.assertTrue(Expression('Integral(x,x) + Integral(x**2,x) - sin(x) + c', is_latex=False) in result)

    def test_domain_is_parsed_correctly(self):
        expression = Expression('Dom(\\sqrt{\\left(3-x\\right)}/(x^2-25))')
        self.assertEquals(expression.sympy_expr.name, 'Dom')
        self.assertEquals(len(expression.sympy_expr.args), 1)
        self.assertEquals(str(expression.sympy_expr.args[0]), 'sqrt(3 - x)/(x**2 - 25)')

    def test_domain_intersection_is_parsed_correctly(self):
        expression = Expression('Dom(\\sqrt{\\left(3-x\\right)}) \\cap Dom(1/(x^2-25))')
        self.assertTrue(expression.is_intersection_of_domains)
        self.assertEquals(len(expression.sympy_expr.args), 2)
        self.assertEquals(str(expression.sympy_expr.args[0].name), 'Dom')
        self.assertEquals(str(expression.sympy_expr.args[0]), 'Dom(sqrt(3 - x))')
        self.assertEquals(str(expression.sympy_expr.args[1].name), 'Dom')
        self.assertEquals(str(expression.sympy_expr.args[1]), 'Dom(1/(x**2 - 25))')

    def test_interval_with_numbers_is_parsed(self):
        expression_both_open = Expression('\\left(0, 5\\right)')
        expression_left_open = Expression('\\left(0, 5\\right]')
        expression_right_open = Expression('\\left[0, 5\\right)')
        expression_none_open = Expression('\\left[0, 5\\right]')
        self.assertEquals(expression_both_open.sympy_expr, Interval.open(0, 5))
        self.assertEquals(expression_left_open.sympy_expr, Interval.Lopen(0, 5))
        self.assertEquals(expression_right_open.sympy_expr, Interval.Ropen(0, 5))
        self.assertEquals(expression_none_open.sympy_expr, Interval(0, 5, False, False))

    def test_interval_with_infty_is_parsed(self):
        expression_both_open = Expression('\\left(-\\infty, 5\\right)')
        expression_left_open = Expression('\\left(-\\infty, 5\\right]')
        expression_right_open = Expression('\\left[5, \\infty\\right)')
        expression_none_open = Expression('\\left[5, 6\\right]')
        self.assertEquals(expression_both_open.sympy_expr, Interval.open(- sympy.oo, 5))
        self.assertEquals(expression_left_open.sympy_expr, Interval.Lopen(-sympy.oo, 5))
        self.assertEquals(expression_right_open.sympy_expr, Interval.Ropen(5, sympy.oo))
        self.assertEquals(expression_none_open.sympy_expr, Interval(5, 6, False, False))

    def test_interval_with_sqrt_is_parsed(self):
        expression_both_open = Expression('\\left(0, \\sqrt{5}\\right)')
        expression_left_open = Expression('\\left(0, \\sqrt{5}\\right]')
        expression_right_open = Expression('\\left[0, \\sqrt{5}\\right)')
        expression_none_open = Expression('\\left[0, \\sqrt{5}\\right]')
        self.assertEquals(expression_both_open.sympy_expr, Interval.open(0, sympy.sqrt(5)))
        self.assertEquals(expression_left_open.sympy_expr, Interval.Lopen(0, sympy.sqrt(5)))
        self.assertEquals(expression_right_open.sympy_expr, Interval.Ropen(0, sympy.sqrt(5)))
        self.assertEquals(expression_none_open.sympy_expr, Interval(0, sympy.sqrt(5), False, False))

    def test_interval_with_two_sqrt_is_parsed(self):
        expression_both_open = Expression('\\left(\\sqrt{2}, \\sqrt{5}\\right)')
        expression_left_open = Expression('\\left(-\\sqrt{2}, \\sqrt{5}\\right]')
        expression_right_open = Expression('\\left[\\sqrt{2}, \\sqrt{5}\\right)')
        expression_none_open = Expression('\\left[-\\sqrt{2}, \\sqrt{5}\\right]')
        self.assertEquals(expression_both_open.sympy_expr, Interval.open(sympy.sqrt(2), sympy.sqrt(5)))
        self.assertEquals(expression_left_open.sympy_expr, Interval.Lopen(-sympy.sqrt(2), sympy.sqrt(5)))
        self.assertEquals(expression_right_open.sympy_expr, Interval.Ropen(sympy.sqrt(2), sympy.sqrt(5)))
        self.assertEquals(expression_none_open.sympy_expr, Interval(-sympy.sqrt(2), sympy.sqrt(5), False, False))

    def test_interval_with_sqrt_and_infty(self):
        expression_both_open = Expression('\\left(-\\infty, \\sqrt{5}\\right)')
        expression_left_open = Expression('\\left(-\\infty, \\sqrt{5}\\right]')
        expression_right_open = Expression('\\left[\\sqrt{5}, \\infty\\right)')
        expression_both_open_positive_infty = Expression('\\left(\\sqrt{5}, \\infty\\right)')
        self.assertEquals(expression_both_open.sympy_expr, Interval.open(- sympy.oo, sympy.sqrt(5)))
        self.assertEquals(expression_left_open.sympy_expr, Interval.Lopen(- sympy.oo, sympy.sqrt(5)))
        self.assertEquals(expression_right_open.sympy_expr, Interval.Ropen(sympy.sqrt(5), sympy.oo))
        self.assertEquals(expression_both_open_positive_infty.sympy_expr, Interval.open(sympy.sqrt(5), sympy.oo))

    def test_interval_with_fraction_right_side(self):
        expression_both_open = Expression('\\left(-\\infty, \\frac{4}{3}\\right)')
        expression_left_open = Expression('\\left(-\\infty, \\frac{4}{3}\\right]')
        expression_right_open = Expression('\\left[-2, \\frac{4}{3}\\right)')
        expression_none_open = Expression('\\left[-2, \\frac{4}{3}\\right]')
        self.assertTrue(expression_both_open.sympy_expr._eval_Eq(Interval.open(-sympy.oo, sympy.Rational(4, 3))))
        self.assertTrue(expression_left_open.sympy_expr._eval_Eq(Interval.Lopen(-sympy.oo, sympy.Rational(4, 3))))
        self.assertTrue(expression_right_open.sympy_expr._eval_Eq(Interval.Ropen(-2, sympy.Rational(4, 3))))
        self.assertTrue(expression_none_open.sympy_expr._eval_Eq(Interval(-2, sympy.Rational(4, 3), False, False)))

    def test_interval_with_negative_fraction_left_side(self):
        expression_both_open = Expression('\\left(\\frac{-4}{3}, \\infty\\right)')
        expression_left_open = Expression('\\left(-\\infty, \\frac{-4}{3}\\right]')
        expression_right_open = Expression('\\left[\\frac{-4}{3}, \\frac{4}{3}\\right)')
        expression_none_open = Expression('\\left[\\frac{-4}{3}, \\frac{4}{3}\\right]')
        self.assertTrue(expression_both_open.sympy_expr._eval_Eq(Interval.open(-sympy.Rational(4, 3), sympy.oo)))
        self.assertTrue(expression_left_open.sympy_expr._eval_Eq(Interval.Lopen(-sympy.oo, sympy.Rational(-4, 3))))
        self.assertTrue(
            expression_right_open.sympy_expr._eval_Eq(Interval.Ropen(sympy.Rational(-4, 3), sympy.Rational(4, 3))))
        self.assertTrue(expression_none_open.sympy_expr._eval_Eq(
            Interval(sympy.Rational(-4, 3), sympy.Rational(4, 3), False, False)))
