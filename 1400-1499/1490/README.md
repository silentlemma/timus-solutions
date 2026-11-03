# 1490. Fire Circle

[Timus 1490](https://acm.timus.ru/problem.aspx?space=1&num=1490) · difficulty 196 · math

Original problem by Alexander Ipatov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A floor is tiled with 1 × 1 squares. A circle of fire of integer radius
R (R ≤ 10⁵) is centred at a point where four tiles meet. A tile is
spoiled if it shares at least two points with the circle. Count the
spoiled tiles.

Time limit: 1 second. Memory limit: 64 MB.

## Input

R.

## Output

The number of spoiled tiles.

## Checking

Compare the exact answer tokens; whitespace formatting is immaterial.

- `1490_two_pointers.java` (Java 1.8): 14 repository cases.

- `1490_two_pointers.py` (PyPy 3.10 x64): 14 repository cases.

- `1490_two_pointers.rs` (Rust 1.75 x64): 14 repository cases.

## Examples

### Example 1

Input:

```
2
```

Output:

```
16
```

### Example 2

Input:

```
4
```

Output:

```
60
```

## Solution

The examples show that the whole disc counts, not only its rim. A tile
meets the disc in more than one point exactly when its corner nearest
to the centre lies strictly inside the disc; a tile whose nearest corner
lies on the circle touches it in that single point.

By symmetry count one quarter and multiply by 4. There the tile with
lower-left corner (i, j) counts when i² + j² < R², so column i holds
⌊√(R² − i² − 1)⌋ + 1 tiles, for i from 0 to R − 1. An integer square
root keeps this exact. The answer reaches about π·10¹⁰ and needs 64
bits. `O(R)`.

Pitfalls:

- a tile that only touches the disc at a corner, such as the one beyond
  (3, 4) for R = 5, does not count (tests 04, 05, 06);
- the answer for R = 10⁵ is 31 416 325 412, beyond 32 bits (test 07);
- a floating square root must be corrected to the exact integer one
  (tests 06, 07).

## Optimized solutions

Keep the square-root teaching sources. The two_pointers versions sweep x=0..R-1 and maintain the number y of first-quadrant nearest corners strictly inside the disc. Decrease y while x*x+(y-1)*(y-1)>=R*R, add y and multiply the final sum by four. The boundary is monotone, so y decreases at most R times over the whole sweep: O(R) integer operations and constant working state. Equality is outside, preventing tangent cells from being counted; no floating-point rounding or coordinate-axis double counting is involved. R<=100000 keeps squares and the final answer within signed64bits. Python explicitly disables PyPy JIT for bounded code-cache memory and runs its single body without an extra frame. Its slower time/lower memory tradeoff is stated below.

- `1490_two_pointers.java`: 0.125 s / 456 KB; base `1490_math.java`: 0.109 s / 1612 KB; relative change: time +14.7%, memory -71.7%.
- `1490_two_pointers.py`: 0.234 s / 308 KB; base `1490_math.py`: 0.078 s / 472 KB; relative change: time +200.0%, memory -34.7%.
- `1490_two_pointers.rs`: 0.031 s / 36 KB; base `1490_math.rs`: 0.031 s / 232 KB; relative change: time -0.0%, memory -84.5%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1490_math.cpp`; covering source `1490_math.cpp`; time/memory places 1/15, other-author entries 93/93.

- Go: preferred teaching base `1490_math.go`; covering source `1490_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1490_math.java`; covering source `1490_two_pointers.java`; time/memory places 4/2, other-author entries 4/4.

- Python/PyPy: preferred teaching base `1490_math.py`; covering source `1490_two_pointers.py`; time/memory places 14/1, other-author entries 15/15.

- Rust: preferred teaching base `1490_math.rs`; covering source `1490_two_pointers.rs`; time/memory places 2/1, other-author entries 1/1.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1490_math.cpp](1490_math.cpp) | G++ 13.2 x64 | math | O(R) | AC | 0.015 s | 128 KB | 11287181 |
| [1490_math.go](1490_math.go) | Go 1.14 x64 | math | O(R) | AC | 0.031 s | 1088 KB | 11287183 |
| [1490_math.java](1490_math.java) | Java 1.8 | math | O(R) | AC | 0.109 s | 1612 KB | 11287185 |
| [1490_math.py](1490_math.py) | Python 3.12 x64 | math | O(R) | AC | 0.078 s | 472 KB | 11287184 |
| [1490_math.rs](1490_math.rs) | Rust 1.75 x64 | math | O(R) | AC | 0.031 s | 232 KB | 11287186 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1490_two_pointers.java](1490_two_pointers.java) \* | Java 1.8 | two_pointers | O(R) time; O(1) working state | AC | 0.125 s | 456 KB | 11307985 |
| [1490_two_pointers.py](1490_two_pointers.py) \* | PyPy 3.10 x64 | two_pointers | O(R) time; O(1) working state | AC | 0.234 s | 308 KB | 11309772 |
| [1490_two_pointers.rs](1490_two_pointers.rs) \* | Rust 1.75 x64 | two_pointers | O(R) time; O(1) working state | AC | 0.031 s | 36 KB | 11309706 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
