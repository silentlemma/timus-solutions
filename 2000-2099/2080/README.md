# 2080. Keep the cards in order of their next use

[Timus 2080](https://acm.timus.ru/problem.aspx?space=1&num=2080) · difficulty 746 · fenwick

Original problem by Eugene Kurpilyansky, prepared by Mikhail Vyatskov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n cards lie in a stack, and they will be used k times in a known order:
each time the card to use must be on top, and after use it may be put
back at any depth. Give the initial order of the stack and, for every
use, the number of cards to leave above the card when it goes back. Any
valid answer is accepted. The limits are 2 seconds and 256 MB.

## Input

n and k, 1 ≤ n, k ≤ 10⁵, then the k card numbers in the order of use.

## Output

The initial stack from top to bottom, then k lines with the number of
cards above each used card after it is put back.

## Checking

A checker replays the uses: every card must be on top when it is
needed, and every reinsertion depth must be at most n − 1.

## Examples

### Example 1

Input:

```
3 5
3 1 2 2 1
```

Output:

```
3 1 2
2
1
0
1
0
```

## Solution

Keep the stack sorted by the time of the next use, with cards that are
never used again at the bottom. Then the top card is always the next one
to use. At the start this is the order of first use, followed by the
unused cards. After the use at moment i, the card's next use is at
moment j (or never), and it must go below exactly the cards whose next
use comes before j. Every such card is used somewhere between i and j,
and every card used there has its next use before j, so their number is
the number of distinct cards among the uses i + 1 … j − 1 (or up to k
when the card is never used again).

Distinct values on ranges are counted offline with a Fenwick tree over
moments. A moment t > i is the first use of its card after i exactly when
the previous use of that card is at most i. So the queries go in
increasing i, and the moment t is added to the tree as soon as i
reaches the previous use of its card (moments that are first uses
overall are added at the start). The answer for i is then the number of
added moments in (i, j). The Fenwick sweep is O((n + k) log k);
the bounds below also include the initial ordering.

In the example card 1 is used at moments 2 and 5, and between them only
card 2 is used, so after moment 2 it goes back under one card.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2080_fenwick.cpp](2080_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n + k log k) | AC | 0.125 s | 2312 KB |
| [2080_fenwick.go](2080_fenwick.go) | Go 1.14 x64 | fenwick | O(n log² n + k log k) | AC | 0.078 s | 5636 KB |
| [2080_fenwick.java](2080_fenwick.java) | Java 1.8 | fenwick | O((n + k) log k) | AC | 0.156 s | 8412 KB |
| [2080_fenwick.py](2080_fenwick.py) | Python 3.12 x64 | fenwick | O((n + k) log k) | AC | 0.718 s | 30084 KB |
| [2080_fenwick.rs](2080_fenwick.rs) | Rust 1.75 x64 | fenwick | O((n + k) log k) | AC | 0.046 s | 9992 KB |
