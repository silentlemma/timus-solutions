# 1013. Counting base-K numbers without two adjacent zeros, modulo M

[Timus 1013](https://acm.timus.ru/problem.aspx?space=1&num=1013) · difficulty 198 · matrix

Original problem: the hardest version of [problems 1009](../1009/README.md) and [1012](../1012/README.md).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count, modulo `M`, the `N`-digit numbers in base `K` (the first digit is not
zero) whose digits contain no two zeros in a row. `2 ≤ N, K, M ≤ 10^18`.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, `K` and `M`, each on its own line.

## Output

The count modulo `M`.

## Checking

Exact integer tokens. New sources keep their own full target-runtime tests and Accepted; previously published bases keep their original own Accepted rather than older archive measurements.

## Examples

### Example 1

Input:

```
5
2
1000
```

Output:

```
8
```

### Example 2

Input:

```
3
10
7
```

Output:

```
2
```

## Solution

The five simple sources retain the two-state matrix algorithm. After
the first nonzero digit, `(zero,other)=(0,K−1)`. Appending a digit gives
`zero'=other`, `other'=(K−1)(zero+other)`: a zero follows only a nonzero,
whereas every valid prefix permits any of `K−1` nonzero digits.
Thus raise `A=[[0,1],[c,c]]`, `c=(K−1) mod M`, to `N−1` by binary
exponentiation and apply it to `(0,c)`. Sum both final states modulo `M`.
This proves correctness without modular division, even for composite `M`.

There are at most 60 exponent bits, so there are `O(log N)` matrix steps
and a constant number of residues. C++/Rust widen products to 128 bits:
the sum of two products is below `2M²≤2·10³⁶<2¹²¹`. Go multiplies to a
high/low pair with `bits.Mul64` and obtains the remainder via `bits.Div64`;
the high word is smaller than `M`, meeting its precondition. Java/Python
use arbitrary-precision integers. Their arithmetic cost depends on
`log M`; “constant residues” does not mean constant bits. Input and the
exponent representation are accounted for separately from matrix state.

Only Rust's input preparation changes: take the three `u64` tokens from
an iterator instead of collecting a vector and indexing it. The matrix
calculation and output stay identical. This accepted simplification is
not called a 30% optimization; its own new metrics replace the old ones.
The other four bases remain byte-exact, and the old Rust bytes are backed up.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1013_matrix.cpp`; covering source `1013_matrix.cpp`; time/memory places 1/2, other-author entries 89/89.

- Go: preferred teaching base `1013_matrix.go`; covering source `1013_matrix.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1013_matrix.java`; covering source `1013_dp_math.java`; time/memory places 3/1, other-author entries 5/5.

- Python/PyPy: preferred teaching base `1013_matrix.py`; covering source `1013_dp_math.py`; time/memory places 26/1, other-author entries 43/43.

- Rust: preferred teaching base `1013_matrix.rs`; covering source `1013_dp_math.rs`; time/memory places 2/1, other-author entries 1/1.

## Optimized solutions

Keep all five matrix teaching algorithms, including the already accepted Rust input simplification. Let c=(K-1) mod M and represent a polynomial by aX+b modulo X²-cX-c. Squaring gives a'=c*a²+2ab and b'=c*a²+b²; multiplying by X gives a'=ca+b,b'=ca. Scan the bits of N from most significant to least, starting with 1, to obtain X^N. The answer is a*c+b modulo M, exactly the two-state recurrence with the nonzero first digit. There is no modular division, so composite M and common factors are safe. Native Rust uses 128-bit products; every unreduced sum is below 3M² < 2^122. Python uses native big integers and an integer bit mask instead of constructing a binary string. There are O(log N) modular steps and a constant number of residues, whose bits depend on log M. Bounded Rust C-ABI I/O avoids heap/startup costs. Compare with the current accepted Rust matrix base at 200 KB, not its older 220 KB measurement.

- `1013_dp_math.java`: 0.125 s / 752 KB; base `1013_matrix.java`: 0.125 s / 1868 KB; relative change: time -0.0%, memory -59.7%.
- `1013_dp_math.py`: 0.109 s / 272 KB; base `1013_matrix.py`: 0.078 s / 400 KB; relative change: time +39.7%, memory -32.0%.
- `1013_dp_math.rs`: 0.031 s / 44 KB; base `1013_matrix.rs`: 0.031 s / 200 KB; relative change: time -0.0%, memory -78.0%.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1013_matrix.cpp](1013_matrix.cpp) | G++ 13.2 x64 | matrix | O(log N) | AC | 0.015 s | 136 KB | 11278088 |
| [1013_matrix.go](1013_matrix.go) | Go 1.14 x64 | matrix | O(log N) | AC | 0.031 s | 1072 KB | 11278089 |
| [1013_matrix.java](1013_matrix.java) | Java 1.8 | matrix | O(log N) | AC | 0.125 s | 1868 KB | 11278093 |
| [1013_matrix.py](1013_matrix.py) | Python 3.12 x64 | matrix | O(log N) | AC | 0.078 s | 400 KB | 11278091 |
| [1013_matrix.rs](1013_matrix.rs) | Rust 1.75 x64 | matrix | O(log N) | AC | 0.031 s | 200 KB | 11308297 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1013_dp_math.java](1013_dp_math.java) \* | Java 1.8 | dp, math | O(log N) modular steps; O(1) residues | AC | 0.125 s | 752 KB | 11308293 |
| [1013_dp_math.py](1013_dp_math.py) \* | PyPy 3.10 x64 | dp, math | O(log N) modular steps; O(1) residues | AC | 0.109 s | 272 KB | 11309745 |
| [1013_dp_math.rs](1013_dp_math.rs) \* | Rust 1.75 x64 | dp, math | O(log N) modular steps; O(1) residues | AC | 0.031 s | 44 KB | 11309707 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
