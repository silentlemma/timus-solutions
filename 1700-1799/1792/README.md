# 1792. Hamming Code

[Timus 1792](https://acm.timus.ru/problem.aspx?space=1&num=1792) · difficulty 84 · implementation

Original problem by Sofia Tekhazheva (prepared by Olga Soboleva), from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Four overlapping disks hold a bit each, and three petals, the regions
shared by three disks, hold the parity of the sum over the disks that
cover them. In the order of the figure in the statement, petal j lies
in every disk except disk j, and the fourth disk covers all three
petals. At most one of the seven bits was changed. Restore a valid
code.

## Input

Seven bits: the four disks, then the three petals.

## Output

The seven bits of a valid code that differs from the input in at most
one place.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant. Print the seven recovered bits in their original order.

## Examples

### Example 1

Input:

```
0 1 0 1 1 0 1
```

Output:

```
0 1 0 0 1 0 1
```

### Example 2

Input:

```
1 1 1 1 1 1 1
```

Output:

```
1 1 1 1 1 1 1
```

## Solution

Check the word as given: petal j must equal the sum of the disks other
than disk j, modulo 2. If it fails, try changing each of the seven bits
in turn and keep the first change that makes the word valid. Two valid
words always differ in at least three places, so the answer is unique.
`O(1)`.

In the first example all three petals are wrong, and only the fourth
disk lies under all of them; changing it from 1 to 0 makes the petals
1, 0, 1, as written.

Pitfalls:

- a wrong petal may be the changed bit itself, not a disk;
- the word may already be valid, and then it is printed unchanged.

Every one of the 128 possible inputs gives the same answer as an
independent accepted implementation.

## Optimized solutions

`1792_bitmask_optimized.py`. Keep the syndrome decoder, packing the seven input bits into one integer. Three masks derived from the parity definitions use bit_count modulo two; the nonzero syndrome identifies the unique erroneous data/check column. Flip that bit and fill a 14-byte output template. The masks encode parity equations, not a table of answers. Logical word work is O(1); reading/splitting input of textual length L costs O(L) time/storage. Raw output and os._exit(0) inside main reduce startup/teardown overhead. All 128 possible received words were independently checked from the 16 valid codewords and zero/one-bit errors. The earlier smaller-memory PyPy decoder and the simple seven-value implementation remain.

Exact-source Python 3.12 x64 Accepted #11327532: 0.078 s / 828 KB. Saved 2026-11-20 compiler-cohort ranks, time then memory: 1/69; 68/69. Strict admission uses time only below 1024 KB: top ten or top 15%, ties share rank and percentage cutoff rounds up. An asterisk remains for the separate first-place-in-both language target. The preserved previous variant has its own paired receipt #11325479 (PyPy 3.10 x64): 0.14 s / 264 KB; do not mix measurements or runtimes. All teaching sources remain unchanged.

- `1792_bitmask_optimized.py`: 0.078 s / 828 KB; retained teaching base `1792_implementation.py` (Python 3.12 x64): 0.093 s / 464 KB.

`1792_bitmask.py`. Decode the three parity checks as a syndrome instead of constructing and testing eight seven-bit candidates. A single set syndrome bit identifies a parity bit; syndrome 7 identifies data bit 3; the remaining two-bit syndromes identify the other data bits by their missing check. Under the promised at-most-one error, flip that bit or leave a zero syndrome unchanged. This different bitmask method has its own filename; retain the simple candidate-enumeration source. Both methods have constant size for seven bits. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `1792_implementation.py`: time 0.093 s → 0.14 s; memory 464 KB → 264 KB.

The optimized solutions (C++, Java) read the seven bits as single
characters with `getchar` and `System.in.read` instead of `iostream` and
`Scanner`, and write the answer character by character (C++) or as one
byte array (Java). The search over single changes is the same.
C++: 84 KB instead of 396 KB, with the same time; Java: 0.109 s instead
of 0.156 s and 380 KB instead of 1604 KB.

`1792_bitmask.rs`. Replace trial changes with a three-bit parity syndrome. A flipped bit toggles precisely its parity-check column; the seven columns are the distinct nonzero three-bit patterns. A zero syndrome needs no change; otherwise flip the unique bit with that column. With at most one error this restores all checks. One fixed seven-byte word replaces cloned candidate vectors; time and space are O(1). Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1792_implementation.rs`: time 0.046 s → 0.046 s; memory 228 KB → 60 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1792_bitmask.py`: time place 63/69, memory place 2/69 in this comparable sample.

`1792_bitmask.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1792_implementation.cpp](1792_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 396 KB | 11303512 |
| [1792_implementation.go](1792_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1168 KB | 11289857 |
| [1792_implementation.java](1792_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1604 KB | 11303513 |
| [1792_implementation.py](1792_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 464 KB | 11303514 |
| [1792_implementation.rs](1792_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB | 11303515 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1792_implementation_optimized.cpp](1792_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 84 KB | 11303639 |
| [1792_implementation_optimized.java](1792_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 380 KB | 11303516 |
| [1792_bitmask.rs](1792_bitmask.rs) \* | Rust 1.75 x64 | bitmask | O(1) | AC | 0.046 s | 60 KB | 11324860 |
| [1792_bitmask.py](1792_bitmask.py) \* | PyPy 3.10 x64 | bitmask | O(1) | AC | 0.14 s | 264 KB | 11325479 |
| [1792_bitmask_optimized.py](1792_bitmask_optimized.py) \* | Python 3.12 x64 | bitmask | O(1) logical work; O(L) input time/storage | AC | 0.078 s | 828 KB | 11327532 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
