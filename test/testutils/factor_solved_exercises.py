from test.testutils.solved_exercise import SolvedExercise


class FactorExercises:

    @staticmethod
    def rational_expression_with_mult() -> SolvedExercise:
        name = "(3x+12)(x-3)^2/((x^2-3x)(x^3-16x))"
        steps = [
            {'expression': '\\frac{(3x+12)}{(x^2-3x)}\\cdot\\frac{(x-3)^2}{(x^3-16x)}', 'variables': []},
            {'expression': '\\frac{(3x+12)}{(x^2-3x)}\\cdot\\frac{(x-3)^2}{(x^3-16x)}', 'variables': []},
            {'expression': '\\frac{3\\cdot(x+4)}{x\\cdot(x-3)}\\cdot\\frac{(x-3)^2}{x\\cdot(x^2-16)}', 'variables': []},
            {'expression': '\\frac{3(x-3)}{x^2(x-4)}', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def square_dif() -> SolvedExercise:
        name = "x^2-1"
        steps = [
            {'expression': 'x^2-1', 'variables': []},
            {'expression': '(x-1)\\cdot(x+1)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def square_binomial() -> SolvedExercise:
        name = "x^2+2x+1"
        steps = [
            {'expression': 'x^2+2x+1', 'variables': []},
            {'expression': '(x+1)^2', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def cube_expression() -> SolvedExercise:
        name = "x^3+x^2-2x"
        steps = [
            {'expression': 'x^3+x^2-2x', 'variables': []},
            {'expression': 'x\\cdot(x^2+x-2)', 'variables': []},
            {'expression': '(x^2-x)\\cdot(x+2)', 'variables': []},
            {'expression': 'x\\cdot(x-1)\\cdot(x+2)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def square_dif_2() -> SolvedExercise:
        name = "x^4-9x^2"
        steps = [
            {'expression': 'x^4-9x^2', 'variables': []},
            {'expression': '(x^2-3x)\\cdot(x^2+3x)', 'variables': []},
            {'expression': 'x^2\\cdot(x-3)\\cdot(x+3)', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

