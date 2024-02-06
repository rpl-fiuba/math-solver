from mathlearning.model.derivative.derivative_theorems import DerivativeTheorems
from mathlearning.model.integral.integrate_theorems import IntegrateTheorems


class Theorems:
    @staticmethod
    def get_all():
        return DerivativeTheorems.get_all() + IntegrateTheorems.get_all()