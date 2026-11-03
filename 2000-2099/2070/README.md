# 2070. Prime powers with a prime number of divisors

[Timus 2070](https://acm.timus.ru/problem.aspx?space=1&num=2070) · difficulty 235 · number_theory

Original problem by Alexey Danilyuk, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

One person calls an integer interesting when it is prime, another when
its number of positive divisors is prime. An integer is satisfying when
both agree, either way. Count the satisfying integers in [L; R]. The
limits are 2 seconds and 64 MB.

## Input

L and R, 2 ≤ L ≤ R ≤ 10¹².

## Output

The number of satisfying integers in [L; R].

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
3 7
```

Output:

```
4
```

### Example 2

Input:

```
2 2
```

Output:

```
1
```

### Example 3

Input:

```
77 1010
```

Output:

```
924
```

## Solution

A prime has 2 divisors, and 2 is prime, so both call every prime
interesting. A composite number is satisfying unless its number of
divisors is prime. For x = p₁^a₁ · … · pₛ^aₛ that number is
(a₁ + 1) · … · (aₛ + 1), and a product is prime only when it has a
single factor. So the unsatisfying numbers are exactly the powers p^k
of a prime with k ≥ 2 and k + 1 prime, and the answer is
R − L + 1 minus their count in [L; R].

Since p^k ≤ 10¹² with k ≥ 2, every such p is at most 10⁶. A sieve up to
10⁶ gives the primes, and for each prime p with p² ≤ R the powers
p², p³, … up to R are walked, counting those at least L whose exponent
plus one is prime. Primes above 10⁴ only have the square, so the walk
is short; the total work is dominated by the sieve, O(N log log N) with
N = 10⁶.

In the first example 4 = 2² has 3 divisors, so it is the only
unsatisfying number among 3 … 7 and the answer is 4.

## Optimized solutions

Separate prime squares from higher qualifying even powers. Count primes up to the required square root with a quotient-value prime-count DP, whose states are the distinct integer quotients. Only the higher powers need an explicit sieve, and their prime bases lie below the fourth root. Count each qualifying exponent as in the simple number-theoretic proof and subtract prefix counts for the requested interval. Integer root corrections avoid floating-point boundary errors.

Here R is the interval's right endpoint, M=floor(sqrt(R)) and P is the number of small primes used for the higher powers. The counted powers are excluded numbers, so subtract their interval count from the interval length.

- `2070_number_theory_dp.cpp`: 0.015 s / 172 KB; base `2070_number_theory.cpp`: 0.015 s / 284 KB; relative change: time -0.0%, memory -39.4%.
- `2070_number_theory_dp.go`: 0.031 s / 1116 KB; base `2070_number_theory.go`: 0.031 s / 2136 KB; relative change: time -0.0%, memory -47.8%.
- `2070_number_theory_dp.java`: 0.125 s / 492 KB; base `2070_number_theory.java`: 0.140 s / 2584 KB; relative change: time -10.7%, memory -81.0%.
- `2070_number_theory_dp.py`: 0.093 s / 940 KB; base `2070_number_theory.py`: 0.109 s / 2772 KB; relative change: time -14.7%, memory -66.1%.
- `2070_number_theory_dp.rs`: 0.046 s / 228 KB; base `2070_number_theory.rs`: 0.046 s / 1200 KB; relative change: time -0.0%, memory -81.0%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `2070_number_theory.cpp`; covering source `2070_number_theory.cpp`; time/memory places 1/1, other-author entries 76/76.

- Go: preferred teaching base `2070_number_theory.go`; covering source `2070_number_theory.go`; time/memory places 1/1, other-author entries 1/1.

- Java: preferred teaching base `2070_number_theory.java`; covering source `2070_number_theory.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `2070_number_theory.py`; covering source `2070_number_theory.py`; time/memory places 1/1, other-author entries 13/13.

- Rust: preferred teaching base `2070_number_theory.rs`; covering source `2070_number_theory.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2070_number_theory.cpp](2070_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.015 s | 284 KB | 11309222 |
| [2070_number_theory.go](2070_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.031 s | 2136 KB | 11294446 |
| [2070_number_theory.java](2070_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.140 s | 2584 KB | 11309223 |
| [2070_number_theory.py](2070_number_theory.py) | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.109 s | 2772 KB | 11309224 |
| [2070_number_theory.rs](2070_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.046 s | 1200 KB | 11309225 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2070_number_theory_dp.cpp](2070_number_theory_dp.cpp) | G++ 13.2 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.015 s | 172 KB | 11308159 |
| [2070_number_theory_dp.go](2070_number_theory_dp.go) | Go 1.14 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.031 s | 1116 KB | 11308162 |
| [2070_number_theory_dp.java](2070_number_theory_dp.java) | Java 1.8 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.125 s | 492 KB | 11308164 |
| [2070_number_theory_dp.py](2070_number_theory_dp.py) | Python 3.12 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.093 s | 940 KB | 11308156 |
| [2070_number_theory_dp.rs](2070_number_theory_dp.rs) | Rust 1.75 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.046 s | 228 KB | 11308166 |
