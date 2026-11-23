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

## Optimized solutions

Python packs the inverted frequency into three big-endian bytes ahead of each word. Sorting these byte strings gives the required ranking without tuples, and the scan checks only prefix lengths that occur in queries. Submission 11317220 took 0.562 s and used 17632 KB, versus 0.656 s and 33184 KB for the base.

Rust packs frequency and letters into a 128-bit sorting key, scans only queried prefix lengths, and stores completed suggestions as bytes. Submission 11317222 took 0.062 s and used 9652 KB, versus 0.109 s and 15020 KB for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321809 · Go 1.14 x64 №11321811 · Java 1.8 №11321814 · Python 3.12 x64 №11322065 · Rust 1.75 x64 №11322067.

C++ stores words in fixed-size records, looks up only queried prefix lengths by string view, and streams the suggestions. G++ 13.2 x64, submission 11322388. Time 0.171 → 0.093 s, memory 11168 → 4104 KB.

Go stores words in fixed-size records, looks up only queried prefix lengths by string view, and streams the suggestions. Go 1.14 x64, submission 11322389. Time 0.187 → 0.109 s, memory 11308 → 10108 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1542_sorting_optimized.java`. Retain the archived algorithm, replacing Scanner with buffered byte input. Output avoids Formatter where ordinary numeric conversion suffices. EOF is stable even without a final newline; the simple source remains unchanged.

Accepted #11328642 (Java 1.8): **0.531 s / 23760 KB**. Archived comparison: `1542_sorting.java` (Java 1.8) — 0.484 s / 36648 KB (#11321814).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1542_sorting.cpp](1542_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + 15 N + M) | AC | 0.171 s | 11168 KB | 11321809 |
| [1542_sorting.go](1542_sorting.go) | Go 1.14 x64 | sorting | O(N log N + 15 N + M) | AC | 0.187 s | 11308 KB | 11321811 |
| [1542_sorting.java](1542_sorting.java) | Java 1.8 | sorting | O(N log N + 15 N + M) | AC | 0.484 s | 36648 KB | 11321814 |
| [1542_sorting.py](1542_sorting.py) | Python 3.12 x64 | sorting | O(N log N + 15 N + M) | AC | 0.656 s | 33184 KB | 11322065 |
| [1542_sorting.rs](1542_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + 15 N + M) | AC | 0.109 s | 15020 KB | 11322067 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1542_sorting_optimized.py](1542_sorting_optimized.py) | Python 3.12 x64 | sorting | O(N log N + 15 N + M) | AC | 0.562 s | 17632 KB | 11317220 |
| [1542_sorting_optimized.rs](1542_sorting_optimized.rs) | Rust 1.75 x64 | sorting | O(N log N + 15 N + M) | AC | 0.062 s | 9652 KB | 11317222 |
| [1542_sorting_optimized.cpp](1542_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(N log N + 15 N + M) | AC | 0.093 s | 4104 KB | 11322388 |
| [1542_sorting_optimized.go](1542_sorting_optimized.go) | Go 1.14 x64 | sorting | O(N log N + 15 N + M) | AC | 0.109 s | 10108 KB | 11322389 |
| [1542_sorting_optimized.java](1542_sorting_optimized.java) | Java 1.8 | sorting | O(N log N + 15 N + M) | AC | 0.531 s | 23760 KB | 11328642 |
