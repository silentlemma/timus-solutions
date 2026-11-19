# 1370. Magician

[Timus 1370](https://acm.timus.ru/problem.aspx?space=1&num=1370) · difficulty 89 · implementation

Original problem by Stanislav Vasiliev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A wheel carries N digits, 11 ≤ N ≤ 1000, around its rim, and a window
shows 10 consecutive ones, at first digits 1 to 10. Every click turns
the wheel by one digit, so after one click the window shows digits 2 to
11. Given M clicks (1 ≤ M ≤ 32 767), print the 10 digits in the window.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then the N digits, one per line.

## Output

The 10 digits in the window, leading zeros included.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
12 7
1
2
3
4
5
6
7
8
9
0
7
7
```

Output:

```
8907712345
```

## Solution

After M clicks the window starts at digit M (counting from 0), and the
wheel wraps around, so the answer is digits (M + i) mod N for
i = 0 … 9. `O(1)` after reading the input.

Pitfalls:

- M can be many times larger than N (test 05);
- the window can wrap past the last digit (example);
- the answer is printed as digits, with its leading zeros (test 03).

## Optimized solutions

The optimized Java solution parses the numbers by hand instead of
`Scanner`, keeps the digits as bytes and writes the ten digits of the
window as one byte array: 0.093 s instead of 0.125 s and 340 KB instead
of 1892 KB.

The optimized C++ solution reads the digits as characters into a fixed
array and prints the ten of them with `putchar`, with no conversion to
numbers and no `std::string`: 120 KB instead of 196 KB, with the same
time.

`1370_implementation_optimized.py`. Reduce the rotation to start=M mod N. While reading digit i, store it only if offset=(i-start) mod N is below ten, at that output offset. Since N>=11, these ten offsets are distinct and each is filled once. This preserves wraparound and leading zeros while dropping the stored wheel. O(N) time and ten output bytes. Use a bytearray of ten positions and the bounded 65536-byte chunk tokenizer. Parser token/block storage remains, but no N-element digit list is retained; only the ten-byte answer is decoded. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1370_implementation.py`: time 0.062 s → 0.14 s; memory 404 KB → 244 KB.

`1370_implementation_optimized.rs`. Reduce the rotation to start=M mod N. While reading digit i, store it only if offset=(i-start) mod N is below ten, at that output offset. Since N>=11, these ten offsets are distinct and each is filled once. This preserves wraparound and leading zeros while dropping the stored wheel. O(N) time and ten output bytes. Use a fixed ten-byte array and O(1) numeric state; emit digits as ASCII bytes with no output String. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1370_implementation.rs`: time 0.015 s → 0.015 s; memory 244 KB → 52 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1370_implementation_optimized.py`: time place 170/179, memory place 1/179 in this comparable sample.

`1370_implementation_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1370_implementation.cpp](1370_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11285595 |
| [1370_implementation.go](1370_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB | 11285596 |
| [1370_implementation.java](1370_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 1892 KB | 11285599 |
| [1370_implementation.py](1370_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 404 KB | 11285597 |
| [1370_implementation.rs](1370_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 244 KB | 11285600 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1370_implementation_optimized.cpp](1370_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 120 KB | 11303744 |
| [1370_implementation_optimized.java](1370_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 340 KB | 11303603 |
| [1370_implementation_optimized.py](1370_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N) | AC | 0.14 s | 244 KB | 11325069 |
| [1370_implementation_optimized.rs](1370_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 52 KB | 11324865 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
