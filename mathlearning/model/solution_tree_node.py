from mathlearning.model.expression_comparator import ExpressionComparator
from mathlearning.model.problem_type import ProblemType
from mathlearning.model.theorem import Theorem
from mathlearning.utils.logger import Logger
from mathlearning.model.expression import Expression
from typing import List
import sympy
from sympy.abc import x

logger = Logger.getLogger()

class SolutionTreeNode:
    def __init__(self, expression: Expression, theorem_applied_name: str, branches: List):
        self.expression = expression
        self.theorem_applied_name = theorem_applied_name
        self.branches = branches

    def explain_solution(self, depth):
        theorem = "None"
        if self.theorem_applied_name is not None:
            theorem = self.theorem_applied_name
        print(depth, ". Expression: " + self.expression.to_string(), ". Teorema aplicado: " + theorem)

        for branch in self.branches:
            branch.explain_solution(depth + 1)

    def to_latex(self):
        self.expression = self.expression.to_latex()
        for branch in self.branches:
            branch.to_latex()

    def to_json(self):
        branches = []
        for branch in self.branches:
            branches.append(branch.to_json())

        if self.theorem_applied_name is not None:
            theorem = self.theorem_applied_name
        else:
            theorem = 'none'

        return {
            'expression': self.expression.to_string(),
            'theorem_applied_name': theorem,
            'branches': branches
        }

    def get_theorem_names(self):
        names = self.get_theorem_names_rec(set())
        names.discard('none')
        return names

    def get_theorem_names_rec(self, accum):
        accum.add(self.theorem_applied_name)
        children_names = set()
        for branch in self.branches:
            children_names |= branch.get_theorem_names_rec(set())
        accum |= children_names
        return accum

    def __str__(self):
        return self.expression.to_string() + self.theorem_applied_name

    def new_expression_is_valid(self, previous_step, new_expression, problem_type: ProblemType):
        # TODO: fix going backwards bug
        return self.contains(new_expression, problem_type)

    def new_expression_is_valid_with_domain(self, previous_step, new_expression, problem_type: ProblemType, domain):
        return self.contains_with_domain(new_expression, problem_type, domain)

    def validate_new_expression(self, new_expression, previous_step, problem_type: ProblemType):
        hints = []
        is_valid = self.new_expression_is_valid(previous_step, new_expression, problem_type)

        if not is_valid:
            if problem_type == ProblemType.INEQUALITY or problem_type == ProblemType.EXPONENTIAL or problem_type == ProblemType.INTERSECTION:
                hints = []
            elif problem_type == ProblemType.FACTORISABLE:
                hints = self.get_hints_for_specific_problem_type(previous_step, problem_type)
            else:
                hints = self.get_hints(previous_step)
            return 'invalid', hints
        if self.is_a_result(new_expression, problem_type):
            if problem_type == ProblemType.FACTORISABLE and self.expression.is_equal_to(new_expression):
                return 'valid', hints
            else:
                return 'resolved', hints

        if problem_type == ProblemType.INEQUALITY or problem_type == ProblemType.EXPONENTIAL or problem_type == ProblemType.INTERSECTION:
            hints = []
        else:
            hints = self.get_hints(new_expression)

        return 'valid', hints

    def get_hints(self, current_expression) -> List[str]:
        current_expression_subtrees = self.get_sub_trees_with_root(current_expression)
        hints = set()
        for current_expression_subtree in current_expression_subtrees:
            for children in current_expression_subtree.branches:
                hints.add(children.theorem_applied_name)

        return list(hints)

    def get_hints_for_specific_problem_type(self, last_valid_step, problem_type):
        last_valid_step_expression = last_valid_step.sympy_expr
        if problem_type == ProblemType.FACTORISABLE:
            nums, denoms = self.get_terms(last_valid_step_expression)

            common_factor_hints = self.build_common_factor_hints(nums, denoms)
            if len(common_factor_hints) > 0:
                return common_factor_hints

            squared_binomial_hints = self.build_squared_binomial_hints(nums, denoms)
            if len(squared_binomial_hints) > 0:
                return squared_binomial_hints

            quadratic_difference_hints = self.build_quadratic_difference_hints(nums, denoms)
            if len(quadratic_difference_hints) > 0:
                return quadratic_difference_hints

            shared_root_hints = self.build_shared_root_hints(nums, denoms)
            if len(shared_root_hints) > 0:
                return shared_root_hints

        return []

    def build_common_factor_hints(self, nums, denoms):
        for term in nums:
            add_terms_in_term = self.get_add_terms(term)
            if len(add_terms_in_term) >= 1 and any(self.has_zeroed_root(add_term) for add_term in add_terms_in_term):
                return ['Sacar factor comun de x en un numerador']
        for term in denoms:
            add_terms_in_term = self.get_add_terms(term)
            if len(add_terms_in_term) >= 1 and any(self.has_zeroed_root(add_term) for add_term in add_terms_in_term):
                return ['Sacar factor comun de x en un denominador']
        return []

    def get_add_terms(self, expression):
        if isinstance(expression, sympy.Add):
            return [expression]
        else:
            add_terms = []
            if expression.args is not None and len(expression.args):
                for arg in expression.args:
                    add_terms = add_terms + self.get_add_terms(arg)
            return add_terms

    def has_zeroed_root(self, term):
        roots = list(sympy.solveset(sympy.simplify(term), x))
        if 0 in roots:
            return True
        return False

    def build_squared_binomial_hints(self, nums, denoms):
        for term in nums:
            if not isinstance(term, sympy.Pow) and sympy.degree(sympy.simplify(term), gen=x) == 2:
                roots = sympy.roots(sympy.simplify(term), gen=x)
                if len(roots) == 1:
                    return ['Factorizar el cuadrado del binomio en un numerador']
        for term in denoms:
            if not isinstance(term, sympy.Pow) and sympy.degree(sympy.simplify(term), gen=x) == 2:
                roots = sympy.roots(sympy.simplify(term), gen=x)
                if len(roots) == 1:
                    return ['Factorizar el cuadrado del binomio en un denominador']
        return []

    def build_quadratic_difference_hints(self, nums, denoms):
        for term in nums:
            if self.is_quadratic_difference(term) or any(self.is_quadratic_difference(arg) for arg in term.args):
                return ['Factorizar la diferencia de cuadrados en un numerador']
        for term in denoms:
            if self.is_quadratic_difference(term) or any(self.is_quadratic_difference(arg) for arg in term.args):
                return ['Factorizar la diferencia de cuadrados en un denominador']
        return []

    def is_quadratic_difference(self, term):
        degree = sympy.degree(sympy.simplify(term), gen=x)
        if not isinstance(term, sympy.Pow) and isinstance(term, sympy.Add) and degree > 0 and degree % 2 == 0:
            roots = list(sympy.roots(sympy.simplify(term), gen=x).keys())
            if len(roots) == 2 and roots[0] == -roots[1]:
                return True
        return False

    def build_shared_root_hints(self, nums, denoms):
        full_num = 1
        full_denom = 1
        for num in nums:
            full_num = sympy.Mul(full_num * num)
        for denom in denoms:
            full_denom = sympy.Mul(full_denom * denom)
        roots_num = sympy.solveset(full_num, symbol=sympy.Symbol('x'))
        roots_denom = sympy.solveset(full_denom, symbol=sympy.Symbol('x'))
        shared_roots = [root for root in roots_num if root in roots_denom]
        if len(shared_roots) > 0:
            return ['Factorizar el numerador y el denominador por x=' + str(
                shared_roots[0]) + ' para simplificar la expresión.']
        return []

    def get_terms(self, mul_expression):
        nums = []
        denoms = []
        if self.mul_has_denom_as_pow(mul_expression):
            nums.append(mul_expression.args[0])
            denoms.append(mul_expression.args[1].args[0])
        elif isinstance(mul_expression, sympy.Pow) and mul_expression.args[1] == -1:
            denoms.append(mul_expression.args[0])
        elif isinstance(mul_expression, sympy.Pow) and mul_expression.args[1] != -1:
            nums.append(mul_expression)
        elif isinstance(mul_expression, sympy.Add) or all(isinstance(arg, sympy.Integer) or isinstance(arg, sympy.Symbol) or self.is_non_negative_pow(arg) for arg in mul_expression.args):
            nums.append(mul_expression)
        else:
            for inner_mul in mul_expression.args:
                (aux_nums, aux_denoms) = self.get_terms(inner_mul)
                nums += aux_nums
                denoms += aux_denoms
        return (nums, denoms)

    def mul_has_denom_as_pow(self, mul_expression):
        return len(mul_expression.args) >= 2 and isinstance(mul_expression.args[1], sympy.Pow) and mul_expression.args[1].args[1] == -1

    def is_non_negative_pow(self, mul_expression):
        return len(mul_expression.args) >= 2 and isinstance(mul_expression.args[1], sympy.Pow) and mul_expression.args[1].args[1] > 0


    def has_binomial_square(self, last_valid_step):
        terms_to_analyze = []
        last_valid_step.sympy_expr



    def get_sub_trees_with_root(self, current_expression):
        if self.expression.is_equivalent_to(current_expression):
            return [self]
        if len(self.branches) == 0:
            return []
        accum = []
        for branch in self.branches:
            accum += branch.get_sub_trees_with_root(current_expression)
        return accum

    def contains(self, expression, problem_type=ProblemType.DERIVATIVE):
        to_check = [self]
        already_checked = set()
        while len(to_check) > 0:
            current = to_check.pop()
            if current.expression.to_string() not in already_checked:
                if ExpressionComparator.is_equivalent_to(problem_type, current.expression, expression) and \
                        current.expression.compare_variables(expression.variables):
                    return True

                if problem_type in [ProblemType.INTEGRAL, ProblemType.DERIVATIVE]:
                    current_replaced = current.expression.replace_variables()
                    expression_replaced = expression.replace_variables()
                    if ExpressionComparator.is_equivalent_to(problem_type, current_replaced, expression_replaced):
                        return True

                for branch in current.branches:
                    to_check.append(branch)
            already_checked.add(current.expression.to_string())
        return False

    def contains_with_domain(self, expression, problem_type, domain):
        to_check = [self]
        already_checked = set()
        while len(to_check) > 0:
            current = to_check.pop()
            if current.expression.to_string() not in already_checked:
                if ExpressionComparator.is_equivalent_to_with_domain(problem_type, current.expression, expression, domain) and \
                        current.expression.compare_variables(expression.variables):
                    return True

                if problem_type in [ProblemType.INTEGRAL, ProblemType.DERIVATIVE]:
                    current_replaced = current.expression.replace_variables()
                    expression_replaced = expression.replace_variables()
                    if ExpressionComparator.is_equivalent_to(problem_type, current_replaced, expression_replaced):
                        return True

                for branch in current.branches:
                    to_check.append(branch)
            already_checked.add(current.expression.to_string())
        return False

    def is_pre_simplification_step(self):
        if len(self.branches) == 1:
            branch = self.branches[0]
            if branch.theorem_applied_name in ['simplificacion', 'factor'] and len(branch.branches) == 0:
                return True
        return False

    def is_a_result(self, expression, type: ProblemType):
        to_check = [self]
        is_contained = False
        while len(to_check) > 0:
            current = to_check.pop()
            if ExpressionComparator.is_a_result_of(type, current.expression, expression):
                is_contained = True
                if not len(current.branches) == 0 and not current.is_pre_simplification_step():
                    return False
            for branch in current.branches:
                to_check.append(branch)

        return is_contained

    def get_amount_of_nodes(self):
        accum = [self]
        count = 0
        while len(accum) > 0:
            count += 1
            current = accum.pop()
            accum += current.branches
        return count

    # for debugging purposes
    def print_tree(self, level=0):
        ret = "\t" * level + 'Theorem: ' + self.theorem_applied_name + "\n"
        ret += "\t" * level + self.expression.to_expression_string() + "\n"
        if len(self.expression.variables) > 0:
            for variable in self.expression.variables:
                ret += "\t" * level + variable.to_print() + "\n"
        for branch in self.branches:
            ret += branch.print_tree(level + 1)
        return ret
