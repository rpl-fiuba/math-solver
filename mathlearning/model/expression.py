import inspect

import math
import sympy
import json

from regex import regex
from sympy import Symbol, S, FiniteSet, SymmetricDifference, imageset
from sympy.calculus.util import continuous_domain
from sympy.parsing.latex import parse_latex
from sympy.core.basic import preorder_traversal
from sympy import Integral
from sympy.core.function import Derivative, UndefinedFunction, Lambda
from sympy.parsing.sympy_parser import parse_expr
from sympy.simplify import simplify
from sympy import factor
import re
from sympy import symbols, solve_univariate_inequality, exp, sympify, oo, Interval, Union, Intersection, solve, ln, Eq, \
    log, E, sqrt, Abs
from sympy.abc import x

from mathlearning.utils.list.list_size_transformer import ListSizeTransformer
from mathlearning.utils.list.commutative_group_transformer import CommutativeGroupTransformer
from mathlearning.utils.list.non_commutative_group_transformer import NonCommutativeGroupTransformer
from mathlearning.utils.latex_utils import clean_latex, find_outermost_brackets, extract_inequality_sides, \
    clean_outermost_brackets_if_irrelevant
from typing import Union, List
from sympy import integrate
from mathlearning.utils.logger import Logger

from mathlearning.utils.sympy_utils import SympyUtils

logger = Logger.getLogger()
sympy_classes = tuple(x[1] for x in inspect.getmembers(sympy, inspect.isclass))
interval_symbols = ['\cup', '\cap']
set_symbols = ['\\mathbb{R}', '\\mathbb{Z}', '\\mathbb{o}']


def parse_latex_set(latex_set):
    if get_pure_set_symbol_if_match(latex_set) is None:
        pattern = r'\\mathbb{(R|Z)}-\{([^}]+(?:\}.*)?)\}'
        matches = re.findall(pattern, latex_set)
        number_group, finite_set = matches[0]
        unparsed_symbols = finite_set.split(',')
        parsed_symbols = list(map(parse_latex, unparsed_symbols))
        return SymmetricDifference(FiniteSet(*parsed_symbols), get_number_group_symbol(number_group))
    else:
        return get_number_group_symbol(get_pure_set_symbol_if_match(latex_set))


def get_number_group_symbol(number_group):
    if str(number_group) == 'R' or str(number_group).strip() == '\\mathbb{R}':
        return S.Reals
    elif str(number_group) == 'Z' or str(number_group).strip() == '\\mathbb{Z}':
        return S.Naturals
    elif str(number_group) == 'O' or str(number_group).strip() == '\\mathbb{o}':
        return S.EmptySet


def parse_latex_interval(latex_interval):
    parts = latex_interval.split("\cup")
    # Define lists to store the intervals
    intervals = []
    # Process each part to create intervals
    for part in parts:
        # Determine whether the interval is open or closed
        left_open = str.lstrip(part).startswith("(")
        right_open = str.rstrip(part).endswith(")")
        # Remove whitespace and brackets
        part = part.replace(" ", "").replace("[", "").replace("(", "").replace(")", "").replace("]", "")
        # Split into start and end
        start, end = part.split(",")
        # Evaluate start and end as expressions
        start = parse_interval_edge(start)
        end = parse_interval_edge(end)
        # Create the interval
        interval = sympy.Interval(start, end, left_open, right_open)
        # Append to the list of intervals
        intervals.append(interval)
    return sympy.Union(*intervals)


def parse_interval_edge(edge):
    if str(edge).strip() == '-\\infty':
        return sympify("-" + sympy.oo.__str__())
    elif is_sympy_exp(edge):
        return sympify(edge)
    else:
        return parse_latex(edge)


def contains_interval_symbol(formula):
    valid_starts = ["[", "\\left[", "(", "\\left("]
    valid_ends = [")", "\\right)", "]", "\\right]"]
    expected_mids = [","]

    has_valid_start = False
    has_valid_end = False
    has_expected_mids = False

    for valid_start in valid_starts:
        if formula.startswith(valid_start):
            has_valid_start = True
            break

    for valid_end in valid_ends:
        if formula.endswith(valid_end):
            has_valid_end = True
            break

    for expected_mid in expected_mids:
        if formula.count(expected_mid) == 1:
            has_expected_mids = True
            break

    if has_valid_start and has_valid_end and has_expected_mids:
        return True
    for symbol in interval_symbols:
        if symbol in formula:
            return True
    return False


def contains_set_symbol(formula):
    for symbol in set_symbols:
        if symbol in formula:
            return True
    return False


def get_pure_set_symbol_if_match(formula):
    for symbol in set_symbols:
        if symbol == formula.strip():
            return symbol
    return None


