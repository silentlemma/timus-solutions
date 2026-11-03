# 1433. Diamonds

[Timus 1433](https://acm.timus.ru/problem.aspx?space=1&num=1433) · difficulty 264 · bruteforce, math

Original problem by Pavel Egorov and Stanislav Vasiliev, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two regular tetrahedra of the same size have each face painted R, G, B
or Y. The colours are listed in the same order for both: the base, the
front left face, the front right face and the back face. Print "equal"
if one tetrahedron can be turned to look exactly like the other, and
"different" otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Two lines of four letters.

## Output

"equal" or "different".

## Checking

Compare the exact lowercase token equal or different. The new exact Python source passed 12 repository fixtures under PyPy 3.10. Also 1600 independent rotation-group colour pairs. Other retained native variants keep their own saved target-runtime checks and exact Accepted receipts. Compare output according to the problem checker, not by choosing one historical formatting.

## Examples

### Example 1

Input:

```
RGRB
GRRB
```

Output:

```
equal
```

## Solution

A turn of a tetrahedron permutes its four faces, and the turns give
exactly the 12 even permutations: a turn about an axis through a corner
moves three faces in a cycle, a half turn about an axis through two
opposite edges swaps two pairs, and an odd permutation, such as one
swap, would be a mirror image. So try all 24 orders of the faces, keep
those with an even number of inversions, and check whether one of them
turns the first colouring into the second. `O(1)`.

Pitfalls:

- mirror images are different: with four distinct colours, swapping two
  faces is not a turn (tests 03, 11);
- with a repeated colour every arrangement of the same colours is equal,
  since swapping the two equal faces fixes the parity (tests 05, 07, 08,
  12).

## Optimized solutions

The teaching versions still enumerate the twelve proper tetrahedron rotations. The new mathematical variants first compare colour multisets. If a colour repeats, swapping two indistinguishable faces changes permutation parity without changing the colouring, so an even representative always exists. Otherwise four distinct colours define a unique permutation; it is a proper rotation exactly when its inversion parity is even. This avoids constructing all rotated colourings. Both branches use a constant number of faces and exact comparisons. The Python version also reads and writes the existing text streams.

- `1433_math.cpp`: 0.015 s / 104 KB; base `1433_bruteforce.cpp`: 0.015 s / 360 KB; relative change: time -0.0%, memory -71.1%.
- `1433_math.java`: 0.093 s / 348 KB; base `1433_bruteforce.java`: 0.125 s / 1568 KB; relative change: time -25.6%, memory -77.8%.
- `1433_math.py`: 0.109 s / 284 KB; base `1433_bruteforce.py`: 0.078 s / 440 KB; relative change: time +39.7%, memory -35.5%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1433_bruteforce.cpp`; covering source `1433_math.cpp`; time/memory places 1/1, other-author entries 48/48.

- Go: preferred teaching base `1433_bruteforce.go`; covering source `1433_bruteforce.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1433_bruteforce.java`; covering source `1433_math.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1433_bruteforce.py`; covering source `1433_math.py`; time/memory places 8/2, other-author entries 15/15.

- Rust: preferred teaching base `1433_bruteforce.rs`; covering source `1433_bruteforce.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1433_bruteforce.cpp](1433_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 360 KB | 11286216 |
| [1433_bruteforce.go](1433_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1084 KB | 11286217 |
| [1433_bruteforce.java](1433_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1568 KB | 11286219 |
| [1433_bruteforce.py](1433_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 440 KB | 11286218 |
| [1433_bruteforce.rs](1433_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 224 KB | 11286220 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1433_math.cpp](1433_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 104 KB | 11309265 |
| [1433_math.java](1433_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 348 KB | 11309266 |
| [1433_math.py](1433_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 284 KB | 11309683 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
