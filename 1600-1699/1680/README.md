# 1680. The First Nonqualifying

[Timus 1680](https://acm.timus.ru/problem.aspx?space=1&num=1680) · difficulty 224 · strings

Original problem by Dmitry Ivankov, prepared by Alexander Ipatov, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A semifinal sends q teams to the finals, at most one per university:
every team that finished below another team of its own university is
struck out of the standings. Print the team that ends up in place
q + 1 after the strike-outs.

## Input

The year, n (n ≤ 201) and q (3 ≤ q ≤ 12), then the n teams in the
order of their places. A team is written as the university name, a
space, '#' and its number from 1 to 8; a university with a single team
may be written without the number. Names consist of Latin letters,
spaces, '.', '-' and '&', at most 36 characters, and two universities
never differ only in letter case. The answer exists.

## Output

The name of that team, as written in the standings.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
1999 10 6
St Petersburg SU #1
Belarusian SU #1
Moscow SU #4
Southern Ural SU
Moscow SU #1
Novosibirsk SU #1
St Petersburg SU #3
Belarusian SU #3
St Petersburg IFMO #1
Ural SU #3
```

Output:

```
Ural SU #3
```

## Solution

Walk down the standings, keeping the set of universities that already
have a team in the list. The university of a team is the text before
its last '#', with the trailing space dropped, or the whole line when
there is no '#'. Since two universities never differ only in case,
names are compared in lower case. A team of an already present
university is skipped; otherwise, if the set already holds q
universities, this team is the answer, and if not, its university joins
the set. `O(n · L)` for names of length L.

Pitfalls:

- the same university can appear in different letter cases ("Ural SU"
  and "URAL SU", test 02), so compare names without case;
- compare whole names: "Ural SU" and "Ural SU State" are different
  universities (test 03);
- print the team exactly as given, number included.

The answers match an independent accepted implementation.

## Optimized solutions

The selection rule remains the first team from each university, with case-insensitive university identity and original team spelling in output. Stop retaining new university keys once the output quota is full. Streaming the prescribed records removes the full input-line list and unnecessary copies. The selected PyPy implementation keeps Unicode handling, so storage optimizations do not silently change case conversion or output encoding.

- `1680_strings_optimized.cpp`: 0.001 s / 100 KB; base `1680_strings.cpp`: 0.001 s / 400 KB; relative change: time -0.0%, memory -75.0%.
- `1680_strings_optimized.py`: 0.125 s / 244 KB; base `1680_strings.py`: 0.078 s / 364 KB; relative change: time +60.3%, memory -33.0%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1680_strings.cpp`; covering source `1680_strings_optimized.cpp`; time/memory places 1/1, other-author entries 47/47.

- Go: preferred teaching base `1680_strings.go`; covering source `1680_strings.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1680_strings.java`; covering source `1680_strings.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1680_strings.py`; covering source `1680_strings_optimized.py`; time/memory places 11/1, other-author entries 12/12.

- Rust: preferred teaching base `1680_strings.rs`; covering source `1680_strings.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1680_strings.cpp](1680_strings.cpp) | G++ 13.2 x64 | strings | O(n · L) | AC | 0.001 s | 400 KB | 11308838 |
| [1680_strings.go](1680_strings.go) | Go 1.14 x64 | strings | O(n · L) | AC | 0.015 s | 1088 KB | 11288810 |
| [1680_strings.java](1680_strings.java) | Java 1.8 | strings | O(n · L) | AC | 0.078 s | 472 KB | 11288813 |
| [1680_strings.py](1680_strings.py) | Python 3.12 x64 | strings | O(n · L) | AC | 0.078 s | 364 KB | 11308839 |
| [1680_strings.rs](1680_strings.rs) | Rust 1.75 x64 | strings | O(n · L) | AC | 0.015 s | 432 KB | 11288816 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1680_strings_optimized.cpp](1680_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(input size) | AC | 0.001 s | 100 KB | 11308250 |
| [1680_strings_optimized.py](1680_strings_optimized.py) \* | PyPy 3.10 x64 | strings | O(input size) | AC | 0.125 s | 244 KB | 11309387 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
