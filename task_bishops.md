# Bishops
Given an integer $N$. How many bishops can you place on a $NxN$ chess board so that no two bishops attack each other?

## Solution:
Trivial for $N=1$ and $N=2$.

For larger $N$, apply diagonal line interpretation framework (down left to top right and down right and top left), $2N-1$ lines for each direction. In total $4N-2$ lines.

Invariant - A placed bishop is attacking along exactly 2 diagonal lines.

Theoretical maximum therefore becomes $(4N-2) / 2 = 2N-1$. Note however that the main diagonal always prevents atleast one of the diagonal edge lines of the opposite direction. By symmetry a total of two diagonal lines are disqualified, the theoretical max is reduced by one biship, giving new theoretical max of $2N-2$ bishops. For $N >= 3$ there exists a configuration that yields $2N-2$ bishops placed. Along two opposite edges only two corners will be left out.