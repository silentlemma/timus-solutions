"""Usage: gen.py SEED MODE; modes: whole, points, prefix, disjoint, zero_reserve, many_enforce, triangular_probe, mixed_point, disjoint_triangle, prefix_triangle, disjoint_two_triangles, disjoint_512_triangles, disjoint_2048_triangles, mixed_cells, mixed_gadgets."""
from collections import deque
from fractions import Fraction
import random


def generate(seed, mode, count=100000):
    rng = random.Random(seed)
    length, rate = 10**9, 100
    events, answers = [], []
    step = 10**9 // count
    if mode in ("mixed_cells", "mixed_gadgets"):
        if mode == "mixed_cells":
            length = 127
        start = 10**9-count+1
        for j in range(count):
            if mode == "mixed_cells":
                left,right = 1,length
                enforce = rng.random() < .48
            else:
                groups = count//100
                width = length//groups
                group,k = divmod(j,100)
                left,right = group*width+1,(group+1)*width
                enforce = k != 99 and rng.random() < .49
            if enforce:
                center = rng.randint(left,right)
                radius = rng.randint(1,min(center-left+1,right+1-center))
                events.append((start+j,1,center,radius))
            else:
                a,b = ((left,right) if mode == "mixed_gadgets" and k == 99 else
                       sorted([rng.randint(left,right),rng.randint(left,right)]))
                events.append((start+j,0,a,b))
    elif mode in ("disjoint_two_triangles", "disjoint_512_triangles", "disjoint_2048_triangles"):
        cycles = {"disjoint_two_triangles":2,"disjoint_512_triangles":512,
                  "disjoint_2048_triangles":2048}[mode]
        initial_time = 10**9-count+1
        center = radius = length//2
        denominator = radius*radius
        for j in range(cycles):
            t = initial_time+2*j
            events.extend([(t,0,1,length),(t+1,1,center,radius)])
            answers.append(Fraction(length*rate*t))
        base_time = initial_time+2*(cycles-1)
        initial = length*rate*base_time
        remaining = count-2*cycles
        positions = list(range(remaining))
        rng.shuffle(positions)
        width = length//remaining
        reserve = weights = 0
        def weight(x):
            if x <= center:
                return x*(x+1)//2
            k = x-center
            return center*(center+1)//2+k*radius-k*(k+1)//2
        for j,cell in enumerate(positions,2*cycles):
            t = initial_time+j
            a,b = cell*width+3,cell*width+width//2
            reserve += rate*(t-base_time)*(b-a+1)
            weights += weight(b)-weight(a-1)
            events.append((t,0,a,b))
            answers.append(Fraction(reserve*denominator+initial*weights,denominator))
    elif mode in ("disjoint_triangle", "prefix_triangle"):
        initial_time = 10**9-count+1
        initial = length*rate*initial_time
        center = radius = length//2
        denominator = radius*radius
        events = [(initial_time,0,1,length),(initial_time+1,1,center,radius)]
        answers = [Fraction(initial)]
        def prefix_weight(x):
            if x <= center:
                return x*(x+1)//2
            k = x-center
            return center*(center+1)//2+k*radius-k*(k+1)//2
        reserve = weights = covered = 0
        positions = list(range(count-2))
        rng.shuffle(positions)
        width = length//(count-2)
        painted = deque([(1,length,initial_time)])
        for j in range(2,count):
            t = initial_time+j
            if mode == "disjoint_triangle":
                cell = positions[j-2]
                a,b = cell*width+3,cell*width+width//2
                reserve += rate*(t-initial_time)*(b-a+1)
                weights += prefix_weight(b)-prefix_weight(a-1)
            else:
                a,b = 1,rng.randint(1,length)
                while painted and painted[0][1] <= b:
                    left,right,last = painted.popleft()
                    reserve += rate*(right-left+1)*(t-last)
                if painted and painted[0][0] <= b:
                    left,right,last = painted.popleft()
                    reserve += rate*(b-left+1)*(t-last)
                    painted.appendleft((b+1,right,last))
                painted.appendleft((1,b,t))
                covered = max(covered,b)
                weights = prefix_weight(covered)
            events.append((t,0,a,b))
            answers.append(Fraction(reserve*denominator+initial*weights,denominator))
    elif mode == "disjoint":
        positions = list(range(count))
        rng.shuffle(positions)
        reserve = 0
        width = length // count
        for j, cell in enumerate(positions):
            t = (j+1)*step
            a, b = cell*width+3, cell*width+width//2
            events.append((t, 0, a, b))
            reserve += rate*t*(b-a+1)
            answers.append(Fraction(reserve))
    elif mode in ("whole", "points", "prefix"):
        positions = rng.sample(range(1, length+1), count) if mode == "points" else None
        painted = deque([(1, length, 0)])
        reserve = 0
        for j in range(count):
            t = (j+1)*step
            if mode == "whole":
                a, b = 1, length
                reserve = length*rate*t
            elif mode == "points":
                a = b = positions[j]
                reserve += rate*t
            else:
                a, b = 1, rng.randint(1, length)
                while painted and painted[0][1] <= b:
                    left, right, last = painted.popleft()
                    reserve += rate*(right-left+1)*(t-last)
                if painted and painted[0][0] <= b:
                    left, right, last = painted.popleft()
                    reserve += rate*(b-left+1)*(t-last)
                    painted.appendleft((b+1, right, last))
                painted.appendleft((1, b, t))
            events.append((t, 0, a, b))
            answers.append(Fraction(reserve))
    elif mode in ("zero_reserve", "many_enforce"):
        for j in range(count):
            t = (j+1)*step
            if mode == "many_enforce" and j % 2 == 0:
                events.append((t, 0, 1, length))
                answers.append(Fraction(length*rate*t))
            else:
                center = rng.randint(1, length)
                radius = rng.randint(1, min(center, length+1-center))
                events.append((t, 1, center, radius))
    elif mode in ("triangular_probe", "mixed_point"):
        initial_time = 10**9-count+1
        initial = length*rate*initial_time
        events.append((initial_time, 0, 1, length))
        answers.append(Fraction(initial))
        if mode == "triangular_probe":
            center, radius = length//2, length//2
            events.append((initial_time+1, 1, center, radius))
            positions = rng.sample(range(1, length+1), count-2)
            elapsed_sum = weights_sum = 0
            denominator = radius*radius
            for j, position in enumerate(positions, 2):
                t = initial_time+j
                events.append((t, 0, position, position))
                elapsed_sum += j
                weights_sum += max(0, radius-abs(position-center))
                answers.append(Fraction(rate*elapsed_sum*denominator+initial*weights_sum, denominator))
        else:
            reserve = initial
            delta = {}
            for j in range(1, count):
                t = initial_time+j
                position = rng.choice((1, length, length//2, rng.randint(1, length)))
                old = delta.get(position, -rate*initial_time)
                if j % 2:
                    events.append((t, 1, position, 1))
                    delta[position] = old+reserve
                    reserve = 0
                else:
                    events.append((t, 0, position, position))
                    reserve += rate*t+old
                    delta[position] = -rate*t
                    answers.append(Fraction(reserve))
    else:
        raise ValueError(mode)
    assert len(events) == count
    assert all(0 <= t <= 10**9 for t, _, _, _ in events)
    assert all(events[j][0] < events[j+1][0] for j in range(count-1))
    return length, rate, events, answers


if __name__ == "__main__":
    import sys
    n,p,events,_ = generate(int(sys.argv[1]),sys.argv[2])
    print(n,p)
    print(len(events))
    for t,kind,a,b in events:
        print(t,"enforce" if kind else "save",a,b)
