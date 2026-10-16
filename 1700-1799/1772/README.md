# 1772. Ski-Trails for Robots

[Timus 1772](https://acm.timus.ru/problem.aspx?space=1&num=1772) · difficulty 738 · segment_tree

Original problem by Alex Samsonov, from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n parallel lanes run from start to finish, and a skier starts on lane s.
Going down the course, it meets k fallen robots in order, each blocking
lanes l to r; between them it may step sideways, one lane per second.
No robot blocks every lane. Find the fewest seconds of sideways steps
needed to get past all of them.

## Input

n, s and k (2 ≤ n ≤ 10⁵, 1 ≤ s ≤ n, 0 ≤ k ≤ 10⁵), then the k blocked
stretches l and r (1 ≤ l ≤ r ≤ n) in the order they are met.

## Output

The fewest seconds.

## Examples

### Example 1

Input:

```
5 3 2
2 5
1 4
```

Output:

```
6
```

## Solution

Let f(x) be the least time to be on lane x after the robots met so far,
free to move on. At the start f(x) = |x − s|, and f never changes by
more than 1 between neighbouring lanes, since one more step fixes the
difference. A robot on lanes l to r leaves f unchanged outside them,
and inside them sets f(x) = min(f(l − 1) + (x − l + 1),
f(r + 1) + (r + 1 − x)): the skier passes on lane l − 1 or r + 1 and
steps back in afterwards. Going round further out never helps, as f is
already cheapest there by the step rule.

So every robot assigns a function of the form min(a + x, b − x) to a
stretch of lanes, and f(x) is given by the latest robot covering x, or
by the start if none does. A segment tree keeps, in each node, the last
robot whose stretch covers the whole node; the latest robot over a lane
is the largest of these on its way to the root. Each robot needs two
lookups and one assignment, and the answer is the least f over all
lanes at the end. `O((n + k) log n)`.

In the example f starts as 2 1 0 1 2. The robot on lanes 2 to 5 leaves
lane 1 at 2 and makes the rest 3 4 5 6; the robot on lanes 1 to 4 leaves
lane 5 at 6 and makes the rest 10 9 8 7, so the answer is 6.

Pitfalls:

- a robot touching an edge can be passed on one side only;
- the total can reach about 10¹⁰ when robots force the skier from edge
  to edge, beyond 32 bits;
- lanes inside a blocked stretch become usable again right after it.

The answers agree with a lane-by-lane dynamic program over all moves on
400 random cases of up to 9 lanes and with an independent accepted
implementation on 48 cases with up to 10⁵ lanes and robots. The Python
solution runs on PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1772_segment_tree.cpp](1772_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O((n + k) log n) | AC | 0.156 s | 2372 KB |
| [1772_segment_tree.go](1772_segment_tree.go) | Go 1.14 x64 | segment_tree | O((n + k) log n) | AC | 0.203 s | 8136 KB |
| [1772_segment_tree.java](1772_segment_tree.java) | Java 1.8 | segment_tree | O((n + k) log n) | AC | 0.140 s | 3184 KB |
| [1772_segment_tree.py](1772_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O((n + k) log n) | AC | 0.359 s | 19444 KB |
| [1772_segment_tree.rs](1772_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O((n + k) log n) | AC | 0.031 s | 6500 KB |