def is_sympy_exp(formula):
    return isinstance(formula, sympy_classes)


def is_intersection_of_intervals(formula):
    return str(formula).__contains__("cap")


def create_intersection_of_intervals(formula):
    interval_terms = formula.split("\\cap")
    expression = None
    for interval_term in interval_terms:
        parsed_term = Expression(interval_term.replace("\\ ", "").strip()).sympy_expr
        if expression is None:
            expression = parsed_term
        elif isinstance(expression, sympy.Mul):
            expression = sympy.Mul(*expression.args, parsed_term, evaluate=False)
        else:
            expression = sympy.Mul(expression, parsed_term, evaluate=False)
    return expression


def is_inequality(formula):
    return str(formula).__contains__("<") or str(formula).__contains__(">") or str(formula).__contains__(
        "\\leq") or str(formula).__contains__("\\geq")


or_separator = "\\vee"
and_separator = "\\wedge"
placeholder_prefix = "HOLDER_NUMBER_"


def parse_inequality(raw_expression):
    raw_expression = clean_outermost_brackets_if_irrelevant(raw_expression)
    if or_separator in raw_expression or and_separator in raw_expression:
        outermost_brackets_map = {}
        outermost_brackets = find_outermost_brackets(raw_expression)
        for idx, expression in enumerate(outermost_brackets):
            placeholder_key = placeholder_prefix + str(idx)
            outermost_brackets_map[placeholder_key] = expression
            raw_expression = raw_expression.replace(expression, placeholder_key)
        if or_separator in raw_expression and and_separator in raw_expression:
            raise (
                        "Invalid expression, only " + or_separator + " or " + and_separator + " are allowed inside same bracket level")
        elif or_separator in raw_expression:
            return parse_inner_inequalities(raw_expression, or_separator, outermost_brackets_map)
        elif and_separator in raw_expression:
            return parse_inner_inequalities(raw_expression, and_separator, outermost_brackets_map)
        else:
            return parse_inner_inequalities(raw_expression, and_separator, outermost_brackets_map)
    else:
        return parse_inner_inequalities(raw_expression, and_separator, {})


def parse_inner_inequalities(inner_expression_without_outmost_brackets, separator, outmost_brackets_map):
    inner_expressions = inner_expression_without_outmost_brackets.split(separator)
    final_expression = None
    for sub_expression in inner_expressions:
        sub_expression = sub_expression.strip()
        if sub_expression in outmost_brackets_map:
            sub_expression_parsed = parse_inequality(outmost_brackets_map[sub_expression])
        else:
            if len(extract_inequality_sides(sub_expression)) > 1:
                left_and_right_inequalities = extract_inequality_sides(sub_expression)
                left_parsed = parse_latex(left_and_right_inequalities[0])
                right_parsed = parse_latex(left_and_right_inequalities[1])
                sub_expression_parsed = sympy.And(left_parsed, right_parsed)
            else:
                sub_expression_parsed = parse_latex(sub_expression)
        if final_expression is None:
            final_expression = sub_expression_parsed
        else:
            if separator == or_separator:
                final_expression = sympy.Or(final_expression, sub_expression_parsed)
            elif separator == and_separator:
                final_expression = sympy.And(final_expression, sub_expression_parsed)
            else:
                raise Exception("Invalid separator: " + separator)
    return final_expression


def contains_exp_results(formula):
    return (formula.__contains__("=") and formula.__contains__("\\vee") and not \
        (formula.__contains__("<") or formula.__contains__(">") or formula.__contains__("["))) or \
           (formula.__contains__("Eq") and formula.__contains__("|")) or \
           (formula.__contains__("E") and formula.__contains__("+"))


def contains_intersection_results_with_condition(formula):
    return (formula.__contains__("=") and \
           formula.__contains__("\\wedge") and \
           (formula.__contains__("<") or formula.__contains__(">"))) or \
           (formula.__contains__("[") and formula.__contains__("\\vee") and formula.__contains__("="))
           # is_inequality(clean_latex(formula.split("\\wedge")[1].strip()))


def parse_latex_exp_results(formula):
    if formula.__contains__("Eq") and formula.__contains__("|"):
        return formula
    if formula.__contains__("\'"):
        formula = formula.replace("\'","")
    list_eq = formula.split("\\vee")
    result = []
    x = symbols("x")
    for i in list_eq:
        if i.__contains__("="):
            if i.__contains__('frac'):
                i = 'x=' + str(parse_latex(clean_latex(i.split("=")[1]))).strip()
            result.append(Eq(x, eval(i.strip().replace('\\','').split("=")[1])))
        elif i.__contains__("Eq"):
            result.append(eval(i.strip().replace('\\','')))

    result_str = ''
    for j in result:
        result_str = result_str + f' {j} |'
    result_final = result_str[:-1].strip()

    return result_final


