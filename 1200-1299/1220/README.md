# 1220. A thousand stacks in three quarters of a megabyte

[Timus 1220](https://acm.timus.ru/problem.aspx?space=1&num=1220) · difficulty 279 · implementation

Original problem by Pavel Atnashev, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Run up to `10⁵` operations on 1000 stacks: `PUSH A B` puts the number
`B ≤ 10⁹` on stack `A`, and `POP A` takes the top of stack `A` and prints
it. Every `POP` finds its stack non-empty. The memory limit is only
0.75 MB.

Time limit: 0.5 seconds. Memory limit: 0.75 MB.

## Input

`N`, then the operations, one per line.

## Output

The value of every `POP`, one per line, in order.

## Examples

### Example 1

Input:

```
7
PUSH 1 100
PUSH 1 200
PUSH 2 300
PUSH 2 400
POP 2
POP 1
POP 2
```

Output:

```
400
200
300
```

## Solution

Storing every pushed value with a pointer to the one below it would need
about 600 KB for `10⁵` values, too close to the limit once the program
itself is counted, and a separate array per stack would waste space on
the empty ones.

So every stack is a chain of blocks of 10 values, the newest block first,
and every block remembers the next older block of the same stack. A
stack's size tells how full its newest block is, so no per-block counter
is needed: a push into a full block (or an empty stack) takes a block
from a free list, and a pop that empties the newest block gives it back.
Only the newest block of each stack can be partly full, so at most
`10⁵/10 + 1000` blocks are ever in use, about 460 KB in total. Small
fixed buffers for reading and writing keep the input and output fast
without much memory. `O(N)`.

Pitfalls:

- the C++ streams library alone costs noticeable memory, so the program
  reads and writes through `fread` and `fwrite`;
- a block must be returned as soon as it empties, or a stack that grows
  and shrinks again and again would exhaust the pool;
- 16-bit block numbers are enough, since there are fewer than 32,768
  blocks.

The output was compared with a plain list-based simulation on every test,
including 100,000 operations of several kinds.

## Language notes

- Timus accepts this problem only in C, C++ and Pascal, so only the C++
  solution is given.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1220_implementation.cpp](1220_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 540 KB |
