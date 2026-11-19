# 1135. Counting the turns of recruits facing each other until the row is stable

[Timus 1135](https://acm.timus.ru/problem.aspx?space=1&num=1135) · difficulty 160 · math

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`1 ≤ N ≤ 30000` recruits stand in a row, each facing left (`<`) or right
(`>`). Every second, all pairs of neighbours facing each other (`><`)
turn around at once. Count the pair turns until nothing changes, or
print `NO` if it never stops.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then exactly `N` characters `<` and `>` spread over lines of up to
255 characters.

## Output

The number of pair turns.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
6
>><<><
```

Output:

```
7
```

## Solution

A turning pair `><` becomes `<>`: as far as the directions go, it is a
swap of two neighbours. Each such swap removes exactly one pair of
recruits (not necessarily neighbours) where a `>` stands before a `<`,
and creates none. The row is stable exactly when no `><` is left, that is
when every `<` stands before every `>`, which has no such pairs at all.
So the process always stops, `NO` is never printed, and the number of
turns equals the number of pairs with `>` before `<`. One pass counts
them: keep the number of `>` seen so far and add it at every `<`. `O(N)`.

Pitfalls:

- count pair turns, not elapsed seconds: test `01` has seven pair turns
  over four seconds;
- the row is split over several lines, possibly with empty ones, so read
  characters until `N` of them are found;
- the answer reaches `15000² = 2.25·10⁸`, still within 32 bits, but 64-bit
  counters cost nothing;
- the order of turns inside a second does not matter for the count.

The answers were compared with a second-by-second simulation on 200
random rows of up to 300 recruits.

## Optimized solutions

`1135_math_optimized.py`. Keep the count of earlier > symbols added for each <, consuming exactly N significant symbols and skipping separators. Read byte data without decoding or rebuilding a joined row. For this short PyPy job, disable optional JIT compilation to avoid paying for hot-loop traces, then flush and exit directly. The CPython fallback skips that optional runtime setting. O(I) time and space for I input bytes; the simple readable counting source remains.

Compared with `1135_math.py`: time 0.078 s → 0.125 s; memory 420 KB → 288 KB.

`1135_math_optimized.go`. Count every earlier > when reading <, consuming exactly N relevant symbols and skipping separators. Keep only the count and total, without storing the input string. For I input bytes, O(N+I) time and constant auxiliary space. Use bounded 256-byte input and 64-byte output buffers with Go 1.14 syscall.Read/Write, retrying EINTR and partial writes and handling zero-byte EOF. This removes fmt/bufio/os.File initialization overhead. Linux tests and Windows cross-builds establish functional/build checks; the paired memory figures below come from our own exact Windows judge Accepted. Preserve the readable teaching source.

Compared with `1135_math.go`: time 0.031 s → 0.031 s; memory 1100 KB → 332 KB.

The fast Java implementation keeps the same inversion count, but reads directly from a reusable 4 KB byte buffer instead of character readers. It skips line breaks while counting exactly `N` directions. Time remains `O(N)` and auxiliary storage is constant. The character-reader implementation remains the base version.

{1135_math_optimized.java}.

Source-matched Accepted runs: base 0.125 s / 532 KB; this version 0.078 s / 364 KB (submission 11307457). The rating target is met in the 2026-10-31 snapshot.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1135_math_optimized.java`: time reduction +37.60%; memory reduction
  +31.58%; base: `1135_math.java`.

`1135_math_optimized.rs`. Stream exactly N direction symbols, skipping whitespace. Count the right-facing symbols already seen; each new left-facing symbol contributes that many facing pairs. This counts every inversion once without retaining the row: O(N) time and O(1) working space under the line-length bound. Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1135_math.rs`: time 0.031 s → 0.015 s; memory 248 KB → 56 KB.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1135_math.cpp](1135_math.cpp).
- [1135_math.go](1135_math.go).
- [1135_math.rs](1135_math.rs).

- All languages skip the line breaks and keep the same running count.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1135_math.cpp](1135_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 132 KB | 11279403 |
| [1135_math.go](1135_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1100 KB | 11279405 |
| [1135_math.java](1135_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 532 KB | 11279408 |
| [1135_math.py](1135_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 420 KB | 11279406 |
| [1135_math.rs](1135_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 248 KB | 11279409 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1135_math_optimized.java](1135_math_optimized.java) | Java 1.8 | math | O(N) | AC | 0.078 s | 364 KB | 11307457 |
| [1135_math_optimized.rs](1135_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 56 KB | 11325144 |
| [1135_math_optimized.go](1135_math_optimized.go) \* | Go 1.14 x64 | math | O(N+I) time; O(1) space | AC | 0.031 s | 332 KB | 11325651 |
| [1135_math_optimized.py](1135_math_optimized.py) \* | PyPy 3.10 x64 | math | O(I) time; O(I) space | AC | 0.125 s | 288 KB | 11325852 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
