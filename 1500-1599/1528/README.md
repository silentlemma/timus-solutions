# 1528. Sequence

[Timus 1528](https://acm.timus.ru/problem.aspx?space=1&num=1528) · difficulty 272 · math

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

With f(1) = g(1) = 1,
f(n) = 1 + f(1)g(1) + … + f(n − 1)g(n − 1) and
g(n) = 1 + 2g(1) + … + 2g(n − 1) − g(n − 1)². For up to 5000 cases
(1 ≤ n ≤ 10000, 2 ≤ p ≤ 2·10⁹), print f(n) mod p.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

Pairs n and p, one per line, ending with 0 0.

## Output

f(n) mod p for each case.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
1 2
2 11
0 0
```

Output:

```
1
2
```

## Solution

Both sequences have closed forms. If g(i) = i for i < n, then
g(n) = 1 + (n − 1)n − (n − 1)² = n. Then f(n) − f(n − 1) =
f(n − 1)·(n − 1), so f(n) = n·f(n − 1) = n!. So each case asks for
n! mod p. When n ≥ p, p itself is one of the factors and the answer
is 0. Otherwise multiply up to n, reducing modulo p as you go; the
products stay below 2·10¹³, within 64 bits. That is up to 5·10⁷
multiplications for all cases, fast in compiled languages (O(n) per case). In Python
the plain loop takes about 6 seconds, so the Python solution keeps the
exact factorials of every multiple of 100 as big integers and reduces
one of them, then multiplies at most 99 more factors: O(n log n) bit
operations per case.

Pitfalls:

- the formulas look heavy, but g(n) = n and f(n) = n! (all tests);
- n ≥ p gives 0 at once (test 02, gen3);
- p reaches 2·10⁹, so the products need 64 bits (test 03, gen1);
- a prime p just above n is a good check: Wilson's theorem gives
  (p − 1)! ≡ −1 (test 05).

## Optimized solutions

After the same reduction to factorial modulo the requested modulus, native implementations multiply adjacent factors together before taking a remainder. The stated bounds keep this product within signed 64-bit arithmetic; neither primality nor modular inverses are assumed. Python builds exact sparse factorial checkpoints and short block products with compiled big-integer multiplication, reusing a tail only for repeated equal arguments. These products are computed from the input bounds, not stored answer constants. The write-up's simple factorial recurrence remains valid for both implementations.

- `1528_math_optimized.cpp`: 0.203 s / 112 KB; base `1528_math.cpp`: 0.328 s / 132 KB; relative change: time -38.1%, memory -15.2%.
- `1528_math_optimized.go`: 0.218 s / 916 KB; base `1528_math.go`: 0.343 s / 1224 KB; relative change: time -36.4%, memory -25.2%.
- `1528_math_optimized.java`: 0.375 s / 840 KB; base `1528_math.java`: 0.609 s / 904 KB; relative change: time -38.4%, memory -7.1%.
- `1528_math_optimized.py`: 0.359 s / 1388 KB; base `1528_math.py`: 0.359 s / 17900 KB; relative change: time -0.0%, memory -92.2%.
- `1528_math_optimized.rs`: 0.156 s / 444 KB; base `1528_math.rs`: 0.250 s / 520 KB; relative change: time -37.6%, memory -14.6%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1528_math.cpp`; covering source `1528_math_optimized.cpp`; time/memory places 3/1, other-author entries 58/58.

- Go: preferred teaching base `1528_math.go`; covering source `1528_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1528_math.java`; covering source `1528_math_optimized.java`; time/memory places 1/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `1528_math.py`; covering source `1528_math_optimized.py`; time/memory places 3/1, other-author entries 5/5.

- Rust: preferred teaching base `1528_math.rs`; covering source `1528_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1528_math.cpp](1528_math.cpp) | G++ 13.2 x64 | math | O(n) per case | AC | 0.328 s | 132 KB | 11287420 |
| [1528_math.go](1528_math.go) | Go 1.14 x64 | math | O(n) per case | AC | 0.343 s | 1224 KB | 11287421 |
| [1528_math.java](1528_math.java) | Java 1.8 | math | O(n) per case | AC | 0.609 s | 904 KB | 11287423 |
| [1528_math.py](1528_math.py) | Python 3.12 x64 | math | O(n log n) bit operations per case | AC | 0.359 s | 17900 KB | 11287422 |
| [1528_math.rs](1528_math.rs) | Rust 1.75 x64 | math | O(n) per case | AC | 0.250 s | 520 KB | 11287424 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1528_math_optimized.cpp](1528_math_optimized.cpp) | G++ 13.2 x64 | math | O(sum N) | AC | 0.203 s | 112 KB | 11309294 |
| [1528_math_optimized.go](1528_math_optimized.go) | Go 1.14 x64 | math | O(sum N) | AC | 0.218 s | 916 KB | 11309296 |
| [1528_math_optimized.java](1528_math_optimized.java) | Java 1.8 | math | O(sum N) | AC | 0.375 s | 840 KB | 11309295 |
| [1528_math_optimized.py](1528_math_optimized.py) \* | Python 3.12 x64 | math | O(N) product construction + bigint query work | AC | 0.359 s | 1388 KB | 11309298 |
| [1528_math_optimized.rs](1528_math_optimized.rs) | Rust 1.75 x64 | math | O(sum N) | AC | 0.156 s | 444 KB | 11309297 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
