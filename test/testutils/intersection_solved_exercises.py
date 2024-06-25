from test.testutils.solved_exercise import SolvedExercise


class IntersectionExercises:

    @staticmethod
    def lineal_expression() -> SolvedExercise:
        name = "2x - 1 = 5x + 4"
        steps = [
            {'expression': '2x - 1 = 5x + 4', 'variables': []},
            {'expression': '2x - 5x = 4 + 1', 'variables': []},
            {'expression': '-3x = 5', 'variables': []},
            {'expression': 'x = -5/3', 'variables': []}
        ]

        invalid_steps = [
            {'expression': '2x + 5x = 4 + 1', 'variables': []},
            {'expression': '3x = 4 + 1', 'variables': []},
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
            {'expression': 'x*(x - 1) = 0', 'variables': []},
            {'expression': 'x=0 \\vee x=1', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '\\sqrt{x} = \\sqrt{x}', 'variables': []},
            {'expression': 'x=0', 'variables': []},
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
            {'expression': '\\frac{(x+4)}{(x+2)} = 0', 'variables': []},
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
            {'expression': '\\left[0, \\infty\\right)', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '\\left(0, \\infty\\right)', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)


