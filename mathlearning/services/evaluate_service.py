from sympy.calculus.util import continuous_domain

from mathlearning.model.problem_type import ProblemType
from mathlearning.utils.logger import Logger
from sympy.core.function import Derivative
from sympy.abc import x
from sympy import latex, imageset, Lambda
from sympy import Integral
from sympy import S

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
                return latex(continuous_domain(expression.sympy_expr, x, S.Reals))
            elif problem_type == ProblemType.IMAGE.value:
                return latex(imageset(Lambda(x, expression.sympy_expr), S.Reals))
            elif problem_type == ProblemType.INEQUALITY.value:
                inequality = expression.sympy_expr
                return latex(Expression(inequality).inequality(str(expression)))

            integral = Integral(expression.sympy_expr, x)
            return latex(integral.doit())

        except:
            logger.info("Invalid expression")
            raise SuspiciousOperation('Invalid expression')
