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
## Bära matkassar från bilen
Du har varit och handlat och alla matvaror ligger löst i bagaget i din bil. Du har en kappsäck med kapacitet $C$ kg och $I$ varor som väger $V_i$ och till antal $C_i$. Vad är det lägsta antalet turer du behöver gå mellan bilen och huset för att få in alla varor?
___
## Placering av matbutik
Givet ett rutnät där vissa rutor har ett hus, återge minimala antalet mataffärer så att varje hus har minst 1 affär med max $D$ rutsteg (ej diagonalt) ifrån sig.
___
## Sköldpaddsdistans
Givet $N$ sköldpaddor som kan bära $B_i$ kilo, väger $V_i$ kilo och kan kravla $L_i$ m, hur långt kan en stack av sköldpaddor maximalt kravla kollektivt?
___
## Sköldpaddssortering
Givet $N$ sköldpaddor som kan bära $B_i$ kilo, väger $V_i$ kilo och kan kravla $L_i$ m, återge antalet att sätt att ordna dessa på ett unikt sätt.
___
## Burgar Bulk
Givet ett antal olika burgare (och tillbehör) med deras kostnad och kalorier, räkna fram högsta antalet kalorier man kan köpa för en given summa.
___
## Första April
Det är första april och två kompisar ska fullfölja ett antal spratt. Kompisarna använder krypterade meddelanden för att kommunicera när spratten ska genomföras. Din uppgift är att avkoda meddelanden givet en method (Kan göras lättare eller svårare utifrån vilken svårighet vi vill ha på problemet).
___
## Fika Cirkel
Ett gäng kollegor har på ett årsmöte bestämt sig för att de ska turas om att ta med fika. Men då några av kolleagorna är mycket förtjusta i fika så tar de med fika oftare. Sedan har vi några kollegor som är mindre för fika och "glömmer" att ta med. Varje kollega $Ki$ tar med fika med $ni$ dagars mellanrum och tog med fika för första gången $fi$ dagar efter årsmötet. Ta reda på den första dagen när alla kollegor tar med fika samtidigt.
___


