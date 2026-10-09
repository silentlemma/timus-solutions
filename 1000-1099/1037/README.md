# 1037. Memory blocks that expire

[Timus 1037](https://acm.timus.ru/problem.aspx?space=1&num=1037) · difficulty 1170 · simulation

Original problem by Alexander Klepinin, from the Fifth Ural State University Team Programming Championship, October 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Simulate a memory manager with `30000` blocks numbered from 1. At first
every block is free. Requests come in order of non-decreasing time:

- an **allocation** takes the free block with the smallest number;
- an **access** to block `b` succeeds if `b` is taken, and fails otherwise.

A successful access or an allocation at time `t` keeps the block taken
until time `t + 600`: at that moment, if no other successful request to it
came, it becomes free again. There are at most 80000 requests, times are
integers from 0 to 65000, and there is always a free block for an
allocation.

Time limit: 0.4 seconds. Memory limit: 64 MB.

## Input

One request per line: `T +` is an allocation at time `T`, `T . B` is an
access to block `B` (`1 ≤ B ≤ 30000`) at time `T`.

## Output

For every request, in order: the number of the allocated block, or `+` /
`-` for a successful / failed access.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
1 +
1 +
1 +
2 . 2
2 . 3
3 . 30000
601 . 1
601 . 2
602 . 3
602 +
602 +
1202 . 2
```

Output:

```
1
2
3
+
+
-
-
+
-
1
3
-
```

### Example 2

Input:

```
0 +
0 +
300 . 1
599 . 2
600 . 2
900 . 1
900 +
900 . 1
1199 +
1200 +
```

Output:

```
1
2
+
+
+
-
1
+
3
2
```

## Solution

Keep for every block whether it is taken and its expiry time. Before
handling a request at time `t`, release all blocks whose expiry is `≤ t`.

Since the times never decrease, every new expiry `t + 600` is at least as
large as all earlier ones, so the expiries can be kept in a plain FIFO
queue in the order they were set. An access does not remove the old entry
of its block; such an entry is stale and is recognised when it reaches the
front: the block's current expiry is different, or the block is already
free. A released block goes into a min-heap of free blocks.

An allocation takes the top of the heap; if the heap is empty, it takes
the next never used block (`1, 2, 3, ...`) — all of them are larger than
any freed block. An access answers `+` if the block is taken and then
moves its expiry. Every request pushes at most one queue entry and one
heap entry, so the total is `O(Q log Q)` for `Q` requests.

Pitfalls:

- the block becomes free exactly at `t + 600`: a request at that moment
  already sees it free;
- a failed access does not take the block and does not change anything;
- several requests at the same time must be handled in input order, and
  blocks released at the same moment are reused from the smallest;
- a block accessed twice at the same moment has two equal queue entries:
  release it only once.

An alternative is a segment tree over the blocks with the minimum of the
expiry times: the first block with expiry `≤ t` is the smallest free one.
The tests were checked with it.

## Language notes

- **C++**, **Rust**: standard priority queues and queues.
- **Go**: a small hand-written heap and a slice as the queue; input is read
  with `bufio.Scanner` by words.
- **Java**: a byte-level input reader, since `StreamTokenizer` would read
  `.` as a number; `PriorityQueue` and two arrays as the queue.
- **Python**: `heapq` and `deque`; the whole input is read at once.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1037_simulation.cpp](1037_simulation.cpp) | G++ 13.2 x64 | simulation | O(Q log Q) | AC | 0.093 s | 984 KB |
| [1037_simulation.go](1037_simulation.go) | Go 1.14 x64 | simulation | O(Q log Q) | AC | 0.031 s | 7772 KB |
| [1037_simulation.java](1037_simulation.java) | Java 1.8 | simulation | O(Q log Q) | AC | 0.140 s | 6620 KB |
| [1037_simulation.py](1037_simulation.py) | Python 3.12 x64 | simulation | O(Q log Q) | AC | 0.171 s | 16500 KB |
| [1037_simulation.rs](1037_simulation.rs) | Rust 1.75 x64 | simulation | O(Q log Q) | AC | 0.046 s | 3180 KB |
