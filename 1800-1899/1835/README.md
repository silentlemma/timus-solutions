# 1835. Swamp Doctor

[Timus 1835](https://acm.timus.ru/problem.aspx?space=1&num=1835) · difficulty 3122 · strings

Original problem by Alexey Samsonov (prepared by Dmitry Ivankov and Ivan Burmistrov), from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An address is a user name and a domain joined by "@", each a non-empty
string of lowercase letters and dots that neither starts nor ends with
a dot and has no two dots in a row. Count the distinct addresses that
occur as substrings of a text.

## Input

The text, at most 10⁶ bytes of characters with codes 32 to 126 and line
breaks.

## Output

The number of distinct addresses in the text.

## Examples

### Example 1

Input:

```
a.b@c.d
b@c.de.
@qq
q@.q
```

Output:

```
5
```

## Solution

Whether a string is an address depends on the string alone, not on
where it occurs. So the classic way of counting distinct substrings
works with a filter: build the suffix array and the LCP of each suffix
with the one before it in sorted order. A prefix of a suffix appears
earlier in that order exactly when it is no longer than this LCP, so
each distinct address is counted once, at the first suffix starting
with it, by counting only its address prefixes longer than the LCP.

For a suffix starting at a letter, its address prefixes are fixed by
the first "@" after it in the same stretch of letters and dots. The
user part must not reach back past the last "..", the "@" must have
letters on both sides, and the domain ends at a letter before the next
"..", "@" or other character. All of this is precomputed per "@", so
each suffix adds a count of letters in a range, by prefix sums.

The suffix array comes from cyclic prefix doubling with counting sort
over a 30-letter alphabet in which every other character is one code;
the LCPs come from Kasai's algorithm. `O(n log n)`.

In the example the addresses are a.b@c, a.b@c.d, b@c, b@c.d and
b@c.de; b@c and b@c.d occur twice but count once.

Pitfalls:

- the same address may occur many times, so counting occurrences
  overcounts;
- "a..b@c" still holds the address b@c, but not a..b@c or .b@c;
- a single "@" between two runs of 5·10⁵ letters gives about 2.5·10¹¹
  addresses, which needs 64-bit integers;
- CPython is far too slow for a suffix array of 10⁶ characters; the
  Python solution runs on PyPy and keeps its arrays compact.

The answers agree with a check of every substring for hundreds of short
random texts and with an independent accepted implementation on texts
of a megabyte.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1835_strings.cpp](1835_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.734 s | 40808 KB |
| [1835_strings.go](1835_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.765 s | 41108 KB |
| [1835_strings.java](1835_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.703 s | 40628 KB |
| [1835_strings.py](1835_strings.py) | PyPy 3.10 x64 | strings | O(n log n) | AC | 1.218 s | 51268 KB |
| [1835_strings.rs](1835_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.718 s | 49896 KB |
