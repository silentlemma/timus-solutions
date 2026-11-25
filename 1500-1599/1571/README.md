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

## Checking

The repository uses a semantic checker and accepts any output satisfying these conditions. The checker requires the minimum interpreter count and distinct lowercase language pairs, with names of at most ten letters. Every pair of team languages must be connected through languages spoken by no other team. Impossible must agree with the expected feasibility result.

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

`1571_constructive_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1571_constructive.java`: time 0.156 s → 0.078 s; memory 1712 KB → 668 KB.

`1571_constructive_optimized.py`. Keep the same duplicate-language cases and minimum star construction through a language no team speaks. Generate one- and two-letter candidate names lazily instead of allocating all 702 names or importing string. The n<=100 promise guarantees an unused name. Keep language tokens as bytes and emit edges separately, flushing the text count before byte edges. Full split input and a language set remain: O(I) storage, not constant space. Time O(n) for bounded names plus the fixed candidate alphabet; retain the simple string-based source.

Compared with `1571_constructive.py`: time 0.078 s → 0.125 s; memory 548 KB → 212 KB.

The new C++, Go and Rust versions sort a bounded table of at most 100 names, each stored in 11 bytes including the zero terminator. Adjacent equal names detect duplicates. For at least three distinct teams, mark the occupied one- and two-letter names and choose an unused hub among 26+26² candidates; 100 teams cannot occupy them all. Connect every team to that unspoken language. This keeps the original private-interpreter construction and its optimal interpreter count, replacing sets/maps and temporary name lists with bounded storage. Sorting costs O(N log N), with name length bounded by ten; it is not an asymptotic improvement over hash-based bases. C++/Rust use C-runtime I/O, Go standard handles. All simple files remain; Java/Python reuse admitted bases.

The accepted base implementations [1571_constructive.java](1571_constructive.java), [1571_constructive.py](1571_constructive.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`1571_constructive_optimized.java`: time place 1/18, memory place 4/18 in this comparable sample.

`1571_constructive_optimized.py`: time place 18/18, memory place 1/18 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1571_constructive.cpp](1571_constructive.cpp) | G++ 13.2 x64 | constructive | O(N log N) | AC | 0.015 s | 436 KB | 11287792 |
| [1571_constructive.go](1571_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1144 KB | 11287793 |
| [1571_constructive.java](1571_constructive.java) \* | Java 1.8 | constructive | O(N) | AC | 0.156 s | 1712 KB | 11287796 |
| [1571_constructive.py](1571_constructive.py) \* | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 548 KB | 11287794 |
| [1571_constructive.rs](1571_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 444 KB | 11325605 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1571_constructive_sorting.cpp](1571_constructive_sorting.cpp) | G++ 13.2 x64 | constructive, sorting | O(N log N) | AC | 0.015 s | 128 KB | 11315139 |
| [1571_constructive_sorting.go](1571_constructive_sorting.go) \* | Go 1.14 x64 | constructive, sorting | O(N log N) | AC | 0.015 s | 304 KB | 11315142 |
| [1571_constructive_sorting.rs](1571_constructive_sorting.rs) | Rust 1.75 x64 | constructive, sorting | O(N log N) | AC | 0.031 s | 48 KB | 11315152 |
| [1571_constructive_optimized.java](1571_constructive_optimized.java) | Java 1.8 | constructive | O(N) | AC | 0.078 s | 668 KB | 11324818 |
| [1571_constructive_optimized.py](1571_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(n) under bounded names; O(I) space | AC | 0.125 s | 212 KB | 11325488 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
