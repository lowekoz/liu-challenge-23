#!/usr/bin/env bash

PPATH=$(realpath ..)
. ../../testdata_tools/gen.sh

use_solution herman.py

compile gen_random.py

MAXN=25000
MAXA=25

samplegroup
limits n=$MAXN
sample 1
sample 2

group group1 25
limits n=1000
tc 1
tc 2
tc small-1 gen_random n=1000 k=1000 maxa=$MAXA mode=random 1
tc small-2 gen_random n=1000 k=1000 maxa=$MAXA mode=star 2
tc small-3 gen_random n=1000 k=1000 maxa=$MAXA mode=long 3

group group2 30
limits n=$MAXN k=10
tc 1
tc 2
tc few-1 gen_random n=$MAXN k=10 maxa=$MAXA mode=random 4
tc few-2 gen_random n=$MAXN k=10 maxa=$MAXA mode=star 5
tc few-3 gen_random n=$MAXN k=10 maxa=$MAXA mode=long 6

group group3 45
limits n=$MAXN
include_group group1
include_group group2
include_group sample
tc large-1 gen_random n=$MAXN k=$MAXN maxa=$MAXA mode=random 7
tc large-2 gen_random n=$MAXN k=$MAXN maxa=$MAXA mode=star 8
tc large-3 gen_random n=$MAXN k=$MAXN maxa=$MAXA mode=long 9
