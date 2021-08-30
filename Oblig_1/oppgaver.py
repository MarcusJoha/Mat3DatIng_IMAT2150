import math as m
import numpy as np


# Chapter 0.1, CP1

def horner(poly, n, x):
    # initialize result
    result = poly[0]
    # Evaluate value of polynomials
    # Using Horner's method
    for i in range(1, n):
        result = result * x + poly[i]
    return result


# Initialize empty list
poly = []

# fill list of 51 elements of value 1
for i in range(0, 51):
    poly.append(1)

# poly = 1 + x + x^2 + x^3 + ... + x^50
# n elements = 51
# value of x = 1.00001
print(horner(poly, 51, 1.00001))

# P(1.00001) = 51.01275208274999
# Q(x) = (x^51-1)/(x-1)
# Q(1.00001) = 51.01275208274523
print(51.01275208274999 - 51.01275208274523)


# Error of computation: |P(x) - Q(x)| = 4.760636329592671e-12


# Chapter 0.4, CP1 a)
# plz kill me

def function_a(x):
    # sec(x) = 1/cos(x)
    return (1 - (1 / m.cos(x))) / (m.tan(x) ** 2)


print("\nValues of function in a)")
for i in range(1, 15):
    x = 10 ** (-i)
    print(x, ": ", function_a(x))


# re-written function of a)
def optimized_function_a(x):
    return -1 / (1 + (1 / m.cos(x)))


print("\nValues of optimized function in a)")
for i in range(1, 15):
    x = 10 ** (-i)
    print(x, ": ", optimized_function_a(x))

# Chapter 0.4, CP5
# Venter med denne jævelen
print(m.hypot(3344556600, 1.2222222))
print(m.hypot(3, 4))


# Chapter 1.1, CP1

#function f, intervall [a,b], N calculations
def bisection(f, a, b, N):
    if f(a) * f(b) >= 0:
        print("Bisection method fails")
        return None
    a_n = a
    b_n = b
    for n in range(1, N + 1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n) / 2


# Defines the function f(x)
f = lambda x: x ** 3 - 9
#function f, intervall [2,3], 4 calculations
print(bisection(f, 2, 3, 4))
