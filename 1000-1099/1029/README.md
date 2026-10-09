# 1029. The cheapest walk up a building of offices

[Timus 1029](https://acm.timus.ru/problem.aspx?space=1&num=1029) · difficulty 354 · dp, dijkstra

Original problem from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A building has `M` floors (`1 ≤ M ≤ 100`) with `N` rooms each
(`1 ≤ N ≤ 500`); every office charges a positive fee. A walk starts in any
room of the first floor; each step goes either one floor up through the same
room number or to a neighbouring room on the same floor. Find a walk that
ends on the top floor and pays the smallest total of the fees of the offices
it visits. Every office can be reached for at most `10^9` in total.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`M` and `N`, then `M` lines of `N` fees: line `i` is floor `i`.

## Output

The room numbers of the offices in the order of the walk. Any cheapest
walk is accepted.

## Checking

The checker restores the floors from the room numbers — the same number
again means one floor up, a number differing by one is a step along the
floor — and verifies that the walk starts on the first floor, ends on the
top one and costs exactly the minimum.

## Examples

### Example 1

Input:

```
3 3
5 1 9
9 1 1
1 9 1
```

Output:

```
2 2 3 3
```

### Example 2

Input:

```
1 1
7
```

Output:

```
1
```

## Solution

**Dynamic programming by floors.** Let `best[i][j]` be the cheapest walk
ending at room `j` of floor `i`. On a floor the cheapest way to an office
comes either from below, or from the left neighbour, or from the right
neighbour — and on one floor a cheapest walk never turns back, because
fees are positive. So each floor takes three passes:

1. from below: `best[i][j] = fee[i][j] + best[i - 1][j]` (on the first floor
   just `fee[0][j]`);
2. left to right: `best[i][j] = min(best[i][j], best[i][j - 1] + fee[i][j])`;
3. right to left: `best[i][j] = min(best[i][j], best[i][j + 1] + fee[i][j])`.

Remember for every office which of the three gave its value; from the
cheapest office of the top floor, follow these choices back to the first
floor and print the rooms in reverse. `O(M·N)`.

**Shortest path.** The offices with the moves up, left and right form a
graph with positive weights on the vertices: Dijkstra's algorithm from all
first-floor offices at once gives the same answer in `O(M·N log(M·N))`.

Pitfalls:

- the walk may first move along the first floor to a cheaper room, so on the
  first floor the horizontal passes matter too;
- the output lists every visited office, including the steps along a floor;
- sums of fees can exceed 32 bits in intermediate comparisons: use 64-bit
  integers.

## Language notes

- **C++**, **Go**, **Python**, **Java**, **Rust**: the dynamic programming.
- **C++** also has Dijkstra's algorithm on the grid.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1029_dijkstra.cpp](1029_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(M·N log(M·N)) | AC | 0.046 s | 1156 KB |
| [1029_dp.cpp](1029_dp.cpp) | G++ 13.2 x64 | dp | O(M·N) | AC | 0.046 s | 1160 KB |
| [1029_dp.go](1029_dp.go) | Go 1.14 x64 | dp | O(M·N) | AC | 0.046 s | 4596 KB |
| [1029_dp.java](1029_dp.java) | Java 1.8 | dp | O(M·N) | AC | 0.125 s | 3564 KB |
| [1029_dp.py](1029_dp.py) | Python 3.12 x64 | dp | O(M·N) | AC | 0.140 s | 6036 KB |
| [1029_dp.rs](1029_dp.rs) | Rust 1.75 x64 | dp | O(M·N) | AC | 0.046 s | 2628 KB |
