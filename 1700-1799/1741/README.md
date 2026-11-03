# 1741. Communication Fiend

[Timus 1741](https://acm.timus.ru/problem.aspx?space=1&num=1741) · difficulty 289 · dp

Original problem by Alex Samsonov (prepared by Marina Mukhacheva), from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A licensed client of version 1 has to reach version n. Each update
takes version x to version y > x and has a size. A pirated update
makes the client pirated for good; a cracked update installs on any
client; a licensed update installs only on a client that is still
licensed. Find the least total size of updates, or report that version
n cannot be reached.

## Input

n and m (2 ≤ n ≤ 10⁴, 1 ≤ m ≤ 10⁴), then m updates `x y d s`
(1 ≤ x < y ≤ n, 1 ≤ d ≤ 10⁶), where s is `Pirated`, `Cracked` or
`Licensed`.

## Output

`Online` and the least total size, or `Offline`.

## Checking

Compare output tokens; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 4
1 3 10 Licensed
1 2 2 Pirated
2 3 3 Licensed
2 3 6 Cracked
```

Output:

```
Online
8
```

### Example 2

Input:

```
3 1
1 2 10 Licensed
```

Output:

```
Offline
```

## Solution

Updates only raise the version, so the versions can be handled in
increasing order, each after everything that leads to it. The state is
the version together with whether the client is still licensed or
already pirated. From each reached state, a pirated update leads to the
pirated state of its target, a cracked one keeps the state, and a
licensed one is allowed only from the licensed state. The answer is
the smaller of the two values at version n. `O(n + m)`.

In the first example the pirated 1 → 2 for 2 and the cracked 2 → 3 for
6 give 8, cheaper than the licensed 1 → 3 for 10; the licensed 2 → 3
for 3 cannot follow the pirated update.

Pitfalls:

- the total can reach about 10¹⁰, more than 32 bits hold;
- a cracked update keeps a licensed client licensed;
- it does not matter whether version n ends up licensed.

The answers match an independent accepted implementation, a shortest
path search, on 200 random cases.

## Optimized solutions

Keep the increasing-version DAG DP with clean and pirated license states. Flat edge arrays replace per-vertex containers and edge objects. A pirated update transfers the minimum of both states only to the pirated state; a cracked update preserves either state, and a licensed update accepts only the clean state. Branch once per update type. Path costs require 64-bit values, while vertex IDs and edge fields fit compact cells. No priority queue or Dijkstra traversal is needed.

- `1741_dp_optimized.cpp`: 0.015 s / 196 KB; base `1741_dp.cpp`: 0.031 s / 1068 KB; relative change: time -51.6%, memory -81.6%.
- `1741_dp_optimized.java`: 0.093 s / 748 KB; base `1741_dp.java`: 0.156 s / 5788 KB; relative change: time -40.4%, memory -87.1%.
- `1741_dp_optimized.py`: 0.109 s / 972 KB; base `1741_dp.py`: 0.109 s / 6872 KB; relative change: time -0.0%, memory -85.9%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1741_dp.cpp`; covering source `1741_dp_optimized.cpp`; time/memory places 1/1, other-author entries 56/56.

- Go: preferred teaching base `1741_dp.go`; covering source `1741_dp.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1741_dp.java`; covering source `1741_dp_optimized.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1741_dp.py`; covering source `1741_dp_optimized.py`; time/memory places 5/1, other-author entries 8/8.

- Rust: preferred teaching base `1741_dp.rs`; covering source `1741_dp.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1741_dp.cpp](1741_dp.cpp) | G++ 13.2 x64 | dp | O(n + m) | AC | 0.031 s | 1068 KB | 11308918 |
| [1741_dp.go](1741_dp.go) | Go 1.14 x64 | dp | O(n + m) | AC | 0.046 s | 3284 KB | 11289495 |
| [1741_dp.java](1741_dp.java) | Java 1.8 | dp | O(n + m) | AC | 0.156 s | 5788 KB | 11308919 |
| [1741_dp.py](1741_dp.py) | Python 3.12 x64 | dp | O(n + m) | AC | 0.109 s | 6872 KB | 11308920 |
| [1741_dp.rs](1741_dp.rs) | Rust 1.75 x64 | dp | O(n + m) | AC | 0.015 s | 2164 KB | 11289501 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1741_dp_optimized.cpp](1741_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N+M) | AC | 0.015 s | 196 KB | 11309342 |
| [1741_dp_optimized.java](1741_dp_optimized.java) | Java 1.8 | dp | O(N+M) | AC | 0.093 s | 748 KB | 11309343 |
| [1741_dp_optimized.py](1741_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N+M) | AC | 0.109 s | 972 KB | 11309341 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