def parse_latex_intersection_results_with_condition(formula):
    return parse_inequality(formula)


def make_sympy_expr(formula, is_latex):
    if isinstance(formula, str) and is_latex:
        if is_intersection_of_intervals(formula):
            return create_intersection_of_intervals(formula)
        elif contains_interval_symbol(formula):
            return parse_latex_interval(clean_latex(formula))
        elif contains_set_symbol(formula):
            return parse_latex_set(clean_latex(formula))
        elif contains_exp_results(formula):
            return parse_latex_exp_results(formula)
        elif contains_intersection_results_with_condition(formula):
            return parse_latex_intersection_results_with_condition(clean_latex(formula))
        else:
            clean_formula = clean_latex(formula)
            if is_inequality(clean_formula):
                return parse_inequality(clean_formula)
            else:
                if str(clean_formula).__contains__("Eq") and str(clean_formula).__contains__("*") and \
                        (not str(clean_formula).__contains__("leq") or not str(clean_formula).__contains__("geq")):
                    sympy_expr = parse_expr(formula)
                else:
                    sympy_expr = parse_latex(clean_formula)  # todo form
            sympy_expr = sympy_expr.subs(simplify(parse_expr("e")), parse_expr("exp(1)"))
            sympy_expr = sympy_expr.xreplace({parse_latex("\\ln(x)"): parse_expr('log(x,E)')})
    elif is_sympy_exp(formula):
        sympy_expr = formula
    elif isinstance(formula, str):
        evaluate = False
        if formula.__contains__("Eq"):
            evaluate = True
            if formula.__contains__("+") and not formula.__contains__("*") and \
                    not str(formula.split(",")[0]).__contains__('E'):
                acc = ''
                for i in formula.split("+"):
                    acc = acc + f'parse_expr(\'{str(i).strip()}\', evaluate={evaluate}) & '
                acc = acc.strip()[:-1]
                sympy_expr = eval(acc.strip())
            else:
                sympy_expr = parse_expr(formula, evaluate=evaluate)
        else:
            sympy_expr = parse_expr(formula, evaluate=evaluate)
    elif isinstance(formula, float) or isinstance(formula, int):
        sympy_expr = parse_expr(str(formula))
    else:
        raise (Exception("error while trying to create an Expression, unsuported formula type" + str(formula)))
    return sympy_expr


def make_complete_sympy_expr(sympy_expr, variables):
    complete_sympy_expr = sympy_expr

    # for variable in variables:
    #    complete_sympy_expr = complete_sympy_expr.subs(parse_expr(variable.tag), variable.expression.sympy_expr)

    return complete_sympy_expr


