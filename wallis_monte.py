import math
import unittest
import random

def wallis(n):
    pi = 2.0
    for i in range(n):
        pi = pi*((4*(i+1)*(i+1))/(4*(i+1)*(i+1)-1))
    return pi

def monte_carlo(nd):
    circ_prob = 0.0
    length = float()
    centre = [0.0,0.0]
    dart = [0.0,0.0]
    for i in range(nd):
        dart[0] = random.random()
        dart[1] = random.random()
        length = math.dist(dart, centre)
        if length < 1.0:
            circ_prob += 1.0
    return 4*circ_prob/nd

print("Monte_carlo = ",monte_carlo(100))
print("Wallis = ", wallis(100))