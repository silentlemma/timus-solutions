# 1789. Searching for the Dodecahedron

[Timus 1789](https://acm.timus.ru/problem.aspx?space=1&num=1789) · difficulty 220 · constructive

Original problem by Mikhail Rubinchik, from the Ural Regional Team Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An artifact stands on one of n pedestals in a row, and copies stand on
the others. Each turn one pedestal is touched. If the artifact is there,
it is found; if not, the artifact moves to a neighbouring pedestal, left
or right, as it likes. Print a sequence of at most 1000 touches that
finds the artifact wherever it starts and however it moves.

## Input

n (2 ≤ n ≤ 100).

## Output

The number of touches, then the touched pedestals in order.

## Checking

Validate a sequence of at most 1000 touches, each pedestal in 1..N; propagate all possible artifact positions after every unsuccessful touch and require that none survive. Any sequence satisfying this guarantee is accepted. The new exact Python source passed 13 repository fixtures under PyPy 3.10. Also 99 streamed-versus-list construction checks for every N=2..100. Other retained native variants keep their own saved target-runtime checks and exact Accepted receipts. Compare output according to the problem checker, not by choosing one historical formatting.

## Examples

### Example 1

Input:

```
3
```

Output:

```
2
2 2
```

## Solution

After every unsuccessful touch the artifact moves, so the parity of its pedestal
flips every turn. Touch 2, 3, …, n − 1. If at the first touch the
artifact stands on an even pedestal, it has the same parity as the
touched one at every turn and is never to its left, so it can never jump
over it and is caught at n − 1 at the latest. Otherwise, after these
n − 2 touches it has the parity of n − 1, so touching n − 1, n − 2, …,
2 sweeps it the same way from the right. For n > 2, pedestals 1 and n
are never touched: an artifact there has to step inwards. That gives
2(n − 2) touches. With n = 2 there is no middle at all, and touching
pedestal 1 twice works. `O(n)`.

In the example both passes are the single touch of pedestal 2: an
artifact on 2 is caught at once, and one on 1 or 3 has to move to 2.

Pitfalls:

- the sweep from the left alone misses the artifact that starts with
  the other parity, which simply slips past;
- for n > 2, touching the end pedestals is wasted, as the artifact
  cannot stay on them;
- n = 2 needs its own answer, since the formula gives no touches.

The checker follows the set of pedestals where the artifact may still
be and requires it to empty out. Every n from 2 to 100 passes, and a
full search over these sets for n up to 12 confirms that no shorter
sequence exists.

## Optimized solutions

Keep the same parity-catching construction and its proof. For N>2, sweep 2..N-1 and then N-1..2; emit the count 2*(N-2). For N=2, emit the two touches 1,1. Compact implementations stream this sequence instead of retaining concatenated lists or expanding an output argument list. The sequence and worst-case guarantee are identical; output time is still O(N), while the streaming implementation needs only bounded working state. All simple files remain available.

- `1789_constructive_optimized.cpp`: 0.015 s / 108 KB; base `1789_constructive.cpp`: 0.031 s / 380 KB; relative change: time -51.6%, memory -71.6%.
- `1789_constructive_optimized.py`: 0.156 s / 240 KB; base `1789_constructive.py`: 0.062 s / 396 KB; relative change: time +151.6%, memory -39.4%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1789_constructive.cpp`; covering source `1789_constructive_optimized.cpp`; time/memory places 1/1, other-author entries 51/51.

- Go: preferred teaching base `1789_constructive.go`; covering source `1789_constructive.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1789_constructive.java`; covering source `1789_constructive.java`; time/memory places 1/1, other-author entries 1/1.

- Python/PyPy: preferred teaching base `1789_constructive.py`; covering source `1789_constructive_optimized.py`; time/memory places 8/1, other-author entries 7/7.

- Rust: preferred teaching base `1789_constructive.rs`; covering source `1789_constructive.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1789_constructive.cpp](1789_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.031 s | 380 KB | 11308929 |
| [1789_constructive.go](1789_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1108 KB | 11289832 |
| [1789_constructive.java](1789_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1604 KB | 11308930 |
| [1789_constructive.py](1789_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.062 s | 396 KB | 11289833 |
| [1789_constructive.rs](1789_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 204 KB | 11289836 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1789_constructive_optimized.cpp](1789_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 108 KB | 11308552 |
| [1789_constructive_optimized.py](1789_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(N) | AC | 0.156 s | 240 KB | 11309701 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
