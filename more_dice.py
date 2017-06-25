#!/bin/env python3
"""

The probability of the occurrence of an event, A, is:


    P(A) = number of favorable outcomes
           ---------------------------
           total number of outcomes

Rules:
1. Any probability, P(A) , is a number between 0 and  1 
    0 <= P(A) <= 1
2. The probability of the sample space, S, is 1 
    P(S) = 1

3. P(A') probability event will not occur.
    P(A) + P(A') = 1
    P(A') = 1 - P(A)

compound event: combination of 2 or more simple events
mutually exclusive: or disjoint if they have no events in common.

4. if two events, A and B, are disjoint, then the probability of either event is the sum of the probabilities of the 2 events 
    union: probability of any of 2 or more events
    P(A or B) = P(A) + P(B)

5. independent: outcome of first event A has no impact on second event B 
   intersection: chance of all events occuring in a sequence of events
    P(A and B) = P(A) x P(B)


     |A or  B| = |A| + |B| + |A and B|
    P(A or  B) = P(A) + P(B) - P(A and B)
    P(A and B) = P(A) + P(B) - P(A or  B)

"""

"""
 single toss of 2 fair evenly weighted six-sided dice, find the probability
 that their sum will be 6 and value on each dice is different.

"""

S = [1, 2, 3, 4, 5, 6]
favorable = 0
total = 0

for i in S:
    for j in S:
       total += 1
       print(i, j)
       if i + j == 6 and i != j:
           favorable += 1

print('{} / {}'.format(favorable, total))
print('{:.2f}'.format(round(favorable / total, 2)))
