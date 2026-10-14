# 1542. Autocompletion

[Timus 1542](https://acm.timus.ru/problem.aspx?space=1&num=1542) · difficulty 624 · sorting

Original problem by Den Raskovalov, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dictionary holds N distinct words (N ≤ 10⁵, at most 15 lowercase
letters each) with their frequencies (up to 10⁶). For each of M ≤ 15000
typed prefixes, list at most ten words that start with it, the most
frequent first and equal frequencies alphabetically.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then N lines with a word and its frequency, then M and the M
prefixes, one per line.

## Output

For each prefix, its suggestions, one per line; the lists of
consecutive prefixes are separated by an empty line.

## Examples

### Example 1

Input:

```
5
kare 10
kanojo 20
karetachi 1
korosu 7
sakura 3
3
k
ka
kar
```

Output:

```
kanojo
kare
korosu
karetachi

kanojo
kare
karetachi

kare
karetachi
```

## Solution

Sort the words once by decreasing frequency and then alphabetically.
Put every distinct query into a hash table with an empty list. Then go
through the sorted words; for each of a word's at most 15 prefixes that
is a query, append the word to that query's list unless it already has
ten. As the words come in the required order, each list ends up exactly
as the answer. Total time is `O(N log N + 15·N + M)`; repeated queries
reuse the same list.

Pitfalls:

- a prefix with no words still takes its place in the output: an empty
  block, also at the very start or end (test 02);
- equal frequencies go alphabetically, so a comes before ab (test 03);
- a query may equal a whole word, or be longer than every word
  (test 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1542_sorting.cpp](1542_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + 15 N + M) | AC | 0.187 s | 11212 KB |
| [1542_sorting.go](1542_sorting.go) | Go 1.14 x64 | sorting | O(N log N + 15 N + M) | AC | 0.203 s | 11304 KB |
| [1542_sorting.java](1542_sorting.java) | Java 1.8 | sorting | O(N log N + 15 N + M) | AC | 0.468 s | 36636 KB |
| [1542_sorting.py](1542_sorting.py) | Python 3.12 x64 | sorting | O(N log N + 15 N + M) | AC | 0.593 s | 32604 KB |
| [1542_sorting.rs](1542_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + 15 N + M) | AC | 0.093 s | 15136 KB |
