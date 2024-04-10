from mathlearning.model.expression import Expression


class SolvedExercise:
    def __init__(self, name: str, steps: list, result: str, non_result_steps: list,
                 result_non_latex: str = None, steps_non_latex: list = None):
        self.name = name
        self.steps = steps
        self.result = result
        self.result_non_latex = result_non_latex
        self.steps_non_latex = steps_non_latex
        self.non_result_steps = non_result_steps

    def get_results_as_expressions(self):
        return list(
            map(
                lambda step: Expression(step['expression'], step['variables'], is_latex=False),
                self.steps_non_latex
            )
        )
    @staticmethod
    def as_expressions(list_to_convert, is_latex=True):
        return list(
            map(
                lambda expression_string: Expression(expression_string['expression'], is_latex=is_latex),
                list_to_convert
            )
        )
