import json

import unittest

from mathlearning.mappers.solution_tree_mapper import SolutionTreeMapper
from mathlearning.model.expression import Expression
from mathlearning.model.problem_type import ProblemType
from mathlearning.model.solution_tree_node import SolutionTreeNode
from test.testutils.derivative_solved_exercises import DerivativeExercises

tree_byte_arr = ''  # TODO
exercise = DerivativeExercises.derivative_e_plus_sin()


# tree = SolutionTreeMapper.parse(json.loads(tree_byte_arr))


class TestSolutionTree(unittest.TestCase):

    def test_get_terms_single_fraction(self):
        node = SolutionTreeNode(Expression("x+1"),
                                'none',
                                [])

        (nums, denoms) = node.get_terms(Expression("(x+1)/(x+2)").sympy_expr)
        self.assertEquals(nums, [Expression("x+1").sympy_expr])
        self.assertEquals(denoms, [Expression("x+2").sympy_expr])

    def test_get_terms_only_numerator(self):
        node = SolutionTreeNode(Expression("x+1"),
                                'none',
                                [])
        (nums, denoms) = node.get_terms(Expression("x+1").sympy_expr)
        self.assertEquals(nums, [Expression("x+1").sympy_expr])
        self.assertEquals(denoms, [])

    def test_get_terms_only_denominator(self):
        node = SolutionTreeNode(Expression("x+1"),
                                'none',
                                [])
        (nums, denoms) = node.get_terms(Expression("1/(x+7)").sympy_expr)
        self.assertEquals(nums, [])
        self.assertEquals(denoms, [Expression("x+7").sympy_expr])

    def test_get_terms_multiple_fractions(self):
        node = SolutionTreeNode(Expression("x+1"),
                                'none',
                                [])

        (nums, denoms) = node.get_terms(Expression("((x+1)/(2x))*((x+1)^2/(x+2))*(x+5)").sympy_expr)
        self.assertEquals(nums, [Expression("x+1").sympy_expr, Expression("(x+1)^2").sympy_expr,
                                 Expression("x+5").sympy_expr])
        self.assertEquals(denoms, [Expression("2x").sympy_expr, Expression("x+2").sympy_expr])

    def test_get_terms_fractions_with_pows(self):
        node = SolutionTreeNode(Expression("x+1"),
                                'none',
                                [])

        (nums, denoms) = node.get_terms(Expression("(1/(7*x^3))*(x+1)^2").sympy_expr)
        self.assertEquals(nums, [Expression("(x+1)^2").sympy_expr])
        self.assertEquals(denoms, [Expression("7*x^3").sympy_expr])

    def test_get_hints_for_specific_problem_type_shared_root(self):
        expression = Expression("((x+2)/(2x)) * ((x+1)^2/(x+2)) * (x+5)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Factorizar el numerador y el denominador por x=-2 para simplificar la expresión.'])

    def test_get_hints_for_specific_problem_type_binomial_squared(self):
        expression = Expression("((x^2+2x+1)/(3x)) * (x+5)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Factorizar el cuadrado del binomio en un numerador'])

    def test_get_hints_for_specific_problem_type_binomial_squared_on_zero_should_not_return_any_hint(self):
        expression = Expression("((x^2)/(x+2)) * (x+5)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 0)

    def test_get_hints_for_specific_problem_type_binomial_squared_denominator(self):
        expression = Expression("((x+1)/(x^2+4x+4)) * (x+5)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Factorizar el cuadrado del binomio en un denominador'])


    def test_get_hints_for_specific_problem_type_quadratic_difference(self):
        expression = Expression("((x^2-4)/(x+2)) * (x+5)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Factorizar la diferencia de cuadrados en un numerador'])


    def test_get_hints_for_specific_problem_type_quadratic_difference_denominator(self):
        expression = Expression("(1/(x^2-4)) * (x+2)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Factorizar la diferencia de cuadrados en un denominador'])

    def test_get_hints_for_specific_problem_type_after_quadratic_difference(self):
        expression = Expression("1/((x-3)*(x+3)) * (x+3)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Factorizar el numerador y el denominador por x=-3 para simplificar la expresión.'])



    def test_get_hints_for_specific_problem_type_common_factor(self):
        expression = Expression("(1/(x^4-9x^2)) * (x+3)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Sacar factor comun de x en un denominador'])

    def test_get_hints_for_specific_problem_type_semi_common_factor(self):
        expression = Expression("((x*(x^3-9x))/(x+2)) * (x+3)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Sacar factor comun de x en un numerador'])


    def test_get_hints_for_specific_problem_type_common_factor_without_fraction(self):
        expression = Expression("x^2+2x")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Sacar factor comun de x en un numerador'])


    def test_get_hints_for_specific_problem_type_common_factor_without_fraction_nor_action(self):
        expression = Expression("x*(x+2)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 0)


    def test_get_hints_for_specific_problem_type_after_common_factor_get_squared_difference(self):
        expression = Expression("((x^2*(x^2-9))/(x+2)) * (x+3)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Factorizar la diferencia de cuadrados en un numerador'])

    def test_get_hints_for_specific_problem_type_common_factor_shared_root(self):
        expression = Expression("((x+2)/(x^2*(x-3)*(x+3))) * (x+3)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Factorizar el numerador y el denominador por x=-3 para simplificar la expresión.'])


    def test_get_hints_for_specific_problem_type_no_action(self):
        expression = Expression("((x+2)/(x^2*(x-3))) * (x+3)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.FACTORISABLE)
        self.assertTrue(len(hints) == 0)

    def test_get_hints_for_square_expression_intersection(self):
        expression = Expression("\\sqrt{x}=5x+2")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Si tenés raíz cuadrada de f(x), recordá que debe cumplirse: \n 1. f(x) >= 0 \n 2. raiz(f(x)) >= 0'])

    def test_get_hints_for_square_expression_intersection_with_pow(self):
        expression = Expression("(x-\\sqrt{x})^2=5x+2")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 0)
        self.assertEquals(hints, [])

    def test_get_hints_for_square_expression_inequality(self):
        expression = Expression("\\sqrt{x}<5x+2")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INEQUALITY)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Si tenés raíz cuadrada de f(x), recordá que debe cumplirse: \n 1. f(x) >= 0 \n 2. raiz(f(x)) >= 0'])

    def test_get_hints_for_square_expression_domain(self):
        expression = Expression("\\sqrt{x+5}")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.DOMAIN)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Si tenés raíz cuadrada de f(x), recordá que debe cumplirse f(x)>=0'])

    def test_get_hints_for_square_expression_image(self):
        expression = Expression("\\sqrt{x+5}")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.IMAGE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Si tenés raíz cuadrada de f(x), siempre obtendrás valores mayores o iguales a 0'])

    def test_get_hints_for_abs_expression_image(self):
        expression = Expression("\\left|x+5\\right|")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.IMAGE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Si tenés |f(x)|, siempre obtendrás valores mayores o iguales a 0'])

    def test_get_hints_for_abs_expression_intersection(self):
        expression = Expression("\\left|x+5\\right| = 2x+1")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Si tenés |f(x)|, debes partir el ejercicio teniendo en cuenta dos casos: \n 1. f(x) >= 0 \n 2. f(x) < 0'])

    def test_get_hints_for_abs_expression_inequality(self):
        expression = Expression("\\left|x+5\\right| > 2x+1")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INEQUALITY)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Si tenés |f(x)|, debes partir el ejercicio teniendo en cuenta dos casos: \n 1. f(x) >= 0 \n 2. f(x) < 0'])

    def test_get_hints_for_trigonometry(self):
        expression = Expression("100.01")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.TRIGONOMETRY)
        self.assertTrue(len(hints) == 2)
        self.assertEquals(hints, ['La formula de Herón conociendo los 3 lados del triángulo', 'El Teorema de Pitágoras para determinar la altura del triángulo y luego calcular el área conociendo la base y altura'])

    def test_get_hints_for_trigonometry_negative_area(self):
        expression = Expression("-100.01")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.TRIGONOMETRY)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['El area no puede ser negativa'])

    def test_get_hints_for_log_expression_intersection(self):
        expression = Expression("\\ln\\left(x+5\\right) = 1")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Aplicar la función exponencial en ambos lados de la ecuación'])

    def test_dont_get_hints_for_log_expression_inequality(self):
        expression = Expression("\\ln\\left(x+5\\right) > x+5")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INEQUALITY)
        self.assertTrue(len(hints) == 0)
        self.assertEquals(hints, [])

    def test_get_hints_for_log_expression_inequality(self):
        expression = Expression("\\ln\\left(x+5\\right) \\le 1")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INEQUALITY)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Aplicar la función exponencial en ambos lados de la inecuación'])

    def test_dont_get_hints_for_log_expression_intersection(self):
        expression = Expression("\\ln\\left(x+5\\right) = x+5")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 0)
        self.assertEquals(hints, [])

    def test_get_hints_for_exp_expression_intersection(self):
        expression = Expression("e^{x+5} = 1")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Aplicar la función logaritmo en ambos lados de la ecuación'])

    def test_dont_get_hints_for_exp_expression_inequality(self):
        expression = Expression("e^{x+5} > x+5")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INEQUALITY)
        self.assertTrue(len(hints) == 0)
        self.assertEquals(hints, [])

    def test_get_hints_for_exp_expression_inequality(self):
        expression = Expression("e^{x+5} \\le 1")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INEQUALITY)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Aplicar la función logaritmo en ambos lados de la inecuación'])

    def test_dont_get_hints_for_exp_expression_intersection(self):
        expression = Expression("e^{x+5} = x+5")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 0)
        self.assertEquals(hints, [])

    def test_get_hints_for_exp_in_both_sides_for_inequality(self):
        expression = Expression("e^{x+5} \\le e^{1}")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INEQUALITY)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Quedarse sólo con los argumentos de la exponencial'])

    def test_get_hints_for_log_in_both_sides_for_inequality(self):
        expression = Expression("\\ln(x+5) \\le \\ln(x)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INEQUALITY)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Quedarse sólo con los argumentos del logaritmo'])

    def test_get_hints_for_log_in_both_sides_with_ln_of_exp_for_intersection(self):
        expression = Expression("\\ln(e^{x}) = \\ln(x)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Logaritmo y exponencial de la misma base se anulan'])

    def test_get_hints_for_exp_in_both_sides_for_intersection(self):
        expression = Expression("e^{x+5} = e^{1}")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Quedarse sólo con los argumentos de la exponencial'])

    def test_get_hints_for_log_in_both_sides_for_intersection(self):
        expression = Expression("\\ln(x+5) = \\ln(x)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Quedarse sólo con los argumentos del logaritmo'])

    def test_get_hints_for_log_of_exp_intersection(self):
        expression = Expression("\\ln(e^{x}) = 1")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INTERSECTION)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Logaritmo y exponencial de la misma base se anulan'])

    def test_get_hints_for_log_of_exp_inequality(self):
        expression = Expression("\\ln(e^{x}) < 1")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.INEQUALITY)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['Logaritmo y exponencial de la misma base se anulan'])

    def test_rational_expression_for_domain(self):
        expression = Expression("Dom(1/x)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.DOMAIN)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['El denominador no puede ser igual a 0'])

    def test_rational_expression_for_domain_without_Dom(self):
        expression = Expression("1/x")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.DOMAIN)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['El denominador no puede ser igual a 0'])

    def test_rational_expression_for_domain_without_Dom_2(self):
        expression = Expression("1/(x+5)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.DOMAIN)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['El denominador no puede ser igual a 0'])

    def test_frac_expression_for_domain_without_Dom(self):
        expression = Expression("\\frac{x}{x+5}")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.DOMAIN)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['El denominador no puede ser igual a 0'])

    def test_image_for_expression_positive(self):
        expression = Expression("Img(x^2)")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.IMAGE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['La función nunca es negativa'])

    def test_image_for_expression_positive_exp(self):
        expression = Expression("Img(e^{x})")
        node = SolutionTreeNode(expression,
                                'none',
                                [])
        hints = node.get_hints_for_specific_problem_type(expression, ProblemType.IMAGE)
        self.assertTrue(len(hints) == 1)
        self.assertEquals(hints, ['La función nunca es negativa'])



    # def test_is_a_result(self):
    #     tree = SolutionTreeMapper.parse(json.loads(tree_byte_arr))
    #     self.assertTrue(tree.is_a_result(Expression(exercise.result['expression'], exercise.result['variables'])))
    #
    # def test_is_a_result_steps_are_not_results(self):
    #     steps = exercise.get_results_as_expressions()
    #     non_result_steps = exercise.get_results_as_expressions()[:len(steps) - 1]
    #     for non_result in non_result_steps:
    #         step_is_result = tree.is_a_result(non_result)
    #         self.assertFalse(step_is_result)
    #         if step_is_result:
    #             print('Non result step returned is result True: ' + non_result.to_string())
    #
    # def test_is_a_result_pre_simplification_steps_are_results(self):
    #     result = Expression("x**2*cos(x) + x*(2*sin(x)) + (x + 1)*exp(x)", is_latex=False)
    #     self.assertTrue(tree.is_a_result(result))
    #
    # def test_get_subtree_with_root(self):
    #     pass
    #
    # def test_contains(self):
    #     all_steps_contained = True
    #     for i in range(0, len(exercise.steps)):
    #         step = exercise.steps[i]
    #         expression = Expression(step['expression'], step['variables'])
    #         all_steps_contained = all_steps_contained and tree.contains(expression)
    #         if not all_steps_contained:
    #             print('failed: ' + expression.to_string())
    #     self.assertTrue(all_steps_contained)
    #
    # def test_get_hints_result_step_should_not_return_hints(self):
    #     resultStep = Expression("x**2*cos(x) + x*(2*sin(x)) + (x + 1)*exp(x)", is_latex=False)
    #     hints = tree.get_hints(resultStep)
    #     self.assertEquals(hints, [])
    #
    # def test_get_hints_initial_step_should_return_hints(self):
    #     initialStep = Expression("Derivative(x*exp(x), x) + Derivative(x**2*sin(x), x)", is_latex=False)
    #     hints = tree.get_hints(initialStep)
    #     hints = list(set(map(lambda h: h.name, hints)))
    #     self.assertTrue('derivada del producto' in hints)
    #     self.assertTrue('resolver derivadas' in hints)
