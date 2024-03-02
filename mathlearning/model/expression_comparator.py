from mathlearning.model.expression import Expression, make_sympy_expr
from mathlearning.model.problem_type import ProblemType


class ExpressionComparator:

    @staticmethod
    def is_equivalent_to(problem_type: ProblemType, original_expression: Expression, new_expression: Expression) -> bool:
        if problem_type == ProblemType.DOMAIN:
            return ExpressionComparator.__equivalent_for_domain__(original_expression, new_expression)
        else:
            return original_expression.is_equivalent_to(new_expression)

    @staticmethod
    def is_a_result_of(problem_type: ProblemType, original_expression: Expression, new_expression: Expression) -> bool:
        if problem_type == ProblemType.FACTORISABLE:
            return original_expression.is_equivalent_to(new_expression) and original_expression.matches_args_with(new_expression)
        else:
            return original_expression.is_equivalent_to(new_expression)

    @staticmethod
    def __equivalent_for_domain__(original_expression: Expression, new_expression: Expression) -> bool:
        both_are_domain = original_expression.is_domain() and new_expression.is_domain()
        neither_is_domain = not original_expression.is_domain() and not new_expression.is_domain()
        if both_are_domain:
            original_inner_expression = original_expression.get_base_function_from_domain()
            new_inner_expression = new_expression.get_base_function_from_domain()
            return original_inner_expression.is_equivalent_to(new_inner_expression)
        elif neither_is_domain:
            return original_expression.is_equivalent_to(new_expression)
        else:
            return False
