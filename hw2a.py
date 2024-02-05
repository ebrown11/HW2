import math

def gaussianPDF(x, mu, sigma):

    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(1/2) * ((x - mu) / sigma) ** 2)
"""
    function that calculates and returns the value of the Gaussian probability density function with parameters:
    x for the value at which the PDF is evaluated
    mu for the mean of the distribution
    sigma for the standard deviation of the distribution
"""
def simpsonRule(a, b, f, n, mu, sigma):

    h = (b - a) / n #calculates the width of each interval
    total = f(a, mu, sigma) + f(b, mu, sigma) #initializes the total with the first and last terms
    for i in range(1, n): #begins a loop that goes through all the intervals
        x = a + i * h #calculates the current x value
        if i % 2 == 0: #checks if i is even and applies Simpson's rule
            total += 2 * f(x, mu, sigma)
        else:
            total += 4 * f(x, mu, sigma)
    return (h / 3) * total #multiplies the value by h/3 and returns the total
"""
    function that performs numerical integration of the function f over the interval using Simpson's rule and
    returns the approximate value of the integral of f from a to b with parameters:
    a for the lower limit
    b for the upper limit
    f for the function to be integrated with the parameters x, mu, sigma
    n for the number of intervals used in the approximation
    mu for the mean parameter
    sigma for the stand deviation parameter
"""
def Probability(PDF, args, c, GT=True):
    mu, sigma = args #extracts mu and sigma from args
    if not GT: #sets the integrations limits depending if P(x>c) or P(x<c)
        a, b = mu - 5 * sigma, c
    else:
        a, b = c, mu + 5 * sigma
    n = 1000  #sets number of intervals

    return 1 - simpsonRule(a, b, PDF, n, mu, sigma) if GT else simpsonRule(a, b, PDF, n, mu, sigma)  #calculates the probability based on the GT flag and returns the result

'''
    function that calculates the probability of a distributed variable being greater than 
    or less than a specified value c with the paramters:
    PDF for the Guassian probability density function to be used for the calculation
    args a tuple containing the mean and standard deviation mu and sigma
    c the value to compare the variable against
    GT a boolean flag indicating whether to calculate the probability of the variable being greater and less than c
'''
def main():
    prob_less_than = Probability(gaussianPDF, (100, 12.5), 105, GT=False) #calculates and prints the probability P(x<105) for a normal distribution N(100,12.5)
    print(f'P(x<105|N(100,12.5))={prob_less_than:.4f}')

    mu, sigma = 100, 3 #calculates and prints the probability P(x>μ+2σ) for a normal distribution N(100,3)
    c = mu + 2 * sigma
    prob_greater_than = Probability(gaussianPDF, (mu, sigma), c, GT=True)
    print(f'P(x>{c}|N({mu},{sigma}))={prob_greater_than:.4f}')
"""
    main function to demonstrate the calculation of specific probabilities using the 
    Gaussian probability density function and Simpson's rule for numerical integration that
    calculates and prints the probability of a Gaussian-distributed variable being less 
    than 105 for a distribution with mean 100 and standard deviation 12.5 and the probability 
    of being greater than the mean plus two standard deviations for a distribution with mean 100 
    and standard deviation of 3
"""
main()