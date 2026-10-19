# 2030. Broadcasting values to tree neighbors

[Timus 2030](https://acm.timus.ru/problem.aspx?space=1&num=2030) · difficulty 517 · dfs

Original problem by Nikita Sivukhin, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected undirected tree has `n` vertices, numbered 1 through `n`. Vertex `v`
initially holds an integer `a[v]`. Process two kinds of requests in order:

- `1 v`: take the current value at `v` and add that snapshot to every
  neighbor's value. The source's own value stays unchanged.
- `2 v`: report the current value at `v` modulo `P = 1000000007`.

Values are not replaced: each neighbor receives an addition. A request
uses the source value before the request; queries and later broadcasts
include all earlier additions. Constraints: `1 ≤ n,m ≤ 100000`, `0 ≤
a[v] ≤ 1000000000`, 2 seconds, 64 MB.

## Input

First `n`, then one line of `n` initial values. The next `n-1` lines
contain edge endpoints `x y`, with `1 ≤ x,y ≤ n`, `x ≠ y`. Connectivity
is guaranteed. Then comes the number `m` and `m` pairs `t v`, where `t`
is 1 or 2 and `1 ≤ v ≤ n`.

## Output

For every request of type 2, print one residue in `[0,P-1]` on its own line.
If no request asks for a value, print nothing. An isolated vertex's broadcasts
have no effect.

## Checking

Outputs are compared token by token.

## Examples

```
4
1 1 1 1
1 2
1 3
2 4
9
2 1
2 2
2 3
2 4
1 1
2 1
2 2
2 3
2 4
```

```
1
1
1
1
1
2
2
1
```

```
2
1 1
1 2
14
2 2
2 1
1 1
2 2
1 2
2 1
1 1
2 2
1 2
2 1
1 1
2 2
1 2
2 1
```

```
1
1
2
3
5
8
13
21
```

## Solution

Root the tree at vertex 1 using an iterative traversal. Every neighbor
is either the unique parent or one of the children. The large degree of
a vertex is therefore handled by splitting its broadcast into a parent
contribution and a children contribution.

Store `direct[v]`, initially `a[v]`, and `broadcast[v]`, initially zero.
The latter is the sum of all snapshots broadcast by `v`. The former
includes the initial value and all snapshots broadcast by the children
of `v`. The invariant is `value(v) = direct[v] + broadcast[parent[v]]
(mod P)` for a nonroot vertex; the root has value `direct[root]` alone.

For either request, first compute `delta = value(v)` using that
invariant. A query prints it. A broadcast adds `delta` to `broadcast[v]`
and, if `v` is not the root, to `direct[parent[v]]`. All additions are
reduced modulo `P`. No neighbor loop is needed while processing
requests.

### Correctness

Initially no vertex has broadcast anything, so the invariant gives each
initial value. Suppose it holds before a broadcast. Every child of `v`
reads `broadcast[v]` in its value, so increasing this one stored total
adds exactly `delta` to every child. The parent, when present, instead
receives the same amount in its own `direct` field. The source reads its
own `direct` and its parent's `broadcast`, neither of which changes.
Vertices outside this neighbor set read neither changed field, so their
values are unchanged. These are exactly the requested additions, and the
invariant is preserved. Queries read the invariant without changing it;
induction proves every answer. Reducing every stored sum modulo `P` is
valid because all operations are integer additions.

In the first sample, the initial four queries return ones. Broadcasting vertex 1
changes only vertices 2 and 3 to two; vertices 1 and 4 stay one. In the second
sample, alternating broadcasts on a single edge generate the successive values
`1,1,2,3,5,8,13,21` reported by the queries.

Traversal takes `O(n)` time and each request takes `O(1)`, for `O(n+m)`
total. The tree, parents and value arrays use `O(n)` working space.
Python buffers up to `O(m)` output strings; Rust also retains the input,
for `O(n+m)` total stored input/output. The C++, Go and Java programs
stream requests and output.

Pitfalls:

- Adding the source to itself is incorrect; there is no self-edge.
- Capture the current source value before modifying any fields.
- A nonroot value includes its parent's broadcast total, not the
  parent's current value.
- Treat the root separately; its parent sentinel must not create a
  self-contribution.
- Use iterative traversal: a path can have 100000 vertices.
- Queries may be absent; do not emit a fabricated zero.

## Language notes

All ports normalize after every addition; adding two residues is at most
`2000000012`, which fits a signed 32-bit integer, including Java's `int`
arrays. C++, Go and Rust use wider value fields. One conditional
subtraction suffices. Java uses primitive adjacency arrays and a byte
parser. Python reads input by line, builds parents iteratively and
releases temporary adjacency before processing requests. No recursion,
degree threshold or logarithmic data structure is needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2030_dfs.cpp](2030_dfs.cpp) | G++ 13.2 x64 | dfs | O(n+m) | AC | 0.109 s | 9368 KB |
| [2030_dfs.go](2030_dfs.go) | Go 1.14 x64 | dfs | O(n+m) | AC | 0.062 s | 14016 KB |
| [2030_dfs.java](2030_dfs.java) | Java 1.8 | dfs | O(n+m) | AC | 0.156 s | 8516 KB |
| [2030_dfs.py](2030_dfs.py) | Python 3.12 x64 | dfs | O(n+m) | AC | 0.546 s | 26824 KB |
| [2030_dfs.rs](2030_dfs.rs) | Rust 1.75 x64 | dfs | O(n+m) | AC | 0.062 s | 18652 KB |
