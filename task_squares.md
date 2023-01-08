# Squares
Given a grid of letters and dots, what is the size of the largest square present consisting of only letters?

## Solution:
Build character count from top left corner to position r,c. By inclusion exclusion principle can count the number of letters within a square. Knows that size of x should have x^2 count letters. Can binary search over maximum square size since the existence of square of size X implies the existent of a square of size X-1.