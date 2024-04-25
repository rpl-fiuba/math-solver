from sympy.calculus.util import continuous_domain

from mathlearning.model.problem_type import ProblemType
from mathlearning.utils.logger import Logger
from sympy.core.function import Derivative
from sympy.abc import x
from sympy import latex, imageset, Lambda, denom, Intersection, solveset, numer
from sympy import Integral
from sympy import S

import sympy

from mathlearning.model.expression import Expression
from django.core.exceptions import SuspiciousOperation

logger = Logger.getLogger()

class EvaluateService:
    def evaluate_problem_input(self, expression: Expression, problem_type):
        logger.info("Starting problem input validation")

        if problem_type not in [type.value for type in ProblemType]:
            raise SuspiciousOperation('Invalid input type')

        try:
            if problem_type == ProblemType.DERIVATIVE.value:
                derivative = Derivative(expression.sympy_expr, 'x')
                return Expression(derivative.doit()).solve_derivatives().to_latex_with_derivatives()
            elif problem_type == ProblemType.FACTORISABLE.value:
                factorisable = expression.sympy_expr
                return latex(Expression(factorisable).factor())
            elif problem_type == ProblemType.DOMAIN.value:
                final_domain_denominator = S.Reals
                if denom(expression.sympy_expr) != 1:
                    singularities_denominator = solveset(denom(expression.sympy_expr), x, S.Reals)
                    domain_denominator = continuous_domain(denom(expression.sympy_expr), x, S.Reals)
                    final_domain_denominator = domain_denominator - singularities_denominator
                domain_numerator = continuous_domain(numer(expression.sympy_expr), x, S.Reals)
                return latex(Intersection(domain_numerator, final_domain_denominator))
            elif problem_type == ProblemType.IMAGE.value:
                return latex(imageset(Lambda(x, expression.sympy_expr), S.Reals))
            elif problem_type == ProblemType.INEQUALITY.value:
                return latex(expression.solve_inequality())
            elif problem_type == ProblemType.EXPONENTIAL.value:
                exponential = expression.sympy_expr
                return latex(Expression(exponential).equation_exp_ln(str(expression)))

            integral = Integral(expression.sympy_expr, x)
            return latex(integral.doit())

        except:
            logger.info("Invalid expression")
            raise SuspiciousOperation('Invalid expression')
