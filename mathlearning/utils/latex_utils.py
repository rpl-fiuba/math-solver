import re

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
    # clean = clean.replace(".", "*")
    clean = clean.replace("sen", "\\sin")
    clean = clean.replace("Dom", "\\Dom")
    clean = replace_sqrt(clean)
    clean = clean.replace("Img", "\\Img")
    clean = clean.replace("\\ ", "")
    clean = clean.replace("\\le", "\\leq")
    clean = clean.replace("\\ge", "\\geq")
    clean = clean.replace("\\leqft", "\\left")
    clean = clean.replace("\\int_{}^{}", "\\int ")
    return clean


def replace_sqrt(string):
    # Define the pattern to match the string
    pattern = r'(.+)sqrt\((.*?)\)(.+)'
    # Replace the matched pattern with the desired format
    replaced_string = re.sub(pattern, r'\1\\sqrt{\2}\3', string)
    return replaced_string
