# 1636. Penalty Time

[Timus 1636](https://acm.timus.ru/problem.aspx?space=1&num=1636) · difficulty 61 · implementation

Original problem by Alex Samsonov, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Teams QXX and ZZZ solved all ten problems; QXX won with penalty time T1
against T2 of ZZZ. Each rejected attempt adds 20 minutes. Given how many
rejected attempts ZZZ made on each problem, decide whether ZZZ would have
won without them. On equal time the teams are ordered by name, so ZZZ
would still be second.

## Input

T1 and T2 (250 ≤ T1 ≤ T2 ≤ 2400) on the first line, then ten counts of
rejected attempts of ZZZ.

## Output

`Dirty debug :(` if the attempts cost ZZZ the first place, otherwise
`No chance.`.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
290 420
0 0 0 2 1 0 2 0 1 0
```

Output:

```
No chance.
```

### Example 2

Input:

```
300 719
0 0 0 0 0 0 21 0 0 0
```

Output:

```
Dirty debug :(
```

## Solution

Subtract 20 minutes per rejected attempt from T2. ZZZ would have won
only with strictly less time than T1, since a tie goes to QXX by the
alphabet. `O(1)`.

Pitfalls:

- equal clean time is still a loss (test 03), one minute less is a win
  (test 04);
- the answers end in a period and in a sad face, both part of the
  expected text.

The answers match an independent accepted implementation on 100 random
tests.

## Optimized solutions

The optimized Java solution parses the numbers byte by byte from
`System.in` instead of using `Scanner`: 368 KB instead of 1600 KB, with
the same time.

`1636_implementation_optimized.py`. Keep the strict comparison T2-20*sum(rejections)<T1; equality must still produce No chance. Read integer byte tokens through a map and consume the remaining ten counts directly with sum, instead of building the separate integer attempts list and decoded input. Work is O(P) for P=10 rejected-attempt counts; parser token storage remains. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1636_implementation.py`: time 0.078 s → 0.109 s; memory 428 KB → 216 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1636_implementation_optimized.py`: time place 62/80, memory place 1/80 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1636_implementation.cpp](1636_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303772 |
| [1636_implementation.go](1636_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB | 11288447 |
| [1636_implementation.java](1636_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1600 KB | 11288449 |
| [1636_implementation.py](1636_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 428 KB | 11288448 |
| [1636_implementation.rs](1636_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 244 KB | 11303773 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1636_implementation_optimized.java](1636_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 368 KB | 11303765 |
| [1636_implementation_optimized.py](1636_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(P), P=10 | AC | 0.109 s | 216 KB | 11325073 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
