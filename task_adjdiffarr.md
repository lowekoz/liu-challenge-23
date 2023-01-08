# Skeleton array

For an array $a$ of size $n$, define the *skeleton array* $s$ of $a$ as


$s(a) =  \begin{cases} [] \text{ if |a| < 2} \\ s_i = a_i - a_{i+1}  \text{ for 1 <= i <n if |a| >= 2}  \end{cases}$

Given $s$, find the (an?) array $a$ whose *skeleton array* is $s$ and |$\sum a$| is minimum.


## Solution:
Math, dynamic storage memo.