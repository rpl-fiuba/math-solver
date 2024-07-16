from test.testutils.solved_exercise import SolvedExercise


class IntersectionExercises:

    @staticmethod
    def lineal_expression() -> SolvedExercise:
        name = "2x - 1 = 5x + 4"
        steps = [
            {'expression': '2x - 1 = 5x + 4', 'variables': []},
            {'expression': '2x - 5x = 4 + 1', 'variables': []},
            {'expression': '-3x = 5', 'variables': []},
            {'expression': '-3x - 5 = 0', 'variables': []},
            {'expression': 'x=\\frac{-5}{3}', 'variables': []}
        ]

        invalid_steps = [
            {'expression': '2x + 5x = 4 + 1', 'variables': []},
            {'expression': '3x = 4 + 1', 'variables': []},
            {'expression': 'x = 5/3', 'variables': []},
            {'expression': 'x = -5/3 \\vee x=0', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def sqrt_expression() -> SolvedExercise:
        name = "sqrt{x} = x"
        steps = [
            {'expression': '\\sqrt{x} = x', 'variables': []},
            {'expression': 'x = x^2', 'variables': []},
            {'expression': '0 = x^2 - x', 'variables': []},
            {'expression': 'x^2 - x = 0', 'variables': []},
            {'expression': 'x*(x - 1) = 0', 'variables': []},
            {'expression': 'x=0 \\vee x=1', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '\\sqrt{x} = \\sqrt{x}', 'variables': []},
            {'expression': 'x=0', 'variables': []},
            {'expression': 'x^2 - x -1 = 0', 'variables': []},
            {'expression': 'x=0 \\vee x=-1', 'variables': []},
            {'expression': 'x*(x - 1) = 2', 'variables': []},
            #TODO: {'expression': '0 = x*(x^2 - x)', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def sqrt_expression_with_constant() -> SolvedExercise:
        name = "sqrt{x} = 2x+1"
        steps = [
            {'expression': '\\sqrt{x} = 2x+1', 'variables': []},
            {'expression': 'x = (2x+1)^2', 'variables': []},
            {'expression': '0 = (2x+1)^2 - x', 'variables': []},
            {'expression': '4x^2 + x + 1 = 0', 'variables': []},
            {'expression': '\\varnothing', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '\\sqrt{x} = 2x', 'variables': []},
            {'expression': 'x=0', 'variables': []},
            {'expression': '4x^2 + x + 1 = 3', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def sqrt_expression_hard() -> SolvedExercise:
        name = "\\sqrt{\\left(3x-8\\right)} = 4 - \\sqrt{x}"
        steps = [
            {'expression': '\\sqrt{\\left(3x-8\\right)} = 4 - \\sqrt{x}', 'variables': []},
            {'expression': '\\sqrt{\\left(3x-8\\right)} + \\sqrt{x} = 4', 'variables': []},
            {'expression': '3x - 8 = (4 - \\sqrt{x})^2', 'variables': []},
            {'expression': '3x - 8 = 4^2 - 2*4*\\sqrt{x} + x', 'variables': []},
            {'expression': '3x - 8 = 16 - 8*\\sqrt{x} + x', 'variables': []},
            {'expression': '2x - 8 = 16 - 8*\\sqrt{x}', 'variables': []},
            {'expression': '2x - 8 - 16 = - 8*\\sqrt{x}', 'variables': []},
            {'expression': '2x - 24 = - 8*\\sqrt{x}', 'variables': []},
            {'expression': '(2x - 24)/(-8) = \\sqrt{x}', 'variables': []},
            {'expression': '-x/4 + 3 = \\sqrt{x}', 'variables': []},
            {'expression': '(-x/4 + 3)^2 = x \\wedge x \\le 12', 'variables': []},
            {'expression': 'x^2/16 - 3/2*x + 9 = x \\wedge x \\le 12', 'variables': []},
            {'expression': 'x^2/16 - 3/2*x - x + 9 = 0 \\wedge x \\le 12', 'variables': []},
            {'expression': 'x^2/16 - 5/2*x + 9 = 0 \\wedge x \\le 12', 'variables': []},
            {'expression': 'x=4', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '(-x/4 + 3)^2 = x \\wedge x \\le 0', 'variables': []},
            {'expression': '(-x/4 + 3)^2 = x', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def sqrt_expression_with_two_conditions() -> SolvedExercise:
        name = "-x = \\sqrt{x}"
        steps = [
            {'expression': '-x = \\sqrt{x}', 'variables': []},
            {'expression': '(-x)^2 = x \\wedge [x\\ge0 \\wedge x\\le0]', 'variables': []},
            {'expression': '(-x)^2 - x = 0 \\wedge [x\\ge0 \\wedge x\\le0]', 'variables': []},
            {'expression': 'x^2 - x = 0 \\wedge [x\\ge0 \\wedge x\\le0]', 'variables': []},
            {'expression': 'x*(x - 1) = 0 \\wedge [x\\ge0 \\wedge x\\le0]', 'variables': []},
            {'expression': 'x=0', 'variables': []},
        ]

        invalid_steps = [
            {'expression': 'x=0 \\vee x=1', 'variables': []},
            {'expression': 'x*(x - 1) = 0 \\wedge x\\ge0', 'variables': []},
            {'expression': '(-x)^2 = x', 'variables': []},
            {'expression': '(-x)^2 - x = 0', 'variables': []},
            {'expression': 'x*(-x + 1) = 0', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def sqrt_expression_with_abs() -> SolvedExercise:
        name = "0.5x = |x-2|"
        steps = [
            {'expression': '0.5*x = \\left|x-2\\right|', 'variables': []},
            {'expression': '0.5*x - \\left|x-2\\right| = 0', 'variables': []},
            {'expression': '[[0.5*x - x + 2 = 0 \\wedge x \\ge 2] \\vee [0.5*x + x - 2 = 0 \\wedge x < 2]]', 'variables': []},
            {'expression': '[[- 0.5x + 2 = 0 \\wedge x \\ge 2] \\vee [1.5x - 2 = 0 \\wedge x < 2]]', 'variables': []},
            {'expression': '[[- 0.5x = -2 \\wedge x \\ge 2] \\vee [1.5x = 2 \\wedge x < 2]]', 'variables': []},
            {'expression': '[[0.5x = 2 \\wedge x \\ge 2] \\vee [x = 4/3 \\wedge x < 2]]', 'variables': []},
            {'expression': '[[x = 4 \\wedge x \\ge 2] \\vee [x = 4/3 \\wedge x < 2]]', 'variables': []},
            {'expression': '[[x = 4] \\vee [x = 4/3 \\wedge x < 2]]', 'variables': []},
            {'expression': 'x=4 \\vee x=\\frac{4}{3}', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '[[0.5*x - x + 2 = 0 \\wedge x \\le 2] \\vee [0.5*x + x - 2 = 0 \\wedge x < 2]]', 'variables': []},
            {'expression': '[[x = 4] \\vee [x = 4/3 \\wedge x > 2]]', 'variables': []},
            {'expression': 'x=4', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def rational_expression() -> SolvedExercise:
        name = "(x+5)/(x-2) = 5/(x+2) + 28/(x^2-4)"
        steps = [
            {'expression': '\\frac{x+5}{x-2} = \\frac{5}{x+2} + \\frac{28}{x^2-4}', 'variables': []},
            {'expression': '\\frac{x+5}{x-2} = \\frac{5}{x+2} + \\frac{28}{(x+2)*(x-2)}', 'variables': []},
            {'expression': '\\frac{x+5}{x-2} = \\frac{5(x-2)}{(x+2)*(x-2)} + \\frac{28}{(x+2)*(x-2)}', 'variables': []},
            {'expression': '\\frac{(x+5)*(x+2)}{(x-2)*(x+2)} = \\frac{5(x-2)}{(x+2)*(x-2)} + \\frac{28}{(x+2)*(x-2)}', 'variables': []},
            {'expression': '\\frac{(x+5)*(x+2)}{(x-2)*(x+2)} - \\frac{5(x-2)}{(x+2)*(x-2)} - \\frac{28}{(x+2)*(x-2)} = 0', 'variables': []},
            {'expression': '\\frac{(x+5)*(x+2) - 5(x-2) - 28}{(x-2)*(x+2)} = 0', 'variables': []},
            {'expression': '\\frac{x^2+7x+10 - 5(x-2) - 28}{(x-2)*(x+2)} = 0', 'variables': []},
            {'expression': '\\frac{x^2+7x+10 - 5x + 10 - 28}{(x-2)*(x+2)} = 0', 'variables': []},
            {'expression': '\\frac{x^2 + 2x - 8}{(x-2)*(x+2)} = 0', 'variables': []},
            {'expression': '\\frac{(x-2)*(x+4)}{(x-2)*(x+2)} = 0', 'variables': []},
            {'expression': '[\\frac{(x+4)}{(x+2)} = 0 \\wedge x < -2] \\vee [\\frac{(x+4)}{(x+2)} = 0 \\wedge 2 > x > -2] \\vee [\\frac{(x+4)}{(x+2)} = 0 \\wedge x > 2]', 'variables': []},
            {'expression': '\\frac{(x+4)}{(x+2)} = 0 \\wedge x < -2', 'variables': []},
            {'expression': '[x=-4] \\vee [\\frac{(x+4)}{(x+2)} = 0 \\wedge x > 2]', 'variables': []},
            {'expression': 'x=-4', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '\\frac{(x+4)}{(x+2)} = 0 \\wedge x > -2', 'variables': []},
            {'expression': 'x=-2', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def rational_expression_with_sqrt() -> SolvedExercise:
        name = "(2x*sqrt(x-1) - x^2/(2*sqrt(x-1)))/(x-1) = 0"
        steps = [
            {'expression': '\\frac{2x*\\sqrt{x-1} - \\frac{x^2}{2*\\sqrt{x-1}}}{x-1} = 0', 'variables': []},
            {'expression': '\\frac{2x*\\sqrt{x-1}*\\sqrt{x-1} - \\frac{x^2*\\sqrt{x-1}}{2*\\sqrt{x-1}}}{(x-1)*\\sqrt{x-1}} = 0', 'variables': []},
            {'expression': '\\frac{2x*(x-1) - \\frac{x^2}{2}}{(x-1)*\\sqrt{x-1}} = 0', 'variables': []},
            {'expression': '\\frac{2x*(x-1) - 1/2*x^2}{(x-1)*\\sqrt{x-1}} = 0', 'variables': []},
            {'expression': '\\frac{2x^2 - 2x - 0.5*x^2}{(x-1)*\\sqrt{x-1}} = 0', 'variables': []},
            {'expression': '\\frac{1.5*x^2 - 2x}{(x-1)*\\sqrt{x-1}} = 0', 'variables': []},
            {'expression': '\\frac{3*x^2 - 4x}{2*(x-1)*\\sqrt{x-1}} = 0', 'variables': []},
            {'expression': '[3*x^2 - 4x = 0 \\wedge x < 1] \\vee [x*(3x - 4) = 0 \\wedge x > 1]', 'variables': []},
            {'expression': '[3*x^2 - 4x = 0 \\wedge x < 1] \\vee [[x = 0 \\wedge x > 1] \\vee [3x - 4 = 0 \\wedge x > 1]]', 'variables': []},
            {'expression': '[3*x^2 - 4x = 0 \\wedge x < 1] \\vee [3x - 4 = 0 \\wedge x > 1]', 'variables': []},
            {'expression': '[[x = 0 \\wedge x < 1] \\vee [3x - 4 = 0 \\wedge x < 1]] \\vee [3x - 4 = 0 \\wedge x > 1]', 'variables': []},
            {'expression': '[x = 0 \\wedge x < 1] \\vee [3x - 4 = 0 \\wedge x > 1]', 'variables': []},
            {'expression': '[x = 0] \\vee [3x = 4 \\wedge x > 1]', 'variables': []},
            {'expression': '[x = 0] \\vee [x = 4/3 \\wedge x > 1]', 'variables': []},
            {'expression': 'x=0 \\vee x=4/3', 'variables': []}
        ]

        invalid_steps = [
            {'expression': '[3*x^2 - 4x = 0 \\wedge x < 0] \\vee [x*(3x - 4) = 0 \\wedge x > 1]', 'variables': []},
            {'expression': '[3*x^2 - 4x = 0 \\wedge x < 1] \\vee [x*(3x - 4) = 0 \\wedge x > 4/3]', 'variables': []},
            {'expression': 'x=4/3', 'variables': []},
            {'expression': 'x=0', 'variables': []},
            {'expression': 'x=0 \\vee x=1', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def expression_with_inf_solutions() -> SolvedExercise:
        name = "x = \\left|x\\right|"
        steps = [
            {'expression': 'x = \\left|x\\right|', 'variables': []},
            {'expression': '[x = x \\wedge x \\ge 0]\\ \\vee\\ [x = -x \\wedge x < 0]', 'variables': []},
            {'expression': '[x - x = 0 \\wedge x \\ge 0] \\vee [x + x = 0 \\wedge x < 0]', 'variables': []},
            {'expression': '[x \\ge 0] \\vee [2x = 0 \\wedge x < 0]', 'variables': []},
            {'expression': '[x \\ge 0] \\vee [x = 0 \\wedge x < 0]', 'variables': []},
            {'expression': '\\left[0, \\infty\\right)', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '\\left(0, \\infty\\right)', 'variables': []},
            {'expression': '[x + x = 0 \\wedge x \\ge 0] \\vee [x + x = 0 \\wedge x < 0]', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def expression_with_sqrt_answer() -> SolvedExercise:
        name = "(x-1)^2 = x"
        steps = [
            {'expression': '(x-1)^2 = x', 'variables': []},
            {'expression': 'x^2 - 2x + 1 = x', 'variables': []},
            {'expression': 'x^2 - 3x + 1 = 0', 'variables': []},
            {'expression': 'x=\\frac{3+\\sqrt{5}}{2}\\vee x=\\frac{3-\\sqrt{5}}{2}', 'variables': []},
        ]

        invalid_steps = [
            {'expression': 'x=\\frac{3+\\sqrt{5}}{2}', 'variables': []},
            {'expression': 'x^2 - 3x + 5 = 0', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def sqrt_expression_solution_varnothing() -> SolvedExercise:
        name = "x = x-2"
        steps = [
            {'expression': 'x = x-2', 'variables': []},
            {'expression': '\\varnothing', 'variables': []},
        ]

        invalid_steps = [
            {'expression': 'x = x/2 + 1', 'variables': []},
            {'expression': 'x = -2', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def ln_expression() -> SolvedExercise:
        name = "\\ln\\left(x^2 + 4x + 4\\right) = 0"
        steps = [
            {'expression': '\\ln\\left(x^2 + 4x + 4\\right) = 0', 'variables': []},
            {'expression': '\\ln\\left((x+3)*(x+1) + 1\\right) = 0', 'variables': []},
            {'expression': 'x^2+4x+4=1', 'variables': []},
            {'expression': '(x+3)*(x+1)=0', 'variables': []},
            {'expression': 'x=-3 \\vee x=-1', 'variables': []}
        ]

        invalid_steps = [
            {'expression': '\\ln\\left(x^2 + 4x + 4\\right)', 'variables': []},
            {'expression': '\\ln\\left(x^2 + 4x + 3\\right) = 0', 'variables': []},
            {'expression': 'x^2 + 4x + 4 = 0', 'variables': []},
            {'expression': 'x^2 + 4x = 1', 'variables': []},
            {'expression': 'x=-1 \\vee x=0', 'variables': []},
            {'expression': 'x=-1 \\vee x=-3 \\vee x=-3', 'variables': []},
            {'expression': 'x=-1', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def exp_expression() -> SolvedExercise:
        name = "\\exp\\left(x^2 + 4x + 4\\right) = 1"
        steps = [
            {'expression': 'e^{x^2 + 4x + 4} = 1', 'variables': []},
            {'expression': 'e^{(x+3)*(x+1) + 1} = 1', 'variables': []},
            {'expression': 'x=-2', 'variables': []}
        ]

        invalid_steps = [
            {'expression': 'e^{x^2 + 4x + 4} = 0', 'variables': []},
            {'expression': 'x^2 + 4x = 1', 'variables': []},
            {'expression': 'x=-1 \\vee x=0', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def exp_expression_with_sqrt() -> SolvedExercise:
        name = "\\exp\\left(\\sqrt{5x+5}\\right) = 7"
        steps = [
            {'expression': '\\e^{\\sqrt{5x+5}} = 7', 'variables': []},
            {'expression': '\\ln(\\e^{\\sqrt{5x+5}}) = \\ln(7)', 'variables': []},
            {'expression': '\\sqrt{5x+5} = \\ln(7)', 'variables': []},
            {'expression': '5x+5 = (\\ln(7))^2', 'variables': []},
            {'expression': '5x = (\\ln(7))^2 -5', 'variables': []},
            {'expression': 'x = \\frac{(\\ln(7))^2 -5}{5}', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '5x = (\\ln(7))^2 + 5', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def ln_with_square() -> SolvedExercise:
        name = "ln(x^2+1)=0"
        steps = [
            {'expression': '\\ln\\left(x^2 + 1\\right) = 0', 'variables': []},
            {'expression': 'x^2 + 1 = 1', 'variables': []},
            {'expression': 'x^2 = 0', 'variables': []},
            {'expression': 'x = 0', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '\\ln\\left(x^2 + 1\\right) = 1', 'variables': []},
            {'expression': 'x^2 = 1', 'variables': []},
            {'expression': 'x=-1 \\vee x=0', 'variables': []},
            {'expression': 'x=-1', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def ln_with_lineal_expression() -> SolvedExercise:
        name = "ln(2x+5)=1"
        steps = [
            {'expression': '\\ln\\left(2x + 5\\right) = 1', 'variables': []},
            {'expression': 'e^{\\ln\\left(2x + 5\\right)} = e^{1}', 'variables': []},
            {'expression': '2x + 5 = \\exp(1)', 'variables': []},
            {'expression': '2x = \\exp(1) - 5', 'variables': []},
            {'expression': 'x = \\frac{\\exp(1)}{2}-\\frac{5}{2}', 'variables': []}
        ]

        invalid_steps = [
            {'expression': '\\ln\\left(2x + 5\\right) = 0', 'variables': []},
            {'expression': '2x + 5 = \\exp(0)', 'variables': []},
            {'expression': '2x = \\exp(1)', 'variables': []},
            {'expression': 'x = \\exp(1)/2 - 5', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def ln_with_lineal_expression_2() -> SolvedExercise:
        name = "ln(x^2+5x+2)=1"
        steps = [
            {'expression': '\\ln\\left(x^2+5x+2\\right) = 1', 'variables': []},
            {'expression': 'e^{\\ln\\left(x^2+5x+2\\right)} = e^{1}', 'variables': []},
            {'expression': 'x^2+5x+2 = e^{1}', 'variables': []},
            {'expression': 'x^2+5x+2 - e = 0', 'variables': []},
            {'expression': 'x=\\frac{-\\sqrt{4*e + 17}}{2} - 2.5 \\vee x=\\frac{\\sqrt{4*e + 17}}{2} - 2.5', 'variables': []},
        ]

        invalid_steps = [
            {'expression': 'e^{\\ln\\left(x^2+5x+2\\right)} = 1', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)



    @staticmethod
    def ln_with_ln() -> SolvedExercise:
        name = "ln(x^2-2x+1)=ln(x-1)"
        steps = [
            {'expression': '\\ln(x^2-2x+1) = \\ln(x-1)', 'variables': []},
            {'expression': 'e^{\\ln(x^2-2x+1)} = e^{\\ln(x-1)} \\wedge x>1', 'variables': []},
            {'expression': 'x^2-2x+1 = x-1 \\wedge x>1', 'variables': []},
            {'expression': 'x^2-3x+2 = 0 \\wedge x>1', 'variables': []},
            {'expression': '[x = 2 \\wedge x>1] \\vee [x = 1 \\wedge x>1]', 'variables': []},
            {'expression': '[x = 2] \\vee [x = 1 \\wedge x>1]', 'variables': []},
            {'expression': 'x = 2', 'variables': []}
        ]

        invalid_steps = [
            {'expression': 'e^{\\ln(x^2-2x+1)} = e^{\\ln(x-1)}', 'variables': []},
            {'expression': 'x^2-2x+1 = x-1', 'variables': []},
            {'expression': 'x = 1 \\wedge x>1', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def ln_with_exp() -> SolvedExercise:
        name = "ln(x^2+1)=exp(x)"
        steps = [
            {'expression': '\\ln(x^2+1) = e^x', 'variables': []},
            {'expression': 'x = -0.768221459771013', 'variables': []}
        ]

        invalid_steps = [
            {'expression': 'x = -1', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def exp_with_exp() -> SolvedExercise:
        name = "exp(x^2)=exp(x)"
        steps = [
            {'expression': 'e^{x^2} = e^x', 'variables': []},
            {'expression': '\\ln(e^{x^2}) = \\ln(e^x)', 'variables': []},
            {'expression': 'x^2 = x', 'variables': []},
            {'expression': 'x^2 - x = 0', 'variables': []},
            {'expression': 'x*(x-1) = 0', 'variables': []},
            {'expression': 'x = 0 \\vee x=1', 'variables': []}
        ]

        invalid_steps = [
            {'expression': '\\ln(e^{x^2}) = e^x', 'variables': []},
            {'expression': 'x = 0', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def exp_with_x() -> SolvedExercise:
        name = "exp(x)=x"
        steps = [
            {'expression': 'e^{x} = x', 'variables': []},
            {'expression': 'e^{x} - x = 0', 'variables': []},
            {'expression': '\\varnothing', 'variables': []},
        ]

        invalid_steps = [
            {'expression': 'x=0', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)

    @staticmethod
    def lineal_frac() -> SolvedExercise:
        name = "3x^2 -5x = 2"
        steps = [
            {'expression': '3x^2 -5x = -2', 'variables': []},
            {'expression': '3x^2 -5x +2 = 0', 'variables': []},
            {'expression': 'x=1\\vee x=\\frac{2}{3}\\ ', 'variables': []},
        ]

        invalid_steps = [
            {'expression': 'x=1', 'variables': []},
            {'expression': 'x=\\frac{2}{3}\\ ', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)
