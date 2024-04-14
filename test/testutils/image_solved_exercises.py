from test.testutils.solved_exercise import SolvedExercise


class ImageExercises:

    @staticmethod
    def full_real_image() -> SolvedExercise:
        name = "Img(x)"
        steps = [
            {'expression': 'Img(x)', 'variables': []},
            {'expression': '\mathbb{R}', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 2]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def positive_numbers_image() -> SolvedExercise:
        name = "Img(x^2)"
        steps = [
            {'expression': 'Img(x^2)', 'variables': []},
            {'expression': '\\left[0, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 2]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)
