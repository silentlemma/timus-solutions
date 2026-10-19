# 1994. Optimal random removals between deterministic losses

[Timus 1994](https://acm.timus.ru/problem.aspx?space=1&num=1994) · difficulty 1050 · dp, probability, combinatorics

Original problem by Denis Dublennykh, prepared by Eugene Kurpilyansky.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A population has `n` active members, of whom `k` are hostile and the
rest are ordinary. Every night each hostile member can eliminate one
ordinary member; assignments maximize the number eliminated, hence the
loss is the smaller of the two populations. On each following day,
choose a positive number of members to exclude. Their identities are
selected uniformly at random; excluded members neither act nor count in
the final result. Choose the daily numbers optimally to maximize the
expected ordinary population still active when losses stop or no
ordinary members remain.

The initial moment is evening, so the first night occurs before the
first exclusion. Identities cannot be targeted. Bounds: `1≤k≤min(n,20)`,
`n≤200`. Time limit: 1 second; memory limit: 64 MB.

## Input

Two integers `n k`.

## Output

One real number: the optimal expected final ordinary population, not a
survival probability.

## Checking

Numbers are compared with absolute or relative error 10⁻⁶.

## Examples

Input:

```
4 1
```

Output:

```
0.6666666667
```

The first night changes `(4,1)` to a day with three members and one
hostile member. Excluding one saves two ordinary members with
probability `1/3`; otherwise the next night removes the last ordinary
member. The expectation is `2/3`.

## Solution

### Day-state dynamic programming

Let `V(N,K)` be the optimum at the start of a day, before exclusion. Set
`V(N,0)=N` and `V(N,N)=0`. This is a count state, even though identities
are hidden: whenever ordinary members survive a night, its death count
equals the remaining hostile count. If all ordinary members die, the
payoff is already zero, so no further inference is needed.

Try retaining `t<N` members. The retained set is uniform, so the chance
that it contains `j` hostile members is hypergeometric. If `j=0`, the
payoff is `t`. If `t≤2j`, the next night eliminates all ordinary
members. Otherwise the next day contains `t−j` total members and `j`
hostile members. The unified recurrence is:

`P(j)=C(K,j)·C(N−K,t−j)/C(N,t)`

`V(N,K)=max[1≤t<N] Σ[max(0,t−(N−K))≤j≤min(K,⌊(t−1)/2⌋)] P(j)·V(t−j,j)`

The `j=0` term uses `V(t,0)=t`; omitted terms have zero payoff.
Retaining nobody also gives zero and can be omitted. Build increasing
`N`, since `t−j<N`. Pascal's triangle supplies the binomial
coefficients. In the implementation, sum the weighted counts first and
divide by the common `C(N,t)` once per action.

The requested answer is zero if `n≤2k`; otherwise it is `V(n−k,k)`,
after the compulsory first night. Do not set an internal day state to
zero just because hostile members are a majority: `V(2,1)=1/2`, since
randomly excluding one can remove the hostile member. Also, removing
only one each day need not be optimal. At day state `(5,2)`, retaining
three gives `0.6`, whereas retaining four gives only `4/15`.

Uniform retention gives the displayed probability. Each possible
retained composition has the stated next-night outcome. Smaller states
already contain the optimal future expectation, so conditioning on the
retained composition gives the expectation of each allowed action.
Maximizing over every positive exclusion count therefore selects an
optimal action. Induction on population size proves the table; applying
the initial night gives the required initial expectation. Randomizing
the chosen count cannot improve on the maximum of its action values.

For `M=n−k`, build the table up to `M` and at most `k` hostile members.
Time `O(M²k²)`; memory `O(M²+Mk)`. Immediate-zero inputs skip the table.
The largest input requires only a few million weighted terms.

Binomial coefficients through 200 are below `10⁶⁰`; numerator sums are
below `10⁶²`, so double does not overflow. All arithmetic sums
nonnegative terms. Under standard round-to-nearest double arithmetic,
Pascal coefficients have relative error below `γ₂₀₀<2.3·10⁻¹⁴`.
Combining two coefficients, at most 21 terms and one division gives a
conservative action-evaluation relative bound below `10⁻¹³`, apart from
existing table error. An expectation has nonnegative weights summing at
most one, and maximum is 1-Lipschitz. Across fewer than 200
decreasing-population steps this bounds absolute error by
`200((1+10⁻¹³)²⁰⁰−1)<5·10⁻⁹`. Positive terms cannot underflow at these
bounds. Twelve decimal places add at most `5·10⁻¹³` rounding error.

## Language notes

All five versions use the same increasing-population DP and double
arithmetic. Java uses a fixed output locale; Go is compatible with 1.14.
Python keeps the action denominator outside the inner hostile-count
loop. Distinguish day states from the initial night, allow batch
exclusions, and start `j` at `max(0,t−(N−K))` when retaining more people
than the ordinary population.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1994_dp_probability.cpp](1994_dp_probability.cpp) | G++ 13.2 x64 | dp, probability | O((n-k)^2 k^2) | AC | 0.015 s | 616 KB |
| [1994_dp_probability.go](1994_dp_probability.go) | Go 1.14 x64 | dp, probability | O((n-k)^2 k^2) | AC | 0.015 s | 1340 KB |
| [1994_dp_probability.java](1994_dp_probability.java) | Java 1.8 | dp, probability | O((n-k)^2 k^2) | AC | 0.125 s | 1968 KB |
| [1994_dp_probability.py](1994_dp_probability.py) | Python 3.12 x64 | dp, probability | O((n-k)^2 k^2) | AC | 0.718 s | 1124 KB |
| [1994_dp_probability.rs](1994_dp_probability.rs) | Rust 1.75 x64 | dp, probability | O((n-k)^2 k^2) | AC | 0.046 s | 428 KB |
