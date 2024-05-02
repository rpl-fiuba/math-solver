from test.testutils.solved_exercise import SolvedExercise


class ExponentialExercises:

    @staticmethod
    def ln_expression() -> SolvedExercise:
        name = "\\ln\\left(x^2 + 4x + 4\\right) = 0"
        steps = [
            {'expression': '\\ln\\left(x^2 + 4x + 4\\right) = 0', 'variables': []},
            {'expression': '\\ln\\left((x+3)*(x+1) + 1\\right) = 0', 'variables': []},
            {'expression': 'x^2+4x+4=1', 'variables': []},
            {'expression': '(x+3)*(x+1)=0', 'variables': []},
            {'expression': 'x=-1 \\vee x=-3', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def exp_expression() -> SolvedExercise:
        name = "\\exp\\left(x^2 + 4x + 4\\right) = 1"
        steps = [
            {'expression': '\\exp\\left(x^2 + 4x + 4\\right) = 1', 'variables': []},
            {'expression': '\\exp\\left((x+3)*(x+1) + 1\\right) = 1', 'variables': []},
            {'expression': 'x=-2', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def ln_with_square() -> SolvedExercise:
        name = "ln(x^2+1)=0"
        steps = [
            {'expression': '\\ln\\left(x^2 + 1\\right) = 0', 'variables': []},
            {'expression': 'x^2 + 1 = 1', 'variables': []},
            {'expression': 'x^2 = 0', 'variables': []},
            {'expression': 'x = 0', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)


