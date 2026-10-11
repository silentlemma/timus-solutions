# 1275. Knights of the Round Table

[Timus 1275](https://acm.timus.ru/problem.aspx?space=1&num=1275) · difficulty 2249 · math

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N knights (2 ≤ N ≤ 1000) sit at a round table, each with some goblets.
On each visit a servant either brings one goblet to each of two knights
sitting K places apart, or takes one away from each. Every knight must
end with F goblets, and the servant may not take a goblet that is not
there. Find a plan with the fewest visits, or print −1 if none exists.
Initial counts and F are between 0 and 1000, and an optimal plan has
at most 30 000 visits.

Time limit: 0.1 seconds. Memory limit: 0.5 MB. The statement allows C, C++
and Pascal; the submit form also offers Rust.

## Input

N, K and F, then the N goblet counts.

## Output

The number of visits M and the visits as `i j +` or `i j -`, or −1.

## Checking

Many plans may be optimal, so the checker accepts any: the number of
visits must equal the least possible, every visit must serve two knights
K places apart, all goblet counts must stay nonnegative, and every knight
must end with F.

## Examples

### Example 1

Input:

```
3 1 4
1 2 3
```

Output:

```
3
1 2 +
1 2 +
3 1 +
```

## Solution

Let x_i be the signed number of visits to the pair (i, i + K): positive
for bringing, negative for taking away. Mixing both on one pair only
wastes visits. Knight i belongs to the pairs (i, i + K) and (i − K, i),
so x_(i−K) + x_i must equal F minus the knight's goblets.

The knights split into gcd(N, K) cycles i, i + K, i + 2K, …, each of
length L = N / gcd(N, K), and every cycle is solved on its own. Setting
the first unknown to t, each rule fixes the next one, giving
x_j = ±t + c_j with alternating signs. The last rule closes the cycle:

- if L is odd, it reads 2t = r: there is exactly one solution, and none
  when r is odd;
- if L is even, t cancels out: there is no solution unless r = 0, and
  then any t works. The number of visits Σ |t − p_j| over the points
  p_j = ∓c_j is least when t is a median of them.

All visits that bring goblets are printed first and those that take
them away afterwards. A knight then only gains goblets at first and
loses them later, so counts stay nonnegative and end at F ≥ 0.

Pitfalls:

- on an even cycle, leaving the first pair without visits can be
  suboptimal; the median picks the best count (test gen3);
- printing a `-` before the `+` it relies on can take a goblet that is
  not there yet;
- with N = 2K the pairs (i, i + K) and (i + K, i) are the same, and the
  two knights must need the same change (test 07);
- the memory limit forbids anything heavy: C++ streams alone take too
  much, so the program uses `scanf` and `printf`.

The least number of visits was compared with an exhaustive search over
all plans on 400 random tables of up to five knights.

## Language notes

- The statement allows only C, C++ and Pascal, but the Timus submit form
  also offers Rust 1.75, so there are C++ and Rust solutions; Go, Python
  and Java cannot be submitted.
- C++ stores goblet changes and signed visit counts as `int`, with
  `long long` for t and the total; Rust uses `i64` for those changes,
  counts and t, and `u64` for the total. Rust also implements input and
  output with fixed 4096-byte buffers instead of `scanf` and `printf`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1275_math.cpp](1275_math.cpp) | G++ 13.2 x64 | math | O(N + M) (on average) | AC | 0.015 s | 152 KB |
| [1275_math.rs](1275_math.rs) | Rust 1.75 x64 | math | O(N + M) | AC | 0.031 s | 244 KB |
