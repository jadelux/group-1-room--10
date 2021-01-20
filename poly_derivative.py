import math
def f(x):
    y = (a0)+(a1*x)+a2*x**2+a3*x**3
    return y


# Polynomial coefficients
a0 = 1
a1 = -2
a2 = 4.6
a3 = 0.2

# Point at which we evaluate the derivative
x = 3.1
p_prime = a1+2*a2*x+3*a3*x**2
print(p_prime)






# This will be True if the code is correct
print(p_prime == 32.286)