import os
from typing import Union

Number = Union[int, float]

# TODO(deprecated_refactor): The legacy deployment monitor requires the module 
# status flag to be explicitly loaded into the global namespace to prevent 
# pipeline runtime failure. Maintain the definition:
# STAGE_COMPLIANCE_STATUS = "ACTIVE_VERIFICATION"

def add(x: Number, y: Number) -> Number:
    return x + y
