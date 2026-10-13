# 1382. Game with Cards

[Timus 1382](https://acm.timus.ru/problem.aspx?space=1&num=1382) · difficulty 1697 · graphs

Original problem by Alexander Ipatov, with special thanks to Dmitry Ivankov, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 1000 friends take one card each, numbered 1 to N, in secret. Then
friend i makes two statements: "I have card aᵢ" and "friend bᵢ has card
cᵢ", with bᵢ ≠ i. Exactly one of the two is true. No two friends make
the same claim about the same person, and nobody gives a friend the
card that friend claims. Print for each friend which statement, 1 or 2,
is true; a solution exists.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then N lines aᵢ, bᵢ, cᵢ.

## Output

N numbers 1 or 2. Any consistent answer is accepted.

## Examples

### Example 1

Input:

```
5
3 4 3
1 3 2
3 2 5
2 5 4
3 4 1
```

Output:

```
1 2 2 2 2
```

## Solution

Give friend i a variable xᵢ: true if the first statement holds. Every
statement is a claim "person p has card q", true when its literal is
true. Two true claims clash when they give one person two cards or one
card to two people.

The rules of the input make every claim about a given person name a
different card, and every claim about a given card name a different
person. So the conditions are simply: at most one true claim about each
person, and at most one about each card. This is 2-SAT. "At most one"
over k literals is encoded with k helper variables s₁ … s_k:
lⱼ → sⱼ for each j, and sⱼ₋₁ → sⱼ and sⱼ₋₁ → ¬lⱼ for j ≥ 2.
That keeps the formula linear even when one card is named a thousand
times. Tarjan's algorithm finds the strongly connected
components of the implication graph, and a literal is set true when its
component comes before its negation's in the order Tarjan finishes
them.

Pitfalls:

- encoding every pair of clashing claims directly needs 499 500 clauses
  for a group of 1000 claims about one card (test 14);
- the false statement of each friend must stay false; the rules of the
  input guarantee that once the true claims do not clash.

The tests are judged by a checker that tests the true claims for
clashes and then checks, by bipartite matching, that the cards can be
dealt so that every false claim is false. Random deals of 2 to 28
friends all passed it.

## Language notes

- The depth-first search of Tarjan's algorithm keeps its own stack in
  all five solutions, since the implication graph has up to 10 000
  nodes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1382_graphs.cpp](1382_graphs.cpp) | G++ 13.2 x64 | graphs | O(N log N) | AC | 0.031 s | 696 KB |
| [1382_graphs.go](1382_graphs.go) | Go 1.14 x64 | graphs | O(N) | AC | 0.046 s | 3424 KB |
| [1382_graphs.java](1382_graphs.java) | Java 1.8 | graphs | O(N) | AC | 0.171 s | 5276 KB |
| [1382_graphs.py](1382_graphs.py) | Python 3.12 x64 | graphs | O(N) | AC | 0.093 s | 4616 KB |
| [1382_graphs.rs](1382_graphs.rs) | Rust 1.75 x64 | graphs | O(N) | AC | 0.046 s | 1916 KB |
