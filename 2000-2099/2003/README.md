# 2003. Pairwise GCD Iteration

[Timus 2003](https://acm.timus.ru/problem.aspx?space=1&num=2003) · difficulty 366 · number_theory

Original problem by Kirill Borozdin, from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An array contains positive integers. A step replaces it with the
greatest common divisor of each unordered pair of distinct positions.
Every pair contributes one element, even when several results or
original values coincide. Thus length `k` becomes `k(k−1)/2`. Find the
minimum number of steps until every element is 1.

## Input

The first line contains `n`, where `3 ≤ n ≤ 10000`. The following `n`
lines contain the array values, each from 1 to `10^7`. Whitespace
separates numbers. Time limit 1 second, memory 64 MB.

## Output

Print the minimum number of steps, or lowercase `infinity` if the target
cannot be reached or the minimum exceeds `10^18`. An array of ones
already satisfies the target and needs zero steps.

## Checking

Outputs are compared token by token.

## Examples

```
3
1
2
3
```

```
1
```

```
4
2
2
2
2
```

```
infinity
```

In the first example every pair has GCD 1, so one step suffices. In the
second example every new element remains 2 forever.

## Solution

Fix a prime `p` and let `c` be the number of current elements divisible
by `p`. A new GCD is divisible by `p` exactly when both selected
positions were divisible by it. Consequently its new incidence is
`c(c−1)/2`. This counts positions, not exponents in a factorization.

The incidence trajectories are `0→0`, `1→0` and `2→1→0`. Incidence 3
remains 3. For any `c≥4`, `c(c−1)/2≥c`, so an incidence of at least 3
never disappears. The array length remains at least 3 because the
initial length is at least 3.

Therefore a prime dividing three original elements proves `infinity`. If
no such prime exists, all primes disappear within two steps. An original
incidence of 2 requires exactly two steps; otherwise any non-one
requires exactly one. With no prime factors at all, the answer is 0.
These cases prove both reachability and minimality. No finite answer
above 2 exists, so the `10^18` clause needs no large arithmetic.

Generate primes up to `B=floor(sqrt(A))`, where `A` is the maximum input
value, with a small sieve. Factor each element by these primes, stopping
when the trial prime squared exceeds the remaining value. Count a
divisor once, remove all its powers, then count a remaining value above
1 once: it is prime. Store incidences in a hash map and return
`infinity` immediately upon the third occurrence. Otherwise return the
largest incidence, initially 0.

Let `P` be the number of primes at most `B` and `F` the total number of
distinct prime factors across the input elements. Expected time is `O(B
log log(B+2) + nP + n log(A+1))`, including divisions and hash updates;
memory is `O(n+B+F)`, including the input. Hash bounds are expected.
Here `B≤3162`, `P≤446` and `F≤8n`: the product of the first nine primes
already exceeds `10^7`. No sieve of size `10^7` or growing GCD array is
stored.

Count each prime only once per input position. For example `[4,8,1]`
needs two steps despite repeated powers of 2. A GCD of the whole array
equal to 1 does not guarantee termination: `[2,2,2,3]` is infinite.
Conversely `[6,10,15]` needs two steps even though every original pair
shares a factor. Repeated input values remain separate positions. Handle
1 without adding a factor and spell `infinity` exactly.

## Language notes

All five ports use the same small-prime trial division and sparse
counters. C++, Go, Java and Rust derive the square-root bound with
integer arithmetic; Python uses `isqrt`. Products fit 32-bit signed
integers under the stated limits. Java uses buffered input, and Python
uses bulk integer parsing. CPython is selected after full-program
maximum-input measurement.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2003_number_theory.cpp](2003_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.031 s | 568 KB |
| [2003_number_theory.go](2003_number_theory.go) | Go 1.14 x64 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.078 s | 2048 KB |
| [2003_number_theory.java](2003_number_theory.java) | Java 1.8 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.156 s | 1480 KB |
| [2003_number_theory.py](2003_number_theory.py) | Python 3.12 x64 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.578 s | 2024 KB |
| [2003_number_theory.rs](2003_number_theory.rs) | Rust 1.75 x64 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.031 s | 1008 KB |
