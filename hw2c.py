def GaussSeidel(Aaug, x, Niter=15):
    N = len(x)  # calculates the number of varibles in the system

    for _ in range(Niter):  # beginning of loop that will run Niter iterations.
        for i in range(N):  # starts another loop that iterates through the varibles to N-1
            x[i] = (Aaug[i][-1]  # represents the right-hand side value  of the 'i'-th equation
                    - sum(Aaug[i][j] * x[j] for j in range(
                        i))  # calculates the sum of the products of coefficients and the current estimates of already updated variables
                    - sum(Aaug[i][j] * x[j] for j in range(i + 1, N))) / Aaug[i][
                       i]  # calculates the sum of the products of coefficients and the current estimates of the remaining variables in the equation.
            # divided by the coefficient of the 'i'-th variable in the 'i'-th equation
            # line 6, 7, 8 copied from stackexchange
    return x


'''
    function using the Guass-Seidel method to estimate the solution to a set of linear equations N expressed
    in matrix form with using three parameters:
    Aaug an augmented matrix with N rows and N+1 column
    x is the list containg the initial guess values
    Niter is the number of iterations to compute

    x is the new vector value after the iterations are complete

'''


def main():
    Aaug1 = [[3, 1, -1, 2], [1, 4, 1, 12],
             [2, 1, 2, 10]]  # defines the augmented matrix Aaug1 and initial guess x for the first equation
    x1 = [0, 0, 0]

    solution1 = GaussSeidel(Aaug1,
                            x1)  # estimates and prints the solution for the first equation using the GuassSeidel function
    print("Solution for the first set of equations:")
    print(solution1)

    Aaug2 = [[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 21],
             [-1, 2, 7, 37]]  # defines the augmented matrix Aaug2 and initial guess x for the second equation
    x2 = [0, 0, 0, 0]

    solution2 = GaussSeidel(Aaug2,
                            x2)  # estimates and prints the solution for the second set of equations using the GuassSeidel function
    print("Solution for the second set of equations:")
    print(solution2)


'''
    the main() function solves the set of linear equations using the Gauss-Seidel method by
    defining the augmented matrix Aaug and an initial guess for the solution x then 
    estimating and printing the solution for the equations.
'''
main()