class Expression:

    def __init__(self, formula: Union['Expression', str], variables: List['ExpressionVariable'] = [], is_latex=True):
        self.variables = variables
        self.is_intersection_of_domains = is_intersection_of_intervals(formula)
        self.commutative_group_transformer = CommutativeGroupTransformer()
        self.non_commutative_group_transformer = NonCommutativeGroupTransformer()
        self.commutative_list_size_transformer = ListSizeTransformer(CommutativeGroupTransformer())
        self.non_commutative_list_size_transformer = ListSizeTransformer(NonCommutativeGroupTransformer())
        self.sympy_expr = make_sympy_expr(formula, is_latex)
        self.sympy_expr = make_complete_sympy_expr(self.sympy_expr, variables)

    def replace_variables(self) -> 'Expression':
        complete_sympy_expr = self.get_copy().sympy_expr
        for variable in self.variables:
            complete_sympy_expr = complete_sympy_expr.subs(parse_expr(variable.tag), variable.expression.sympy_expr)
        return Expression(complete_sympy_expr)

    def is_leaf(self) -> bool:
        return len(self.sympy_expr.args) == 0

    def is_commutative(self) -> bool:
        return self.sympy_expr.is_commutative

    def is_constant(self) -> bool:
        free_symbols = self.sympy_expr.expr_free_symbols
        for symbol in free_symbols:
            if isinstance(symbol, Symbol):
                return False
        return True

    def get_copy(self) -> 'Expression':
        return Expression(parse_expr(str(self.sympy_expr)), self.variables)

    # Search and derivate expressions
    def solve_derivatives(self) -> 'Expression':
        derivatives_solved = self.get_copy()
        for exp in preorder_traversal(self.sympy_expr):
            # TODO
            exp = Expression(exp)
            if exp.is_derivative():
                derivative_applied = exp.apply_derivative()
                derivatives_solved.replace(exp, derivative_applied)
        return derivatives_solved

    def replace_derivatives_for_json(self):
        replacements = []
        for exp in preorder_traversal(self.sympy_expr):
            # TODO
            expression = Expression(exp)
            if expression.is_derivative():
                content = Expression(exp.args[0]).to_latex()
                variable = Expression(exp.args[1][0]).to_latex()

                replacement = '\\frac{d(%s)}{d%s}' % (content, variable)
                replacements.append({"derivative": expression.to_latex(), "replacement": replacement})
        return replacements

    # possibilities of solving just 1 derivative
    def derivatives_solving_possibilities(self) -> List['Expression']:

        derivatives = []
        for exp in preorder_traversal(self.sympy_expr):
            exp = Expression(exp)
            if exp.is_derivative():
                derivatives.append(exp)

        possibilities = []
        for derivative in derivatives:
            derivative_solved = self.get_copy()
            derivative_solved.replace(derivative, derivative.apply_derivative())
            possibilities.append(derivative_solved)

        return possibilities

    # possibilities of solving just 1 integral
    def integrals_solving_possibilities(self) -> List['Expression']:

        integrals = []
        for exp in preorder_traversal(self.sympy_expr):
            exp = Expression(exp)
            if exp.is_integral():
                integrals.append(exp)

        possibilities = []
        for integral in integrals:
            applied_integral = integral.apply_integral()

            # without integral constant
            integral_solved = self.get_copy()
            integral_solved.replace(integral, applied_integral)
            possibilities.append(integral_solved)

            # with integral constant
            integral_solved = self.get_copy()
            integral_solved.replace(integral, applied_integral)
            c = sympy.symbols('c')
            expression_with_constant = Expression(sympy.Add(integral_solved.sympy_expr, c))
            possibilities.append(expression_with_constant)

        return possibilities

    @staticmethod
    def build_area_expression(problem_input):
        sides = problem_input["expression"]["sides"]
        left_side = next((side["value"] for side in sides if side["label"] == "leftSide"), None)
        right_side = next((side["value"] for side in sides if side["label"] == "rightSide"), None)
        bottom_side = next((side["value"] for side in sides if side["label"] == "bottomSide"), None)
        angles = problem_input["expression"]["angles"]
        left_angle = next((angle["value"] for angle in angles if angle["label"] == "leftAngle"), None)
        right_angle = next((angle["value"] for angle in angles if angle["label"] == "rightAngle"), None)
        top_angle = next((angle["value"] for angle in angles if angle["label"] == "topAngle"), None)
        height = math.sin((left_angle * math.pi) / 180) * left_side
        return Expression(bottom_side * height / 2)

    def is_integral(self):
        return isinstance(self.sympy_expr, sympy.Integral)

    def is_derivative(self) -> bool:
        return isinstance(self.sympy_expr, Derivative)

    def is_domain(self) -> bool:
        return hasattr(self.sympy_expr.func, 'name') and self.sympy_expr.func.name == 'Dom'

    def is_image(self) -> bool:
        return hasattr(self.sympy_expr.func, 'name') and self.sympy_expr.func.name == 'Img'

    def is_interval(self) -> bool:
        return isinstance(self.sympy_expr, sympy.Union) or \
            isinstance(self.sympy_expr, sympy.Intersection) or \
            isinstance(self.sympy_expr, sympy.Interval)

    def is_integral(self) -> bool:
        return isinstance(self.sympy_expr, Integral)

    # This method will remove the higher function call
    # get_inner_function("Dom(1/3x)") --> 1/3x
    # get_inner_function("Img(cos(3x))") --> cos(3x)
    def get_inner_function(self) -> 'Expression':
        return Expression(make_sympy_expr(str(self.sympy_expr.args[0]), False))

    def apply_derivative(self) -> 'Expression':
        deriv = Derivative(self.sympy_expr.args[0], self.sympy_expr.args[1])
        return Expression(deriv.doit())

    def apply_integral(self) -> 'Expression':
        integrand = Expression(self.sympy_expr.args[0])
        if self.contains_derivative() or integrand.contains_integral():
            return self
        return Expression(integrate(self.sympy_expr.args[0], self.sympy_expr.args[1]))

    def simplify(self) -> 'Expression':
        copy = self.get_copy()
        return Expression(simplify(copy.sympy_expr))

    def factor(self) -> 'Expression':
        copy = self.get_copy()
        return Expression(factor(copy.sympy_expr))

    def result_in_domain(self, result):
        results = []
        for i in result.split("\\vee"):
            posible_value = i.split("=")[1].strip()
            if self.sympy_expr.contains(sympify(posible_value)):
                if isinstance(sympify(posible_value), sympy.Add):
                    results.append(f'x={posible_value}')
                else:
                    results.append(symbols(f'x={posible_value}'))
        final = str(list(set(results))).replace("[", "").replace("]", "").replace(",", " \\vee")
        try:
            if isinstance(eval(final), str):
                final = eval(final)
        except:
            return final
        return final

    def is_equal_to(self, expression):
        return self.matches_args_with(expression)

    def equation_exp_ln(self, ecuacion_str):
        x = symbols('x', real=True)
        condition = sympy.Reals
        if ecuacion_str == 'False':
            return '\\varnothing'
        if ecuacion_str == 'True':
            return sympy.Reals

        if isinstance(self.sympy_expr, sympy.And):
            condition_and = []
            for inner_condition in self.sympy_expr.args:
                if isinstance(inner_condition, Eq):
                    ecuacion_str = str(inner_condition)
                else:
                    condition_and.append(inner_condition)
            condition = Expression(sympy.And(*condition_and)).solve_inequality()
        # ((x < 2) & Eq(0.5*x + x - 2, 0)) | ((x >= 2) & Eq(-x + 0.5*x + 2, 0))
        if isinstance(self.sympy_expr, sympy.Or):
            solutions = []
            for inner_condition in self.sympy_expr.args:
                # ((x < 2) & Eq(0.5*x + x - 2, 0))
                if isinstance(inner_condition, sympy.And):
                    condition_and = []
                    for inner_condition_2 in inner_condition.args:
                        if isinstance(inner_condition_2, Eq):
                            ecuacion_str = str(inner_condition_2)
                        else:
                            condition_and.append(inner_condition_2)
                    condition = Expression(sympy.And(*condition_and)).solve_inequality()
                    maybe_solution = self.solve_expression_intersection_or_exponential(ecuacion_str, condition, x)
                    if maybe_solution != '':
                        solutions.append(maybe_solution)
                elif isinstance(inner_condition, Eq):
                    maybe_solution = self.solve_expression_intersection_or_exponential(str(inner_condition), condition, x)
                    if maybe_solution != '':
                        solutions.append(maybe_solution)
                else:
                    if str(inner_condition).__contains__('<') or str(inner_condition).__contains__('>') or \
                        str(inner_condition).__contains__('\\ge') or str(inner_condition).__contains__('\\le'):
                        maybe_solution = Expression(str(inner_condition).replace('>=','\\ge').replace('<=','\\le')).solve_inequality()
                        solutions.append(maybe_solution)
            final = ''
            final_interval = sympy.EmptySet
            for i in solutions:
                if not isinstance(i, sympy.Interval):
                    final = final + i + "$"
                else:
                    final_interval = sympy.Union(*[final_interval,i])

            if final == '' and final_interval == sympy.EmptySet:
                final = '\\varnothing'
            elif final == '' and final_interval != sympy.EmptySet:
                final = final_interval
            else:
                if final != '' and final_interval != sympy.EmptySet:
                    final = final[:-1]
                    final = final.replace('$', ' \\vee ')
                    f_to_interval = sympy.EmptySet
                    for f in final.split('\\vee'):
                        f_to_interval = sympy.Union(*[Interval(eval(f.split('=')[1].strip()), eval(f.split('=')[1].strip())), f_to_interval])
                    final = f_to_interval
                else:
                    final = final[:-1]
                    final = final.replace('$', ' \\vee ')

            return final

        if self.solve_expression_intersection_or_exponential(ecuacion_str, condition, x) == '':
            final = '\\varnothing'
        else:
            final = self.solve_expression_intersection_or_exponential(ecuacion_str, condition, x)

        return final

    def solve_expression_intersection_or_exponential(self, ecuacion_str, condition, x):
        try:
            soluciones = solve(eval(ecuacion_str), x)
        except NotImplementedError:
            x = symbols('x')
            soluciones = sympy.solveset(self.sympy_expr, x, domain=Interval(-oo, oo))
            if isinstance(soluciones, sympy.ConditionSet):
                soluciones = sympy.nsolve(self.sympy_expr, x, (0,1))
                if not isinstance(soluciones, list):
                    soluciones = [soluciones]
            else:
                return Intersection(*[soluciones, condition])
        # [x1, x2]
        final_sol = []
        for i in soluciones:
            if isinstance(i, sympy.Add):
                final_sol.append(f'x={i}')
            else:
                final_sol.append(symbols(f'x={i}'))
        final = str(list(set(final_sol))).replace("[", "").replace("]", "").replace(",", " \\vee").replace('\'','')
        try:
            if isinstance(eval(final), str):
                final = eval(final)
        except:
            if condition != sympy.Reals:
                return Expression(condition).result_in_domain(final)
            else:
                return final
        if condition != sympy.Reals:
            return Expression(condition).result_in_domain(final)
        else:
            return final

    def intersection_resolve(self, ecuacion_str):
        return self.equation_exp_ln(ecuacion_str)

    def is_direct_comparsion(self, condition):
        return isinstance(condition, sympy.LessThan) or isinstance(condition, sympy.StrictLessThan) or isinstance(
            condition, sympy.GreaterThan) or isinstance(condition, sympy.StrictGreaterThan)

    def solve_direct_comparison(self, direct_comparsion):
        return sympy.solve_univariate_inequality(direct_comparsion, x, relational=False)

    def solve_and(self, and_condition):
        result_interval = sympy.Reals
        for inner_condition in and_condition.args:
            if isinstance(inner_condition, tuple):
                partial_result_interval = self.solve_auxiliar_inequality(*inner_condition)
            elif isinstance(inner_condition, list):
                partial_result_interval = self.solve_auxiliar_inequality(inner_condition)
            else:
                partial_result_interval = self.solve_auxiliar_inequality([inner_condition])
            result_interval = sympy.Intersection(result_interval, partial_result_interval)
        return result_interval

    def solve_or(self, or_condition):
        result_interval = sympy.EmptySet
        for inner_condition in or_condition.args:
            if isinstance(inner_condition, tuple):
                partial_result_interval = self.solve_auxiliar_inequality(*inner_condition)
            elif isinstance(inner_condition, list):
                partial_result_interval = self.solve_auxiliar_inequality(inner_condition)
            else:
                partial_result_interval = self.solve_auxiliar_inequality([inner_condition])
            result_interval = sympy.Union(result_interval, partial_result_interval)
        return result_interval

    def solve_inequality(self):
        if isinstance(self.sympy_expr, sympy.And):
            return self.solve_and(self.sympy_expr)
        elif isinstance(self.sympy_expr, sympy.Or):
            return self.solve_or(self.sympy_expr)
        elif self.is_direct_comparsion(self.sympy_expr):
            return self.solve_direct_comparison(self.sympy_expr)
        else:
            raise Exception("Error while solving condition", str(self.sympy_expr))

    def solve_auxiliar_inequality(self, condition_list):
        result_interval = sympy.Reals
        for condition in condition_list:
            if isinstance(condition, sympy.And):
                partial_result_interval = self.solve_and(condition)
            elif isinstance(condition, sympy.Or):
                partial_result_interval = self.solve_or(condition)
            elif self.is_direct_comparsion(condition):
                partial_result_interval = self.solve_direct_comparison(condition)
            else:
                raise Exception("Error while solving condition", str(condition))
            result_interval = sympy.Intersection(result_interval, partial_result_interval)
        return result_interval

    def is_user_defined_func(self) -> bool:
        return isinstance(self.sympy_expr.func, UndefinedFunction) and not self.is_derivative()

    def to_string(self) -> str:
        return json.dumps({
            'expression': str(self.sympy_expr),
            'variables': list(map(lambda variable: variable.to_json(), self.variables))
        })

    def to_json(self):
        return {
            'expression': str(self.sympy_expr),
            'variables': list(map(lambda variable: variable.to_json(), self.variables))
        }

    def to_expression_string(self):
        return str(self.sympy_expr)

    def to_latex(self) -> str:
        return sympy.latex(self.sympy_expr)

    def to_latex_with_derivatives(self) -> str:
        replacements = self.replace_derivatives_for_json()
        latex_exp = sympy.latex(self.sympy_expr)
        for replacement in replacements:
            latex_exp = latex_exp.replace(replacement['derivative'], replacement['replacement'])
        return latex_exp

    def is_equivalent_to(self, expression: 'Expression') -> bool:
        if expression.is_intersection_of_domains:
            return False
        if str(simplify(self.sympy_expr)) == str(simplify(expression.sympy_expr)) or \
                self == expression:
            return True
        self_simplifications = self.get_simplifications()
        expression_simplifications = expression.get_simplifications()

        # simplify both expressions and compare them
        # TODO use a set to reduce time complexity
        for self_simplification in self_simplifications:
            for expression_simplification in expression_simplifications:
                simplifications_match = str(self_simplification.sympy_expr) == str(expression_simplification.sympy_expr)
                if simplifications_match:
                    return True

        return False

    def has_same_domain_as(self, expression: 'Expression') -> bool:
        self_domain = Expression(self.get_domain())
        other_expression_domain = Expression(expression.get_domain())
        return self_domain.is_equivalent_to(other_expression_domain)

    def get_domain(self) -> Interval:
        return continuous_domain(self.sympy_expr, x, S.Reals)

    def get_domain_for_eq(self) -> Interval:
        function_eq = self.sympy_expr.args[0] - self.sympy_expr.args[1]
        #imageset(Lambda(x, self.get_inner_function().sympy_expr), S.Reals)
        return continuous_domain(function_eq, x, S.Reals)

    def has_same_image_as(self, expression: 'Expression') -> bool:
        self_image = Expression(imageset(Lambda(x, self.sympy_expr), S.Reals))
        other_expression_image = Expression(imageset(Lambda(x, expression.sympy_expr), S.Reals))
        return self_image.is_equivalent_to(other_expression_image)

    def matches_args_with(self, expression):
        return (len(sympify(self, evaluate=False).args) == len(sympify(expression, evaluate=False).args)) and \
            set(sympify(self, evaluate=False).args).issubset(sympify(expression, evaluate=False).args)

    def contains_user_defined_funct(self) -> bool:
        if self.is_user_defined_func():
            return True
        if len(self.get_children()) == 0:
            return False
        result = False
        for child in self.get_children():
            result = result or child.contains_user_defined_funct()
        return result

    def compare_func(self, expression: 'Expression') -> bool:
        return self.sympy_expr.func == expression.sympy_expr.func

    def has_all_free_symbols(self, free_symbols) -> bool:
        for free_symbol in free_symbols:
            if free_symbol.func == Symbol and not self.sympy_expr.has(free_symbol) and str(free_symbol) != "e":
                return False
        return True

    def free_symbols_match(self, expression: 'Expression') -> bool:
        result = self.has_all_free_symbols(expression.sympy_expr.expr_free_symbols)
        result &= expression.has_all_free_symbols(self.sympy_expr.expr_free_symbols)
        return result

    def children_amount(self) -> int:
        # TODO: handle this cases derivatives
        if self.is_derivative():
            return 1
        return len(self.get_children())

    def get_children(self) -> List['Expression']:
        children = []
        if self.is_derivative():
            children.append(Expression(self.sympy_expr.args[0]))
            return children
        for child in self.sympy_expr.args:
            expression_child = Expression(child)
            if self.is_commutative() and self.compare_func(expression_child):
                children.extend(expression_child.get_children())
            else:
                children.append(expression_child)
        return children

    # todo remove side effect
    def replace(self, to_replace: 'Expression', replacement: 'Expression'):
        to_replace_sympy = to_replace.sympy_expr
        replacement_sympy = simplify(replacement.sympy_expr)
        new_sympy_expr = self.sympy_expr.subs({to_replace_sympy: replacement_sympy})

        if (new_sympy_expr == self.sympy_expr and self.contains_derivative()):
            # TODO: workaround because sympy issue https://github.com/sympy/sympy/issues/5670
            new_sympy_expr = new_sympy_expr.xreplace({to_replace_sympy: replacement_sympy})

        if new_sympy_expr == self.sympy_expr:
            to_replace_sympy = simplify(to_replace.sympy_expr)
            self.sympy_expr = self.sympy_expr.subs({to_replace_sympy: replacement_sympy})
        else:
            self.sympy_expr = new_sympy_expr

    # Refactor
    def get_child_with_size_possibilities(self, size) -> List['Expression']:
        if self.is_commutative():
            transformer = self.commutative_group_transformer
        else:
            transformer = self.non_commutative_list_size_transformer
        possibilities = []
        combinations = transformer.combinations_of_n_elements(self.get_children(), size)

        for combination in combinations:
            sympy_elements = []
            for element in combination.elements:
                sympy_elements.append(element.sympy_expr)
            children_sympy = self.sympy_expr.func(*sympy_elements)
            possibilities.append(Expression(children_sympy))
        return possibilities

    def get_children_with_size(self, size) -> List[List['Expression']]:
        # TODO refactor
        if self.is_commutative():
            transformer = self.commutative_list_size_transformer
        else:
            transformer = self.non_commutative_list_size_transformer
        transformations = transformer.transform(list(self.sympy_expr.args), size)
        results = []
        for transformation in transformations:
            children_transformation = []
            for item in transformation:
                if len(item) == 1:
                    children_transformation.append(Expression(item[0]))
                elif len(item) > 1:
                    children_sympy = self.sympy_expr.func(*item)
                    children_transformation.append(Expression(children_sympy))
            results.append(children_transformation)
        return results

    def get_simplifications(self) -> List['Expression']:
        simplifications = []
        posible_simplifications = [
            Expression(sympy.cancel(self.sympy_expr)),
            Expression(sympy.simplify(self.sympy_expr)),
            Expression(sympy.factor(self.sympy_expr))
        ]
        if not self.is_interval() and not str(self).__contains__("&"):
            posible_simplifications.append(Expression(sympy.expand(self.sympy_expr)))

        original_integral_amount = self.amount_of_integrals()

        # TODO check how to do this (Integral(x,x) + Integral(cos(x), x) is simplified to Integral(x+cos(x))
        # This workaround solves that problem
        for posible_simplification in posible_simplifications:
            if posible_simplification.amount_of_integrals() == original_integral_amount:
                simplifications.append(posible_simplification)

        return simplifications

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Expression):
            are_formulas_equals = self.to_string() == other.to_string()

            if len(self.variables) != len(other.variables):
                return False

            if len(self.variables) == 0 and len(other.variables) == 0:  # TODO Lucas: add tests for it
                return are_formulas_equals

            self_variables_set = set((x.tag, x.expression) for x in self.variables)
            different_values = [x for x in other.variables if (x.tag, x.expression) not in self_variables_set]
            are_variables_equal = len(different_values) == 0

            return are_formulas_equals and are_variables_equal

        return False

    def __hash__(self):
        return hash(self.sympy_expr)

    def __str__(self):
        return str(self.sympy_expr)

    # TODO: refactor
    def get_operators_by_level(self):
        operators = {}
        to_check = [{
            'expression': self,
            'level': 0
        }]
        while len(to_check) > 0:
            current = to_check.pop()
            current_level = current['level']
            current_expression = current['expression']
            operator = current['expression'].sympy_expr.func

            if not isinstance(operator, UndefinedFunction) and not current_expression.is_constant() \
                    and not operator.is_symbol:

                if current_level not in operators:
                    operators[current_level] = []

                if SympyUtils.is_division(current_expression.sympy_expr):
                    operators[current_level].append('Division')

                operators[current_level].append(operator)
                to_check += list(
                    map(
                        lambda expression: {'expression': expression, 'level': current_level + 1},
                        current['expression'].get_children()
                    )
                )

        return operators

    # TODO: refactor
    # Compares if all the operators or a sub_expression are contained and in the right level order
    def operators_and_levels_match(self, sub_expression: 'Expression'):
        self_operators = self.get_operators_by_level()
        sub_expression_operators = sub_expression.get_operators_by_level()

        if len(sub_expression_operators) == 0:
            return True

        # expression  x + x**(2+x) -- 0: [Add] ; 1: [Pow] ; 2: [Add]
        # sub_expression  x**(2+x) -- 0: [Pow] ; 1: [Add]
        # self_level is used  to find the starting point where the first Pow of sub_expression is.
        # in this example the only possible values are 0 and 1  since if we select 2 as the starting level
        # we have to match the 1: [Add] sub_expression level with an non existent level.
        for self_level in range(0, len(self_operators) - len(sub_expression_operators) + 1):
            first_sub_expression_operator = sub_expression_operators[0][0]
            if first_sub_expression_operator in self_operators[self_level]:
                all_match = True
                # check if the rest of the levels match
                for self_level_to_check in range(self_level, self_level + len(sub_expression_operators)):
                    sub_level_to_check = self_level_to_check - self_level
                    sub_level_operators = sub_expression_operators[sub_level_to_check]
                    for sub_level_operator in sub_level_operators:
                        if sub_level_operator not in self_operators[self_level_to_check]:
                            all_match = False
                if all_match:
                    return True
        return False

    # TODO: refactor
    def get_subtrees_with_root_func_by_level(self, expression: 'Expression'):
        subtrees = []
        func = expression.sympy_expr.func
        to_check = [{
            'expression': self,
            'level': 0
        }]
        while len(to_check) > 0:
            current = to_check.pop()
            current_level = current['level']
            if current['expression'].sympy_expr.func == func:
                subtrees.append(current)
            to_check += list(
                map(
                    lambda expression: {'expression': expression, 'level': current_level + 1},
                    current['expression'].get_children()
                )
            )
        return subtrees

    # TODO: refactor
    def get_depth(self):
        if self is None:
            return 0

        to_check = [{
            'expression': self,
            'depth': 1
        }]

        max = 0
        while len(to_check) > 0:
            current = to_check.pop()
            if current['depth'] > max:
                max = current['depth']
            if not current['expression'].is_user_defined_func():
                to_check += list(
                    map(
                        lambda expression: {'expression': expression, 'depth': current['depth'] + 1},
                        current['expression'].get_children()
                    )
                )
        return max

    def can_group_children(self):
        if self.sympy_expr.func in [sympy.Add, sympy.Mul]:
            return True
        return False

    def contains_derivative(self):
        for exp in preorder_traversal(self.sympy_expr):
            expression = Expression(exp)
            if expression.is_derivative():
                return True
        return False

    def contains_integral(self):
        for exp in preorder_traversal(self.sympy_expr):
            expression = Expression(exp)
            if expression.is_integral():
                return True
        return False

    def amount_of_integrals(self):
        count = 0
        for exp in preorder_traversal(self.sympy_expr):
            expression = Expression(exp)
            if expression.is_integral():
                count += 1
        return count

    def compare_variables(self, variables):
        for self_variable in self.variables:
            contained = False
            for variable in variables:
                if self_variable == variable:
                    contained = True
            if not contained:
                return False

        return True
