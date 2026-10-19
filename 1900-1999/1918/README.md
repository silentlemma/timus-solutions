# 1918. Maps That Escape Every Proper Prefix

[Timus 1918](https://acm.timus.ru/problem.aspx?space=1&num=1918) · difficulty 936 · dp

Original problem by Denis Dublennykh, from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose a function f from {1,…,n} to itself: each of the n controls independently
selects one of n values. Start in state 1. An activation moves state i to f(i);
waiting allows a decrease from i to i−1 when i>1. Activations can be applied
at any intermediate state. Count the functions for which state n can be reached.
Limits: 2 seconds, 64 MB.

## Input

One integer n, 2≤n≤5000.

## Output

The number of suitable functions modulo M=1 000 000 007.

## Checking

Compare one integer token exactly.

## Examples

```
2
```

```
2
```

## Solution

Reachable states form a prefix: whenever a state is reachable, waiting
also reaches every smaller positive state. Let a[k] count suitable maps
on {1,…,k}, with the auxiliary base a[1]=1.

Partition all nⁿ maps by their final reachable prefix {1,…,k}. For this
prefix to be final, its first k mapping values must stay within it, and
the restricted map must reach k. There are a[k] such restrictions. The
other n−k mapping values are arbitrary choices from all n states, giving
n^(n−k) extensions. Conversely every such choice has exactly that reachable
prefix. No binomial coefficient appears: the state set is the fixed prefix,
not an arbitrary subset. Hence

nⁿ = Σ(k=1..n) a[k]·n^(n−k).

Isolating a[n] yields a triangular DP. Factor out n and define
H=Σ(k=1..n−1) a[k]·n^(n−1−k). Then

a[n] = n·(n^(n−1)−H) mod M.

Compute H by Horner evaluation in increasing k: start at zero and replace
H by (H·n+a[k]) mod M. Modular binary exponentiation computes n^(n−1).
Normalize the subtraction before multiplying in fixed-width languages.
This identity and the exhaustive partition prove the DP correct by induction.

### Python loop cost

Python processes two coefficients at once:
H←(H·n²+a[k]·n+a[k+1]) mod M. This is exactly two Horner steps with one
remainder operation. If the coefficient count n−1 is odd, process its final
coefficient separately. The shared iterator used by `zip` may consume the
unpaired last value without processing it, so the tail is read by index.
The native ports use ordinary one-coefficient Horner steps.

Time is `O(n²)` modular operations, including the smaller `O(n log n)`
power work; memory is `O(n)`. Ordinary Horner products are below about
5·10¹², and binary-power products below M², both safe in 64 bits. Python's
paired intermediate is below about 2.501·10¹⁶ and is exact as well.

For n=2, f(1) must be 2; f(2) can be either value. Therefore the example
has two suitable control settings. The auxiliary n=1 case is only a DP base.

Use n choices, not n−k choices, for controls outside the reachable prefix.
Count each final prefix once, include a[1], handle negative modular
subtraction, and process the odd Horner tail. Do not confuse a reachable
prefix with an arbitrary connected subset, or use floating powers.

## Language notes

C++/Go/Java/Rust use 64-bit modular arithmetic. Python uses exact integers
and paired evaluation, with temporary coefficient slices still taking `O(n)`
memory. CPython3.12 is selected: measured PyPy memory exceeds this problem's
64 MB limit. Every source computes the prefix table and prints only its
n-th entry; no complete state graph or function list is built.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1918_dp.cpp](1918_dp.cpp) | G++ 13.2 x64 | dp | O(n^2) | AC | 0.031 s | 416 KB |
| [1918_dp.go](1918_dp.go) | Go 1.14 x64 | dp | O(n^2) | AC | 0.062 s | 1128 KB |
| [1918_dp.java](1918_dp.java) | Java 1.8 | dp | O(n^2) | AC | 0.328 s | 496 KB |
| [1918_dp.py](1918_dp.py) | Python 3.12 x64 | dp | O(n^2) | AC | 1.734 s | 8620 KB |
| [1918_dp.rs](1918_dp.rs) | Rust 1.75 x64 | dp | O(n^2) | AC | 0.046 s | 252 KB |
