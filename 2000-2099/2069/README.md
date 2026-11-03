# 2069. The best route with at most two turns

[Timus 2069](https://acm.timus.ru/problem.aspx?space=1&num=2069) · difficulty 226 · greedy

Original problem by Oleg Merkurev, prepared by Alexander Borzunov, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city is a grid of n vertical and m horizontal streets, and every street
has its own popularity. A route goes along the streets from the upper
left corner to the lower right one, and its coolness is the smallest
popularity among the streets on which it covers a non-zero distance. Find
the largest possible coolness. The limits are 1 second and 64 MB.

## Input

n and m, 2 ≤ n, m ≤ 10⁵, then the n popularities of the vertical streets
from left to right and the m popularities of the horizontal streets from
top to bottom, one per line, each from 1 to 10⁹.

## Output

The largest coolness.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
2 3
4
8
2
7
3
```

Output:

```
4
```

### Example 2

Input:

```
4 3
12
4
12
3
21
5
16
```

Output:

```
12
```

## Solution

Let v₁ … vₙ be the vertical streets and h₁ … hₘ the horizontal ones; the
route starts where v₁ meets h₁ and ends where vₙ meets hₘ. Its first
step goes along v₁ or h₁, and its last step along vₙ or hₘ, so there are
four cases.

- It starts on v₁ and ends on hₘ. The coolness is at most min(v₁, hₘ),
  and going down v₁ and then right along hₘ reaches it.
- It starts on h₁ and ends on vₙ: at most min(h₁, vₙ), reached by going
  right and then down.
- It starts on h₁ and ends on hₘ. To change rows the route must move
  along some vertical street, so the coolness is at most
  min(h₁, max v, hₘ). Going right along h₁ to the best vertical street,
  down it and right along hₘ gives at least this value.
- It starts on v₁ and ends on vₙ: symmetrically min(v₁, max h, vₙ).

Every route falls into one of the cases and each bound is reached, so
the answer is the largest of the four values, found in O(n + m).

In the first example the first two cases give min(4, 3) = 3 and
min(2, 8) = 2, while the last one goes down v₁ = 4, right along h₂ = 7
and down v₂ = 8, with coolness 4.

## Optimized solutions

Stream the maxima and endpoint values of both street directions instead of storing every street. A threshold is feasible exactly when a street of each direction reaches it and each endpoint has an incident qualifying street. Their cross-grid is connected, so these conditions are sufficient as well as necessary. Taking the minimum of the two directional maxima and the two endpoint maxima gives the answer, preserving the simple case analysis with constant working storage.

- `2069_greedy_optimized.cpp`: 0.015 s / 84 KB; base `2069_greedy.cpp`: 0.156 s / 964 KB; relative change: time -90.4%, memory -91.3%.
- `2069_greedy_optimized.go`: 0.031 s / 1020 KB; base `2069_greedy.go`: 0.062 s / 5704 KB; relative change: time -50.0%, memory -82.1%.
- `2069_greedy_optimized.java`: 0.109 s / 404 KB; base `2069_greedy.java`: 0.140 s / 1260 KB; relative change: time -22.1%, memory -67.9%.
- `2069_greedy_optimized.py`: 0.171 s / 412 KB; base `2069_greedy.py`: 0.125 s / 21628 KB; relative change: time +36.8%, memory -98.1%.
- `2069_greedy_optimized.rs`: 0.031 s / 196 KB; base `2069_greedy.rs`: 0.015 s / 6308 KB; relative change: time +106.7%, memory -96.9%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `2069_greedy.cpp`; covering source `2069_greedy_optimized.cpp`; time/memory places 1/1, other-author entries 51/51.

- Go: preferred teaching base `2069_greedy.go`; covering source `2069_greedy_optimized.go`; time/memory places 1/1, other-author entries 1/1.

- Java: preferred teaching base `2069_greedy.java`; covering source `2069_greedy.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `2069_greedy.py`; covering source `2069_greedy_optimized.py`; time/memory places 2/1, other-author entries 4/4.

- Rust: preferred teaching base `2069_greedy.rs`; covering source `2069_greedy_optimized.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2069_greedy.cpp](2069_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.156 s | 964 KB | 11309218 |
| [2069_greedy.go](2069_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.062 s | 5704 KB | 11294438 |
| [2069_greedy.java](2069_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.140 s | 1260 KB | 11309219 |
| [2069_greedy.py](2069_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.125 s | 21628 KB | 11309220 |
| [2069_greedy.rs](2069_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.015 s | 6308 KB | 11309221 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2069_greedy_optimized.cpp](2069_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N+M) | AC | 0.015 s | 84 KB | 11308572 |
| [2069_greedy_optimized.go](2069_greedy_optimized.go) | Go 1.14 x64 | greedy | O(N+M) | AC | 0.031 s | 1020 KB | 11308575 |
| [2069_greedy_optimized.java](2069_greedy_optimized.java) | Java 1.8 | greedy | O(N+M) | AC | 0.109 s | 404 KB | 11308581 |
| [2069_greedy_optimized.py](2069_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(N+M) | AC | 0.171 s | 412 KB | 11308586 |
| [2069_greedy_optimized.rs](2069_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(N+M) | AC | 0.031 s | 196 KB | 11308590 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
