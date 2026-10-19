# 2011. At Least Six Distinct Arrangements

[Timus 2011](https://acm.timus.ru/problem.aspx?space=1&num=2011) · difficulty 103 · combinatorics

Original problem by Alexey Kungurtsev, from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

You have `n` symbols, each of one of three types. Rearrange all of them
into a word of length `n`; equal symbols are indistinguishable. Decide
whether at least six different words are possible. Every available
symbol must be used exactly once.

## Input

The first line contains `n`, `1 ≤ n ≤ 100`. The second contains `n`
integers from 1 to 3 specifying symbol types. Time limit 0.5 seconds,
memory 64 MB.

## Output

Print `Yes` if there are at least six different words, or `No`
otherwise. Capitalization matters. The unique answer is compared token
by token.

## Checking

Outputs are compared token by token.

## Examples

```
6
1 2 2 3 3 3
```

```
Yes
```

The multiplicities are 1, 2 and 3. There are `6!/(1!·2!·3!)=60`
different words, so the answer is `Yes`.

## Solution

For a prefix of length `i` with multiplicities `c1,c2,c3`, the exact
number of distinct words is `i!/(c1!·c2!·c3!)`: permutations of equal
symbols do not change the word. Computing the full factorials in
fixed-width integers would overflow. We only need to reach six.

Start with counts zero and `ways=1` for the empty prefix. Read the
symbols in their given order. When adding a symbol of type `v`, increase
its count to `c`, increase the prefix length to `i`, and update `ways =
ways·i/c`. Multiply before dividing. The quotient is exact: the new
numerator gains factor `i`, while just that symbol's factorial in the
denominator gains factor `c`.

As soon as `ways≥6`, return `Yes`. This is safe even with unread
symbols: append a fixed remaining sequence to every distinct prefix
word. The resulting full words are still distinct and use exactly all
symbols, so their number cannot decrease. If no prefix reaches six, the
final exact count is below six and the answer is `No`.

Inductively the stored count is exact at every step before return, since
the update is the ratio of consecutive multinomial coefficients. The
append argument proves that an early positive answer stays positive. If
there is no early return, the last exact count decides the condition.
Together these establish correctness.

Before every update `ways≤5` and `i≤100`, so the multiplication is at
most 500. Ordinary integer types suffice; there is no rounding, modulo,
saturation error or factorial overflow. Use an array of three counts
indexed by `v−1`. For example, five copies of one type and one of
another give six words, whereas four plus one give only five. All equal
symbols always give one word regardless of `n`.

Time is `O(n)`; the counting state uses `O(1)` extra space. These
complete programs retain the input symbols, using `O(n)` total space. An
alternative is to multiply binomial coefficients for the three
multiplicities and stop once the same threshold is reached.

## Language notes

Count distinct words rather than permutations of labeled pieces. The
condition includes exactly six. Do not divide `ways` by `c` before
multiplying by `i`: that intermediate division need not be exact. Do not
cap the count and then continue applying an exact-count recurrence;
return as soon as the threshold is reached. All five ports use integer
division after multiplication. Python uses CPython; no large-integer
work is needed in the solver. Go 1.14, Java 8 and Rust 1.75 need only
fixed arrays and ordinary integer arithmetic.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2011_combinatorics.cpp](2011_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.031 s | 380 KB |
| [2011_combinatorics.go](2011_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 1112 KB |
| [2011_combinatorics.java](2011_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.109 s | 408 KB |
| [2011_combinatorics.py](2011_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.109 s | 516 KB |
| [2011_combinatorics.rs](2011_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 232 KB |
