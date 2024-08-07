import unittest
import sympy

from mathlearning.model.problem_type import ProblemType
from mathlearning.services.generate_service import GenerateService


class TestGenerateService(unittest.TestCase):
    generate_service = GenerateService()

    def test_factorisable_expression_has_numerator_and_denominator(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.FACTORISABLE)
        generated_numerator = sympy.numer(generated_expression.sympy_expr)
        generated_denominator = sympy.denom(generated_expression.sympy_expr)
        self.assertTrue(sympy.degree(generated_numerator, sympy.symbols('x')) >= 1)
        self.assertTrue(sympy.degree(generated_denominator, sympy.symbols('x')) >= 1)

    def test_factorisable_expression_can_actually_be_factorized(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.FACTORISABLE)
        generated_numerator = sympy.numer(generated_expression.sympy_expr)
        generated_denominator = sympy.denom(generated_expression.sympy_expr)
        factorized_expression = sympy.factor(generated_expression)
        factorized_expression_numerator = sympy.numer(factorized_expression)
        factorized_expression_denominator = sympy.denom(factorized_expression)

        self.assertTrue(sympy.degree(generated_numerator) > sympy.degree(factorized_expression_numerator))
        self.assertTrue(sympy.degree(generated_denominator) > sympy.degree(factorized_expression_denominator))

    def test_intersection_expression_is_an_equal(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.INTERSECTION)
        self.assertTrue(isinstance(generated_expression.sympy_expr, sympy.Eq))

    def test_intersection_has_x_on_both_sides(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.INTERSECTION)
        left_side = generated_expression.sympy_expr.args[0]
        right_side = generated_expression.sympy_expr.args[1]
        self.assertTrue(str(left_side).__contains__("x"))
        self.assertTrue(str(right_side).__contains__("x"))

    def test_inequality_has_right_operator(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.INEQUALITY)
        has_right_operator = isinstance(generated_expression.sympy_expr, sympy.StrictLessThan) or \
                             isinstance(generated_expression.sympy_expr, sympy.LessThan) or \
                             isinstance(generated_expression.sympy_expr, sympy.GreaterThan) or \
                             isinstance(generated_expression.sympy_expr, sympy.StrictGreaterThan)
        self.assertTrue(has_right_operator)

    def test_inequality_has_x_on_both_sides(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.INEQUALITY)
        left_side = generated_expression.sympy_expr.args[0]
        right_side = generated_expression.sympy_expr.args[1]
        self.assertTrue(str(left_side).__contains__("x"))
        self.assertTrue(str(right_side).__contains__("x"))


    def test_exponential_has_x_on_left_side_only(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.EXPONENTIAL)
        left_side = generated_expression.sympy_expr.args[0]
        right_side = generated_expression.sympy_expr.args[1]
        self.assertTrue(str(left_side).__contains__("x"))
        self.assertFalse(str(right_side).__contains__("x"))


    def test_exponential_matches_right_side_based_on_operator(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.EXPONENTIAL)
        full_expression = generated_expression.sympy_expr
        left_side = generated_expression.sympy_expr.args[0]
        right_side = generated_expression.sympy_expr.args[1]
        self.assertTrue(isinstance(full_expression, sympy.Eq))
        self.assertTrue((isinstance(left_side, sympy.exp) and right_side > 0) or (isinstance(left_side, sympy.log) and right_side in sympy.Interval(-5,5)))

    def test_exponential_has_x_on_left_side_only(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.EXPONENTIAL)
        left_side = generated_expression.sympy_expr.args[0]
        right_side = generated_expression.sympy_expr.args[1]
        self.assertTrue(str(left_side).__contains__("x"))
        self.assertFalse(str(right_side).__contains__("x"))


    def test_domain_is_not_a_comparison(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.DOMAIN)
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.Eq))
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.StrictLessThan))
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.LessThan))
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.GreaterThan))
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.StrictGreaterThan))

    def test_domain_has_denominator(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.DOMAIN)
        generated_numerator = sympy.numer(generated_expression.sympy_expr)
        generated_denominator = sympy.denom(generated_expression.sympy_expr)
        self.assertTrue(str(generated_numerator).__contains__("x"))
        self.assertTrue(str(generated_denominator).__contains__("x"))


    def test_image_is_not_a_comparison(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.IMAGE)
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.Eq))
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.StrictLessThan))
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.LessThan))
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.GreaterThan))
        self.assertFalse(isinstance(generated_expression.sympy_expr, sympy.StrictGreaterThan))

    def test_image_does_not_have_denominator(self):
        generated_expression = self.generate_service.generate_problem_input(ProblemType.IMAGE)
        generated_numerator = sympy.numer(generated_expression.sympy_expr)
        generated_denominator = sympy.denom(generated_expression.sympy_expr)
        self.assertTrue(str(generated_numerator).__contains__("x"))
        self.assertEquals(generated_denominator, 1)