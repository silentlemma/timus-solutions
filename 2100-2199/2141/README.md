# 2141. Maximum alternating sum of a segment

[Timus 2141](https://acm.timus.ru/problem.aspx?space=1&num=2141) · difficulty 251 · dp

Original problem by Alexander Lozhkin, from the Ural Team Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose a contiguous segment of a sequence, possibly empty, and sum it
with alternating signs: the first chosen element with a plus, the second
with a minus and so on. Find the largest possible value. The limits are
1 second and 256 MB.

## Input

n, 1 ≤ n ≤ 10⁵, then a₁ … aₙ, −10⁵ ≤ aᵢ ≤ 10⁵.

## Output

The largest alternating sum (0 for the empty segment).

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
5
1 2 3 4 5
```

Output:

```
5
```

### Example 2

Input:

```
5
1 -2 3 -4 5
```

Output:

```
15
```

### Example 3

Input:

```
5
-1 -2 -3 -4 -5
```

Output:

```
2
```

## Solution

Scan the sequence keeping two values for segments that end at the
current element: P, the best sum when this element has a plus, and M,
the best sum when it has a minus. An element with a plus either starts a
new segment or follows an element with a minus, and an element with a
minus always follows one with a plus:

- P = a + max(0, previous M),
- M = previous P − a.

The first element can only have a plus, so it starts with P = a₁, and M
is set to 0, which in the next step only means "start anew". The answer
is the largest P or M seen, or 0. Sums reach 10¹⁰, so they need 64-bit
integers. The scan takes O(n).

In the second example 1 − (−2) + 3 − (−4) + 5 = 15.

## Optimized solutions

Keep the two-state DP for alternating signed segments, including the empty answer. Each new negative state uses the previous positive state, so capture the old value before overwriting either state. Compare directly instead of making repeated helper calls. Bounded signed-token input replaces the complete token list, integer list and slice; a token split across buffers is carried forward correctly. Native sums use 64-bit arithmetic.

- `2141_dp_optimized.cpp`: 0.031 s / 84 KB; base `2141_dp.cpp`: 0.078 s / 140 KB; relative change: time -60.3%, memory -40.0%.
- `2141_dp_optimized.go`: 0.031 s / 924 KB; base `2141_dp.go`: 0.078 s / 1916 KB; relative change: time -60.3%, memory -51.8%.
- `2141_dp_optimized.py`: 0.156 s / 1392 KB; base `2141_dp.py`: 0.156 s / 12300 KB; relative change: time -0.0%, memory -88.7%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `2141_dp.cpp`; covering source `2141_dp_optimized.cpp`; time/memory places 6/1, other-author entries 105/105.

- Go: preferred teaching base `2141_dp.go`; covering source `2141_dp_optimized.go`; time/memory places 1/1, other-author entries 1/1.

- Java: preferred teaching base `2141_dp.java`; covering source `2141_dp.java`; time/memory places 1/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `2141_dp.py`; covering source `2141_dp_optimized.py`; time/memory places 8/1, other-author entries 22/22.

- Rust: preferred teaching base `2141_dp.rs`; covering source `2141_dp.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2141_dp.cpp](2141_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.078 s | 140 KB | 11294922 |
| [2141_dp.go](2141_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.078 s | 1916 KB | 11294923 |
| [2141_dp.java](2141_dp.java) | Java 1.8 | dp | O(n) | AC | 0.109 s | 488 KB | 11309242 |
| [2141_dp.py](2141_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.156 s | 12300 KB | 11309243 |
| [2141_dp.rs](2141_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.031 s | 2136 KB | 11309244 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2141_dp_optimized.cpp](2141_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.031 s | 84 KB | 11308803 |
| [2141_dp_optimized.go](2141_dp_optimized.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 924 KB | 11308805 |
| [2141_dp_optimized.py](2141_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N) | AC | 0.156 s | 1392 KB | 11308802 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
