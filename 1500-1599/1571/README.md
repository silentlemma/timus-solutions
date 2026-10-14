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
`O(N)`.

Pitfalls:

- two teams of one language need nobody, but three teams with a repeated
  language are impossible (tests 03, 05);
- a team may itself speak english, and a longer made-up name for the
  middle language is rejected (tests 06, 08);
- other answers are accepted, such as a triangle of direct pairs for
  three teams, so a checker verifies privacy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1571_constructive.cpp](1571_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 436 KB |
| [1571_constructive.go](1571_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1144 KB |
| [1571_constructive.java](1571_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.156 s | 1712 KB |
| [1571_constructive.py](1571_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 548 KB |
| [1571_constructive.rs](1571_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 456 KB |
