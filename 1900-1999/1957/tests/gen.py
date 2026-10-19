"""Finite proof: all unit-sided elimination choices, independent of variable order."""
from functools import lru_cache
from itertools import combinations,product
from math import gcd
import json
import sys

def normal(rows):
    result=set()
    for a in rows:
        divisor=0
        for x in a:divisor=gcd(divisor,x)
        if divisor:result.add(tuple(x//divisor for x in a))
    return tuple(sorted(result))

maximum_coefficient=maximum_rows=choices_checked=0
@lru_cache(None)
def every_path(rows):
    global maximum_coefficient,maximum_rows,choices_checked
    if not rows:return True
    maximum_rows=max(maximum_rows,len(rows))
    maximum_coefficient=max(maximum_coefficient,max(abs(x) for a in rows for x in a))
    n=len(rows[0]);available=[]
    for i in range(n):
        positive=[a for a in rows if a[i]>0];negative=[a for a in rows if a[i]<0]
        if all(a[i]==1 for a in positive) or all(a[i]==-1 for a in negative):
            available.append(i)
    assert available,rows
    for i in available:
        positive=[a for a in rows if a[i]>0];negative=[a for a in rows if a[i]<0]
        out=[a[:i]+a[i+1:] for a in rows if a[i]==0]
        for lower in negative:
            for upper in positive:
                out.append(tuple(upper[i]*lower[j]-lower[i]*upper[j] for j in range(n) if i!=j))
        choices_checked+=1
        assert every_path(normal(out))
    return True

families=0;pairs=list(combinations(range(4),2))
for decisions in product((-1,0,1),repeat=6):
    edges=[(a,b,s) for (a,b),s in zip(pairs,decisions) if s]
    for mask in range(8):
        n=len(edges);rows=[tuple(-int(i==j) for j in range(n)) for i in range(n)]
        for k in range(3):
            if mask>>k&1:
                rows.append(tuple(-s*((a==k)-(b==k)-(a==k+1)+(b==k+1)) for a,b,s in edges))
        assert every_path(normal(rows));families+=1
report={'all_passed':True,'initial_coefficient_families':families,'all_unit_pivot_paths_certified':True,
        'arbitrary_column_permutations_covered':True,'unique_projected_coefficient_systems':every_path.cache_info().currsize,
        'unit_pivot_steps':choices_checked,'maximum_normalized_coefficient':maximum_coefficient,'maximum_distinct_inequalities':maximum_rows,
        'proof_scope':'4 ranked teams,6 possible unknown oriented non-draw edges,3 adjacent rank inequalities selected by any tie mask. Constants do not affect coefficient trace; parallel bounds merge by minimum. Integer gcd floor changes only RHS. Every possible unit-sided pivot path ends without a stuck system, including all variable-order tie breaks.'}
if sys.argv[1:] == ['--proof']:
    print(json.dumps(report))
else:
    assert sys.argv[1:] == ['certificate']
    print(0)
