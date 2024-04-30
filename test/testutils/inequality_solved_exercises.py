from test.testutils.solved_exercise import SolvedExercise


class InequalityExercises:

    @staticmethod
    def sample_exercise_with_initial_vee() -> SolvedExercise:
        name = "(x-1)\\cdot(\\left|x-2\\right|-3)\\ge0"
        steps = [
            {'expression': '(x-1)\\cdot(\\left|x-2\\right|-3)\\ge0', 'variables': []},
            {'expression': '[x-1\\ge0 \\wedge |x-2|-3\\ge0] \\vee [x-1\\le0 \\wedge |x-2|-3\\le0]', 'variables': []},
            {'expression': '[x\\ge1 \\wedge |x-2|\\ge3] \\vee [x\\le1 \\wedge |x-2|\\le3]', 'variables': []},
            {'expression': '[x\\ge1 \\wedge [x-2\\ge3 \\vee x-2\\le-3]] \\vee [x\\le1 \\wedge |x-2|\\le3]', 'variables': []},
            {'expression': '[x\\ge1 \\wedge [x-2\\ge3 \\vee x-2\\le-3]] \\vee [x\\le1 \\wedge -3\\le x-2 \\le 3]', 'variables': []},
            {'expression': '[x\\ge1 \\wedge [x\\ge5 \\vee x\\le-1]] \\vee [x\\le1 \\wedge -1\\le x \\le 5]', 'variables': []},
            {'expression': '[x\\ge1 \\wedge [x\\ge5 \\vee x\\le-1]] \\vee [-1\\le x \\le 1]', 'variables': []},
            {'expression': '[x\\ge5 \\wedge x\\ge-1] \\vee [-1\\le x \\le 1]', 'variables': []},
            {'expression': '[x\\ge5] \\vee [-1\\le x \\le 1]', 'variables': []},
            {'expression': 'x \\ge 5 \\vee [-1\\le x \\le 1]', 'variables': []},
            {'expression': 'x \\ge 5 \\vee -1\\le x \\le 1', 'variables': []},
            {'expression': '\\left[-1, 1\\right] \\cup \\left[5, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def single_abs_greater_than_equal() -> SolvedExercise:
        name = "|x-5|\\ge10"
        steps = [
            {'expression': '[|x-5|\\ge10]', 'variables': []},
            {'expression': '|x-5|\\ge10', 'variables': []},
            {'expression': '[x-5\\ge10] \\vee [x-5\\le-10]', 'variables': []},
            {'expression': 'x-5\\ge10 \\vee x-5\\le-10', 'variables': []},
            {'expression': '[x\\ge15] \\vee [x\\le-5]', 'variables': []},
            {'expression': 'x\\ge15 \\vee x\\le-5', 'variables': []},
            {'expression': '\\left(-\\infty, -5] \\cup \\left[15, \\infty\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)


    @staticmethod
    def single_abs_less_than_without_including_edge() -> SolvedExercise:
        name = "|x-9|<17"
        steps = [
            {'expression': '[|x-9|<17]', 'variables': []},
            {'expression': '|x-9|<17', 'variables': []},
            {'expression': '[x-9<17] \\wedge [x-9>-17]', 'variables': []},
            {'expression': 'x-9<17 \\wedge x-9>-17', 'variables': []},
            {'expression': '[x<26] \\wedge [x>-8]', 'variables': []},
            {'expression': 'x<26 \\wedge x>-8', 'variables': []},
            {'expression': '-8<x<26', 'variables': []},
            #{'expression': '\\left(-8, \\infty) \\cap \\left(-\\infty, 26\\right)', 'variables': []}, todo add parser from domain/image intersection of domains
            {'expression': '\\left(-8, 26\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)

    @staticmethod
    def double_limited_abs_inequality() -> SolvedExercise:
        name = "0<|x-1|<2"
        steps = [
            {'expression': '0<|x-1|<2', 'variables': []},
            {'expression': '0<|x-1| \\wedge |x-1|<2', 'variables': []},
            {'expression': '|x-1|>0 \\wedge |x-1|<2', 'variables': []},
            {'expression': '|x-1|>0 \\wedge |x-1|<2', 'variables': []},
            {'expression': '[[x-1>0 \\vee x-1<0] \\wedge |x-1|<2]', 'variables': []},
            {'expression': '[x-1>0 \\vee x-1<0] \\wedge |x-1|<2', 'variables': []},
            {'expression': '[x-1>0 \\vee x-1<0] \\wedge [x-1<2 \\wedge x-1>-2]', 'variables': []},
            {'expression': '[x-1>0 \\vee x-1<0] \\wedge x-1<2 \\wedge x-1>-2', 'variables': []},
            {'expression': '[x-1>0 \\vee x-1<0] \\wedge -2<x-1<2', 'variables': []},
            {'expression': '[x>1 \\vee x<1] \\wedge -1<x<3', 'variables': []},
            #{'expression': '\\left(-8, \\infty) \\cap \\left(-\\infty, 26\\right)', 'variables': []}, todo add parser from domain/image intersection of domains
            {'expression': '\\left(-1, 1\\right) \\cup \\left(1, 3\\right)', 'variables': []}
        ]

        non_result_steps = steps[:len(steps) - 1]

        return SolvedExercise(name, steps, steps[len(steps) - 1], non_result_steps)