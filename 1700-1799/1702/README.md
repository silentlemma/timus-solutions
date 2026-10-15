# 1702. Crossroad

[Timus 1702](https://acm.timus.ru/problem.aspx?space=1&num=1702) · difficulty 2314 · backtracking

Original problem by Sergey Pupyrev, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Cars approach a crossroad from four sides, and each side splits into
three flows: right turn, straight on and left turn. That gives 12 flows
with their own traffic lights. Flow i holds nᵢ cars, and while green it
lets vᵢ cars through per minute. The lights change once a minute, and
two flows may be green together only if they do not cross and do not
end in the same direction. Over 10 minutes, make the largest number of
cars left in any flow as small as possible.

## Input

n₁ … n₁₂ (0 ≤ nᵢ ≤ 1000), then v₁ … v₁₂ (1 ≤ vᵢ ≤ 1000).

## Output

That smallest possible maximum.

## Examples

### Example 1

Input:

```
2 0 0 14 13 0 20 0 0 0 60 7
1 1 1 1 3 1 2 1 1 1 5 1
```

Output:

```
10
```

## Solution

Following the statement's picture, flows 1–3 come from the south,
4–6 from the east, 7–9 from the north and 10–12 from the west, each
group in the order right turn, straight on, left turn, with right-hand
traffic. Drawing their paths through the crossroad gives the conflict
graph: flows from one side never conflict, flows with the same
destination always do, and the rest conflict when their paths cross.
For instance flow 1 conflicts only with 9 and 11. A minute's lights
form a set of pairwise compatible flows, and opening more flows never
hurts, so only the 17 maximal sets matter. Each of them opens exactly
four flows.

Binary search the answer L. Leaving at most L cars in flow i needs
⌈(nᵢ − L) / vᵢ⌉ green minutes for it. The question becomes whether 10
maximal sets cover those needs, which a memoized search decides. Some
minute must open the flow with the largest remaining need, so branch
only over the sets containing it. Prune when a need exceeds the minutes
left, or when the total need exceeds four times the minutes left. The
search stays small: well under 0.1 s per input.

Pitfalls:

- a flow needing more than 10 minutes makes that L impossible at once;
- the conflict graph comes from the picture, so getting the numbering
  right (and the merge rule for equal destinations) is the whole
  difficulty;
- two crossing flows of 100 cars at 10 per minute share the 10 minutes
  and keep 50 each (test 06).

The answers match an independent accepted implementation on 310 random
inputs, including heavy flows that need three or four minutes each.

Complexity: `O(S^T·log C)` for S = 17 maximal sets of lights, T = 10
minutes and C the largest number of cars, for the binary search.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1702_backtracking.cpp](1702_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(S^T·log C) | AC | 0.015 s | 280 KB |
| [1702_backtracking.go](1702_backtracking.go) | Go 1.14 x64 | backtracking | O(S^T·log C) | AC | 0.046 s | 1880 KB |
| [1702_backtracking.java](1702_backtracking.java) | Java 1.8 | backtracking | O(S^T·log C) | AC | 0.187 s | 6920 KB |
| [1702_backtracking.py](1702_backtracking.py) | Python 3.12 x64 | backtracking | O(S^T·log C) | AC | 0.125 s | 1712 KB |
| [1702_backtracking.rs](1702_backtracking.rs) | Rust 1.75 x64 | backtracking | O(S^T·log C) | AC | 0.031 s | 552 KB |
