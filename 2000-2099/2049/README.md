# 2049. Construct transfers by reversing equal splits

[Timus 2049](https://acm.timus.ru/problem.aspx?space=1&num=2049) · difficulty 3274 · constructive

Original problem by Daniil Ayzenshteyn, prepared by Egor Shchelkonogov, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n containers, each holding one unit. An action a → b pours
from a into b exactly as much as b currently holds, so (x, y) becomes (x
− y, 2y); it is allowed only when x ≥ y. Using at most 3n actions, make
container 1 hold exactly k units; the other containers may end with
anything. The limits are 1 second and 64 MB.

## Input

Two integers n and k, 1 ≤ k ≤ n ≤ 100 000.

## Output

Print `-1` if it is impossible. Otherwise print the number of actions M,
0 ≤ M ≤ 3n, and then M lines with the pairs a b of distinct containers.

## Checking

A checker performs the actions and verifies that each one is allowed and
that container 1 ends with k units; any valid sequence is accepted, and
`-1` only when the task is impossible.

## Examples

```
5 3
```

```
4
2 1
4 3
3 1
1 5
```

```
5 5
```

```
-1
```

The first example changes the volumes as
`[1,1,1,1,1]→[2,0,1,1,1]→[2,0,2,0,1]→[4,0,0,0,1]→[3,0,0,0,2]`. The first
container ends at three. In the second example all five units would have
to be concentrated together; the invariant below makes this impossible.

## Solution

### Feasibility

If `k` is a power of two, including one, the answer exists. Otherwise it
exists exactly when `n≥k+1+(k mod 2)`.

The odd part of the gcd of all volumes never changes. For any odd prime
power `q`, all coordinates after `(x,y)→(x-y,2y)` are divisible by `q`
exactly when they were before, because two is invertible modulo `q`.
Initially the gcd is one. Therefore, if `n=k`, concentrating everything
would require `k` to be a power of two.

For odd `k>1`, consider the first time container one becomes `k`. It
cannot be the destination, since doubling gives an even amount. As donor
it must previously hold `k+y` while the recipient holds `y≥1`, requiring
at least `k+2` units in total. These prove all excluded cases.
Sufficiency follows from the construction.

### Reverse construction

Use `N=k` containers for a power of two, otherwise `N=k+1+(k mod 2)`.
Unused containers stay at one. Begin at the desired **final** state:
`[k,0,…]` for a power of two, or `[k,N-k,0,…]` otherwise. Here `N-k` is
one or two and the odd gcd part is one.

A reverse action chooses a positive even amount `2h` in container `b`
and moves half into another container `a`: `(x,2h)→(x+h,h)`. Record the
original forward pair `(a,b)`. Each such step can later be undone
legally, since `x+h≥h`. Reverse the **order** of the recorded pairs at
the end, keeping each pair's direction.

Maintain empty containers, positive even containers, and groups of
positive odd containers by amount.

1. If there are at least two even containers, split any one into an
   empty container.
2. If the only even amount is divisible by four, also split it into an
   empty container.
3. Otherwise it is `2h` with `h` odd. Choose an odd amount `a≠h`. Keep
   these **same two containers** and apply reverse actions, swapping
   their even/odd roles after each action, until the even amount becomes
   divisible by four. Then split that amount on the next iteration.
4. If no odd amount differs from `h`, the odd gcd part would be `h`;
   hence `h=1`. Only one amount is two and all other positive amounts
   are one. Split the last two.

An empty container always exists when needed: mass `N` and a positive
amount greater than one imply fewer than `N` nonempty containers. A
plain split preserves an even container unless it is the final split.
The other reverse steps also preserve one.

For the fixed pair `(2h,a)`, the half and odd amount evolve as
`(h,a)→((h+a)/2,h)` while the new half remains odd. Their nonzero
difference `D=a-h` becomes `-D/2`. Thus, after exactly `t=ν2(|D|)`
steps, the half is even and the whole even amount is divisible by four.
Every such run terminates, after which a split increases the number of
positive containers. Eventually there are `N` positives with total mass
`N`, hence all are one. Reversing the recorded actions gives a valid
forward solution with the required first container.

### Proving the action limit

This proof uses an analytic bound and a small **exhaustive finite
verification**, supplied below and in [tests/gen.py](tests/gen.py).

Let `L(v)=floor(log2(v))` for positive `v`, `F=sum L(v)` and `P` be the
number of positive containers. Charge each action or group of actions at
most `2ΔF+3ΔP`.

A plain split `2h→h,h` costs one, has `ΔP=1` and `ΔF=L(h)-1≥-1`, so its
charge is sufficient.

Group a run of `t` reverse actions with its immediately following split.
This phase costs `t+1` and has `ΔP=1`. Write `a-h=2^t d` with `d` odd
and signed, `ε=(-1)^t` and `T=2h+a`. After the phase the pair has become
three positive amounts `b,b,c`, where `b=(T-εd)/3` is even and `c=T-2b`
is odd. Indeed the half recurrence is `h_next=(T-h)/2`, whose fixed
point is `T/3`; solving it gives this formula.

We need `ΔF≥floor((t-1)/2)`, which implies `t+1≤2ΔF+3`.

For `t=1`, `b=(h+a)/2,c=h`. If `q=L(max(h,a))`, then `b≥max(h,a)/2`
gives `ΔF=2L(b)-L(a)-1≥q-3`. This suffices for `q≥3`; otherwise both
inputs are below eight.

For `t≥2` put `u=min(h,a),v=max(h,a),p=L(u),q=L(v)`. Averaging keeps
`b,c≥u`. Also `b,c≥v/4`: for `a≥h`, even `t` gives `b≥(a+3h)/4,c≥a/3`,
while odd `t≥3` gives `c≥(a+3h)/4,b≥a/3`; for `h>a` the formulas give
both at least `h/2`. Therefore `ΔF≥3max(p,q-2)-p-q-1≥q-5`. Since
`|a-h|≥2^t`, `q≥t`. For `t≥8` this proves the desired inequality. For
`2≤t≤7` it also suffices when `q≥5+floor((t-1)/2)`. In the remaining
cases `q≤7`, so both odd inputs are below 256.

Consequently all remaining cases, including the small `t=1` cases, are
exactly covered by checking all 16256 ordered distinct positive odd
inputs below 256:

```python
L = lambda x: x.bit_length() - 1
for h in range(1, 256, 2):
    for a in range(1, 256, 2):
        if a == h:
            continue
        D = a - h
        t = (abs(D) & -abs(D)).bit_length() - 1
        d = D // (1 << t)
        T = 2 * h + a
        b = (T - (-1) ** t * d) // 3
        c = T - 2 * b
        delta = 2 * L(b) + L(c) - L(2 * h) - L(a)
        assert t + 1 <= 2 * delta + 3
```

All assertions pass, completing the phase inequality. Summing over plain
splits and complete phases, the final state has `F=0,P=N`, so
`M≤2(0-F_initial)+3(N-P_initial)≤3N≤3n`. No empirical cutoff on `n` or
on the number of moves is used.

### Implementation and complexity

Use doubly linked lists stored in arrays. Positive even containers share
one list; odd containers belong to the list indexed by their current
amount. Another list contains the nonempty odd-amount groups. To find an
odd amount different from `h`, use that group's head or the next group.
Each transfer removes its two old memberships before changing amounts,
then inserts the new memberships. Container links can be reused between
the even and odd lists.

All list operations are constant time, with no scanning of sparse sets.
Each recorded action and output line costs constant time, so time and
space are `O(N+M)=O(n)`.

## Language notes

The destination doubles; the amount transferred is not arbitrary.
Preserve the first container's identity. Reverse action order, not the
pairs themselves. Keep the same pair throughout a run so the termination
and phase proof apply. Empty containers are needed only for splits. Zero
actions are correct for `k=1`.

All ports use compact arrays and separate action buffers. Python uses
unsigned `array` fields and chunked output; Java uses primitive arrays
and a reusable byte output buffer. C++/Go/Rust stream buffered output.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2049_constructive.cpp](2049_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.031 s | 5052 KB |
| [2049_constructive.go](2049_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.046 s | 14800 KB |
| [2049_constructive.java](2049_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 7888 KB |
| [2049_constructive.py](2049_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.593 s | 5608 KB |
| [2049_constructive.rs](2049_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.015 s | 9200 KB |
