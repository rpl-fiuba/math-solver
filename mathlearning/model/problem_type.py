from enum import Enum


class ProblemType(Enum):
    DERIVATIVE = 'derivative'
    INTEGRAL = 'integral'
    FACTORISABLE = 'factorisable'
    DOMAIN_AND_IMAGE = 'domain_and_image'
    INEQUALITY = 'inequality'
