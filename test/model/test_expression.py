import unittest
import sympy
from sympy import Add, Derivative, Pow, Mul, cos, Interval

from mathlearning.model.expression import Expression
from mathlearning.utils.latex_utils import find_outermost_brackets
from sympy.parsing.latex import parse_latex


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

    def test_set_with_plain_numbers(self):
        self.assertEquals(Expression('\\mathbb{o}').sympy_expr, sympy.EmptySet)
        self.assertEquals(Expression('\\mathbb{R}').sympy_expr, sympy.Reals)
        self.assertEquals(Expression('\\mathbb{R}-{1}').sympy_expr,
                          sympy.SymmetricDifference(sympy.Reals, sympy.FiniteSet(1)))
        self.assertEquals(Expression('\\mathbb{R}-{2,3,15,5}').sympy_expr,
                          sympy.SymmetricDifference(sympy.Reals, sympy.FiniteSet(2, 3, 5, 15)))

    def test_set_with_expressions(self):
        self.assertEquals(Expression('\\mathbb{R}-{\\sqrt{5}}').sympy_expr,
                          sympy.SymmetricDifference(sympy.Reals, sympy.FiniteSet(sympy.sqrt(5))))
        self.assertEquals(Expression('\\mathbb{R}-{\\sqrt{5}, 3, 0}').sympy_expr,
                          sympy.SymmetricDifference(sympy.Reals, sympy.FiniteSet(sympy.sqrt(5), 0, 3)))
        # TODO check test with rationals in the edges
        # self.check_equality_with_substractions(Expression('\\mathbb{R}-{\\sqrt{5}, 15, \\frac{17}{3}}').sympy_expr,
        #                                       sympy.SymmetricDifference(sympy.Reals, sympy.FiniteSet(sympy.sqrt(5), 15, sympy.Mul(17, sympy.Pow(3, -1)))))

    # def check_equality_with_substractions(self, set_left, set_right):
    # is_sub_set = set_left.is_subset(set_right)
    #    difference_left = set_left - set_right
    #    difference_right = set_right - set_right
    #    self.assertEquals(difference_left, sympy.EmptySet)
    #    self.assertEquals(difference_right, sympy.EmptySet)
    # self.assertTrue(is_sub_set)

    def test_whitespaces_in_intervals(self):
        expression_unparsed = '(-\\infty,3]\\ \\cap\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ (-\\infty,-5)\\ \\ \\ \\ \\ \\ \\ \\ \\cup\\ \\ \\ \\ \\ \\ \\ \\ (-5,5)\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\cup\\ (5,\\infty)'
        self.assertEquals(len(Expression(expression_unparsed).sympy_expr.args), 2)
        self.assertEquals(Expression(expression_unparsed).sympy_expr.args[0], Interval.Lopen(-sympy.oo, 3))
        self.assertEquals(len(Expression(expression_unparsed).sympy_expr.args[1].args), 3)
        self.assertTrue(
            Expression(expression_unparsed).sympy_expr.args[1].args[0]._eval_Eq(Interval.open(-sympy.oo, -5)))
        self.assertTrue(Expression(expression_unparsed).sympy_expr.args[1].args[1]._eval_Eq(Interval.open(-5, 5)))
        self.assertTrue(Expression(expression_unparsed).sympy_expr.args[1].args[2]._eval_Eq(Interval.open(5, sympy.oo)))

    def test_correct_parsing_of_inequality_without_vee_inside(self):
        expression_unparsed = '[[x\\ge1 \\wedge |x-2|\\ge3] \\vee [x\\le1 \\wedge |x-2|\\le3]]'
        expression_parsed = Expression(expression_unparsed)
        self.assertTrue(isinstance(expression_parsed.sympy_expr, sympy.Or))
        self.assertEquals(len(expression_parsed.sympy_expr.args), 2)
        self.assertTrue(isinstance(expression_parsed.sympy_expr.args[0], sympy.And))
        self.assertEquals(str(expression_parsed.sympy_expr.args[0]), '(x >= 1) & (Abs(x - 2) >= 3)')
        self.assertTrue(isinstance(expression_parsed.sympy_expr.args[1], sympy.And))
        self.assertEquals(str(expression_parsed.sympy_expr.args[1]), '(x <= 1) & (Abs(x - 2) <= 3)')

    # def test_correct_parsing_of_inequality_with_vee_inside(self):
    #    expression_unparsed = '{x\\ge1 \\wedge {x-2\\ge3 \\vee x-2\\le-3}} \\vee {x\\le1 \\wedge |x-2|\\le3}'
    #    expression_parsed = Expression(expression_unparsed)
    #    # Example usage
    #    expr_str = 'x<1 \\wedge [x<2 \\vee [x<2 \\wedge x<3] \\vee x>5] \\wedge x<3'
    #    find_outermost_brackets(expr_str)
    #    self.assertTrue(isinstance(expression_parsed.sympy_expr, sympy.Or))
    #    self.assertEquals(len(expression_parsed.sympy_expr.args), 2)

    def test_obfuscate_expression_between_top_level_brackets(self):
        expr_str = '[x<2 \\vee [x<2 \\wedge x<3] \\vee x>5] \\vee [x<17]'
        expressions_in_top_level_brackets = find_outermost_brackets(expr_str)
        self.assertEqual(len(expressions_in_top_level_brackets), 2)
        self.assertEqual(expressions_in_top_level_brackets[0], '[x<2 \\vee [x<2 \\wedge x<3] \\vee x>5]')
        self.assertEqual(expressions_in_top_level_brackets[1], '[x<17]')

    def test_find_top_level_brackets(self):
        expr_str = '[x<2 \\vee [x<2 \\wedge x<3] \\vee x>5] \\vee [x<17]'
        expressions_in_top_level_brackets = find_outermost_brackets(expr_str)
        self.assertEqual(len(expressions_in_top_level_brackets), 2)
        self.assertEqual(expressions_in_top_level_brackets[0], '[x<2 \\vee [x<2 \\wedge x<3] \\vee x>5]')
        self.assertEqual(expressions_in_top_level_brackets[1], '[x<17]')

        expr_str = 'x<2 \\vee [x<2 \\wedge x<3] \\vee x>5'
        expressions_in_top_level_brackets = find_outermost_brackets(expr_str)
        self.assertEqual(len(expressions_in_top_level_brackets), 1)
        self.assertEqual(expressions_in_top_level_brackets[0], '[x<2 \\wedge x<3]')

        expr_str = '[x<2 \\wedge x<3 \\vee x>5]'
        expressions_in_top_level_brackets = find_outermost_brackets(expr_str)
        self.assertEqual(len(expressions_in_top_level_brackets), 1)
        self.assertEqual(expressions_in_top_level_brackets[0], '[x<2 \\wedge x<3 \\vee x>5]')

        expr_str = 'x<2 \\wedge x<3 \\vee x>5'
        expressions_in_top_level_brackets = find_outermost_brackets(expr_str)
        self.assertEqual(len(expressions_in_top_level_brackets), 0)

    def test_parsing_inside_brackets_and(self):
        and_expression_1 = '[x<1]'
        and_expression_2 = '[x<1 \\wedge x<2]'
        and_expression_3 = '[x\\le8 \\wedge x<1 \\wedge x\\ge3]'
        self.assertEqual(Expression(and_expression_1).sympy_expr, parse_latex('x<1'))
        self.assertEqual(Expression(and_expression_2).sympy_expr, sympy.And(parse_latex('x<1'), parse_latex('x<2')))
        self.assertEqual(Expression(and_expression_3).sympy_expr,
                         sympy.And(parse_latex('x\\leq8'), parse_latex('x<1'), parse_latex('x\\geq3')))

    def test_parsing_inside_brackets_or(self):
        or_expression_1 = '[x<1]'
        or_expression_2 = '[x<1  \\vee  x<2]'
        or_expression_3 = '[x\\le8    \\vee   x<1    \\vee   x\\ge3]'
        self.assertEqual(Expression(or_expression_1).sympy_expr, parse_latex('x<1'))
        self.assertEqual(Expression(or_expression_2).sympy_expr, sympy.Or(parse_latex('x<1'), parse_latex('x<2')))
        self.assertEqual(Expression(or_expression_3).sympy_expr,
                         sympy.Or(parse_latex('x\\leq8'), parse_latex('x<1'), parse_latex('x\\geq3')))

    def test_parsing_inside_brackets_or_nested(self):
        or_expression_1 = '[x<1 \\vee [  x<2  \\vee  x<3  ] \\vee [x<5]]'
        self.assertEqual(Expression(or_expression_1).sympy_expr,
                         sympy.Or(parse_latex('x<1'), parse_latex('x<2'), parse_latex('x<5'), parse_latex('x<3')))

        or_expression_2 = '[x<1 \\vee [x>2 \\vee x<3] \\vee [x<5 \\vee x\\le7]]'
        self.assertEqual(Expression(or_expression_2).sympy_expr,
                         sympy.Or(parse_latex('x<1'), parse_latex('x>2'), parse_latex('x<3'), parse_latex('x<5'),
                                  parse_latex('x\\leq7')))

        or_expression_3 = '[[x<2 \\vee x<3] \\vee [x<5 \\vee x>-18]]'
        self.assertEqual(Expression(or_expression_3).sympy_expr,
                         sympy.Or(parse_latex('x<2'), parse_latex('x<3'), parse_latex('x<5'), parse_latex('x>-18')))

        or_expression_4 = '[[x<2 \\vee    x<3]   \\vee [x<5 \\vee   [  x>-18 \\vee x>23]]]'
        self.assertEqual(Expression(or_expression_4).sympy_expr,
                         sympy.Or(parse_latex('x<2'), parse_latex('x<3'), parse_latex('x<5'), parse_latex('x>-18'),
                                  parse_latex('x>23')))

    def test_parsing_inside_brackets_and_nested(self):
        AND_expression_1 = '[x<1 \\wedge [  x<2  \\wedge  x<3  ] \\wedge [x<5]]'
        self.assertEqual(Expression(AND_expression_1).sympy_expr,
                         sympy.And(parse_latex('x<1'), parse_latex('x<2'), parse_latex('x<5'), parse_latex('x<3')))

        AND_expression_2 = '[x<1 \\wedge [x>2 \\wedge x<3] \\wedge [x<5 \\wedge x\\le7]]'
        self.assertEqual(Expression(AND_expression_2).sympy_expr,
                         sympy.And(parse_latex('x<1'), parse_latex('x>2'), parse_latex('x<3'), parse_latex('x<5'),
                                   parse_latex('x\\leq7')))

        AND_expression_3 = '[[x<2 \\wedge x<3] \\wedge [x<5 \\wedge x>-18]]'
        self.assertEqual(Expression(AND_expression_3).sympy_expr,
                         sympy.And(parse_latex('x<2'), parse_latex('x<3'), parse_latex('x<5'), parse_latex('x>-18')))

        AND_expression_4 = '[[x<2 \\wedge    x<3]   \\wedge [x<5 \\wedge   [  x>-18 \\wedge x>23]]]'
        self.assertEqual(Expression(AND_expression_4).sympy_expr,
                         sympy.And(parse_latex('x<2'), parse_latex('x<3'), parse_latex('x<5'), parse_latex('x>-18'),
                                   parse_latex('x>23')))

    def test_parsing_inside_brackets_ors_with_and_nested(self):
        expression_1 = '[[x<1 \\vee x<2] \\wedge [x<3 \\wedge x>-5]]'
        self.assertEqual(Expression(expression_1).sympy_expr,
                         sympy.And(
                             sympy.Or(parse_latex('x<1'), parse_latex('x<2')),
                             sympy.And(parse_latex('x<3'), parse_latex('x>-5')))
                         )

        expression_2 = '[[x<1 \\vee x<2] \\wedge [x<3 \\wedge [x>-5 \\vee x<-17]]]'
        self.assertEqual(Expression(expression_2).sympy_expr,
                         sympy.And(
                             sympy.Or(parse_latex('x<1'), parse_latex('x<2')),
                             sympy.And(
                                 parse_latex('x<3'),
                                 sympy.Or(parse_latex('x>-5'), parse_latex('x<-17'))))
                         )

    def test_parsing_inside_with_abs(self):
        expression = '[|x-1|<1 \\vee x>-59]'
        self.assertEqual(Expression(expression).sympy_expr, sympy.Or(parse_latex('x>-59'), parse_latex('|x-1|<1')))
        self.assertEqual(Expression(expression).sympy_expr, sympy.Or(parse_latex('|x-1|<1'), parse_latex('x>-59')))

        expression = '[|x-1|<1 \\vee |6-x|>2]'
        self.assertEqual(Expression(expression).sympy_expr, sympy.Or(parse_latex('|6-x|>2'), parse_latex('|x-1|<1')))

        expression = '[[|x-1|<1 \\wedge |10-x|<2] \\vee |6-x|>2]'
        self.assertEqual(Expression(expression).sympy_expr,
                         sympy.Or(parse_latex('|6-x|>2'),
                                  sympy.And(parse_latex('|x-1|<1'), parse_latex('|10-x|<2'))))

        expression = '[[|x-1|<1 \\wedge |10-x|<2] \\wedge [|6-x|>2 \\vee 8x\\le25]]'
        self.assertEqual(Expression(expression).sympy_expr,
                         sympy.And(sympy.Or(parse_latex('|6-x|>2'), parse_latex('8x\\leq25')),
                                   sympy.And(parse_latex('|x-1|<1'), parse_latex('|10-x|<2'))))

    def test_simple_inequalities(self):
        expression = 'x<1'
        self.assertEqual(Expression(expression).sympy_expr, parse_latex('x<1'))

        expression = '1<x'
        self.assertEqual(Expression(expression).sympy_expr, parse_latex('1<x'))

        expression = '1\\lex'
        self.assertEqual(Expression(expression).sympy_expr, parse_latex('1 \\leq x'))


        expression = '[x<1]'
        self.assertEqual(Expression(expression).sympy_expr, parse_latex('x<1'))

        expression = 'x<1 \\wedge x>0'
        self.assertEqual(Expression(expression).sympy_expr, sympy.And(parse_latex('x<1'), parse_latex('x>0')))

        expression = '[x<1 \\wedge x>0]'
        self.assertEqual(Expression(expression).sympy_expr, sympy.And(parse_latex('x<1'), parse_latex('x>0')))

        expression = '[[x<1] \\wedge [x>0]]'
        self.assertEqual(Expression(expression).sympy_expr, sympy.And(parse_latex('x<1'), parse_latex('x>0')))

    def test_parsing_inside_bounded_both_sides(self):
        expression = '0<x<5'
        self.assertEqual(Expression(expression).sympy_expr, sympy.And(parse_latex('0<x'), parse_latex('x<5')))

        expression = '6<x\\le15'
        self.assertEqual(Expression(expression).sympy_expr, sympy.And(parse_latex('6<x'), parse_latex('x\\leq15')))

        expression = '-6\\le x\\le22'
        self.assertEqual(Expression(expression).sympy_expr,
                         sympy.And(parse_latex('-6\\leq x'), parse_latex('x\\leq22')))

        expression = '30 \\ge x \\ge 12'
        self.assertEqual(Expression(expression).sympy_expr,
                         sympy.And(parse_latex('30\\geq x'), parse_latex('x \\geq 12')))

        expression = '0<|x-1|<5'
        self.assertEqual(Expression(expression).sympy_expr, sympy.And(parse_latex('0<|x-1|'), parse_latex('|x-1|<5')))

        expression = '[3<x<7 \\vee -2<|x-1|<7]'
        self.assertEqual(Expression(expression).sympy_expr,
                         sympy.Or(
                             sympy.And(parse_latex('3<x'), parse_latex('x<7')),
                             sympy.And(parse_latex('-2<|x-1|'), parse_latex('|x-1|<7'))
                         )
                         )

        expression = '[[3<x<7 \\vee -2\\le|x-1|<7] \\wedge [x>0]]'
        self.assertEqual(Expression(expression).sympy_expr,
                         sympy.And(sympy.Or(
                             sympy.And(parse_latex('3<x'), parse_latex('x<7')),
                             sympy.And(parse_latex('-2\\leq|x-1|'), parse_latex('|x-1|<7'))
                         ), parse_latex('x>0')
                         ))

    def test_resolve_exponential(self):
        exp = Expression("x=-1 \\vee x=-3")
        x = sympy.symbols('x')
        self.assertEqual(exp.sympy_expr, 'Eq(x, -1) | Eq(x, -3)')
