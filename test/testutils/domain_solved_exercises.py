from test.testutils.solved_exercise import SolvedExercise


class DomainExercises:

    @staticmethod
    def rational_domain_root_zero() -> SolvedExercise:
        name = "Dom(1/(x+x))"
        steps = [
            {'expression': 'Dom(1/(x+x))', 'variables': []},
            {'expression': 'Dom(1/(2x))', 'variables': []},
            {'expression': '\\left(-\\infty, 0\\right) \\cup \\left(0, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 2]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def square_root_domain() -> SolvedExercise:
        name = "Dom(sqrt(x - 3))"
        steps = [
            {'expression': 'Dom(sqrt(x - 3))', 'variables': []},
            {'expression': '\\left[3, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 2]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)


    @staticmethod
    def rational_domain_root_moved() -> SolvedExercise:
        name = "Dom(1/(x+3+x-x))"
        steps = [
            {'expression': 'Dom(1/(x+3+x-x))', 'variables': []},
            {'expression': 'Dom(1/(x+3))', 'variables': []},
            {'expression': '\\left(-\\infty, -3\\right) \\cup \\left(-3, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 2]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)
