"""Usage: gen.py SEED MODE; modes: zero, identical, horizontal, vertical, diagonal, antipodal, farey, four_groups, six_groups, random, parabola, grid."""
import random

MODES=('zero','identical','horizontal','vertical','diagonal','antipodal',
       'farey','four_groups','six_groups','random','parabola','grid')

def generate(seed,mode,n=1000):
    rng=random.Random(seed)
    types=None
    if mode=='zero':
        types=[(0,0)]
    elif mode=='identical':
        types=[(10**6,-10**6)]
    elif mode=='antipodal':
        types=[(10**6,10**6-1),(-10**6,-10**6+1)]
    elif mode=='farey':
        types=[(10**6,10**6-1),(10**6-1,10**6-2),
               (-10**6,-10**6+1),(-10**6+1,-10**6+2)]
    elif mode=='four_groups':
        types=[(10**6,10**6),(10**6,-10**6),(-10**6,10**6),(-10**6,-10**6)]
    elif mode=='six_groups':
        types=[(10**6,1),(-10**6,-1),(137,-999983),(-999979,997),
               (0,0),(931937,771991)]
    if types is not None:
        counts=[n//len(types)+(i<n%len(types)) for i in range(len(types))]
        points=[point for point,count in zip(types,counts) for _ in range(count)]
        rng.shuffle(points)
        return points,{'kind':'types','types':types,'counts':counts}
    if mode in ('horizontal','vertical','diagonal'):
        limit=5*10**5 if mode=='diagonal' else 10**6
        values=[rng.randint(-limit,limit) for _ in range(n)]
        if mode=='horizontal':
            direction=(1,0)
        elif mode=='vertical':
            direction=(0,1)
        else:
            direction=(1,2)
        return [(v*direction[0],v*direction[1]) for v in values],{
            'kind':'collinear','values':values,'direction':direction}
    if mode=='random':
        points=[(rng.randint(-10**6,10**6),rng.randint(-10**6,10**6)) for _ in range(n)]
    elif mode=='parabola':
        points=[((i-n//2)*2000,(i-n//2)**2) for i in range(n)]
        rng.shuffle(points)
    elif mode=='grid':
        points=[((i%32-16)*60000,(i//32-16)*60000) for i in range(n)]
        rng.shuffle(points)
    else:
        raise ValueError(mode)
    return points,{'kind':'projection_certificate'}

if __name__=='__main__':
    import sys
    points,_=generate(int(sys.argv[1]),sys.argv[2])
    print(len(points))
    for x,y in points:
        print(x,y)
