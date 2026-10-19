# 1911. Minimum Energy to Let a Moving Barrier Pass

[Timus 1911](https://acm.timus.ru/problem.aspx?space=1&num=1911) · difficulty 4214 · math

Original problem by Denis Dublennykh, from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cart of length l moves along a corridor at speed v. A barrier of thickness
L follows at speed V>v; initially its front is distance D behind the cart's
rear. Choose exactly one bypass from the available entry/exit intervals.
The cart maintains speed v until it is fully inside the bypass, then
decelerates uniformly at rate b≥a. Increasing the natural rate a costs
s(b−a) once for that bypass. A shield can hold the barrier against the
cart's rear after it catches up, at cost k per second. It is unnecessary
when the cart is wholly inside the bypass. The whole barrier must pass
the exit before the cart's front returns to the corridor. Stopping and
waiting, then proceeding on foot, is allowed. Minimize total energy.
Limits: 1 second, 64 MB.

## Input

First v,l,V,L,D,a,k,s, all integers. The first six are strictly between
0 and 100 000, v<V, and 0≤k,s≤10 000. Then n, 1≤n≤1000, followed by n
pairs xᵢ,yᵢ giving entry and exit distances from the cart's initial front.
They satisfy 0<xᵢ, xᵢ+l<yᵢ, yᵢ<xᵢ₊₁ for consecutive bypasses,
and yᵢ<100 000. Lengths are in meters, speeds in m/s and deceleration
in m/s²; k is energy per second and s energy per unit of extra deceleration.

## Output

One minimum energy value, with absolute or relative error at most 10⁻⁵.

## Checking

One finite numeric token, compared with absolute/relative tolerance 10⁻⁵.

## Examples

```
1 1 2 1 1 100 1 1234
1
100 102
```

```
100.000
```

## Solution

Evaluate each bypass (x,y) independently. The cart becomes fully hidden
at time τ=(x+l)/v. Without shielding, the barrier catches its rear at
t_c=D/(V−v). Thus the unavoidable shield cost is k·max(0,τ−t_c).
Release the barrier immediately when hidden: holding it longer both
costs more and delays its passage, so cannot help.

The remaining gap at entry is g=max(D−(V−v)τ,0). The barrier front is
then x−g and its rear x−g−L. From that moment it needs
T=(y−x+L+g)/V to clear the exit. The cart's front still has distance
d=y−x−l>0 to travel while fully inside.

With deceleration b, displacement after time t before stopping is
vt−bt²/2. Among trajectories reaching the exit while moving, increasing
b increases arrival time from d/v to 2d/v. The stopping threshold is
b_stop=v²/(2d); stopping permits arbitrary additional waiting.
Consequently the least required deceleration is zero for T≤d/v,
b_stop for T≥2d/v, and 2(vT−d)/T² between these bounds. In the middle
case this follows by solving d=vT−bT²/2; the bounds ensure nonnegative
velocity at arrival. Natural deceleration may already suffice, so the
extra cost is s·max(0,b_required−a).

The shield duration is forced until complete entry, and the least
braking rate is optimal because its price is nonnegative. Taking the
minimum of shield plus braking costs over all bypasses is therefore optimal.
Bypasses not chosen leave the main-corridor speed unchanged.

Avoid subtracting close floating-point quantities before multiplying by
the prices. Express T=N/(vV) and both costs as exact rational numbers:

```text
W = V-v
H = (x+l)W-Dv
N = v(y-x+L)+max(0,-H)
shield cost = k*max(0,H)/(vW)

if N >= 2dV:  Bnum = v²,                 Bden = 2d
elif N <= dV: Bnum = 0,                  Bden = 1
else:         Bnum = 2v²V(N-dV),          Bden = N²

extra = max(0, Bnum-a*Bden)
branch cost = shield cost + s*extra/Bden
```

The comparisons and subtraction in `extra` are integer operations.
Only the two final nonnegative quotients are converted to floating point.
In particular, an exactly zero required energy remains zero. N≤3·10¹⁰;
braking products are below 10²⁶ and energy numerators below 10³⁰, fitting
signed 128 bits. All denominators are positive.

Time is O(n), storing the bypasses takes O(n) space, and the computation
uses O(1) additional state. In the sample, natural braking already stops
the cart; only 100 seconds of shielding must be paid for.

## Language notes

C++ and Rust use signed 128-bit integers for the exact expressions.
Go 1.14 and Java 8 use 64-bit integers for bounded terms and math/big or
BigInteger for wide products. Go converts an exact big.Rat quotient;
Java converts positive numerator and denominator values separately.
Python 3.12 uses exact integers. C++ uses long double for final ratios,
the other ports double precision; all print twelve decimal places.
Handle zero prices, exact arrival/stopping thresholds and v close to V.

The answers agree with a step-by-step simulation of the motion in
90-digit arithmetic, with a binary search on the braking instead of the
formula, on 628 cases, 28 of them built around exact thresholds and zero
prices.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1911_math.cpp](1911_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.031 s | 528 KB |
| [1911_math.go](1911_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1472 KB |
| [1911_math.java](1911_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 3760 KB |
| [1911_math.py](1911_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 612 KB |
| [1911_math.rs](1911_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 324 KB |
