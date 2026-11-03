# 1794. Masterpieces of World Architecture

[Timus 1794](https://acm.timus.ru/problem.aspx?space=1&num=1794) · difficulty 197 · implementation

Original problem by Vladislav Isenbaev (prepared by Oleg Dolgorukov), from the Ural Regional Team Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n students sit in a circle, numbered 1 to n clockwise, and will speak
one after another clockwise. Student i would like to speak aᵢ-th.
Choose who speaks first so that as many students as possible speak
exactly at the turn they want. Any best choice is accepted.

## Input

n (2 ≤ n ≤ 10⁵), then a₁, …, aₙ (1 ≤ aᵢ ≤ n).

## Output

The number of the student who starts.

## Checking

Accept any starting student attaining the maximum number of satisfied wishes; a unique smallest-index choice is not required.

## Examples

### Example 1

Input:

```
4
4 1 2 3
```

Output:

```
2
```

### Example 2

Input:

```
3
1 1 1
```

Output:

```
3
```

## Solution

If student k starts, student i speaks at turn ((i − k) mod n) + 1. So
student i is pleased by exactly one start, k = ((i − aᵢ) mod n) + 1.
Count these votes over all students and print a start with the most
votes. `O(n)`.

In the first example all four students vote for start 2: for instance
student 1 wants to be fourth, and 2, 3, 4, 1 puts them fourth.

Pitfalls:

- i − aᵢ may be negative, and in C++, Go and Java the remainder then
  is negative too;
- several starts may tie, as in the second example, where any of the
  three is accepted.

The checker counts the votes itself and accepts any start with the
most. It agrees with a direct count over every start on 300 small
classes, and the answers agree with an independent accepted
implementation on large ones.

## Optimized solutions

Keep the vote count for each possible starting student. The index difference lies strictly between the negative and positive class size, so one conditional addition replaces general remainder operations. Buffered input avoids retaining all preferences; packed unsigned 32-bit counters fit because each count is at most the class size. The implementation selects the first greatest count, although the statement accepts any optimal starting student.

- `1794_implementation_optimized.cpp`: 0.015 s / 520 KB; base `1794_implementation.cpp`: 0.078 s / 568 KB; relative change: time -80.8%, memory -8.5%.
- `1794_implementation_optimized.py`: 0.187 s / 912 KB; base `1794_implementation.py`: 0.125 s / 8004 KB; relative change: time +49.6%, memory -88.6%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1794_implementation.cpp`; covering source `1794_implementation_optimized.cpp`; time/memory places 1/8, other-author entries 96/96.

- Go: preferred teaching base `1794_implementation.go`; covering source `1794_implementation.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1794_implementation.java`; covering source `1794_implementation.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1794_implementation.py`; covering source `1794_implementation_optimized.py`; time/memory places 13/1, other-author entries 13/13.

- Rust: preferred teaching base `1794_implementation.rs`; covering source `1794_implementation.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1794_implementation.cpp](1794_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.078 s | 568 KB | 11308931 |
| [1794_implementation.go](1794_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 2400 KB | 11289873 |
| [1794_implementation.java](1794_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 792 KB | 11308933 |
| [1794_implementation.py](1794_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.125 s | 8004 KB | 11308935 |
| [1794_implementation.rs](1794_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 2124 KB | 11308936 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1794_implementation_optimized.cpp](1794_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 520 KB | 11308385 |
| [1794_implementation_optimized.py](1794_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.187 s | 912 KB | 11309462 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
