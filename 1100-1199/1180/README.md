# 1180. Who wins when stones are taken in powers of two

[Timus 1180](https://acm.timus.ru/problem.aspx?space=1&num=1180) · difficulty 89 · games

Original problem by Dmitry Filimonenkov, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N ≤ 10²⁵⁰` stones. Two players take turns removing a power of
two (1, 2, 4, 8, …) stones; whoever takes the last stone wins. Say who
wins with best play, and if it is the first player, the smallest number
of stones the first move can take and still win.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, with up to 251 digits.

## Output

`2`, or `1` and the smallest winning first move.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
8
```

Output:

```
1
2
```

## Solution

No power of two is divisible by 3, so from a multiple of 3 every move
leaves a pile that is not a multiple of 3. From any other pile, taking 1
or 2 stones, the remainder modulo 3, leaves a multiple of 3. Zero is a
multiple of 3, so the player who always leaves a multiple of 3 takes the
last stone. The second player wins exactly when `N` is divisible by 3;
otherwise the first player wins, and the smallest winning move is
`N mod 3`, because no move of 1 or 2 other than that one leaves a
multiple of 3. `N mod 3` is the digit sum modulo 3. `O(digits)`.

Pitfalls:

- `N` has up to 251 digits, so a 64-bit integer is insufficient;
- the winning move must be the smallest one, and both 1 and 2 are powers
  of two, so the remainder itself is it.

The answers were checked against a direct game search for every `N` up to
399.

## Optimized solutions

The optimized solutions (C++, Java) add up the digits one by one as
they are read with `getchar` and `System.in.read`, without storing the
number as a string, and write the short answer byte by byte. C++:
88 KB instead of 384 KB, with the same time; Java: 0.093 s instead of
0.125 s and 328 KB instead of 1568 KB.

`1180_games_optimized.py`. Keep the power-of-two game classification by N modulo three. A zero remainder loses; otherwise taking the remainder, one or two stones, is the smallest winning move. Process the D decimal digits without converting the whole huge number to an integer. Sum the digit byte codes directly: ASCII zero is 48, divisible by three, so the remainder is unchanged. The byte string is still stored: O(D) time and O(D) input storage. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1180_games.py`: time 0.078 s → 0.125 s; memory 400 KB → 236 KB.

`1180_games_optimized.rs`. Keep the power-of-two game classification by N modulo three. A zero remainder loses; otherwise taking the remainder, one or two stones, is the smallest winning move. Process the D decimal digits without converting the whole huge number to an integer. Update the bounded remainder for each incoming digit and retain no input line. Time O(D), auxiliary state O(1). The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1180_games.rs`: time 0.015 s → 0.031 s; memory 212 KB → 56 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1180_games_optimized.py`: time place 64/77, memory place 3/77 in this comparable sample.

`1180_games_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1180_games.cpp](1180_games.cpp) | G++ 13.2 x64 | games | O(digits) | AC | 0.015 s | 384 KB | 11283296 |
| [1180_games.go](1180_games.go) | Go 1.14 x64 | games | O(digits) | AC | 0.015 s | 1104 KB | 11283304 |
| [1180_games.java](1180_games.java) | Java 1.8 | games | O(digits) | AC | 0.125 s | 1568 KB | 11283311 |
| [1180_games.py](1180_games.py) | Python 3.12 x64 | games | O(digits) | AC | 0.078 s | 400 KB | 11283308 |
| [1180_games.rs](1180_games.rs) | Rust 1.75 x64 | games | O(digits) | AC | 0.015 s | 212 KB | 11283312 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1180_games_optimized.cpp](1180_games_optimized.cpp) \* | G++ 13.2 x64 | games | O(digits) | AC | 0.031 s | 88 KB | 11303574 |
| [1180_games_optimized.java](1180_games_optimized.java) | Java 1.8 | games | O(digits) | AC | 0.093 s | 328 KB | 11303452 |
| [1180_games_optimized.py](1180_games_optimized.py) \* | PyPy 3.10 x64 | games | O(D) | AC | 0.125 s | 236 KB | 11324925 |
| [1180_games_optimized.rs](1180_games_optimized.rs) \* | Rust 1.75 x64 | games | O(D) | AC | 0.031 s | 56 KB | 11325088 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
