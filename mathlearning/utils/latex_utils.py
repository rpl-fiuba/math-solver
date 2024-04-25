import re

from regex import regex
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
    clean = clean.replace("\\le", "\\leq ")
    clean = clean.replace("\\ge", "\\geq ")
    clean = clean.replace("\\leq ft", "\\left")
    clean = clean.replace("\\int_{}^{}", "\\int ")
    return clean


def replace_sqrt(string):
    # Define the pattern to match the string
    pattern = r'(.+)sqrt\((.*?)\)(.+)'
    # Replace the matched pattern with the desired format
    replaced_string = re.sub(pattern, r'\1\\sqrt{\2}\3', string)
    return replaced_string


def find_outermost_brackets(input_string):
    # The regular expression pattern for finding the outermost brackets
    pattern = r'\[(?:[^\[\]]++|(?R))*\]'
    # Use regex.findall to find all occurrences of the pattern
    matches = regex.findall(pattern, input_string)
    # Return the matches
    return matches


def clean_outermost_brackets_if_irrelevant(input_string):
    if find_outermost_brackets(input_string) == [input_string]:
        return input_string[1:-1]
    else:
        return input_string


def extract_inequality_sides(input_string):
    delimiters = ['<', '>', '\\leq', '\\geq']
    pattern = '|'.join(map(re.escape, delimiters))
    parts = re.split(pattern, input_string)
    matches = re.findall(pattern, input_string)
    if not matches:
        return []
    result = []
    for i in range(len(parts) - 1):
        result.append(parts[i] + matches[i] + parts[i + 1])
    return result
