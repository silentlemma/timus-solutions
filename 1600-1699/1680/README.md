# 1680. The First Nonqualifying

[Timus 1680](https://acm.timus.ru/problem.aspx?space=1&num=1680) · difficulty 223 · strings

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1680_strings.cpp](1680_strings.cpp) | G++ 13.2 x64 | strings | O(n · L) | AC | 0.015 s | 420 KB |
| [1680_strings.go](1680_strings.go) | Go 1.14 x64 | strings | O(n · L) | AC | 0.015 s | 1088 KB |
| [1680_strings.java](1680_strings.java) | Java 1.8 | strings | O(n · L) | AC | 0.078 s | 472 KB |
| [1680_strings.py](1680_strings.py) | Python 3.12 x64 | strings | O(n · L) | AC | 0.078 s | 456 KB |
| [1680_strings.rs](1680_strings.rs) | Rust 1.75 x64 | strings | O(n · L) | AC | 0.015 s | 432 KB |
