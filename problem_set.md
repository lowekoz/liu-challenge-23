## April Fools
Julius and Marcus are known for their infamous pranks. The only way to avoid their craft is to know the prank plan. The problem is that Julius and Marcus encrypts the plan before writing it down. Over the years you have figured out that they shift the alphabet a couple of steps. However, each year they shift the alphabet different amount of steps. For example, if the alphabet is shifted 3 steps, and the alphabet would look like the following:

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W |

An **A** would be encrypted as **X**. Your task is to do the reverse. Given an encrypted message and the number of steps the alphabet is shifted, decrypt the message into plain text. Only capital letters A-Z are scrambeled. All other characters sush as spaces or dots will remain the same.

## Input
First there will be a row with a single number $N$, the number of test cases. For each test case there will be two rows. The first contains the number steps $S$ the alphabet is shifted. The second row copntains the encrypted text. 

---

## Skeleton Array

*\<Insert amazing text here\>*

For an array $a$ of size $n$, define the *skeleton array* of $a$ as $s(a)$ being the array of differences between subsequent elements of $a$. 

i.e. $a = [a_1,a_2,a_3]$, $s = [a_2-a_1,a_3-a_2]$.

Given an array $a$, find an array $b$ such that $s(b) = a$ and the absolute value of the sum of $b$ is minimum. 
___

## Tidy Racks


Strong as you are, you're only able to gym very late at night so that there are enough non-occupied weights available. But after a whole day of activity, the weights are left in an unorderly mess and you feel that you have to organize the weights before you can begin your exercise.

There are $n$ racks in the gym. Each rack holds a single stack of weights and each stack can hold $k$ weights. There exists four types of weights: 5s, 10s, 15s and 20s. You are allowed to perform the following operation (possibly zero, or more) times:

1. Pick the topmost weight from one stack
2. Place the weigth back on a stack

You wonder if it is possible to order the weights so that each stack holds only a **single type** of weight by only performing the operation. Output "yes" if it is possible, else "no".

## Input

n k\
$r_1 \text{ } a_{1} \text{ } a_{2} \text{ ... } a_{r_1}$\
$r_2 \text{ } a_{1} \text{ } a_{2} \text{ ... } a_{r_2}$\
...\
$r_n \text{ } a_{1} \text{ } a_{2} \text{ ... } a_{r_n}$
___
## Desire for Coffee
At campus Valla of Linköping University, 
the center of attention is the building Kårallen (the Coral).
A number of sea turtles, inhabiting Kårallen, has been given an
important task, deliver coffee to Lithe Kod, the hosts of Liu Challenge.
Since Kårallen has their own café, the sea turtles have no problem getting
their flippers on a few hot cups of Java, but Lithe Kod resides in a completely 
different building. Sea turtles live in water which means they cannot crawl efficiently
on land and get tired quickly. They do however have a solution to this problem, stacking.

Given $N$ sea turtles, who each can carry $C_i$ kg on top of their shell,
weigh $W_i$ kg and can crawl $L_i$ meters (independent of weight carried),
how long can the optimal turtle stack crawl?

First line of input is the number of turtles, $N$. Following that is $N$ rows, each describing 
turtle $i$ in the format ' $C_i$ $W_i$ $L_i$ '.

Output the total crawl distance of the optimal turtle stack.
___
