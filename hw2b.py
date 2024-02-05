import math
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    for i in range(maxiter): #starts loop that will run for a maximum of maxiter
        f_x0 = fcn(x0) #caluates values of the function at initial guesses
        f_x1 = fcn(x1)
        if f_x1 - f_x0 == 0:  #checks to see if difference is 0 (kept getting error)
            return None
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)  #calculates new estimate and stores in x_new using secant formula
        if abs(x_new - x1) < xtol:  #checks if the estimate is smaller than the exit tolerance xtol
            return x_new  #returns if so
        x0, x1 = x1, x_new  #updates the values of x0 and x1 for the next iteration
    return x_new  #returns the estimated values of x0 and x1 if max iterations are reached
'''
    function using the secant method to approximate the root of a function with five parameters:
    fcn is the function for which the root is found
    x0 is the initial guess for the root.
    x1 is the other initial guess for the root.
    maxiter is the maximum number of iterations with the default set at 10.
    xtol checks whether the difference between the new estimate x_new and the 
    previous estimate x1 is smaller than the specified exit tolerance xtol. If so,
    it returns the x_new value
'''
def main():
    def fcn1(x):
        return x - 3 * math.cos(x)  # function 1
    def fcn2(x):
        return math.cos(2 * x) * x ** 3 # function 2

    print("Root of function 1 with maxiter = 5 and xtol = 1e-4:", Secant(fcn1, 1, 2, maxiter=5, xtol=1e-4))
    print("Root of function 2 with maxiter = 15 and xtol = 1e-8:", Secant(fcn2, 1, 2, maxiter=15, xtol=1e-8))
    print("Root of function 2 with maxiter = 3 and xtol = 1e-8:", Secant(fcn2, 1, 2, maxiter=3, xtol=1e-8))

'''
    these three lines take the fcn1 and fcn2 function expressions (depending on which function is used in the line), the iterations amount 
    called for maxiter, the exit tolerance xtol, and runs it through the secant function.
'''

main() #calling the main function