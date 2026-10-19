# 2018. Counting Sequences with Bounded Runs

[Timus 2018](https://acm.timus.ru/problem.aspx?space=1&num=2018) · difficulty 102 · dp, prefix_sums

Original problem by Olga Soboleva, prepared by Alex Samsonov, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count length-`n` sequences over symbols 1 and 2. A consecutive run of ones
may have length at most `a`; a run of twos may have length at most `b`.
Two sequences are different if some position differs. Return the count
modulo `1,000,000,007`.

The limits are `1 ≤ a,b ≤ 300` and `max(a,b)+1 ≤ n ≤ 50,000`.
Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The only line contains `n a b`.

## Output

Print the number of valid sequences modulo `1,000,000,007`.

## Checking

Outputs are compared token by token.

## Examples

```
3 2 1
```

```
4
```

## Solution

Let `A_i` count valid prefixes of length `i` ending in 1, and `B_i` those
ending in 2. Set artificial boundary values `A_0 = B_0 = 1`: each denotes
the empty prefix before the first run of the opposite symbol.
For positive `i`, split a sequence before its final maximal run:

- `A_i = sum(B_(i−r), 1 ≤ r ≤ min(a,i))`.
- `B_i = sum(A_(i−r), 1 ≤ r ≤ min(b,i))`.

The prefix either is empty or ends with the other symbol. Conversely,
appending the chosen run creates a valid sequence with a unique final run.
Thus these sums count every sequence exactly once. The answer is
`(A_n + B_n) mod 1,000,000,007`, since the final symbols are disjoint.

Do not sum up to 300 terms afresh for every length. Before processing `i`,
maintain `S_A = sum(B_j, max(0,i−a) ≤ j < i)` and
`S_B = sum(A_j, max(0,i−b) ≤ j < i)`, initially both one.
Their current values are exactly `A_i` and `B_i`. Save both values before
updating either sum. For the next length, add `B_i` to `S_A` and remove
`B_(i−a)` when `i ≥ a`; add `A_i` to `S_B` and remove `A_(i−b)` when `i ≥ b`.
Reduce all updates modulo the modulus, normalizing subtraction to a
nonnegative residue. These updates preserve the stated window invariant,
which proves by induction that the computed counts satisfy the recurrence.

Only recently produced values can expire. Store the `B` values in a circular
buffer of size `a+1`, and the `A` values in one of size `b+1`. Read expired
entries before writing the new ones. A value being overwritten is already
outside its window; the extra slot also separates the current value from
the one expiring now. In particular, the `A` buffer is sized by **b**, not a.
The algorithm uses `O(n)` time and `O(a+b)` space, at most 602 buffered counts.

For the sample, the permitted sequences are `112`, `121`, `211`, `212`.
The pair `22` is forbidden by `b=1`; `111` exceeds `a=2`, so the answer is four.

Pitfalls:

- Include the artificial empty prefix exactly once in each recurrence,
  then expire it normally.
- Compute both current counts from the old windows before updating the windows.
- Expire at `i ≥ a` or `i ≥ b`, including equality, and use the opposite
  ending type.
- Use wide intermediate arithmetic: an update with an added modulus can
  approach three moduli.
- Normalize negative subtraction and do not count the two empty boundary
  states as real answers.

## Language notes

All versions use the same two circular buffers and modular windows. C++,
Go and Java use signed 64-bit counts; Rust uses `u64`, and Python uses
integers with a nonnegative modulo operation. No recursion or large DP
table is needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2018_dp_prefix_sums.cpp](2018_dp_prefix_sums.cpp) | G++ 13.2 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 388 KB |
| [2018_dp_prefix_sums.go](2018_dp_prefix_sums.go) | Go 1.14 x64 | dp, prefix_sums | O(n) | AC | 0.031 s | 1088 KB |
| [2018_dp_prefix_sums.java](2018_dp_prefix_sums.java) | Java 1.8 | dp, prefix_sums | O(n) | AC | 0.125 s | 404 KB |
| [2018_dp_prefix_sums.py](2018_dp_prefix_sums.py) | Python 3.12 x64 | dp, prefix_sums | O(n) | AC | 0.125 s | 452 KB |
| [2018_dp_prefix_sums.rs](2018_dp_prefix_sums.rs) | Rust 1.75 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 216 KB |
