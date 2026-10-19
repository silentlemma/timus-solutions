# 2062. Accumulate radiation at divisors

[Timus 2062](https://acm.timus.ru/problem.aspx?space=1&num=2062) · difficulty 295 · fenwick

Original problem by Alexey Danilyuk, prepared by Nikita Sivukhin, from the Ural Regional School Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A chain has n particles with initial charges a[i]. Directing power d at
particle k adds d to every particle whose number is a multiple of k. An
operation `2 l r d` directs power d at every particle from l to r, each
separately, so a particle reached from several of them gets several
additions; an operation `1 i` asks for the current charge of particle i.
The limits are 3 seconds and 128 MB.

## Input

First n, then the n charges a[i], then q and the q operations. 1 ≤ n, q
≤ 300 000, 0 ≤ a[i], d ≤ 10⁶, 1 ≤ i ≤ n, 1 ≤ l ≤ r ≤ n.

## Output

The answers to the queries, one per line.

## Checking

Outputs are compared token by token.

## Examples

Each input block below is followed by its output.

```
3
1 2 3
2
2 1 3 5
1 2
```

```
12
```

```
6
1 2 1 4 5 6
5
2 2 4 2
1 3
1 4
2 3 5 1
1 5
```

```
3
8
6
```

In the first experiment, irradiating `[1,3]` with power five contributes
from sources one and two to particle two. Its initial charge is two, so
the measured value is `2+5+5=12`. Initial charges are not themselves
radiation sources.

In the second experiment, the first update gives each source in `[2,4]`
power two. Particle three receives only source three, giving `1+2=3`.
Particle four receives sources two and four, giving `4+2+2=8`. The next
update on `[3,5]` adds power one to source five; particle five therefore
becomes `5+1=6`.

## Solution

### Separate directed power from physical charge

Let `v[k]` be the accumulated power directed at source `k`, initially
zero. An update adds `d` to `v[l..r]`. A source reaches particle `i`
exactly when its index divides `i`. Therefore its physical charge is
`a[i]+sum(v[k] : k divides i)`. This follows for one irradiation from
the rule, and addition preserves it after every operation. Different
divisors are different sources, so their contributions must all be
included; overlapping waves do not cancel or merge.

### Range additions with a Fenwick tree

Maintain the difference sequence of `v` in a Fenwick tree. Adding `d` to
the inclusive interval needs a point addition at `l` and a point
subtraction at `r+1` when that index exists. The prefix sum through `k`
is exactly `v[k]`: the two boundary deltas telescope, contributing `d`
precisely inside the interval. The Fenwick point-update and prefix-query
paths partition the required ranges and take `O(log n)` operations each.
A measurement sums these prefix queries over the divisors of its index,
then adds its own unchanged initial charge. Thus every reported value
equals the physical charge invariant.

### Enumerate divisor pairs with compact CSR storage

Every divisor belongs to the pair `(d,i/d)` with its smaller member
satisfying `d²≤i`. Precompute only those smaller members: for each `d`
with `d²≤n`, visit `d²,d²+d,…≤n`. These are exactly the multiples having
`d` as a small divisor. A counting pass builds one count per particle;
prefix sums produce offsets into one flat array; a second pass fills
those slices. For particle `i`, visit its slice, query both members of
each pair, and query only once when they are equal. The pair with
minimum member `d` is unique, so every positive divisor is included
exactly once, including one and `i`. Perfect squares need the explicit
equality check.

The flat small-divisor values fit 16 bits because
`d≤floor(sqrt(300000))=547`. Signed Java shorts also suffice. The number
of entries is at most `n·547=164100000<2³¹`, so offsets fit signed 32
bits; actual allocation uses the counted size. More precisely, the
number of entries is `S=sum(floor(n/d)−d+1,1≤d≤floor(sqrt(n)))`, bounded
by a harmonic sum `O(n log n)`. Both sieve passes and the offsets use
this bound, with no list of boxed integers per particle.

Do not sum initial charges over divisors. Update the directed powers,
not only the measured particles. The right endpoint is inclusive, so the
negative delta belongs at `r+1`; when `r=n` it lies outside the tree and
is omitted. Start indices at one, since a Fenwick update at zero never
advances. Do not double-count a square root, truncate a large answer to
32 bits, omit source one, or print an extra answer for an update.
Repeated measurements and zero-power updates remain valid.

## Language notes

All charges and Fenwick cells are signed 64-bit values. A safe loose
bound on a charge is `1000000+q·n·1000000≤90000000001000000<2⁶³`: at
most `n` sources contribute per update. Difference cells can be negative
even though actual radiation powers are nonnegative. Index arithmetic
and `d²` fit 32 bits under these bounds.

Preprocessing takes `O(n log n)` time and space. With `u` updates and
measurement indices `i₁,…,iₘ`, total time is `O(n log n+u log
n+sum(τ(iⱼ) log n))`, where `τ(i)` counts its divisors. One update costs
`O(log n)` and one measurement `O(τ(i) log n)`; measurements are not
constant-time. All five ports use the same pair slices. C++, Go, Java
and Rust use primitive arrays/vectors and buffered input/output. Python
uses packed 16-bit divisor values, 32-bit offsets and 64-bit
initial/Fenwick arrays, reads one line at a time and flushes output in
batches of 1024 lines. The Python solution runs on PyPy, as CPython is
too slow for the largest tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2062_fenwick.cpp](2062_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n + q tau_max log n) | AC | 0.437 s | 10720 KB |
| [2062_fenwick.go](2062_fenwick.go) | Go 1.14 x64 | fenwick | O(n log n + q tau_max log n) | AC | 0.843 s | 42280 KB |
| [2062_fenwick.java](2062_fenwick.java) | Java 1.8 | fenwick | O(n log n + q tau_max log n) | AC | 0.703 s | 14964 KB |
| [2062_fenwick.py](2062_fenwick.py) | PyPy 3.10 x64 | fenwick | O(n log n + q tau_max log n) | AC | 1.875 s | 38992 KB |
| [2062_fenwick.rs](2062_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n log n + q tau_max log n) | AC | 0.406 s | 27256 KB |
