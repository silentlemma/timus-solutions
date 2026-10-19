# 1936. Expected Rounds in a Three-Gesture Elimination Game

[Timus 1936](https://acm.timus.ru/problem.aspx?space=1&num=1936) · difficulty 1123 · probability, dp

Original problem from Open Ural FU Championship 2012 | by Denis Dublennykh (prepared by Oleg Dolgorukov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n players repeatedly choose one of three gestures, independently and
uniformly in every round. The gestures form a directed cycle: each beats
one other gesture. If exactly two gestures appear, only players showing
the winning one remain. With one or all three gestures present, everyone
remains. Stop at one player; the winner receives a reward equal to the
total rounds played, including rounds without elimination. Find the
expected reward conditional on a specified player winning.
Limits: 1 second, 64 MB.

## Input

One integer n, 2≤n≤100, the initial number of players.

## Output

One real number: the expected winner's reward. Absolute or relative
error at most 10⁻⁶ is accepted.

## Checking

The answer is compared with absolute or relative error 10⁻⁶.

## Examples

```
2
```

```
1.5
```

## Solution

The conditioning does not divide the answer by n. For any duration r,
permuting player labels preserves probabilities and maps any winner to
any other. Hence P(T=r,winner=i)=P(T=r)/n and P(winner=i)=1/n.
The duration distribution conditioned on that winner is unchanged.
We may compute the unconditional expected total number of rounds.

Let E_m denote that expectation with m players; E_1=0. There are 3^m
equally likely gesture assignments. For exactly k survivors, 1≤k<m,
choose the survivor subset in C(m,k) ways and the winning gesture in
three ways. The losing gesture is then forced, giving 3C(m,k)
assignments. Thus there are 3(2^m−2) assignments that eliminate someone;
all other assignments leave the same state. That positive probability
also guarantees finite expected waiting time before a smaller state.

Every round contributes one. Moving the unchanged-state term to the
left and cancelling the common factor 3 gives the stable recurrence

E_m = (3^(m−1) + Σ_{k=1}^{m−1} C(m,k)·E_k) / (2^m−2).

Compute E_2,...,E_n in increasing order. Each needed smaller expectation
is already known, so the first-step expectation equation uniquely
determines the next value and proves the DP correct. Generate binomial
coefficients within a row from B_0=1 and B_k=B_{k−1}(m−k+1)/k.
Maintain powers of 2 and 3 by multiplication, without integer overflow.

Do not evaluate the denominator as 1−P(no elimination) in floating point.
For n=96..100, that probability rounds to 1 in double precision.
The displayed recurrence divides by 2^m−2 directly and adds only positive
terms. Binomial coefficients, powers and the answer remain finite in
double precision, even though some coefficients exceed 64-bit integers.
The largest expectation is about 1.355203941481465·10¹⁷. Twelve decimal
places give ample accuracy under the allowed absolute-or-relative rule.

O(n²) time and O(n) space. One binomial row is generated on the fly;
there is no full coefficient matrix or simulation of individual rounds.

Unsuccessful rounds still count. Do not estimate the rare decisive event
by subtracting two rounded probabilities, store binomial coefficients in
ordinary integer types, or divide the expectation by the player's
winning probability. The cyclic orientation of the three gestures does
not change the three possible winning/losing pairs.

## Language notes

All five versions use double/float64/f64 for expectations, powers and
binomial coefficients. Indices alone are integers. C++ uses fixed stream
precision; Go uses formatted output, Java specifies Locale.US, Python
uses an f-string, and Rust uses formatting precision. Each prints one
number with 12 fractional digits and a final newline.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1936_probability_dp.cpp](1936_probability_dp.cpp) | G++ 13.2 x64 | probability, dp | O(n^2) | AC | 0.015 s | 444 KB |
| [1936_probability_dp.go](1936_probability_dp.go) | Go 1.14 x64 | probability, dp | O(n^2) | AC | 0.031 s | 1128 KB |
| [1936_probability_dp.java](1936_probability_dp.java) | Java 1.8 | probability, dp | O(n^2) | AC | 0.125 s | 1064 KB |
| [1936_probability_dp.py](1936_probability_dp.py) | Python 3.12 x64 | probability, dp | O(n^2) | AC | 0.093 s | 480 KB |
| [1936_probability_dp.rs](1936_probability_dp.rs) | Rust 1.75 x64 | probability, dp | O(n^2) | AC | 0.031 s | 260 KB |
