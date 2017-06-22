#!/bin/env python3
""" Calculate the standard deviation

expected value, mu a.ka. average, mean

variance, sigma**2:
    average magnitude of fluctuations of X from its expected value, mu
    expectation of a random variable's squared deviation from its mean.

    given a data set, X of size n:

                  n
    sigma**2 = ( sum  ( x_i - u ) ** 2 )
                  i_0..n
               ----------------
                  n
INPUT: 2 lines
 n, int num of elements in array X
 n, space separated int in array X

Constraints:
 5 <= 5 <= 100
 0 < x_i <= 10**5, where x_i is the ith element of array X

OUTPUT: 1 line
    standard deviation rounded to a scale of 1 decimal place
"""


from math import sqrt


def get_variance(array, m):
    """
    INPUT: array of m elements
    OUTPUT: variance
    Find the sum of the squares of each element minus the average,
    and divide by the number of elements.
    """
    mean = sum(array) / m
    variance = sum([(i - mean) ** 2 for i in array])/m
    return variance


if __name__ == '__main__':
    n = int(input())
    X = list(map(int, input().split()))
    sigma = sqrt(get_variance(X, n))
    print("{:.1f}".format(round(sigma, 1)))
