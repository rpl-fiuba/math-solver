from enum import Enum


class ProblemType(Enum):
    DERIVATIVE = 'derivative'
    INTEGRAL = 'integral'
    FACTORISABLE = 'factorisable'
    DOMAIN = 'domain'
    INEQUALITY = 'inequality'
    IMAGE = 'image'
    TRIGONOMETRY = 'trigonometry'
    EXPONENTIAL = 'exponential'
