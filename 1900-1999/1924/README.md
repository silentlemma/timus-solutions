# 1924. A Sign Game with Fixed Parity

[Timus 1924](https://acm.timus.ru/problem.aspx?space=1&num=1924) · difficulty 39 · math

Original problem: folklore, from Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The integers 1 through n appear in order. Two teams alternate placing
either + or − in an unused gap between consecutive integers. The first
team, `black`, wants the completed expression to be even; `grimy` wants
it odd. Both play optimally and black moves first. Determine the winner.
For n=1 there are no gaps, and the expression is simply 1.
Limits: 1 second, 64 MB.

## Input

One integer n, 1≤n≤50.

## Output

Print exactly `black` if the even-result team wins, otherwise `grimy`.

## Checking

Compare the single word token exactly, including lowercase spelling.

## Examples

```
1
```

```
grimy
```

```
4
```

```
black
```

## Solution

Changing the sign in front of a number x from + to − changes the result
by 2x, an even number. So every expression the players can make has the
same parity as 1 + 2 + … + n = n(n + 1)/2, and no move changes the
winner: black wins if this sum is even, grimy if it is odd. `O(1)`.

Pitfall: with n = 1 there are no moves at all, and the parity of 1 still
decides.

## Optimized solutions

The optimized C++ solution reads with `scanf` and prints with `puts`
instead of `iostream`: 116 KB instead of 380 KB. The formula is the
same.

The optimized Java solution parses the number byte by byte from
`System.in` instead of using `Scanner`: 336 KB instead of 1616 KB, with
the same time.

`1924_math_optimized.py`. Use the four-value parity period instead of constructing N(N+1)/2: its parity is even exactly when N mod 4 is 0 or 3. Changing plus to minus changes a total by an even number, so play cannot affect the winner. This is a smaller form of the same parity argument, with O(1) time and storage. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1924_math.py`: time 0.093 s → 0.125 s; memory 396 KB → 192 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1924_math_optimized.py`: time place 110/125, memory place 2/125 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1924_math.cpp](1924_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 380 KB | 11291523 |
| [1924_math.go](1924_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1100 KB | 11291530 |
| [1924_math.java](1924_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1616 KB | 11291534 |
| [1924_math.py](1924_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 396 KB | 11291532 |
| [1924_math.rs](1924_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB | 11291542 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1924_math_optimized.cpp](1924_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 116 KB | 11303649 |
| [1924_math_optimized.java](1924_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 336 KB | 11303788 |
| [1924_math_optimized.py](1924_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 192 KB | 11325078 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
