"""Usage: gen.py SEED MODE; modes: uniform_max_one, uniform_max_half, uniform_max_all, uniform_unit_half, line_one, line_half, line_all, one_missing, random_one, random_half, random_many, hub."""
import random

MODES=('uniform_max_one','uniform_max_half','uniform_max_all','uniform_unit_half',
       'line_one','line_half','line_all','one_missing','random_one','random_half','random_many','hub')

def generate(seed,mode):
    rng=random.Random(seed)
    n=100
    if mode.endswith('_one'):k=1
    elif mode.endswith('_all'):k=n
    elif mode.endswith('_many') or mode=='one_missing':k=n-1
    else:k=n//2
    plants=rng.sample(range(n),k)
    cost=[[0]*n for _ in range(n)]
    if mode.startswith('uniform_'):
        price=100000 if mode.startswith('uniform_max') else 1
        for a in range(n):
            for b in range(a+1,n):cost[a][b]=cost[b][a]=price
        info={'kind':'uniform','expected':(n-k)*price}
    elif mode.startswith('line_'):
        for a in range(n):
            for b in range(a+1,n):cost[a][b]=cost[b][a]=b-a
        info={'kind':'unit_line','expected':n-k}
    elif mode=='hub':
        plants=[0,n-1]
        center=n//2
        for a in range(n):
            for b in range(a+1,n):cost[a][b]=cost[b][a]=100000
        for v in range(n):
            if v==center:continue
            price=2 if v==0 else 3 if v==n-1 else 1
            cost[v][center]=cost[center][v]=price
        info={'kind':'unpowered_hub','expected':n-len(plants)+1,'center':center}
    else:
        for a in range(n):
            for b in range(a+1,n):cost[a][b]=cost[b][a]=rng.randint(1,100000)
        if mode=='one_missing':
            missing=next(v for v in range(n) if v not in plants)
            info={'kind':'one_missing','expected':min(cost[missing][v] for v in plants),'missing':missing}
        else:info={'kind':'independent_Kruskal'}
    assert 1<=len(plants)<=n and len(set(plants))==len(plants)
    assert all(cost[a][a]==0 for a in range(n))
    assert all(1<=cost[a][b]<=100000 and cost[a][b]==cost[b][a] for a in range(n) for b in range(a+1,n))
    return cost,plants,info

if __name__=='__main__':
    import sys
    cost,plants,_=generate(int(sys.argv[1]),sys.argv[2])
    print(len(cost),len(plants))
    print(*(v+1 for v in plants))
    for row in cost:print(*row)
