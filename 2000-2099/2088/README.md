# 2088. Win chance with the best colour chosen after a blind draw

[Timus 2088](https://acm.timus.ru/problem.aspx?space=1&num=2088) · difficulty 5167 · dp, combinatorics

Original problem by Eugene Kurpilyansky.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A deck has cards of colours 0 … k; colour 0 is a joker. Sasha takes some
known cards, then gets t random cards from the rest. Knowing the hand,
Sasha names a colour c ≥ 1 that maximises the chance to win; then y
random cards are opened from the remaining deck, and Sasha wins if the
hand holds at least x more cards of colours 0 and c than the opened
ones. Find the probability of Sasha's win modulo 10⁹ + 7. The limits are
2 seconds and 256 MB.

## Input

k ≤ 100 and t ≤ 100, the counts c₀ … c_k of each colour in the deck (at
most 100 cards), the counts s₀ … s_k Sasha takes, then x and y.

## Output

The probability p/q as p·q⁻¹ modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
3 1
1 2 0 1
0 1 0 0
1 2
```

Output:

```
666666672
```

### Example 2

Input:

```
2 3
6 5 3
2 2 0
5 3
```

Output:

```
176428573
```

## Solution

After the known cards, rᵢ cards of colour i remain, R in total, and
D = R − t stay in the deck after the blind draw. Suppose the hand holds
h cards of colours 0 and c. The deck then holds u = c₀ + c_c − h such
cards, the opened ones follow a hypergeometric law, and Sasha wins when
at most h − x of the y opened cards are of colours 0 and c. So the
number of winning openings, out of C(D, y), is
W(u, h − x) = Σ_{j ≤ h−x} C(u, j) C(D − u, y − j), a table computed once.

The blind draw takes z jokers and dᵢ cards of colour i, with
Σ dᵢ = t − z; it has C(r₀, z) Π C(rᵢ, dᵢ) equally likely variants. For a
fixed z the score of colour i depends only on dᵢ, and the answer needs
the sum over all draws of the maximum score. That sum is collected by
thresholds: all pairs (colour, dᵢ > 0) are sorted by score, and a
polynomial P(X) = Π Fᵢ(X) is kept, where Fᵢ sums C(rᵢ, d) X^d over the
counts d allowed so far (d = 0 is always allowed, which also gives the
baseline score max over colours of the score with dᵢ = 0). Allowing one
more pair (i, d) turns Fᵢ into Fᵢ + C(rᵢ, d) X^d, so P grows by
C(rᵢ, d) X^d · P / Fᵢ; the division is exact because Fᵢ starts with 1.
The growth of the coefficient of X^{t−z} counts the draws whose best
score just became this one, and each is added with that score. The
counts are reduced modulo 10⁹ + 7, and the result is divided by
C(R, t) C(D, y). Precomputation takes O(N²) operations, where N = 100
is the card limit. There are O(t + 1) joker counts and O(k t) events per
count; each formal division computes O(t) coefficients using up to O(t)
earlier terms per coefficient. A worst-case time bound is
O(N² + k (t + 1)^4).

Pitfall (generator test gen8, arguments `5 8`): the polynomial division
is quadratic, so counting it as linear misses a factor of t. For even
t ≤ 50, the valid family k = 1, c = (t, t), s = (0, 0), x = y = 0
executes t²(t² − 4)/48 inner division iterations, despite every answer
being 1. Thus the threshold DP can take Θ(t^4) time even with one colour.

In the first example every hand makes colour 1 the best choice, and two
of the three equally likely hands win, so the answer is 2/3.

## Language notes

Scores are compared exactly; they reach C(100, 50) ≈ 10²⁹. C++ and Rust
keep them in unsigned 128-bit integers, Go and Java in big integers, and
Python in its own integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2088_dp_combinatorics.cpp](2088_dp_combinatorics.cpp) | G++ 13.2 x64 | dp, combinatorics | O(N^2 + k (t+1)^4) | AC | 0.015 s | 672 KB |
| [2088_dp_combinatorics.go](2088_dp_combinatorics.go) | Go 1.14 x64 | dp, combinatorics | O(N^2 + k (t+1)^4) | AC | 0.031 s | 2368 KB |
| [2088_dp_combinatorics.java](2088_dp_combinatorics.java) | Java 1.8 | dp, combinatorics | O(N^2 + k (t+1)^4) | AC | 0.125 s | 2536 KB |
| [2088_dp_combinatorics.py](2088_dp_combinatorics.py) | Python 3.12 x64 | dp, combinatorics | O(N^2 + k (t+1)^4) | AC | 0.093 s | 1268 KB |
| [2088_dp_combinatorics.rs](2088_dp_combinatorics.rs) | Rust 1.75 x64 | dp, combinatorics | O(N^2 + k (t+1)^4) | AC | 0.046 s | 476 KB |
