# 1935. Minimum Sheets with Reorderable Clearances

[Timus 1935](https://acm.timus.ru/problem.aspx?space=1&num=1935) · difficulty 80 · greedy

Original problem from Open Ural FU Championship 2012 | by Tatiana Sharypova (prepared by Oleg Dolgorukov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place n thin objects between the sheets of a book, in any order.
Object i requires at least a_i sheets between itself and each neighboring
object or cover. The same gap must satisfy both adjacent objects.
Find the minimum total number of sheets. Limits: 1 second, 64 MB.

## Input

The first line contains n, 1≤n≤100. The next line contains n integers
a_i, 1≤a_i≤100. The input order does not restrict placement order.

## Output

One integer: the minimum sufficient sheet count.

## Checking

Outputs are compared token by token.

## Examples

```
3
5 10 3
```

```
28
```

## Solution

Let S be the sum of all requirements and M their maximum. The answer
is S+M. Compute these two quantities directly; no sorting is necessary.

To prove the lower bound, fix any placement and select an object with
requirement M. Charge every object strictly to its left to the gap on
that object's left. Charge every object strictly to its right to the
gap on that object's right. Charge the selected maximum to both of its
adjacent gaps. These are all n+1 different gaps, each of which must
contain at least the charged requirement. Every requirement is counted
once and the selected maximum twice, giving at least S+M sheets.
This also covers n=1 and repeated maxima.

For an upper bound, arrange the requirements in nondecreasing order
b_1≤...≤b_n. Use b_1 sheets before the first object, b_{i+1} sheets
between objects i and i+1, and b_n after the last. An internal gap has
the larger of its two requirements, so every constraint holds. The
total is b_1+(b_2+...+b_n)+b_n=S+M. The lower bound is attainable,
and the formula is therefore optimal. Sorting is only a proof witness.

O(n) time. These implementations store the input values, so total
space is O(n), with O(1) additional arithmetic state.

Adjacent objects share sheets: add the larger clearance, not both.
Do not preserve the input order: requirements 100,1,100 need 301 sheets
after reordering, whereas that fixed order uses 400. The largest
requirement contributes one extra time. A single object needs 2a_1
sheets because both covers matter; repeated maxima add no extra rule.

## Language notes

The answer is at most 100·100+100=10100, so ordinary 32-bit integers
are sufficient. C++ uses integer accumulation and a maximum element;
Go and Java combine them in one loop. Python uses sum and max. Rust
uses i32 accumulation and the maximum of a nonempty slice. All programs
read whitespace-separated integers and print a final newline.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1935_greedy.cpp](1935_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 428 KB |
| [1935_greedy.go](1935_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.015 s | 1092 KB |
| [1935_greedy.java](1935_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 436 KB |
| [1935_greedy.py](1935_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.078 s | 332 KB |
| [1935_greedy.rs](1935_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.015 s | 236 KB |
