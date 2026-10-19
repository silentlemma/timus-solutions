# 1952. Surviving Alternating Area Attacks

[Timus 1952](https://acm.timus.ru/problem.aspx?space=1&num=1952) · difficulty 8210 · dp

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Denis Dublennykh.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n attackers and m healers, N=n+m. Everyone starts at (0,0),
has health H and moves at speed v. An aura has a maximum c, growth rate r
while its owner casts, and decay rate f while its owner runs. Its power
stays in [0,c], changes continuously, and remains active during movement.
An attacker removes its power from the target's health per second. Each
healer adds its power to every participant's health per second, capped at H.
Initially attacking powers are zero and healing powers are their maxima.

Attacks follow a given chronological list. At the start of Storm everyone
runs straight to its center and then casts. Storm deals D damage per second
only until each individual reaches the center. During Breath, choose a
bijection from people to its N distinct sites. Everyone runs straight to
their assigned site and then casts; D damage continues for the entire Breath,
including time at the site. Passing another site does not permit casting.
Tail immediately kills everyone and occurs exactly once, last. There are
never three consecutive Breaths. All movement takes at most the attack's
duration. Each Storm lasts long enough for surviving people to regain full
health and all aura maxima. Every D is strictly larger than the sum of
healing maxima.

Health zero kills the entire group immediately. Target health zero alone
does not end the attacks: an instantaneous finishing action additionally
requires everyone alive and together at the active Storm's center. At a
boundary the previous attack still applies. Find the earliest attack index
where a finish is possible. Time limit 1 second; memory limit 64 MB.

## Input

First n,m,k: 1≤n,m≤9, N≤10, 1≤k≤10. Next H,v,G, where G is target
health: 1≤H,G≤10⁹, 1≤v≤10⁶. Then n attacking and m healing triples c,r,f,
each integer in [1,10⁶]. Each of the k blocks starts with its case-sensitive
name. Storm has a line D,T followed by one x,y center. Breath has D,T
followed by N x,y sites. Tail has no other fields. For both spells,
1≤D,T≤10⁶ and −1000≤x,y≤1000. All stated guarantees apply. Movement
time is Euclidean distance divided by v and can be irrational.

## Output

If impossible print `You are not prepared`. Otherwise print
`No useful loot again` and the earliest 1-based attack index on the next line.

## Checking

Outputs are compared token by token.

## Examples

```
1 1 2
1 5 10
1 3 2
1 1 1
Storm
7 10
0 0
Tail
```

```
You are not prepared
```

```
1 1 2
1 5 10
1 3 2
1 1 1
Storm
7 11
0 0
Tail
```

```
No useful loot again
1
```

## Solution

Storm endpoints reset positions, health and powers. Partition the list into
blocks with zero, one or two Breaths followed by Storm, using the initial
state as a virtual endpoint. Ignore a final Breath-only suffix before Tail.
Only the initial block starts with attacking powers zero. Maximize target
damage separately in every surviving block, then accumulate it; future
choices are independent because each endpoint is a full reset.

Let L be the largest distance from the last Breath's sites to the next center,
divided by v. Every site is occupied, so L is assignment independent. Before
L, at least the last-arriving person is under damage. Since D exceeds total
possible healing, that person's health decreases strictly throughout all
Breaths and until arrival. Earlier arrivals avoid some damage and therefore
have at least as much health. Thus checking strict survival at L is enough;
after L everyone is safe and may finish at any time through Storm's end.

Write B for the sum of healing maxima. The unavoidable loss is
ΣBreath (D−B)T + (Dstorm−B)L. Subtract it from H to obtain budget K.
For each healer and choice of sites, its additional cost is the integral
of (c−power) through the Breaths and the first L seconds of Storm. Survival
requires the sum of these nonnegative costs to be strictly below K.
For attackers, the weight is the integral of power through the entire block,
including all of the final Storm. Integrate falling and rising linear pieces,
clipping at zero and c. Using deficits directly avoids subtracting two large
nearly equal total healing integrals.

For a party process its people in fixed order. With one Breath, dp[S] is
the best weight after assigning the first |S| people to sites S. With two,
dp[S,U] uses those two subsets in the respective Breaths. Add one unused
site in each layer and the current person's weight for that pair. Minimize
healer costs and maximize attacker damage separately. For every healer
mask or mask pair that survives, use the complementary attacker masks.
The recurrence enumerates every injection and keeps its optimum; disjoint
complements fill all sites, proving both feasibility and maximal damage.
With no Breath there is no assignment and survival is a direct radical
comparison. Return the first Storm whose cumulative maximum damage is ≥G.

### Exact comparisons

An epsilon cannot distinguish a dead person at exactly zero health. General
geometry uses outward-rounded intervals for travel, aura integration and
assignment error. A threshold is accepted only when the whole enclosure
proves the inequality. Otherwise refine the relevant restricted assignment
exactly. Store values as canonical sums Σ q_d√d with rational coefficients
and squarefree d. These radicals are linearly independent over the rationals,
so zero has exactly all coefficients zero. For a nonzero sum bound each
radical with integer square roots at increasing decimal precision; the
interval eventually excludes zero. Exact comparisons also choose between
overlapping candidate assignments and resolve cumulative damage ties.
No fixed tolerance or unproved floating-point tie rule is used.

Python additionally uses exact integer weights when all travel lengths are
rational. Scale powers by v and time by v; a party's common denominator is
2v² times the lcm of its growth and decay rates. Reduce weights and the
denominator by their gcd. Strict health becomes integer cost <ceil(KQ).
If a two-layer integer tensor is exactly a row term plus a column term,
solve its two layers independently. This shortcut is checked exactly.

For a two-Breath block, the combined parties' ordinary DP has exactly
N²·C(2N−2,N−1) transitions, at most 4,862,000 for N=10. One layer costs
O(N·2ᴺ). Native ports store compact equal-cardinality mask pairs, using
O(C(2N,N)) states (184,756 at N=10); Python uses O(4ᴺ) addressed slots.
Weights need O(N³) work and storage. Multiply by the number of blocks.
Exact ambiguous comparisons add restricted assignment work and arbitrary
precision arithmetic; the ordinary transition count alone does not bound
their bit complexity. Refinement terminates by the radical sign argument.

Do not stop damage at Breath arrival, freeze a running aura, heal only its
owner, permit two occupants at one site, or finish while passing an old
center during Breath. Initial Breaths are legal. Mage health must be >0,
but target health may be zero. Initial attacking power is zero. The Storm
recovery promise is essential for decomposing blocks; stress inputs must
also satisfy it. Keep enough integer range for squared coordinates, rates
and exact rational numerators.

## Language notes

Go and Java use their arbitrary-precision integers, Python its integers
and Fraction, C++ its own long arithmetic with fractions, long division
and an integer square root, and Rust its own numbers of 32-bit limbs.
Java shares the tensors of identical auras and frees temporary exact
objects from time to time to keep its heap small. The exact refinement
restores the choices through parent links instead of keeping a symbolic
number in every subset state.

Python first decides in doubles with certified error bounds: a matching
relaxation and one-layer completion DPs give bounds that settle most
battles, and the full DP and the exact arithmetic run only when the
bounds cannot decide. It runs under PyPy, 0.83 s of the 1 s on the
judge; an earlier version that always ran the full DP exceeded the time
limit on the judge's test 21. Rust follows the Go solution with plain
loops and few generic functions: an earlier Rust version ran out of the
judge's compilation time.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1952_dp.cpp](1952_dp.cpp) | G++ 13.2 x64 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.156 s | 3100 KB |
| [1952_dp.go](1952_dp.go) | Go 1.14 x64 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.078 s | 17616 KB |
| [1952_dp.java](1952_dp.java) | Java 1.8 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.312 s | 10864 KB |
| [1952_dp.py](1952_dp.py) | PyPy 3.10 x64 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.828 s | 26964 KB |
| [1952_dp.rs](1952_dp.rs) | Rust 1.75 x64 | dp | O(k N^2 C(2N-2,N-1)) plus exact refinement | AC | 0.062 s | 4224 KB |
