# 1846. GCD 2010

[Timus 1846](https://acm.timus.ru/problem.aspx?space=1&num=1846) · difficulty 155 · segment_tree

Original problem by Alexey Samsonov, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A multiset of positive integers starts empty. Each operation adds a
number or removes one copy of a number that is there. After every
operation print the greatest common divisor of the whole multiset; the
gcd of an empty multiset is declared to be 1.

## Input

q (1 ≤ q ≤ 10⁵), then q lines "+ x" or "- x" with 1 ≤ x ≤ 10⁹. Only
numbers present are removed.

## Output

The gcd after each operation, one per line.

## Examples

### Example 1

Input:

```
5
+ 8
+ 6
+ 8
- 8
- 8
```

Output:

```
8
2
2
2
6
```

## Solution

A gcd cannot be undone, so removing a number needs a structure. Give
every addition its own leaf of a segment tree over the operations, and
keep for each value a stack of the leaves that hold it. Adding x writes
x into the leaf of that operation; removing x empties the top leaf of
its stack, writing 0, which leaves any gcd unchanged since
gcd(a, 0) = a. Each internal node holds the gcd of its children, so the
root is the gcd of the multiset, and a root of 0 means the multiset is
empty: print 1. Updating a leaf recomputes its ancestors, and the walk
up can stop at the first node whose value stays the same, since nothing
above it changes then. `O(q log q log x)`.

In the example the leaves hold 8, 6 and 8, so the gcd is 2. Removing
the two 8s empties two leaves and leaves 6.

Pitfalls:

- the empty multiset prints 1, not 0;
- equal numbers may be added several times and removed one at a time;
- with half a second, stopping the walk early and reading the input
  quickly both matter; the simple Python solution runs on PyPy.

The answers agree with an independent accepted implementation on thirty
random files of up to 10⁵ operations.

## Optimized solutions

The optimized C++ solution reads all operations first, sorts and
deduplicates their values and gives every distinct value one leaf with a
counter of its copies, instead of a leaf per addition and a hash map of
leaf stacks. The leaf holds x while the counter is positive and 0
otherwise, so the tree changes only when a value appears or disappears.
An operation is stored as one signed `int`, +x or −x, which fits since
x ≤ 10⁹; the leaf of a value is found by binary search. The numbers are
parsed by hand from a 4 KB buffer refilled with `fread`:
{1846_segment_tree_optimized.cpp}.

The optimized Go solution reads all operations first, sorts and
deduplicates their values and gives every distinct value one leaf with a
counter of its copies, instead of a leaf per addition and a map of leaf
slices. The leaf holds x while the counter is positive and 0 otherwise,
so the tree changes only when a value appears or disappears. An
operation is stored as one `int32`, +x or −x, which fits since x ≤ 10⁹,
and the tree and the counters are `int32` slices; the leaf of a value is
found by binary search. The numbers are parsed by hand from a `bufio`
reader instead of splitting the input into words:
{1846_segment_tree_optimized.go}.

The optimized Java solution reads all operations first with a hand
parser over a 64 KB buffer instead of `StreamTokenizer`. It numbers the
values by binary search in a sorted copy and keeps the leaves holding
each value as linked stacks in two `int` arrays, the top leaf of every
value and the leaf below every leaf, instead of a `HashMap` of
`ArrayDeque<Integer>`, so no number is boxed; every addition still has
its own leaf: {1846_segment_tree_optimized.java}.

The optimized Python solution reads the input in one batch and splits it into
lines, avoiding a buffered-stream call on every operation. Every distinct value
has one leaf and one multiplicity counter, so duplicate copies do not update
the tree. The tree and counters are integer lists rather than `array("I")`,
avoiding conversion of array cells on each access in the update loop. Values
are looked up once in the dictionary; answers are still written in batches of
1024. Use PyPy 3.10: the earlier streaming version submitted under CPython
exceeded the time limit: {1846_segment_tree_optimized.py}.

The optimized Rust solution reads all operations first and frees the
input text, sorts and deduplicates the values and gives every distinct
value one leaf with a counter of its copies, instead of a leaf per
addition and a `HashMap` of `Vec` stacks. The leaf holds x while the
counter is positive and 0 otherwise, so the tree changes only when a
value appears or disappears. An operation is stored as one `i32`,
+x or −x, which fits since x ≤ 10⁹, and the tree and the counters are
`u32`; the answers are written through a `BufWriter` instead of being
collected in a `String`: {1846_segment_tree_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1846_segment_tree_optimized.cpp`: time reduction +61.58%; memory
  reduction +75.57%; base: `1846_segment_tree.cpp`.

- `1846_segment_tree_optimized.go`: time reduction -19.23%; memory
  reduction +75.57%; base: `1846_segment_tree.go`.

- `1846_segment_tree_optimized.java`: time reduction +46.58%; memory
  reduction +50.17%; base: `1846_segment_tree.java`.

- `1846_segment_tree_optimized.py`: time reduction -6.00%; memory
  reduction +39.87%; base: `1846_segment_tree.py`.

- `1846_segment_tree_optimized.rs`: time reduction -69.57%; memory
  reduction +74.46%; base: `1846_segment_tree.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1846_segment_tree.cpp](1846_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(q log q log x) | AC | 0.203 s | 8612 KB | 11304079 |
| [1846_segment_tree.go](1846_segment_tree.go) | Go 1.14 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 14000 KB | 11290662 |
| [1846_segment_tree.java](1846_segment_tree.java) | Java 1.8 | segment_tree | O(q log q log x) | AC | 0.234 s | 20164 KB | 11305869 |
| [1846_segment_tree.py](1846_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(q log q log x) | AC | 0.250 s | 37060 KB | 11290667 |
| [1846_segment_tree.rs](1846_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(q log q log x) | AC | 0.046 s | 12328 KB | 11290670 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1846_segment_tree_optimized.cpp](1846_segment_tree_optimized.cpp) | G++ 13.2 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 2104 KB | 11305870 |
| [1846_segment_tree_optimized.go](1846_segment_tree_optimized.go) | Go 1.14 x64 | segment_tree | O(q log q log x) | AC | 0.093 s | 3420 KB | 11305877 |
| [1846_segment_tree_optimized.java](1846_segment_tree_optimized.java) | Java 1.8 | segment_tree | O(q log q log x) | AC | 0.125 s | 10048 KB | 11307314 |
| [1846_segment_tree_optimized.py](1846_segment_tree_optimized.py) | PyPy 3.10 x64 | segment_tree | O(q log q log x) | AC | 0.265 s | 22284 KB | 11307371 |
| [1846_segment_tree_optimized.rs](1846_segment_tree_optimized.rs) | Rust 1.75 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 3148 KB | 11305885 |
