# 6.00 Problem Set 2
#
# Successive Approximation
#

# Import the math processor module
# 
import math_polyParcing
polyParce = math_polyParcing.polyParce

# Import Debugger
#
import pdb

# Define main 
def main():
    # Determine which Problem Set to do
    while True:
        problem_set = raw_input("Which Problem Set: [1, 2, or 3] ")
        if problem_set == '1':
            # Problem Set 1
            probSet_1()
            break
        elif problem_set == '2':
            # Problem Set 2
            probSet_2()
            break
        elif problem_set == '3':
            # Problem Set 3
            probSet_3()
            break
        else:
            print("Not a vaild problem set.")

    # Done
    quit

# PROBLEM SET 1
def probSet_1():
    print("\n\t!!! Starting Problem Set 1 !!!\n")
    
    # Get the polynomial
    polynomial_str = raw_input("Please enter a polynomial: ")
    
    # Process the polynomial
    math_polyParcing.polynomial = []
    temp = polyParce(polynomial_str)
    
    # Get the value to solve for
    evaluate_x = raw_input("Please enter a value to solve for: ")
    
    # Evaluate the polynomial (solve for x)
    func_value = evaluate_poly(temp, evaluate_x)

    print("The solution = " + str(func_value))
        
    #Done
    print("\n\t!!! Problem Set 1 Completed !!!\n")
    return

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """

    # Define variables
    x = float(x)
    i = 0
    term_count = len(poly)
    func_value = 0.0

    # Solve for & tally, each Term
    while i < term_count:
        term_value = poly[i] * x ** i
        func_value = func_value + term_value
        i = i + 1

    #Done
    return func_value



# PROBLEM SET 2
def probSet_2():
    print("\n\t!!! Starting Problem Set 2 !!!\n")
    
    # Get the polynomial
    polynomial_str = raw_input("Please enter a polynomial: ")
    
    # Process the polynomial
    math_polyParcing.polynomial = []
    temp = polyParce(polynomial_str)
    
    # Evaluate the derivative of the polynomial
    poly_new = compute_deriv(temp)

    print("The derivative = " + poly_new)
    
    #Done
    print("\n\t!!! Problem Set 2 Completed !!!\n")
    return

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ... 

    # Define variables
    term_count = len(poly) - 1
    term_coef = 0
    term_new = ''
    poly_new = ''

    # Solve for & tally, each Term
    while term_count > 1:
        term_value = poly[term_count] * term_count

        if term_value != 0:
            if term_value < 0:
                # Negative Term
                if term_count == len(poly) - 1:
                    # If the first coefficent is negative, place the sign next to it
                    poly_new = poly_new + "-"
                else:
                    # Otherwise treat as an operator (add a space)
                    poly_new = poly_new + "- "
            elif term_value > 0 and term_count != len(poly) - 1:
                poly_new = poly_new + "+ "

            term_new = str(abs(term_value)) + "x"
            if (term_count - 1) > 1:
                term_new = term_new + "^" + str(term_count - 1) + " "
            poly_new = poly_new + term_new

        term_count = term_count - 1

    return poly_new

    #Done
    return



# PROBLEM SET 3
def probSet_3():
    print("\n\t!!! Starting Problem Set 3 !!!\n")
    
    # Get the polynomial
    polynomial_str = raw_input("Please enter a polynomial: ")
    
    # Get the x_0
    x_0 = raw_input("x_0 = ")
    
    # Get the x_0
    epsilon = raw_input("epsilon = ")
    
    # Evaluate the derivative
    tup = compute_root(polynomial_str, x_0, epsilon)

    # Print Results
    print("Solution: (" + str(tup[0]) + ", " + str(tup[1]) + ")")

    #Done
    print("\n\t!!! Problem Set 3 Completed !!!\n")
    return

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # TO DO ... 

    # Process the polynomial
    math_polyParcing.polynomial = []
    poly_0 = polyParce(poly)
    print("Polynomial = " + str(poly_0))

    # Find the derivative of the poly
    deriv = compute_deriv(poly_0)
    math_polyParcing.polynomial = []
    poly_1 = polyParce(deriv)
    print("Derivative Polynomial = " + str(poly_1))
    
    # Define variables
    epsilon = float(epsilon)
    x_0 = float(x_0)
    iterations = 1
    iterate = True

    # Find the root
    while True:
        #x0_value = evaluate_poly(poly_0, x_0)
        if abs(evaluate_poly(poly_0, x_0)) < epsilon:
            iterate = False
            break
        else:
            iterations += 1
            x_0 = x_0 - evaluate_poly(poly_0, x_0) / evaluate_poly(poly_1, x_0)

        print(x_0)
    #Done
    print(x_0,iterations)
    returnTuple = [x_0, iterations]
    return returnTuple

# Start the ball rolling...
main()










    
