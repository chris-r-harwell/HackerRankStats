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

4. if two events, A and B, are disjoint, then the probability of either
event is the sum of the probabilities of the 2 events
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
 3 urns labeled X, Y and Z
  Urn X contains 4 red balls and 3 black balls: 7 balls
     P(Ex,r) = 4/7 red
     P(Ex,b) = 3/7 black
  Urn Y contains 5 red balls and 4 black balls: 9 balls
     P(Ey,r) = 5/9 red
     P(Ey,b) = 4/9 black
  Urn Z contains 4 red balls and 4 black balls: 8 balls 4/8 red, 4/8 black
  Urn Z contains 4 red balls and 4 black balls: 8 balls
     P(Ez,r) = 1/2 red
     P(Ez,b) = 1/2 black

  One ball is drawn from each of the 3 urns.
  What is the probability that, of the 3 balls drawn,
  2 are red and 1 is black?

  E(X,Y,Z)
  1 E(R,R,B)
    P(E(R,R,B)) = P(Ex,r) x P(Ey,r) x P(Ez,b) = (4/7)(5/9)(1/2)

  2 E(R,B,R)
    P(E(R,B,R)) = P(Ex,r) x P(Ey,b) x P(Ez,r) = (4/7)(4/9)(1/2)

  3 E(B,R,R)
    P(E(B,R,R)) = P(Ex,b) x P(Ey,r) x P(Ez,r) = (3/7)(5/9)(1/2)


  P(R and R and B) = indepent so sum
   P(E(R,R,B)) + P(E(R,B,R)) + P(E(B,R,R)
    (4/7)(5/9)(1/2) + (4/7)(4/9)(1/2) + (3/7)(5/9)(1/2)

"""

X = ['R', 'R', 'R', 'R', 'B', 'B', 'B']
Y = ['R', 'R', 'R', 'R', 'R', 'B', 'B', 'B', 'B']
Z = ['R', 'R', 'R', 'R', 'B', 'B', 'B', 'B']

favorable = 0
total = 0

# frequentist
for i in X:
    for j in Y:
        for k in Z:
            s = (i, j, k)
            num_red = s.count('R')
            num_black = s.count('B')
            total += 1
            if num_red == 2 and num_black == 1:
                favorable += 1
                # print(s)

print('{} / {}'.format(favorable, total))
print('{:.2f}'.format(round(favorable / total, 2)))

# bayesian
P_E_RRB = (4 / 7) * (5 / 9) * (1 / 2)
P_E_RBR = (4 / 7) * (4 / 9) * (1 / 2)
P_E_BRR = (3 / 7) * (5 / 9) * (1 / 2)
P_RRB = P_E_RRB + P_E_RBR + P_E_BRR
print('{:.2f}'.format(round(P_RRB, 2)))
