# 1737. Mnemonics and Palindromes 3

[Timus 1737](https://acm.timus.ru/problem.aspx?space=1&num=1737) · difficulty 254 · strings

Original problem by Alexander Ipatov, from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

List, in alphabetical order, all words of length n over the letters a,
b and c that have no palindromic substring of two or more letters. If
they would take more than 100 000 letters in total, print `TOO LONG`.

## Input

n (1 ≤ n ≤ 20 000).

## Output

The words, one per line, or `TOO LONG`.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
2
```

Output:

```
ab
ac
ba
bc
ca
cb
```

## Solution

A palindrome of two or more letters has a palindrome of two or three
letters in its middle, so it is enough that no two neighbouring
letters are equal and no two letters one apart are equal. Then any
three letters in a row are a, b and c in some order, and each letter
repeats the one three places back: the word is one of the six orders
of a, b and c repeated. So there are three words for n = 1 and six for
every longer n, and the answer is `TOO LONG` when 6n > 100 000, that is
from n = 16 667 on. `O(n)`.

Pitfalls:

- for n = 1 the six orders give only three different words;
- the limit is on the total length, not on the number of words.

The lists match all words over a, b and c checked one by one for n up
to 9.

## Optimized solutions

For a length of at least two, the first two distinct letters uniquely determine a valid periodic word. Iterate those pairs in alphabetic order: this directly emits the six words in lexicographic order without a set, deduplication or sorting. The single-letter case emits three words separately. Determine whether the output would be too long before constructing it, then write bounded blocks rather than keeping all words and a joined output string.

- `1737_strings_optimized.cpp`: 0.031 s / 112 KB; base `1737_strings.cpp`: 0.031 s / 232 KB; relative change: time -0.0%, memory -51.7%.
- `1737_strings_optimized.go`: 0.015 s / 964 KB; base `1737_strings.go`: 0.031 s / 1448 KB; relative change: time -51.6%, memory -33.4%.
- `1737_strings_optimized.java`: 0.093 s / 388 KB; base `1737_strings.java`: 0.109 s / 3016 KB; relative change: time -14.7%, memory -87.1%.
- `1737_strings_optimized.py`: 0.093 s / 444 KB; base `1737_strings.py`: 0.109 s / 980 KB; relative change: time -14.7%, memory -54.7%.
- `1737_strings_optimized.rs`: 0.015 s / 196 KB; base `1737_strings.rs`: 0.015 s / 328 KB; relative change: time -0.0%, memory -40.2%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1737_strings.cpp`; covering source `1737_strings_optimized.cpp`; time/memory places 42/1, other-author entries 48/48.

- Go: preferred teaching base `1737_strings.go`; covering source `1737_strings.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1737_strings.java`; covering source `1737_strings_optimized.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1737_strings.py`; covering source `1737_strings_optimized.py`; time/memory places 5/7, other-author entries 15/15.

- Rust: preferred teaching base `1737_strings.rs`; covering source `1737_strings.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1737_strings.cpp](1737_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 232 KB | 11308913 |
| [1737_strings.go](1737_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1448 KB | 11289457 |
| [1737_strings.java](1737_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 3016 KB | 11308916 |
| [1737_strings.py](1737_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.109 s | 980 KB | 11308917 |
| [1737_strings.rs](1737_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 328 KB | 11289460 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1737_strings_optimized.cpp](1737_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(output size) | AC | 0.031 s | 112 KB | 11308823 |
| [1737_strings_optimized.go](1737_strings_optimized.go) | Go 1.14 x64 | strings | O(output size) | AC | 0.015 s | 964 KB | 11308824 |
| [1737_strings_optimized.java](1737_strings_optimized.java) | Java 1.8 | strings | O(output size) | AC | 0.093 s | 388 KB | 11308825 |
| [1737_strings_optimized.py](1737_strings_optimized.py) \* | Python 3.12 x64 | strings | O(output size) | AC | 0.093 s | 444 KB | 11308821 |
| [1737_strings_optimized.rs](1737_strings_optimized.rs) | Rust 1.75 x64 | strings | O(output size) | AC | 0.015 s | 196 KB | 11308826 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
