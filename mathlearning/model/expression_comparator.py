import sympy

from mathlearning.model.expression import Expression, make_sympy_expr
from mathlearning.model.problem_type import ProblemType


class ExpressionComparator:

    @staticmethod
    def is_equivalent_to_with_domain(problem_type: ProblemType, original_expression: Expression, new_expression: Expression, domain) -> bool:
        if problem_type == ProblemType.INTERSECTION:
            return ExpressionComparator.is_equivalent_to_intersection_with_domain(original_expression, new_expression, domain)
        else:
            return original_expression.is_equivalent_to(new_expression)

    @staticmethod
    def is_equivalent_to(problem_type: ProblemType, original_expression: Expression, new_expression: Expression) -> bool:
        if problem_type == ProblemType.DOMAIN:
            return ExpressionComparator.__equivalent_for_domain__(original_expression, new_expression)
        elif problem_type == ProblemType.INEQUALITY:
            return ExpressionComparator.is_equivalent_to_for_inequality(original_expression, new_expression)
        elif problem_type == ProblemType.IMAGE:
            return ExpressionComparator.__equivalent_for_image__(original_expression, new_expression)
        elif problem_type == ProblemType.TRIGONOMETRY:
            return round(original_expression.sympy_expr, 3) == round(new_expression.sympy_expr, 3)
        elif problem_type == ProblemType.EXPONENTIAL:
            return ExpressionComparator.is_equivalent_to_for_exp(original_expression, new_expression)
        elif problem_type == ProblemType.INTERSECTION:
            return ExpressionComparator.is_equivalent_to_intersection_with_domain(original_expression, new_expression)
        else:
            return original_expression.is_equivalent_to(new_expression)

    @staticmethod
    def is_a_result_of(problem_type: ProblemType, original_expression: Expression, new_expression: Expression) -> bool:
        if problem_type == ProblemType.FACTORISABLE:
            return original_expression.is_equivalent_to(new_expression) and original_expression.matches_args_with(new_expression)
        elif problem_type == ProblemType.TRIGONOMETRY:
            return round(original_expression.sympy_expr, 2) == round(new_expression.sympy_expr, 2)
        elif problem_type == ProblemType.INEQUALITY:
            return ExpressionComparator.is_equivalent_to_for_inequality(original_expression,new_expression)
        elif problem_type == ProblemType.DOMAIN:
            return not new_expression.is_intersection_of_domains and original_expression.is_equivalent_to(new_expression)
        elif problem_type == ProblemType.EXPONENTIAL:
            return ExpressionComparator.is_equivalent_to_for_exp(original_expression,new_expression)
        elif problem_type == ProblemType.INTERSECTION:
            return ExpressionComparator.is_equivalent_to_intersection_with_domain(original_expression,new_expression)
        else:
            return original_expression.is_equivalent_to(new_expression)

    @staticmethod
    def is_a_result_of_with_domain(problem_type: ProblemType, original_expression: Expression, new_expression: Expression, domain) -> bool:
        if problem_type == ProblemType.INTERSECTION:
            return ExpressionComparator.is_equivalent_to_intersection_with_domain(original_expression, new_expression, domain)
        else:
            return original_expression.is_equivalent_to(new_expression)

    @staticmethod
    def __equivalent_for_domain__(original_expression: Expression, new_expression: Expression) -> bool:
        both_are_domain = original_expression.is_domain() and new_expression.is_domain()
        neither_is_domain = not original_expression.is_domain() and not new_expression.is_domain()
        if both_are_domain:
            original_inner_expression = original_expression.get_inner_function()
            new_inner_expression = new_expression.get_inner_function()
            return original_inner_expression.is_equivalent_to(new_inner_expression) and original_inner_expression.has_same_domain_as(new_inner_expression)
        elif new_expression.is_intersection_of_domains and not original_expression.is_domain():
            evaluated_domain = sympy.Reals
            inner_domains_from_new_expression = new_expression.sympy_expr.args
            for current_domain in inner_domains_from_new_expression:
                if isinstance(current_domain, sympy.Interval) or isinstance(current_domain, sympy.Union):
                    interval_from_current_domain = current_domain
                else:
                    interval_from_current_domain = Expression(current_domain).get_domain()
                evaluated_domain = sympy.Intersection(evaluated_domain, interval_from_current_domain)
            return original_expression.is_equivalent_to(Expression(evaluated_domain))
        elif neither_is_domain:
            return original_expression.is_equivalent_to(new_expression)
        else:
            return False

    @staticmethod
    def __equivalent_for_image__(original_expression: Expression, new_expression: Expression) -> bool:
        both_are_image = original_expression.is_image() and new_expression.is_image()
        neither_is_image = not original_expression.is_image() and not new_expression.is_image()
        if both_are_image:
            original_inner_expression = original_expression.get_inner_function()
            new_inner_expression = new_expression.get_inner_function()
            return original_inner_expression.has_same_image_as(new_inner_expression) and original_inner_expression.is_equivalent_to(new_inner_expression)
        elif neither_is_image:
            return original_expression.is_equivalent_to(new_expression)
        else:
            return False

    @staticmethod
    def is_equivalent_to_for_inequality(original_expression: Expression, new_expression: Expression) -> bool:
        original_is_inequality = str(original_expression).__contains__("<") or str(original_expression).__contains__(">")
        new_is_inequality = str(new_expression).__contains__("<") or str(new_expression).__contains__(">")

        both_are_inequality = original_is_inequality and new_is_inequality
        neither_is_inequality = not original_is_inequality and not new_is_inequality

        if both_are_inequality:
            result_for_new_inequality = new_expression.solve_inequality()
            return original_expression.solve_inequality() == result_for_new_inequality
        elif neither_is_inequality:
            return original_expression.is_equivalent_to(new_expression)
        else:
            return False

    @staticmethod
    def is_equivalent_to_for_exp(original_expression: Expression, new_expression: Expression) -> bool:
        original_is_equation = ((str(original_expression).__contains__("+") or str(original_expression).__contains__("-")) and str(original_expression).__contains__("*") and \
                                str(original_expression).__contains__("Eq"))\
                                or (str(original_expression).__contains__("**") and str(original_expression).__contains__("Eq")) \
                                or ((str(original_expression).__contains__("Eq") and not str(original_expression).__contains__("|") and not str(original_expression).__contains__("exp")) and \
                                (str(original_expression).split(",")[0].__contains__("x") and str(original_expression).split(",")[1].__contains__("x")))
        new_is_equation = ((str(new_expression).__contains__("+") or str(new_expression).__contains__("-")) and str(new_expression).__contains__("*") and str(new_expression).__contains__("Eq")) \
                          or (str(new_expression).__contains__("**") and str(new_expression).__contains__("Eq")) \
                          or ((str(new_expression).__contains__("Eq") and not str(new_expression).__contains__("|") and not str(new_expression).__contains__("exp")) and \
                              (str(new_expression).split(",")[0].__contains__("x") and str(new_expression).split(",")[1].__contains__("x")))

        both_are_equation = original_is_equation and new_is_equation
        neither_is_equation = not original_is_equation and not new_is_equation

        if both_are_equation:
            return original_expression.equation_exp_ln(str(original_expression)) == new_expression.equation_exp_ln(str(new_expression))
        elif neither_is_equation:
            original_expression = str(original_expression).replace("|", "\\vee")
            new_expression = str(new_expression).replace("|", "\\vee")
            if str(original_expression).__contains__("\\vee") and not str(new_expression).__contains__("\\vee"):
                return False
            elif str(new_expression).__contains__("\\vee") and not str(original_expression).__contains__("\\vee"):
                return False
            elif not str(original_expression).__contains__("\\vee") and not str(new_expression).__contains__("\\vee"):
                original = Expression(sympy.sympify(str(original_expression).split(",")[1][:-1])).sympy_expr.args
                new = Expression(sympy.sympify(str(new_expression).split(",")[1][:-1])).sympy_expr.args
                if len(original) == len(new) and len(new) == 0:
                    return Expression(sympy.sympify(str(original_expression).split(",")[1][:-1])) == Expression(sympy.sympify(str(new_expression).split(",")[1][:-1]))
                if len(original) == len(new):
                    equal = True
                    for i in original:
                        if str(i).__contains__("E"):
                            if i in new:
                                continue
                            else:
                                equal = False
                                break
                        else:
                            if float(i) in new:
                                continue
                            else:
                                equal = False
                                break
                    return equal
                else:
                    return False
            else:
                results_original = []
                results_new = []

                for i in str(original_expression).strip().split("\\vee"):
                    results_original.append(i.strip())
                for j in str(new_expression).split("\\vee"):
                    results_new.append(j.strip())

                if len(results_original) == len(results_new) and \
                        set(results_original).issubset(results_new):
                    return True
        else:
            return False

    @staticmethod
    def is_an_answer_for_intersection(some_expression: Expression):
        if 'varnothing' in str(some_expression):
            return True
        elif str(some_expression).__contains__('&'):
            return False
        elif str(some_expression).__contains__('|') and '[' not in str(some_expression):
            return True
        elif isinstance(some_expression.sympy_expr, sympy.Eq):
            args_eq = some_expression.sympy_expr.args
            left = str(args_eq[0]).replace('exp','e')
            right = str(args_eq[1]).replace('exp','e')
            if left.__contains__('x') and right.__contains__('x'):
                return False
            elif (left.__contains__('x') and 'x' not in right) and \
                    (left.strip() == 'x'):
                return True
            elif (right.__contains__('x') and 'x' not in left) and \
                    (right.strip() == 'x'):
                return True
            else:
                return False
        elif isinstance(some_expression.sympy_expr, sympy.Interval):
            return True
        else:
            return False


    @staticmethod
    def is_equivalent_to_intersection_with_domain(original_expression: Expression, new_expression: Expression) -> bool:
        both_are_equation = not ExpressionComparator.is_an_answer_for_intersection(original_expression) and \
                            not ExpressionComparator.is_an_answer_for_intersection(new_expression)
        neither_is_equation = ExpressionComparator.is_an_answer_for_intersection(original_expression) and \
                              ExpressionComparator.is_an_answer_for_intersection(new_expression)

        # si algo es una ecuacion y no es ni varnothing ni un intervalo ni Eq, está mal
        if ('Eq' not in str(original_expression) and 'varnothing' not in str(original_expression) and 'Interval' not in str(original_expression)) \
                or \
           ('Eq' not in str(new_expression) and 'varnothing' not in str(new_expression) and 'Interval' not in str(new_expression)):
            return False

        if both_are_equation:
            original_in_domain = original_expression.equation_exp_ln(str(original_expression))
            new_in_domain = new_expression.equation_exp_ln(str(new_expression))
            if isinstance(original_in_domain, sympy.Interval) and isinstance(new_in_domain, sympy.Interval):
                return original_in_domain == new_in_domain
            elif (isinstance(original_in_domain, sympy.Interval) and not isinstance(new_in_domain, sympy.Interval)) or \
                    (not isinstance(original_in_domain, sympy.Interval) and isinstance(new_in_domain, sympy.Interval)):
                return False
            if original_in_domain.__contains__("\\vee") and new_in_domain.__contains__("\\vee") and not\
                    (new_in_domain.__contains__("Eq") or original_in_domain.__contains__("Eq")):
                results_original = []
                results_new = []

                for i in str(original_in_domain).strip().split("\\vee"):
                    if 'sqrt' not in i:
                        number_i = i.split('=')[1].strip()
                        results_original.append(str(round(float(eval(number_i)),2)))
                    else:
                        number_i = i.split('=')[1].strip()
                        results_original.append(Expression(number_i).sympy_expr.evalf())
                for j in str(new_in_domain).split("\\vee"):
                    if 'sqrt' not in j:
                        number_j = j.split('=')[1].strip()
                        results_new.append(str(round(float(eval(number_j)),2)))
                    else:
                        number_j = j.split('=')[1].strip()
                        results_new.append(Expression(number_j).sympy_expr.evalf())

                if len(results_original) == len(results_new) and \
                        set(results_original).issubset(results_new):
                    return True
            else:
                return original_in_domain == new_in_domain
        elif neither_is_equation:
            if isinstance(original_expression.sympy_expr, sympy.Interval) and isinstance(new_expression.sympy_expr, sympy.Interval):
                return original_expression == new_expression
            elif (isinstance(original_expression.sympy_expr, sympy.Interval) and not isinstance(new_expression.sympy_expr, sympy.Interval)) or \
                    (not isinstance(original_expression.sympy_expr, sympy.Interval) and isinstance(new_expression.sympy_expr, sympy.Interval)):
                return False
            original_expression = str(original_expression).replace("|", "\\vee")
            new_expression = str(new_expression).replace("|", "\\vee")
            if str(original_expression).__contains__("\\vee") and not str(new_expression).__contains__("\\vee"):
                return False
            elif str(new_expression).__contains__("\\vee") and not str(original_expression).__contains__("\\vee"):
                return False
            elif not str(original_expression).__contains__("\\vee") and not str(new_expression).__contains__("\\vee"):
                if 'varnothing' in original_expression:
                    original = original_expression
                else:
                    original = Expression(sympy.sympify(str(original_expression).split(",")[1][:-1])).sympy_expr.args
                if 'varnothing' in new_expression:
                    new = new_expression
                else:
                    new = Expression(sympy.sympify(str(new_expression).split(",")[1][:-1])).sympy_expr.args
                if len(original) == len(new) and len(new) == 0:
                    return Expression(sympy.sympify(str(original_expression).split(",")[1][:-1])) == Expression(sympy.sympify(str(new_expression).split(",")[1][:-1]))
                if len(original) == len(new) and ('varnothing' not in original) and ('varnothing' not in new):
                    equal = True
                    for i in original:
                        if str(i).__contains__("E"):
                            if i in new:
                                continue
                            else:
                                equal = False
                                break
                        else:
                            if float(i) in new:
                                continue
                            else:
                                equal = False
                                break
                    return equal
                elif original.__contains__('varnothing') and new.__contains__('varnothing'):
                    return True
                elif (('varnothing' not in original) and new.__contains__('varnothing')) or \
                        (original.__contains__('varnothing') and ('varnothing' not in new)):
                    return False
                else:
                    return False
            else:
                results_original = []
                results_new = []

                for i in str(original_expression).strip().split("\\vee"):
                    if 'sqrt' not in i:
                        number_i = i.split(',')[1].strip().replace(')','')
                        results_original.append(str(round(float(eval(number_i)),2)))
                    else:
                        number_i = i.split(',')[1].strip()[:-1]
                        results_original.append(Expression(number_i).sympy_expr.evalf())
                for j in str(new_expression).split("\\vee"):
                    if 'sqrt' not in j:
                        number_j = j.split(',')[1].strip().replace(')','')
                        results_new.append(str(round(float(eval(number_j)),2)))
                    else:
                        number_j = j.split(',')[1].strip()[:-1]
                        results_new.append(Expression(number_j).sympy_expr.evalf())


                if len(results_original) == len(results_new) and \
                        set(results_original).issubset(results_new):
                    return True
        else:
            return False

