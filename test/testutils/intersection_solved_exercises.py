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
            #{'expression': '[x = 4] \\vee [x = 4/3]', 'variables': []},
            {'expression': 'x=4 \\vee x=4/3', 'variables': []},
        ]

        invalid_steps = [
            {'expression': '[[0.5*x - x + 2 = 0 \\wedge x \\le 2] \\vee [0.5*x + x - 2 = 0 \\wedge x < 2]]', 'variables': []},
            {'expression': '[[x = 4] \\vee [x = 4/3 \\wedge x > 2]]', 'variables': []},
            {'expression': 'x=4', 'variables': []},
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps, invalid_steps=invalid_steps)



