# 1445. Christmas gifts

[Timus 1445](https://acm.timus.ru/problem.aspx?space=1&num=1445) · difficulty 593 · math

Original problem by Stanislav Vasiliev, from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Harry's friends form N companies (1 ≤ N ≤ 500) of sizes from 1 to 500.
Harry meets the friends one at a time, hands each a gift and receives a
gift back. A friend may get a gift prepared by Harry or one received
from a member of another company, never one from the same company.
Find the smallest number of gifts Harry must prepare when Harry chooses
the order of the meetings, and when the order is the worst possible.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then the sizes of the companies.

## Output

The best and the worst number of prepared gifts.

## Examples

### Example 1

Input:

```
4
3 7 3 2
```

Output:

```
1 7
```

## Solution

Let m be the size of the largest company and S the number of friends.
Every exchange returns one gift, so Harry always holds as many gifts as
were prepared. The m members of the largest company need gifts from
outside it, and only S − m gifts ever come from outside, so at least
2m − S gifts must be prepared, and at least one in any case. That many
are enough: if 2m > S, serve 2m − S members of the largest company first,
then alternate it with the others. Otherwise, order the friends so
consecutive friends belong to different companies; one gift suffices.

In the worst order the largest company comes first; its gifts are
useless inside it, so m gifts are needed. They are also enough: Harry
holds m gifts, of which at most as many come from a company as its
members already met, so some gift from outside is left for every member
still waiting. `O(N)`.

Pitfalls:

- a single company needs every gift prepared in both cases (tests 02,
  03);
- one gift is enough when the largest company is no bigger than the
  rest plus one (tests 05, 06, 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1445_math.cpp](1445_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 128 KB |
| [1445_math.go](1445_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.046 s | 1112 KB |
| [1445_math.java](1445_math.java) | Java 1.8 | math | O(N) | AC | 0.140 s | 1988 KB |
| [1445_math.py](1445_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 468 KB |
| [1445_math.rs](1445_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 232 KB |
