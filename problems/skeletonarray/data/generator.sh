#!/bin/bash

. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution lk.py lk.cpp 

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
tc skel-001 gen_random n=10 m=5 seed=1
tc skel-002 gen_random n=10 m=5 seed=2
tc skel-003 gen_random n=10 m=5 seed=3
tc skel-004 gen_random n=100000 m=1000 seed=4
tc skel-005 gen_random n=100000 maxa=1 m=1000 seed=5

tc skel-011 gen_random n=1 m=5 seed=111
tc skel-012 gen_random n=10 m=5 seed=222
tc skel-013 gen_random n=100 m=1000 seed=333
tc skel-014 gen_random n=100000 m=1000 seed=444
tc skel-015 gen_random n=100000 maxa=1 m=1000 seed=555

tc skel-021 gen_random n=1 m=5 seed=9111
tc skel-022 gen_random n=10 m=5 seed=9222
tc skel-023 gen_random n=100 m=1000 seed=9333
tc skel-024 gen_random n=100000 m=1000 seed=9444
tc skel-025 gen_random n=100000 maxa=1 m=1000 seed=9555

