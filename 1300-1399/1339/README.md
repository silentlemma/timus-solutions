# 1339. Babies

[Timus 1339](https://acm.timus.ru/problem.aspx?space=1&num=1339) · difficulty 852 · graphs

Original problem by Magaz Asanov, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A kindergarten has k boys and k girls, k ≤ 250 000. A boy likes at most
one girl and no girl is liked by two boys; in the same way a girl likes
at most one boy and no boy is liked by two girls. Split the children
into k boy–girl pairs so that in every pair with a child who likes
someone, the boy likes the girl of the pair or the girl likes the boy.
Any such split is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

k, then for each boy the number of the girl liked, or 0, then for each
girl the number of the boy liked, or 0.

## Output

For each boy, the number of the girl in the pair.

## Checking

The checker accepts any split into pairs that keeps the rule.

## Examples

### Example 1

Input:

```
3
3 0 0
0 2 0
```

Output:

```
3 2 1
```

## Solution

Draw an arrow from every child to the child they like. Every child has
at most one arrow out and, since nobody is liked twice, at most one
arrow in, and arrows always join a boy and a girl. So the arrows form
separate paths and cycles that alternate boys and girls.

Walk each path from its start, the child nobody likes, and pair the
children two by two along it. Everyone on the path except the last
child likes the next one, and only the last child of a path of odd
length is left over; that child likes nobody. A cycle alternates boys
and girls, so it has even length and pairs up completely. All pairs made
so far are joined by an arrow, so they keep the rule. The children left
over like nobody, and as many boys as girls are left, so they can be
paired in any way: such a pair has no child who likes someone.
`O(k)`.

Pitfalls:

- a path of odd length must leave out its end, not its start: the
  start likes someone and must be paired with that child (test 04);
- a single cycle through all 500 000 children must not be followed by
  recursion (test gen2);
- the free children have to be paired boy with girl, and they always
  come out in equal numbers.

The splits were checked on 500 random cases with up to 10 couples.

## Language notes

- CPython needs about 0.7 seconds for 250 000 couples, too close to the
  1-second limit, so the Python solution is submitted under PyPy 3.10,
  where it takes about 0.3 seconds.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1339_graphs.cpp](1339_graphs.cpp) | G++ 13.2 x64 | graphs | O(k) | AC | 0.328 s | 6632 KB |
| [1339_graphs.go](1339_graphs.go) | Go 1.14 x64 | graphs | O(k) | AC | 0.078 s | 13600 KB |
| [1339_graphs.java](1339_graphs.java) | Java 1.8 | graphs | O(k) | AC | 0.156 s | 18876 KB |
| [1339_graphs.py](1339_graphs.py) | PyPy 3.10 x64 | graphs | O(k) | AC | 0.359 s | 52392 KB |
| [1339_graphs.rs](1339_graphs.rs) | Rust 1.75 x64 | graphs | O(k) | AC | 0.062 s | 31828 KB |
