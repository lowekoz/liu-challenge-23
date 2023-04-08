Turtle 'i' has a carrying capacity Ci and a weight Wi.

We want to prove: 
Subject to ordering Ci+Wi >= Cj+Wj for (i<j) of turtles, it is better (or as good) to place the j:th turtle on top of the i:th
turtle for (i<j), as it will preserve more (or as much) carrying capacity as the other choice.

Proof:
Place i on j: resulting capacity -> min(Cj-Wi,Ci)
Place j on i: resulting capacity -> min(Ci-Wj,Cj)

Note that, by ordering we have 

Ci+Wi >= Cj+Wj <=>
Ci-Wj >= Cj-Wi

Furthermore, it is clear that

Ci > Ci-Wj and Cj > Cj-Wi since we are handling positive integers only.

Therefore we can say that

Ci > Ci-Wj >= Cj-Wi and Cj > Cj-Wi always holds.

This means that Cj-Wi of option 'Place i on j' will always be the minimum and therefore the worst possible choice. The other option 'Place j on i' is guaranteed to be equal or better, never worse.
