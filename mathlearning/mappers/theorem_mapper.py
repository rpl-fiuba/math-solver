from mathlearning.model.integral.integrate_by_parts import IntegrateByPartsTheorem, IntegrateByPartsApplyTheorem, \
    IntegrateByPartsReplaceUVTheorem
from mathlearning.model.theorem import Theorem
from typing import List


class TheoremMapper:

    @staticmethod
    def theorems(theorems: List) -> List[Theorem]:
        parsed_theorems = []
        for theo in theorems:
            theo_object = TheoremMapper.theorem(theo)
            parsed_theorems.append(theo_object)
        return parsed_theorems

    @staticmethod
    def theorem(theo: dict) -> Theorem:
        if theo.get("name") == IntegrateByPartsTheorem().name:
            return IntegrateByPartsTheorem()
        elif theo.get("name") == IntegrateByPartsApplyTheorem().name:
            return IntegrateByPartsApplyTheorem()
        elif theo.get("name") == IntegrateByPartsReplaceUVTheorem().name:
            return IntegrateByPartsReplaceUVTheorem()

        return Theorem(
            theo.get("name"),
            theo.get("left") if 'left' in theo else None,
            theo.get("right")if 'right' in theo else None,
            theo.get("conditions") if 'conditions' in theo else {}
        )

