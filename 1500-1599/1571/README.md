# 1571. Interpreters

[Timus 1571](https://acm.timus.ru/problem.aspx?space=1&num=1571) · difficulty 451 · constructive

Original problem by Sergey Pupyrev, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 100 building teams each speak one language. An interpreter knows any
two languages. Every two teams must be able to talk, and no other team
may understand their talk. Print the fewest interpreters with their
languages as `lang1-lang2`, or `Impossible`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the language of each team.

## Output

The number of interpreters and their language pairs, or `Impossible`.
Any best set is accepted.

## Examples

### Example 1

Input:

```
3
russian
french
german
```

Output:

```
3
russian-english
english-german
english-french
```

## Solution

If two teams share a language, a third team, if there is one, cannot
talk to the first without the second understanding; with only those two
teams nobody is needed. Otherwise let the k languages be different. One
team needs nobody, and two teams need one interpreter for their two
languages.

For k ≥ 3, a talk that passes through another team's language is
overheard by that team, so between any two teams the interpreters must
form a chain whose inner languages no team speaks. If the interpreters
used only the teams' languages, they would form a connected graph on
those k languages, and with only k − 1 edges it would be a tree, where
some chain passes through a third language. So k interpreters are
needed, and k suffice: each team's language paired with one language
nobody speaks, such as english. If a team speaks english, the middle
language is the first free name of one or two letters: the output
languages must also have at most ten letters, and 100 teams cannot
take all 702 such names.
`O(N log N)` in C++; `O(N)` on average in the other languages.

Pitfalls:

- two teams of one language need nobody, but three teams with a repeated
  language are impossible (tests 03, 05);
- a team may itself speak english, so the middle language must be one
  no team speaks (tests 06, 08);
- other answers are accepted, such as a triangle of direct pairs for
  three teams, so a checker verifies privacy.

## Optimized solutions

The new C++, Go and Rust versions sort a bounded table of at most 100 names, each stored in 11 bytes including the zero terminator. Adjacent equal names detect duplicates. For at least three distinct teams, mark the occupied one- and two-letter names and choose an unused hub among 26+26² candidates; 100 teams cannot occupy them all. Connect every team to that unspoken language. This keeps the original private-interpreter construction and its optimal interpreter count, replacing sets/maps and temporary name lists with bounded storage. Sorting costs O(N log N), with name length bounded by ten; it is not an asymptotic improvement over hash-based bases. C++/Rust use C-runtime I/O, Go standard handles. All simple files remain; Java/Python reuse admitted bases.

The accepted base implementations [1571_constructive.java](1571_constructive.java), [1571_constructive.py](1571_constructive.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1571_constructive.cpp](1571_constructive.cpp) | G++ 13.2 x64 | constructive | O(N log N) | AC | 0.015 s | 436 KB | 11287792 |
| [1571_constructive.go](1571_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1144 KB | 11287793 |
| [1571_constructive.java](1571_constructive.java) \* | Java 1.8 | constructive | O(N) | AC | 0.156 s | 1712 KB | 11287796 |
| [1571_constructive.py](1571_constructive.py) \* | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 548 KB | 11287794 |
| [1571_constructive.rs](1571_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 456 KB | 11287797 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1571_constructive_sorting.cpp](1571_constructive_sorting.cpp) | G++ 13.2 x64 | constructive, sorting | O(N log N) | AC | 0.015 s | 128 KB | 11315139 |
| [1571_constructive_sorting.go](1571_constructive_sorting.go) \* | Go 1.14 x64 | constructive, sorting | O(N log N) | AC | 0.015 s | 304 KB | 11315142 |
| [1571_constructive_sorting.rs](1571_constructive_sorting.rs) \* | Rust 1.75 x64 | constructive, sorting | O(N log N) | AC | 0.031 s | 48 KB | 11315152 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
