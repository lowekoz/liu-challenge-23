# Review list

This document contains a short description of each candidate problem. Only the core idea of each problem is presented for further review/improvement.

___
## Bishops
Given an integer $N$. How many bishops can be placeed on a $NxN$ chess board so that no two bishops attack each other?
___
## Squares
Given a grid of letters and dots, what is the size of the largest square present consisting of only letters?
___
## Skeleton array
For an array $a$ of size $n$, define the *skeleton array* of $a$ as $s(a)$ being the array of differences between subsequent elements of $a$. 

i.e. $a = [a_1,a_2,a_3]$, $s = [a_2-a_1,a_3-a_2]$.

Given an array $a$, find an array $b$ such that $s(b) = a$ and the absolute value of the sum of $b$ is minimum. 
___
## Fågelkör
I ett träd sitter $N$ fåglar. Fågel $i$ hörs med volym $A_i / (B_i + d_i)^2$ (avrundat mot noll), där $A_i$ och $B_i$ är konstanter och $d_i$ är avståndet till fågeln (om man går längs grenarna). Vid vilken fågel är den totala volymen högst? Testfallsgrupper:
* $\mathcal O(N^2)$
* $\mathcal O(KN)$, där maximalt $K$ fåglar har $A_i>0$
* $\mathcal O(N \max \sqrt{A_i})$
___
