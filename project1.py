'''---------------------------------------------------
--------------- Import Modules -----------------------
------------------------------------------------------'''
from functions_quad import *   # import all functions from the functions-quad module
import math

'''-----------------------------------------------------
-------------  Main program starts here  ---------------
--------------------------------------------------------'''

print("\n--------------Welcome to the Quadratic Solver Tool----------------")
print("                      f(x)=a*x**2+b*x+c\n")

## ask user to input coefficient values
a=float(input("Enter value for a (a/=0): "))
b=float(input("Enter value for b: "))
c=float(input("Enter value for c: "))

## display user equation
print("\n-Equation is:\t"+my_quad_equation(a,b,c))

## display derivative equation
print("-Derivative is:\t"+my_quad_equation_derivative(a,b))

##display info on extremum
x0=-b/(2*a)
print("-Extremum is:\t%s at x0=%s and f(x0)=%s"%(info_extremum(a),x0,evaluate_quad_equation(a,b,c,x0)))

##display info on discriminant
delta=compute_discriminant(a,b,c)
print("-Discriminant is:\t"+str(delta))

##display solution of f(x)=0
print("-Solving for f(x)=0")
print_info_solution_quad(a,b,c,delta)


print("\n-----------------Thanks and come back soon!----------------------\n")

