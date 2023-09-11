from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    return fibonnaci(n-1) + fibonnaci(n-2)

n = int(input())
a = fibonnaci(n)
print(a)