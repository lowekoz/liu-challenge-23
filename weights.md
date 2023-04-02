n - number of racks\
k - rack size\
w1,w2,w3,w4 - weight types 5 10 15 20 respectivly\
x1,x2,x3,x4 - xi denotes number of weights of type i\
x - total number of weights (x = x1+x2+x3+x4)\
r1,r2,r3,r4 - ri denotes the number of racks required to hold all weights of type wi subject to rack size k, ri= ceil(xi/k)\
r - total racks required (r = r1+r2+r3+r4)

First consider the test case:\
3 3\
0\
3 5 10 15\
3 15 15 15

In this case r = 4 but n = 3, therefore no solution can exist. This leads us to the first condition that has to be true. 

    r <= n must hold. (1)

Next consider case k=1, then everything is solved from start.

Next consider special cases n=1 and n=2. If n=1 then (1) is sufficient for there to be a solution, else no. If n=2, we may concatenate the stacks top-to-top  and check whether $a[i] \neq a[i+1]$ holds at most one time, together with (1).  

Next do case work for n>=3 and k >= 2 over 0 <= x <= (n-1)k; (n-1)k < x <= nk


**case 0 <= x <= (n-1)k:**

Note that x <= (n-1)k implies that we can create an empty rack by moving all weights from one rack into the others. 

Claim:\
We can rearrange the weights however we want subject to the constraints if we have an empty rack with n>=3 and k >= 2.

Proof*:

1) Wlog. denote racks A,B,E where E is empty initially, and both A and B are non-empty racks. We can swap weights A[i] and A[j] (i<j) of stack A all else  equal with the following steps:
    ```
    Move 1 weight from B to E.
    Move weights from A to E until A[i] is on top of A.
    Move 1 weight (A[i]) from A to B.
    Move weights from A to E until A[j] is the last to be placed on E.
    Move 1 weight (A[i]) from B to A.
    Move 1 weight (A[j]) from E to B.
    Move weights from E to A until next position of A is A[i]'s old position.
    Move 1 weight (A[j]) from B to A.
    Move weights from E to A until one weight is left on E
    Move 1 from E to B.
    ```

2) Wlog. denote racks A,B,E where E is empty initially, and both A and B are non-empty racks.  We can swap any two weights from different stacks i.e. swap A[i] with B[j].
    ```
    Use 1) to put A[i] on top of A.
    Use 1) to put B[j] on top of B.
    Move 1 (A[i]) from A to E
    Move 1 (B[j]) from B to A
    Move 1 (A[i]) from E to B
    ```


3) If (1) holds, then a target configuration that solves the problem exists. The given operation (move one topmost weight from one stack to another), together with operations 1. and 2. is enough for us to construct the target operation by first creating the full stacks of the same weight type. And then constructing the remaining, at most 4 incomplete sacks, by wlog. the first stack of weight type x, and the remaining space of the first stack with weight type c. The second stack of weight type y, and the remaining space of the second stack with weight type c. The third stack of weight type z and the remaining (last of) weight c on top of that. Then, move all weights of type c onto the empty stack.

**case (n-1)k < x <= nk:**

This case is similar to the previous case only that, we can never reach the x-(n-1)k lowest weights in each rack. Simply, check if the bottom-most x-(n-1)k weights of each stack are of the same type, and that the configuration is a superset of what our requirements are. i.e. if our given configuration has r1=X, r2 = Y, r3 = Z and r4 = C, then we must have atleast X bottom locked stacks of type w1, Y of w2, Z of w3 and C of w4, else it is impossible. If we do however, then we can omit thinking about the **locked** bottom x-(n-1)k weights and use the algorithm described for previous case to order all the weights correctly. $\square$ 
    