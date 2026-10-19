# 2047. A sequence constrained by prefix divisor counts

[Timus 2047](https://acm.timus.ru/problem.aspx?space=1&num=2047) · difficulty 483 · number_theory

Folklore problem, prepared by Alexander Ipatov, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Construct n integers a₁, …, aₙ with 1 ≤ aᵢ ≤ 300 such that for every k
from 2 to n the prefix sum a₁ + … + aₖ has exactly aₖ distinct positive
divisors. The first term has no condition of its own. The limits are 1
second and 64 MB.

## Input

One integer n, 2 ≤ n ≤ 100 000.

## Output

Print a valid sequence as space-separated integers, or `Impossible` if
there is none.

## Checking

A checker verifies the length and the bounds and counts the divisors of
every prefix sum from the second one on; any valid sequence is accepted,
and `Impossible` only when no sequence exists.

## Examples

```
3
```

```
1 3 4
```

The first constrained prefix is `1+3=4`, with divisors `1,2,4`, so its
last term is three. The next sum is `8`, with divisors `1,2,4,8`, so the
last term is four. Another valid answer is `2 4 6`: the constrained sums
are `6` and `12`, with four and six divisors.

## Solution

Let `τ(s)` be the number of positive divisors of `s`. If a sequence of
at least two terms ends at sum `s`, its last term is forced to be
`d=τ(s)`, so the preceding sum is uniquely `s-d`. Search these
predecessor edges in increasing sum order.

Define `depth[s]` as the maximum length of a valid sequence ending at
`s`. A one-term sequence is allowed exactly when `1≤s≤300`, giving a
base value of one; otherwise start at zero, meaning unreachable. If
`d≤300`, `s>d` and `depth[s-d]>0`, also consider `depth[s-d]+1`. Take
the larger value.

The search cap is the proven bound `M=300n`, since every requested
sequence has total sum at most that. Stop at the first sum whose depth
reaches `n`. Trace `n-1` predecessor edges, recording their forced last
terms, then use the remaining sum as the first term and reverse the
collected values. If all sums through `M` are exhausted without reaching
`n`, print `Impossible`.

### Computing divisor counts with limited working memory

Generate primes through `floor(sqrt(M))` once. Process sums in blocks of
`K=65536` values. For each block, initialize a remaining value to the
integer itself and its count to one. For every prime `p` with
`p²≤right`, visit its multiples in the block, divide out all `e` copies
of `p` and multiply the count by `e+1`. A remaining factor greater than
one is prime and contributes a final factor of two. This is the
prime-factor formula `τ(s)=product(e+1)`.

Append computed counts to compact history for reconstruction. Only the
previous 300 sums can be predecessors of valid edges, so keep depths in
a ring of 301 entries. Read the predecessor before overwriting the
current ring entry. Invalid edges with a divisor count above 300 are
skipped, even though their counts remain representable.

### Correctness

Prime division removes every factor at most the square root of the
block's upper endpoint. Any composite remainder would have such a prime
factor, a contradiction; therefore the final remainder is one or a
single prime. Multiplying exponent counts gives every divisor count
exactly, including `τ(1)=1`.

By induction on the sum, the depth recurrence is exact. Every valid
sequence either has one allowed first term, or its final term is `τ(s)`
and its preceding sequence ends at the uniquely determined smaller sum.
Conversely, extending any reachable predecessor by that term satisfies
the new prefix condition and preserves earlier ones. Taking the maximum
therefore finds the longest possible sequence. The ring retains
precisely the needed predecessor because its distance is between one and
300.

Before the first successful sum, every depth is less than `n`, so its
successful depth is exactly `n`, not larger. Backtracking follows the
very recurrence edges and reduces the depth by one each time. It ends at
a depth-one base sum at most 300, proving all term bounds and all
required prefix conditions. If no success occurs through `300n`, a valid
requested sequence would contradict the exact depth at its endpoint.
Thus both a printed sequence and `Impossible` are justified without
assuming a guessed search cutoff.

### Complexity and search span

The conservative worst-case bound is `O(M log M+n)` time and
`O(M+K+sqrt(M)+n)` space, with early termination. If `B` sums are
scanned, history uses `O(B)` space and at most one additional block is
factored. Prime-loop overhead is bounded here because `sqrt(M)≤5477<K`.
Every divisor count fits 16 bits: `τ(s)≤2sqrt(s)≤2sqrt(30000000)<11000`;
even Java's signed short suffices.

An independent ordinary-sieve search found and trial-factor-verified a
valid 100000-term chain ending at sum `1568617`. Its prefixes certify
existence for every legal length. Consequently every first successful
endpoint is at most this sum; the programs still use the complete cap
`300n`, without embedding that witness or endpoint as a cutoff.

## Language notes

Do not impose the prefix condition at `k=1`. A divisor count is a count
of different positive divisors, not prime factors. Preserve zero for an
unreachable predecessor. The 301-entry ring keeps the current slot
distinct from all 300 possible predecessor slots; read the predecessor
before replacing the current depth. Save divisor history for
reconstruction, not just the depth ring. Start factorization at positive
one, never zero.

All ports use segmented factorization and the same proven search. Java
grows a primitive short history; C++, Go and Rust also use 16-bit
history. Python uses `array("H")` for history and small lists for the
current block and ring.

The Python solution runs under PyPy: under CPython 3.12 it exceeds the
time limit on the judge's test 13, while PyPy 3.10 is accepted in
0.437 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2047_number_theory.cpp](2047_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(M log M+n) | AC | 0.078 s | 4972 KB |
| [2047_number_theory.go](2047_number_theory.go) | Go 1.14 x64 | number_theory | O(M log M+n) | AC | 0.140 s | 15940 KB |
| [2047_number_theory.java](2047_number_theory.java) | Java 1.8 | number_theory | O(M log M+n) | AC | 0.171 s | 13508 KB |
| [2047_number_theory.py](2047_number_theory.py) | PyPy 3.10 x64 | number_theory | O(M log M+n) | AC | 0.437 s | 11296 KB |
| [2047_number_theory.rs](2047_number_theory.rs) | Rust 1.75 x64 | number_theory | O(M log M+n) | AC | 0.093 s | 5644 KB |
