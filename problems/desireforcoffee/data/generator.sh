#!/bin/bash

. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution anton_dp.py

compile gen_random.py

samplegroup
sample 1
sample 2

group g1 100
include_group sample
tc coff-001 gen_random n=10 m=5 seed=1
tc coff-002 gen_random n=10 m=5 seed=2
tc coff-003 gen_random n=10 m=500 seed=3
tc coff-004 gen_random n=1000 m=500 seed=4
tc coff-005 gen_random n=1000 maxa=1 m=500 seed=5

tc coff-011 gen_random n=2 m=5 seed=91
tc coff-012 gen_random n=10 m=50 seed=92
tc coff-013 gen_random n=100 m=500 seed=93
tc coff-014 gen_random n=1000 m=500 seed=94
tc coff-015 gen_random n=1000 maxa=1 m=500 seed=95

tc coff-021 gen_random n=99 m=10 seed=29111
tc coff-022 gen_random n=99 m=10 seed=29222
tc coff-023 gen_random n=99 m=10 seed=29333
tc coff-024 gen_random n=1000 m=10 seed=29444
tc coff-025 gen_random n=1000 maxa=1 m=10 seed=29555