# 1220. A thousand stacks in three quarters of a megabyte

[Timus 1220](https://acm.timus.ru/problem.aspx?space=1&num=1220) · difficulty 281 · implementation

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

## Checking

Compare the exact answer tokens; whitespace formatting is immaterial.

- `1220_implementation_optimized.rs` (Rust 1.75 x64): 13 repository cases; 8 additional source-bound comparisons.

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

Storing every pushed value with a 32-bit link to the one below it would need
about 800 KB for `10⁵` values, already over the memory limit, and a
separate array per stack would waste space on the empty ones.

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

## Optimized solutions

Only C++ and Rust are judge-supported here; preserve both simple sources. The compact Rust still implements ordinary LIFO stacks, but chains blocks of eight values instead of retaining a per-stack allocation. Since every value is at most10^9<2^30, eight values occupy30bytes. A u16 link points to the preceding block; empty blocks enter a free list and are reused. At most1000top blocks are partial, while full blocks contain eight live values, so100000/8+1000+1slots suffice and fit u16 indices. Push/pop touch a bounded four/five-byte window and preserve neighbouring packed cells. Fixed global storage and bounded C-ABI input/output avoid heap and unused startup facilities. Total time O(Q), storage O(Q+S) for S=1000stacks. The exact source passed thirteen repository cases and eight independent stress inputs, including100000operations and block reuse.

- `1220_implementation_optimized.rs`: 0.031 s / 436 KB; base `1220_implementation.rs`: 0.031 s / 672 KB; relative change: time -0.0%, memory -35.1%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1220_implementation.cpp`; covering source `1220_implementation.cpp`; time/memory places 1/4, other-author entries 55/55.

- Rust: preferred teaching base `1220_implementation.rs`; covering source `1220_implementation_optimized.rs`; time/memory places 1/1, other-author entries 2/2.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1220_implementation.cpp](1220_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 540 KB | 11283689 |
| [1220_implementation.rs](1220_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 672 KB | 11286809 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1220_implementation_optimized.rs](1220_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(Q) time; O(Q+S) bounded storage | AC | 0.031 s | 436 KB | 11309741 |
