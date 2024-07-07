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

