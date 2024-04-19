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

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def square_root_domain() -> SolvedExercise:
        name = "Dom(sqrt(x - 3))"
        steps = [
            {'expression': 'Dom(sqrt(x - 3))', 'variables': []},
            #{'expression': 'Dom(\\sqrt{(x - 3)})', 'variables': []},
            #{'expression': 'Dom(\\sqrt{\\left(x - 3 \\right)})', 'variables': []},
            {'expression': 'Dom(\\sqrt{\\left(\\frac{1}{x}\\cdot x\\cdot x-3\\right)})', 'variables': []},
            {'expression': '\\left[3, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)


    @staticmethod
    def rational_domain_root_moved() -> SolvedExercise:
        name = "Dom(1/(x+3+x-x))"
        steps = [
            {'expression': 'Dom(1/(x+3+x-x))', 'variables': []},
            {'expression': 'Dom(1/(x+3))', 'variables': []},
            {'expression': '\\left(-\\infty, -3\\right) \\cup \\left(-3, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def intermediate_results_as_intersection_of_domains() -> SolvedExercise:
        name = "Dom(\\sqrt{\\left(3-x\\right)}/(x^2-25))"
        steps = [
            {'expression': 'Dom(\\sqrt{\\left(3-x\\right)}/(x^2-25))', 'variables': []},
            {'expression': 'Dom(\\sqrt{\\left(3-x\\right)}) \\cap Dom(1/(x^2-25))', 'variables': []},
            {'expression': '\\left(-\\infty, 3\\right] \\cap Dom(1/(x^2-25))', 'variables': []},
            {'expression': 'Dom(\\sqrt{\\left(3-x\\right)}) \\cap \\left(-\\infty, -5\\right) \\cup \\left(-5, 5\\right) \\cup \\left(5, \\infty\\right)', 'variables': []},
            {'expression': '\\left(-\\infty, -5\\right) \\cup \\left(-5, 3\\right]', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def intermediate_results_as_intersection_of_three_domains() -> SolvedExercise:
        name = "Dom(\\sqrt{\\left(3-x\\right)}/((x^2-25)*(x+17)))"
        steps = [
            {'expression': 'Dom(\\sqrt{\\left(3-x\\right)}/((x^2-25)*(x+17)))', 'variables': []},
            {'expression': 'Dom(\\sqrt{\\left(3-x\\right)}) \\cap Dom(1/((x^2-25)*(x+17)))', 'variables': []},
            {'expression': 'Dom(\\sqrt{\\left(3-x\\right)}) \\cap Dom(1/(x^2-25)) \\cap Dom(1/(x+17))', 'variables': []},
            {'expression': '\\left(-\\infty, 3\\right] \\cap Dom(1/(x^2-25)) \\cap Dom(1/(x+17))', 'variables': []},
            {'expression': '\\left(-\\infty, 3\\right] \\cap \\left(-\\infty, -5\\right) \\cup \\left(-5, 5\\right) \\cup \\left(5, \\infty\\right) \\cap Dom(1/(x+17))', 'variables': []},
            {'expression': '\\left(-\\infty, 3\\right] \\cap Dom(1/(x^2-25)) \\cap \\left(-\\infty, -17\\right) \\cup \\left(-17, \\infty\\right)', 'variables': []},
            {'expression': '\\left(-\\infty, -17\\right) \\cup \\left(-17, -5\\right) \\cup \\left(-5, 3\\right]', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def intermediate_results_as_intersection_of_domains_combined_inside() -> SolvedExercise:
        name = "Dom(\\sqrt{\\left(10-x\\right)/x}/(x-2))"
        steps = [
            {'expression': 'Dom(\\sqrt{\\left(10-x\\right)/x}/(x-2))', 'variables': []},
            {'expression': 'Dom(\\sqrt{\\left(10-x\\right)/x}) \\cap Dom(1/(x-2))', 'variables': []},
            {'expression': 'Dom(\\sqrt{\\left(10-x\\right)}) \\cap Dom(\\sqrt{\\left(1\\right)/x}) \\cap Dom(1/(x-2))', 'variables': []},
            {'expression': '\\left(-\\infty, 10\\right] \\cap Dom(\\sqrt{\\left(1\\right)/x}) \\cap Dom(1/(x-2))', 'variables': []},
            {'expression': '\\left(-\\infty, 10\\right] \\cap \\left(0, \\infty\\right) \\cap Dom(1/(x-2))', 'variables': []},
            {'expression': '\\left(0, 10\\right] \\cap Dom(1/(x-2))', 'variables': []},
            {'expression': '\\left(0, 2\\right) \\cup \\left(2, 10\\right]', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)


    @staticmethod
    def intermediate_results_as_intersection_of_domains_in_sum_of_terms() -> SolvedExercise:
        name = "Dom(\\sqrt{\\left(x-5\\right)} + 1/(x-10))"
        steps = [
            {'expression': 'Dom(\\sqrt{\\left(x-5\\right)} + 1/(x-10))', 'variables': []},
            {'expression': 'Dom(\\sqrt{\\left(x-5\\right)}) \\cap Dom(1/(x-10))', 'variables': []},
            {'expression': '\\left[5, 10\\right) \\cup \\left(10, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)


    @staticmethod
    def intermediate_results_mixing_domains_and_intervals() -> SolvedExercise:
        name = "Dom(\\sqrt{\\left(x-5\\right)} + 1/(x-10))"
        steps = [
            {'expression': 'Dom(\\sqrt{\\left(x-5\\right)} + 1/(x-10))', 'variables': []},
            {'expression': 'Dom(\\sqrt{\\left(x-5\\right)}) \\cap Dom(1/(x-10))', 'variables': []},
            {'expression': '\\left[5, \\infty\\right) \\cap Dom(1/(x-10))', 'variables': []},
            {'expression': '\\left[5, 10\\right) \\cup \\left(10, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)
