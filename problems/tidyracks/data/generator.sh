#!/bin/bash
USE_SCORING=0
. ../../testdata_tools/gen.sh

#PPATH=$(realpath ..)
#. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution lk.cpp

compile gen_random.py 
compile gen_targeted.py

sample 1
sample 2
#sample_manual 1
#sample_manual 2

#group empty
tc empty-001 gen_random n=5 k=5 mode=empty seed=9
tc empty-002 gen_random n=5 k=5 mode=empty seed=2
tc empty-003 gen_random n=500 k=50 mode=empty seed=3
tc empty-004 gen_random n=10000 k=100 mode=empty seed=4
tc empty-005 gen_random n=10000 k=100 mode=empty seed=5
tc empty-006 gen_random n=10000 k=100 maxa=1 mode=empty seed=6

#group no_empty
tc no-empty-001 gen_random n=5 k=5 mode=no_empty seed=1
tc no-empty-002 gen_random n=5 k=5 mode=no_empty seed=2
tc no-empty-003 gen_random n=500 k=50 mode=no_empty seed=3
tc no-empty-004 gen_random n=10000 k=100 mode=no_empty seed=4
tc no-empty-005 gen_random n=10000 k=100 mode=no_empty seed=5
tc no-empty-006 gen_random n=10000 k=100 mode=no_empty seed=6
tc no-empty-007 gen_random n=8 k=8 mode=no_empty seed=318
tc no-empty-008 gen_random n=8 k=8 mode=no_empty seed=328
tc no-empty-009 gen_random n=8 k=8 mode=no_empty seed=338
tc no-empty-010 gen_random n=8 k=8 mode=no_empty seed=348

#group rand
tc rand-001 gen_random n=5 k=5 seed=1
tc rand-002 gen_random n=5 k=5 seed=266
tc rand-003 gen_random n=500 k=50 seed=3
tc rand-004 gen_random n=10000 k=100 seed=4
tc rand-005 gen_random n=10000 k=100 maxa=1 seed=123
tc rand-006 gen_random n=10000 k=100 maxa=1 seed=1234

tc fool-001 gen_targeted target=1
tc fool-002 gen_targeted target=2
tc fool-003 gen_targeted target=3