# 1574. Mathematicians and Brackets

[Timus 1574](https://acm.timus.ru/problem.aspx?space=1&num=1574) · difficulty 353 · strings

Original problem by Alexander Toropov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a non-empty line of up to 100000 brackets, count the cyclic shifts, by 0 to
n − 1 characters, that turn it into a correct bracket sequence. Shifts
by different amounts count separately even when they give the same line.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The line of brackets.

## Output

The number of such shifts.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
)(()
```

Output:

```
1
```

### Example 2

Input:

```
)()(
```

Output:

```
2
```

### Example 3

Input:

```
()
```

Output:

```
1
```

## Solution

If the numbers of opening and closing brackets differ, no shift works.
Otherwise take the balance after each prefix: opening brackets minus
closing ones. A shift that starts right after position i changes every
balance by −p(i), where p(i) is the balance there, so it never goes
below zero exactly when p(i) is the lowest balance of all. The answer is
the number of prefixes whose balance equals that minimum. `O(n)`.

Pitfalls:

- a line such as `)()(` gives the same correct line by two different
  shifts, and both count (the second example);
- the shift by zero counts too (the third example);
- an unbalanced line has no answer but 0, even when a shift keeps every
  balance non-negative (tests 04, 05).

## Optimized solutions

`1574_strings_optimized.java`. Count occurrences of the minimum prefix balance online, and return zero unless the final balance is zero. For a balanced string the minimum is nonpositive, so initializing lowest=0 without counting the empty prefix gives the same cyclic-shift count. Java reads bracket bytes directly and needs only fixed input storage rather than retaining the line. Python removes the list of all prefix sums but still reads the whole byte string: its total storage remains O(n), while Java auxiliary storage is O(1). Both take O(n) time. The Python variant flushes its answer before os._exit(0); that runtime change does not change the algorithmic bound.

Compared with `1574_strings.java`: time 0.125 s → 0.125 s; memory 1196 KB → 480 KB.

`1574_strings_optimized.py`. Count occurrences of the minimum prefix balance online, and return zero unless the final balance is zero. For a balanced string the minimum is nonpositive, so initializing lowest=0 without counting the empty prefix gives the same cyclic-shift count. Java reads bracket bytes directly and needs only fixed input storage rather than retaining the line. Python removes the list of all prefix sums but still reads the whole byte string: its total storage remains O(n), while Java auxiliary storage is O(1). Both take O(n) time. The Python variant flushes its answer before os._exit(0); that runtime change does not change the algorithmic bound.

Compared with `1574_strings.py`: time 0.093 s → 0.14 s; memory 5252 KB → 1 412 KB.

The C++, Go and Rust variants count occurrences of the minimum prefix balance while reading the input. When a lower balance appears, reset the count to one. Count the prefixes of lengths 1 through n. When the final balance is zero, the length-n prefix replaces the empty prefix and the two represent the same cyclic cut. C++ uses buffered standard I/O, Go reads fixed-size blocks and Rust reads through the standard input buffer. Each takes O(n) time and O(1) extra space.

The accepted base implementations [1574_strings.java](1574_strings.java), [1574_strings.py](1574_strings.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1574_strings_optimized.java`: time place 13/22, memory place 2/22 in this comparable sample.

`1574_strings_optimized.py`: time place 28/45, memory place 25/45 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1574_strings.cpp](1574_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 500 KB | 11287829 |
| [1574_strings.go](1574_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1768 KB | 11287832 |
| [1574_strings.java](1574_strings.java) \* | Java 1.8 | strings | O(n) | AC | 0.125 s | 1196 KB | 11287835 |
| [1574_strings.py](1574_strings.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 5252 KB | 11287834 |
| [1574_strings.rs](1574_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 2068 KB | 11287836 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1574_strings_optimized.cpp](1574_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 88 KB | 11310381 |
| [1574_strings_optimized.go](1574_strings_optimized.go) \* | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 824 KB | 11310380 |
| [1574_strings_optimized.rs](1574_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 208 KB | 11310379 |
| [1574_strings_optimized.java](1574_strings_optimized.java) \* | Java 1.8 | strings | O(n) | AC | 0.125 s | 480 KB | 11325019 |
| [1574_strings_optimized.py](1574_strings_optimized.py) \* | PyPy 3.10 x64 | strings | O(n) | AC | 0.14 s | 1412 KB | 11325071 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
