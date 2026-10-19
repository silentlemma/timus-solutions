# 2052. Count fixed positions after digit-sum sorting

[Timus 2052](https://acm.timus.ru/problem.aspx?space=1&num=2052) · difficulty 1485 · dp, binary_search

Original problem by Alexander Ipatov, prepared by Bulat Zaynullin, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The numbers 1, …, n are sorted by their decimal digit sum, ties by
value. Count the numbers that keep their position. The limits are 1
second and 64 MB.

## Input

One integer n, 2 ≤ n ≤ 10⁹.

## Output

The number of positions that stay the same.

## Checking

Outputs are compared token by token.

## Examples

```
19
```

```
3
```

For nineteen the new order is
`1,10,2,11,3,12,4,13,5,14,6,15,7,16,8,17,9,18,19`. Exactly `1,18,19`
retain their positions, giving three. Their digit sums are one, nine and
ten.

## Solution

### Express the sorted position

Let `C(b,s)` count positive integers no larger than `b` with digit sum
`s`. For a fixed sum `s`, let `L_s=sum_{t<s} C(n,t)`. Its group occupies
sorted positions `[L_s+1,L_s+C(n,s)]`. If `x` has digit sum `s`, its
sorted position is `rank(x)=L_s+C(x,s)`, because smaller digit sums
precede it and numeric tie-breaking counts precisely the members of its
own group up to and including `x`. It is fixed exactly when
`x-C(x,s)=L_s`.

### At most one fixed integer per digit sum

Write the members of one group in numeric order as `x_1<x_2<…`. Their
sorted positions are `L_s+j`. Consecutive integers never have the same
decimal digit sum: adding one changes that sum by `1-9k`, where `k` is
the number of trailing nines, and this cannot be zero. Hence
`x_{j+1}≥x_j+2`, so `x_j-j` increases strictly. It can equal `L_s` at
most once. We therefore only need to find one candidate for each digit
sum.

Define `F_s(b)=b-C(b,s)`. On incrementing `b`, the count increases by
either zero or one; therefore `F_s` is nondecreasing. Search within the
group's sorted-position interval for the **last** integer satisfying
`F_s(b)≤L_s`. Ignore empty groups. Check the resulting candidate is
inside that interval, has digit sum `s` and satisfies the equality
exactly; if so add one.

This search is complete. Any fixed integer lies in its own group's
position interval and satisfies the predicate. Immediately after such an
integer, the next number has a different digit sum, so `F_s` increases
to `L_s+1`, unless the search interval has already ended. Monotonicity
prevents any later satisfying integer. Thus the search returns that
fixed integer whenever one exists. The final checks prove every counted
candidate really has its original position.

### Exact digit counts in linear digit time

Let `D` be the number of digits of `n` and `S=9D`. Precompute `W_l(q)`,
the number of length-`l` decimal strings with sum `q`, allowing leading
zeros: `W_0(0)=1`, and `W_l(q)=sum_{a=0..9} W_{l-1}(q-a)`. A sliding
window computes each row. Store cumulative sums `P_l(q)=sum_{r≤q}
W_l(r)`; negative indices mean zero and indices above the possible sum
mean `10^l`. Only lengths through `D-1` are needed.

To count up to `b`, scan its digits from left to right, keeping the
remaining required sum `q`. At a current digit `d` with `l` positions
remaining, smaller choices `a=0,…,d-1` leave sums `q-a` for the suffix.
Their total is `P_l(q)-P_l(q-d)`. Add it, subtract `d` from `q` and
continue along the equal prefix. If `q` becomes negative, stop; at the
end include `b` itself exactly when `q=0`. Each shorter number is
represented uniquely with leading zeros. We only ask positive sums
`s≥1`, so zero is automatically excluded from ranks. This computes
`C(b,s)` in `O(D)` time without enumerating integers.

Loop over `s=1,…,S`, compute its group size, perform the monotone search
and accumulate `L_s`. Use exact integer arithmetic for counts and ranks;
the suffix tables cover at most nine free digits here, and 64-bit
counters are ample.

Positions are one-based and the member `x` is included in `C(x,s)`. Zero
participates in suffix strings but not in positive-integer groups.
Handle empty digit-sum groups and decimal carries. The searched
predicate is monotone only after fixing a digit sum; the entire
digit-sum permutation is not a globally monotone numeric order. Search
the last satisfying integer and verify its digit sum; a neighbouring
nongroup integer can satisfy the same inequality. The uniqueness proof
is what permits adding at most one per group.

## Language notes

Precomputation takes `O(D·S)` time and space. There are at most `S`
searches of `O(log n)` steps, each using an `O(D)` count, for total
`O(D·S·(1+log n))` time and `O(D·S)` auxiliary space. Here `D≤10,S≤90`.
The full permutation is never constructed.

All five implementations use the same suffix-prefix counts and
group-bound searches. C++/Go/Java/Rust use 64-bit counters; Python uses
exact integers. Decimal strings are used only for the at most ten digits
of a query, not for a loop over all numbers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2052_dp.cpp](2052_dp.cpp) | G++ 13.2 x64 | dp | O(D*S*(1+log n)) | AC | 0.015 s | 436 KB |
| [2052_dp.go](2052_dp.go) | Go 1.14 x64 | dp | O(D*S*(1+log n)) | AC | 0.031 s | 1136 KB |
| [2052_dp.java](2052_dp.java) | Java 1.8 | dp | O(D*S*(1+log n)) | AC | 0.109 s | 552 KB |
| [2052_dp.py](2052_dp.py) | Python 3.12 x64 | dp | O(D*S*(1+log n)) | AC | 0.109 s | 688 KB |
| [2052_dp.rs](2052_dp.rs) | Rust 1.75 x64 | dp | O(D*S*(1+log n)) | AC | 0.031 s | 252 KB |
