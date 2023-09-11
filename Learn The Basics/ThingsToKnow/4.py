from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    if ch == 1:
        area = math.pi*a[0]*a[0]
    elif ch == 2:
        area = a[0]*a[1]
    return format(area, '.5f')
