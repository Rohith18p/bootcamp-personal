print("om sai ram")
print("pushed to git")

import math
import unittest
import random

def wallis(n):
    pi = 2.0
    for i in range(n):
        pi = pi*((4*(i+1)*(i+1))/(4*(i+1)*(i+1)-1))
    return pi

wallis(1)
