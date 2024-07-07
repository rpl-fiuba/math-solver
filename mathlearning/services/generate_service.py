from typing import List

from sympy.calculus.util import continuous_domain
import random

from mathlearning.model.problem_type import ProblemType
from mathlearning.services.evaluate_service import EvaluateService
from mathlearning.services.result_service import ResultService
from mathlearning.utils.logger import Logger
from sympy.core.function import Derivative
from sympy.abc import x
from sympy import Function
from sympy import latex, imageset, Lambda, denom, Intersection, solveset, numer
from sympy import Integral
from sympy import S

import sympy

from mathlearning.model.expression import Expression
from django.core.exceptions import SuspiciousOperation

logger = Logger.getLogger()






class GenerateService:

    def __init__(self):
        self.evaluate_service = EvaluateService()
        self.result_service = ResultService()

    def generate_problem_input(self, problem_type: ProblemType):
        generated_problem_expression = self.__generate_problem_expression(problem_type)
        # generated_problem_result = self.evaluate_service.evaluate_problem_input(generated_problem_expression, problem_type)
        # (generated_problem_result_status, generated_problem_result) = result_service.resolve(problem_input, solution_tree, step_list, current_expression, problem_type)
        return generated_problem_expression

    def __generate_problem_expression(self, problem_type: ProblemType) -> Expression:
        if problem_type == ProblemType.TRIGONOMETRY:
            return Expression("", [])
        elif problem_type == ProblemType.FACTORISABLE:
            return self.__generate_factorisable_polynomial_expression()

    def __generate_linear_function(self):
        values_for_x_scalar = [1, 2, 3, 4, 5]
        values_for_constant = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        a = random.choice(values_for_x_scalar)
        b = random.choice(values_for_constant)
        f = a * x + b
        return f

    def __generate_quadratic_difference(self):
        values_for_constant = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        b = random.choice(values_for_constant)
        return (x + b) * (x - b)

    def __generate_factorisable_polynomial_expression(self) -> Expression:
        sympy_expr = 1
        variants = self.__get_variants_for_factorisable_polynomial_expression()
        for variant in variants:
            if variant == '0_binomial_square':
                binomial = self.__generate_linear_function()
                sympy_expr = sympy.simplify(sympy.Mul(sympy_expr, binomial, binomial, evaluate=True))
            elif variant == '1_quadratic_difference':
                quadratic_difference = self.__generate_quadratic_difference()
                sympy_expr = sympy.simplify(sympy.Mul(sympy_expr, sympy.simplify(quadratic_difference), evaluate=True))
            elif variant == '2_rooted_denominator':
                roots = list(solveset(sympy_expr, x, S.Reals))
                degree = sympy.degree(sympy_expr, gen=x)
                max_amount_of_roots_to_add = max(0, min(degree - 1, len(roots)))
                amount_of_roots_to_add = random.randint(1, max_amount_of_roots_to_add)
                rooted_denom = 1
                for i in range(amount_of_roots_to_add):
                    rooted_denom = sympy.Mul(rooted_denom * (x - random.choice(roots)), evaluate=False)
                sympy_expr = Expression(str(sympy_expr) + " / " + "(" + str(rooted_denom) + ")", is_latex=False).sympy_expr
        return Expression(sympy_expr)

    def __get_variants_for_factorisable_polynomial_expression(self) -> List[str]:
        variants = ['0_binomial_square', '1_quadratic_difference']
        amount_of_variants_to_pick = random.randint(2, len(variants))
        picked_variants = random.sample(variants, amount_of_variants_to_pick)
        picked_variants.append('2_rooted_denominator')
        picked_variants.sort()
        return picked_variants
