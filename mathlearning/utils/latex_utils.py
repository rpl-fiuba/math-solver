from sympy import Union
from sympy.core.numbers import Infinity


def clean_latex(latex: str) -> str:
    clean = latex.replace("\\left\\{", "{")
    clean = clean.replace("\\left(", "(")
    clean = clean.replace("left(", "(")
    clean = clean.replace("\\right\\}", "}")
    clean = clean.replace("\\right)", ")")
    clean = clean.replace("\\left|", "|")
    clean = clean.replace("left|", "|")
    clean = clean.replace("\\right|", "|")
    clean = clean.replace("\\left[", "[")
    clean = clean.replace("left[", "[")
    clean = clean.replace("\\right]", "]")
    clean = clean.replace("\\cdot ", "*")
    clean = clean.replace(".", "*")
    clean = clean.replace("sen", "\\sin")
    clean = clean.replace("Dom", "\\Dom")
    clean = clean.replace("\\ ", "")
    clean = clean.replace("\\le", "\\leq")
    clean = clean.replace("\\ge", "\\geq")
    clean = clean.replace("\\int_{}^{}", "\\int ")
    return clean
