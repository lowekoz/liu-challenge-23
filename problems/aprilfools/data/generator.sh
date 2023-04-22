#!/bin/bash
PPATH=$(realpath ..)
. ../../testdata_tools/gen.sh

#PPATH=$(realpath ..)
#. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution solve.py 

compile gen_random.py

samplegroup
sample 1
sample 2
#sample_manual 1
#sample_manual 2

#group empty
#tc empty-001 gen_random n=5 k=5 mode=empty seed=9

group g1 100
include_group sample
tc test-001 gen_random n=10 m=5 extra=0.0 seed=1
tc test-002 gen_random n=10 m=5 extra=0.0 seed=2
tc test-003 gen_random n=10 m=5 extra=0.0 seed=3
tc test-004 gen_random n=100 m=1000 extra=0.0 seed=4
tc test-005 gen_random n=100 m=1000 extra=0.0 seed=5

tc test-011 gen_random n=1 m=5 extra=0.5 seed=111
tc test-012 gen_random n=10 m=5 extra=0.5 seed=222
tc test-013 gen_random n=100 m=1000 extra=0.5 seed=333
tc test-014 gen_random n=100 m=1000 extra=0.5 seed=444
tc test-015 gen_random n=100 m=1000 extra=0.5 seed=555

tc test-021 gen_random n=1 m=5 extra=1.0 seed=1432
tc test-022 gen_random n=10 m=5 extra=1.0 seed=2432
tc test-023 gen_random n=100 m=1000 extra=1.0 seed=3432
tc test-024 gen_random n=100 m=1000 extra=1.0 seed=4432
tc test-025 gen_random n=100 m=1000 extra=1.0 seed=5432
