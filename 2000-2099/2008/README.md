# 2008. Three Ballistic Jumps

[Timus 2008](https://acm.timus.ru/problem.aspx?space=1&num=2008) · difficulty 1038 · math

Original problem by Olga Karpova. (Prepared by Alexey Kungurtsev), from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A point object starts at one of two hand points, whose identity is
unknown. It jumps to the other hand, back to its starting hand, then to
a head point. Each jump may choose a new initial velocity of magnitude
at most `v`. During a jump the only force is downward gravity `g=9.8`;
horizontal velocity is constant. Determine whether either starting hand
permits all three jumps. The three locations are fixed distinct points
in one vertical plane, with the y-axis pointing upward.

## Input

Integer `v`, followed by three coordinate pairs in the order head, left
hand, right hand. Speed and every coordinate are nonnegative integers at
most 10000. Coordinates are in meters and speed in meters per second.
Time 0.5 seconds, memory 64 MB.

## Output

Print exactly `Yes` if the jumps are possible, otherwise `No`. The
single token is compared exactly.

## Checking

Outputs are compared token by token.

## Examples

```
10
0 5
0 0
10 0
```

```
Yes
```

```
10
10 5
0 0
10 0
```

```
Yes
```

```
5
0 5
0 0
10 0
```

```
No
```

At speed 10 the hand-to-hand jumps of distance 10 are possible. The
first example finishes from the left hand; the second finishes from the
right. Speed 5 cannot bridge the hands in the third example.

## Solution

Both directions between the hands are required regardless of the
starting hand. The last jump can start at either hand. Thus require
`left→right` and `right→left`, together with `left→head` or
`right→head`. Vertical displacement makes reachability directional.

For a single jump let displacements be `dx,dy`, flight time `t>0`, and
`r=sqrt(dx²+dy²)>0`. The needed launch components are `ux=dx/t` and
`uy=dy/t+g t/2`. Their squared magnitude is

`u²(t)=r²/t²+g dy+g²t²/4`.

The first and last terms have minimum sum `g r`, attained at `t²=2r/g`.
Consequently the minimum possible squared launch speed is `g(r+dy)`.
This is nonnegative, and every pair of distinct points has a positive
minimizing flight time. A purely vertical downward jump may require zero
launch speed: free fall is valid.

A jump is possible exactly when `v²≥(49/5)(r+dy)`. Let `T=5v²−49dy`. The
condition becomes `T≥49r`, equivalent to `T≥0` and `T²≥49²(dx²+dy²)`.
These are exact integer comparisons. The sign check must precede
squaring; equality is reachable and no floating-point tolerance is
required.

Each of the four directed reachability checks is necessary as stated. If
the two hand directions and a hand-to-head direction pass, choose that
hand as the initial one, use its two hand jumps and then its head jump.
Conversely any valid sequence has those same required directions. This
proves the complete decision.

Time `O(1)` and memory `O(1)` for the fixed three points. Signed 64-bit
integers suffice: `|T|≤500490000`, so `T²≤250490240100000000<2^63`, and
`49²(dx²+dy²)≤480200000000`. Multiplication must already be in 64-bit
arithmetic.

## Language notes

Read the head before the hands. Test both hand directions, and allow
either hand for the last jump. Use signed displacements despite
nonnegative input coordinates. Keep `g=49/5` exactly; do not round it to
10 or take square roots in the program. Handle `v=0`, negative `dy`,
vertical trajectories and equality. C++, Go, Java and Rust use signed
64-bit arithmetic throughout; Python integers are exact.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2008_math.cpp](2008_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 384 KB |
| [2008_math.go](2008_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1092 KB |
| [2008_math.java](2008_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 440 KB |
| [2008_math.py](2008_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 516 KB |
| [2008_math.rs](2008_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.062 s | 228 KB |
