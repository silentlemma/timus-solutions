# 1890. Money out of Thin Air

[Timus 1890](https://acm.timus.ru/problem.aspx?space=1&num=1890) · difficulty 465 · fenwick

Original problem by Dmitry Ivankov, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A rooted tree contains n employees numbered 0 through n − 1, with root 0.
Each vertex has a nonnegative integer salary. Process q conditional
updates in the given order:

- `employee x y z`: if the current salary at x is strictly less than y,
  add z to that salary;
- `department x y z`: if the current average salary in the subtree of x
  is strictly less than y, add z to every salary in that subtree,
  including x.

Find every final salary. The tree never changes. The limits are
1 second and 64 MB.

## Input

The first line contains n, q and the initial salary s₀ of the root:
1 ≤ n, q ≤ 50 000 and 0 ≤ s₀ ≤ 10⁹.

For each i from 1 through n − 1, the next line contains its parent pᵢ
and initial salary sᵢ, where 0 ≤ pᵢ < i and 0 ≤ sᵢ ≤ 10⁹.

The next q lines contain the updates in the form given above, with
0 ≤ x < n and 1 ≤ y, z ≤ 10⁹.

## Output

Print n final salaries, one per line, in increasing vertex order.

## Checking

Outputs are compared token by token as integers.

## Examples

### Example 1

Input:

```
4 3 1
0 10
0 10
1 10
employee 2 15 1
employee 3 5 1
department 0 10 1
```

Output:

```
2
11
12
11
```

## Solution

Lay out the tree in preorder. Let tin[x] be the position of x and
size[x] the number of vertices in its subtree. That subtree occupies
precisely the interval [tin[x], tin[x] + size[x]).

Since each parent has a smaller number than its children, compute the
subtree sizes by adding them to their parents in decreasing vertex
order. Then process vertices in increasing order. Each parent reserves
a consecutive block of size[x] for a child x, starting just after the
parent's position and any previously reserved child blocks. This builds
the preorder positions in `O(n)` time without recursion.

Maintain the salaries in this order with two Fenwick trees supporting
an interval increment and an interval sum. To obtain this structure,
let dᵢ be the difference between consecutive salaries, indexed from 1,
with d₁ equal to the first salary. The first tree stores dᵢ, and the
second stores (i − 1)dᵢ. If their
prefix sums through k are B₁(k) and B₂(k), the sum of the first k
salaries is k·B₁(k) − B₂(k). Adding z on an interval changes only the
two boundary differences, so both trees need only two point updates.
An interval sum is the difference of two prefix sums.

For an employee update, query the one-element interval of x. For a
department update, query its whole subtree and let the result be S.
The exact test for the average is S < y·size[x]; division and floating
point are unnecessary. If the relevant strict inequality holds, add z
to the same interval. Otherwise change nothing.

The preorder intervals select exactly the required employees. The
Fenwick formula gives their current salary sum after every earlier
update, so each condition and each increment matches the operation.
Finally, undo the first Fenwick tree's construction: in decreasing
index order, subtract each entry from its Fenwick parent. The entries
then contain the current differences dᵢ. A prefix sum recovers every
salary in linear time; print them in the original vertex order.

Each query or increment costs `O(log n)`. Build the initial Fenwick
trees by propagating each entry to its Fenwick parent in increasing
index order. Both initialization and the final decoding are linear, so
the total time is `O(n + q log n)` and the memory usage is `O(n)`.

In the example, employee 2 changes from 10 to 11. Employee 3 stays at
10 because 10 is not less than 5. The whole tree then has sum 32 and
average 8, below 10, so the last update adds 1 to all four salaries.
They become 2, 11, 12 and 11 in vertex order.

Pitfalls:

- equality never triggers an update;
- a department includes its root and all descendants;
- vertex numbers are not generally consecutive within a subtree;
- use signed 64-bit arithmetic for salaries, sums, weighted differences
  and products such as y·size[x]; Python integers already handle these;
- print by vertex number, not by traversal position.

## Language notes

Use buffered input and output. Fixed-width implementations need 64-bit
Fenwick entries; tree indices can remain ordinary integers.

The answers agree with a brute-force simulation on 160 small random
cases and with an independent accepted implementation on 37 generated
ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1890_fenwick.cpp](1890_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n + q log n) | AC | 0.062 s | 2728 KB |
| [1890_fenwick.go](1890_fenwick.go) | Go 1.14 x64 | fenwick | O(n + q log n) | AC | 0.046 s | 11840 KB |
| [1890_fenwick.java](1890_fenwick.java) | Java 1.8 | fenwick | O(n + q log n) | AC | 0.187 s | 6316 KB |
| [1890_fenwick.py](1890_fenwick.py) | Python 3.12 x64 | fenwick | O(n + q log n) | AC | 0.843 s | 29672 KB |
| [1890_fenwick.rs](1890_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n + q log n) | AC | 0.046 s | 7924 KB |
