#!/bin/env python3
"""
Task:
     Calculate interquartile range.

     which is the difference between the first Q_1 and the third Q_3 quartiles.
     That is Q_3 - Q_1.

     Construct a data set S where ea x_i occurs at frequency f_i.
     Then, calculate and print S's interquartile range,
     rounded to a scale of 1 decimal place.

INPUT: 3 lines
 n ele in arrays X and F
 n space separated int in array X
 n space separated int in array F, frequency of elements in X

Constraints:
    5 <= n <= 50
    0 < x_i <= 100, where x_i is the ith element of the array.
    0 < f_i <= 10**3, where f_i is the ith element of the array.
    num ele in S equal to sum F

OUTPUT: 1 line float, rounded to a scale of 1 decimal place.
     interquartile range
"""


def get_median(a, n):
    """
    INPUT: sorted array, num elements
    OUTPUT: median, middle number if odd,
    average of middle two numbers if even.
    """
    assert len(a) == n
    mid = n // 2
    median = a[mid]
    if n % 2 == 0:
        mid -= 1
        median += a[mid]
        median /= 2.0

    return median


def get_quartiles(a, n):
    """
    INPUT: sorted array of ints a, num n
    OUTPUT: 1st, 2nd and 3rd quartiles
    """
    m = n // 2
    L = a[0:m]

    if n % 2 == 0:  # even
        U = a[m:]
    else:  # odd, exclude median
        U = a[m+1:]

    q1 = get_median(L, m)
    q2 = get_median(a, n)
    q3 = get_median(U, m)

    return (q1, q2, q3)


if __name__ == '__main__':
    # INPUT
    n = int(input())
    X = list(map(int, input().split()))
    F = list(map(int, input().split()))

    # Construct S and find new length
    S = list()
    for i in range(n):
        for j in range(F[i]):
            S.append(X[i])
    S.sort()
    n = len(S)

    # Find quartiles and print interquartile range
    q1, q2, q3 = get_quartiles(S, n)
    print("{:.1f}".format(round(q3 - q1, 1)))
