# 1134. Checking whether numbers read from cards showing k − 1 and k are possible

[Timus 1134](https://acm.timus.ru/problem.aspx?space=1&num=1134) · difficulty 197 · greedy

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `n ≤ 1000` cards; card `k` shows `k − 1` on one side and `k` on
the other. A child took `m ≤ n` different cards in some order and read
one side of each. Given the `m` numbers read, decide whether they could
have come from some choice of cards and sides.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` and `m`, then the `m` numbers, each from `0` to `n`.

## Output

`YES` if the readings are possible, otherwise `NO`.

## Checking

Compare output tokens; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5 4
2 0 1 2
```

Output:

```
NO
```

## Solution

The question is whether every reading can get its own card. The number
`x` appears on cards `x` and `x + 1` (only card 1 for `0`, only card `n`
for `n`), so each reading may use one of two neighbouring cards. Count
the readings of each number and go up from `0`. Readings of `x` first take
card `x`, then card `x + 1`. Taking the lower card first is safe: card
`x` shows only `x − 1` and `x`, and all readings of `x − 1` are already
placed, so nothing later can use it. If some reading of `x` finds both of
its cards taken, no assignment exists. `O(n + m)`.

Pitfalls:

- `0` and `n` each appear on one card only;
- the same number may be read several times, at most twice for a
  possible answer;
- the readings come in arbitrary order; only their counts matter.

The answers were compared with Kuhn's bipartite matching on every test
and on 400 random cases.

## Optimized solutions

The lower-card-first greedy assignment is unchanged. A byte count for each card value replaces separate frequency and used-card arrays; a single occupancy state carries the boundary between adjacent choices. Process demands in value order and always consume the smallest still possible card, leaving larger cards for later demands. The sentinel removes endpoint branches. The chosen Python interpreter and the measured storage reduction are stated in the tables.

- `1134_greedy_optimized.py`: 0.140 s / 288 KB; base `1134_greedy.py`: 0.078 s / 492 KB; relative change: time +79.5%, memory -41.5%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1134_greedy.cpp`; covering source `1134_greedy.cpp`; time/memory places 1/3, other-author entries 69/69.

- Go: preferred teaching base `1134_greedy.go`; covering source `1134_greedy.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1134_greedy.java`; covering source `1134_greedy.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1134_greedy.py`; covering source `1134_greedy_optimized.py`; time/memory places 12/1, other-author entries 12/12.

- Rust: preferred teaching base `1134_greedy.rs`; covering source `1134_greedy.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1134_greedy.cpp](1134_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.015 s | 192 KB | 11279396 |
| [1134_greedy.go](1134_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.031 s | 1104 KB | 11279398 |
| [1134_greedy.java](1134_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.078 s | 432 KB | 11279401 |
| [1134_greedy.py](1134_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.078 s | 492 KB | 11279399 |
| [1134_greedy.rs](1134_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.015 s | 204 KB | 11279402 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1134_greedy_optimized.py](1134_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(N+M) | AC | 0.140 s | 288 KB | 11309377 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
