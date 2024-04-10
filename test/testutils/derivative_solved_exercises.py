from test.testutils.solved_exercise import SolvedExercise


class DerivativeExercises:

    @staticmethod
    def derivative_e_plus_sin() -> SolvedExercise:
        name = "e + sen"
        steps = [
            {'expression': '\\frac{d(e^x.\\ x)}{dx}\\ +\\ \\frac{d(sen(x)* x^2)}{dx}', 'variables': []},
            {'expression': '\\frac{d(e^x)}{dx}* x\\ +\\ \\frac{d(x)}{dx}* e^x\\ +\\ \\frac{d(\\sin(x)* x^2)}{dx}', 'variables': []},
            {'expression': 'e^x* x\\ +\\ \\frac{d(x)}{dx}* e^x\\ +\\ \\frac{d(\\sin(x)* x^2)}{dx}', 'variables': []},
            {'expression': 'e^x* x\\ +\\ e^x\\ +\\ \\frac{d(\\sin(x)* x^2)}{dx}', 'variables': []},
            {'expression': 'e^x* x\\ +\\ e^x\\ +\\ \\frac{d(\\sin(x))}{dx}* x^2+\\sin(x)* \\frac{d(x^2)}{dx}', 'variables': []},
            {'expression': 'e^x* x\\ +\\ e^x\\ +\\ \\frac{d(\\sin(x))}{dx}* x^2+\\sin(x)* 2\\ * x', 'variables': []},
            {'expression': 'e^x* x\\ +\\ e^x\\ +\\ \\cos(x)* x^2+\\sin(x)* 2\\ * x', 'variables': []},
            {'expression': 'e^x* (1\\ +x)+\\ \\cos(x)* x^2+\\sin(x)* 2\\ * x', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 2]

        result = {'expression': 'e^x* (1\\ +x)+\\ \\cos(x)* x^2+\\sin(x)* 2\\ * x', 'variables': []}

        steps_non_latex = [
            {'expression': 'Derivative(x*exp(x), x) + Derivative(x**2*sin(x), x)', 'variables': []},
            {'expression': 'x*Derivative(exp(x), x) + exp(x)*Derivative(x, x) + Derivative(x**2*sin(x), x)', 'variables': []},
            {'expression': 'x*exp(x) + exp(x)*Derivative(x, x) + Derivative(x**2*sin(x), x)', 'variables': []},
            {'expression': 'x*exp(x) + exp(x) + Derivative(x**2*sin(x), x)', 'variables': []},
            {'expression': 'x*exp(x) + exp(x) + x**2 * Derivative(sin(x), x) + sin(x) * Derivative(x**2, x)', 'variables': []},
            {'expression': 'x*exp(x) + exp(x) + x**2 * Derivative(sin(x), x) + sin(x) * 2 * x', 'variables': []},
            {'expression': 'x**2*cos(x) + x*2*sin(x) + (x + 1)*exp(x)', 'variables': []}
        ]

        result_non_latex = {'expression': 'x**2*cos(x) + x*(2*sin(x)) + (x + 1)*exp(x)', 'variables': []}

        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    @staticmethod
    def derivative_sin_divided_by_cos() -> SolvedExercise:
        name = "sen / cos"
        steps = [
            {'expression': '\\frac{d(\\frac{sen(x)}{\\cos(x)})} {dx}', 'variables': []},
            {'expression': '\\frac{\\frac{d(sen(x))}{dx}* \\cos(x)\\ -\\ sen(x)\\ * \\ \\frac{d(\\cos(x))}{dx}}{\\cos ^2(x)}', 'variables': []},
            {'expression': '\\frac{\\cos^2(x)\\ +\\ sen^2(x)\\ }{\\cos ^2(x)}', 'variables': []},
            {'expression': '\\frac{1}{\\cos^2(x)}', 'variables': []}
        ]
        result = {'expression': '\\frac{1}{\\cos^2(x)}', 'variables': []}

        non_result_steps = steps[:len(steps) - 2]

        steps_non_latex = [
            {'expression': 'Derivative(sin(x)/cos(x), x)', 'variables': []},
            {'expression': '(-sin(x)*Derivative(cos(x), x) + cos(x)*Derivative(sin(x), x))/cos(x)**2', 'variables': []},
            {'expression': '(sin(x)**2 + cos(x)**2)/cos(x)**2', 'variables': []},
            {'expression': '1/(cos(x)**2)', 'variables': []}
        ]

        result_non_latex = {'expression': '1/(cos(x)**2)', 'variables': []}

        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)

    @staticmethod
    def sum_derivative_x2_derivative_sum_x_cos() -> SolvedExercise:
        name = "deriv x**2 + dervi suma x + cos"

        steps = [
            {'expression': '\\frac{d(x^2)}{dx}+\\frac{d(x\\ +\\cos(x))}{dx}', 'variables': []},
            {'expression': '\\frac{d(x^2)}{dx}+\\frac{d(x)}{dx}+\\frac{d(\\cos(x))}{dx}', 'variables': []},
            {'expression': '2* x+\\frac{d(x)}{dx}+\\frac{d(\\cos(x))}{dx}', 'variables': []},
            {'expression': '2* x+1+\\frac{d(\\cos(x))}{dx}', 'variables': []},
            {'expression': '2* x+1-\\sin(x)', 'variables': []}
        ]
        result = {'expression': '2  * x+1-\\sin(x)', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        result_non_latex = {'expression': '2*x + 1 - sin(x)', 'variables': []}
        steps_non_latex = [
            {'expression': 'Derivative(x**2, x) + Derivative(x + cos(x), x)', 'variables': []},
            {'expression': 'Derivative(x, x) + Derivative(x**2, x) + Derivative(cos(x), x)', 'variables': []},
            {'expression': '2*x + Derivative(x, x) + Derivative(cos(x), x)', 'variables': []},
            {'expression': '2*x + 1 + Derivative(cos(x), x)', 'variables': []},
            {'expression': '2*x + 1 - sin(x)', 'variables': []}
        ]

        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)


    @staticmethod
    def derivative_mult_of_three_elem() -> SolvedExercise:
        name = "multiplication of 3 elem"

        steps = [
            {'expression': 'x^2\\sin(x)\\frac{d(\\cos(x))}{dx}+\\cos(x)\\frac{d(x^2\\sin(x))}{dx}', 'variables': []},
            {'expression': 'x^2\\sin(x)\\ (-\\sin(x))+\\cos(x)\\frac{d(x^2\\sin(x))}{dx}', 'variables': []},
            {'expression': '-\\ x^2\\sin ^2(x)\\ +\\cos(x)\\frac{d(x^2\\sin(x))}{dx}', 'variables': []},
            {'expression': '- x^{2} \\sin^{2}{(x )} + (x^{2} \\frac{d}{d x} \\sin{(x )} + \\sin(x) \\frac{d}{d x} x^{2}) \\cos{(x )}', 'variables': []},
            {'expression': '- x^{2} \\sin^{2}{(x )} + (x^{2} \\frac{d}{d x} \\sin{(x )} + 2 x \\sin{(x )}) \\cos{(x )}', 'variables': []},
            {'expression': '- x^{2} \\sin^{2}{(x )} + (x^{2} \\cos{(x )} + 2 x \\sin{(x )}) \\cos{(x )}', 'variables': []}
        ]

        result = {'expression': '- x^{2} \\sin^{2}{(x )} + (x^{2} \\cos{(x )} + 2 x \\sin{(x )}) \\cos{(x )}', 'variables': []}

        non_result_steps = steps[:len(steps) - 1]

        steps_non_latex = [
            {'expression': 'x**2*(sin(x)*Derivative(cos(x), x)) + cos(x)*Derivative(x**2*sin(x), x)', 'variables': []},
            {'expression': 'x**2*((-sin(x))*sin(x)) + cos(x)*Derivative(x**2*sin(x), x)', 'variables': []},
            {'expression': '-x**2*sin(x)**2 + cos(x)*Derivative(x**2*sin(x), x)', 'variables': []},
            {'expression': '-x**2*sin(x)**2 + (x**2*Derivative(sin(x), x) + sin(x)*Derivative(x**2, x))*cos(x)', 'variables': []},
            {'expression': '-x**2*sin(x)**2 + (x**2*Derivative(sin(x), x) + sin(x)* 2 * x)*cos(x)', 'variables': []},
            {'expression': '-x**2*sin(x)**2 + (x**2*cos(x) + sin(x)* 2 * x)*cos(x)', 'variables': []}
        ]

        result_non_latex = {'expression': "x**2*(- sin(x)**2) + (x**2*cos(x) + sin(x)* 2 * x)*cos(x)", 'variables': []}

        return SolvedExercise(name, steps, result, non_result_steps, result_non_latex, steps_non_latex)
