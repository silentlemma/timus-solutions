# 2142. Paying red, blue and any mana with dual lands

[Timus 2142](https://acm.timus.ru/problem.aspx?space=1&num=2142) · difficulty 127 · greedy

Original problem by Valentin Zuev, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are A red lands, B blue lands and C dual lands; each gives one
mana, and a dual land gives red or blue as chosen. A spell needs X red
mana, Y blue mana and Z more of any color. Decide whether the lands are
enough. The limits are 1 second and 256 MB.

## Input

A, B, C, then X, Y, Z, all between 0 and 10⁹.

## Output

"It is a kind of magic" if the spell can be paid, otherwise "There are
no miracles in life".

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
3 3 1
2 2 1
```

Output:

```
It is a kind of magic
```

### Example 2

Input:

```
5 6 5
6 5 6
```

Output:

```
There are no miracles in life
```

## Solution

Red lands should pay for red mana and blue lands for blue mana first,
since any land can pay the any-color part. What they leave unpaid,
max(0, X − A) + max(0, Y − B), has to come from the dual lands. After
that every remaining land of any kind can pay for the Z mana of any
color, so the second condition is A + B + C ≥ X + Y + Z. Both together
are necessary and sufficient. The sums reach 3 · 10⁹, beyond 32-bit
integers.

Pitfall (test 02, the second example): covering both colors is not enough.
Red needs 6 − 5 = 1 dual land, but in total 16 lands face 17 mana.

## Optimized solutions

`2142_greedy_optimized.go`. Keep both necessary and sufficient mana checks: dual lands cover max(0,X-A)+max(0,Y-B), then total lands must cover X+Y+Z. After colored deficits are paid, any remaining land can supply neutral mana. Preserve both exact output phrases, including the all-zero instance. Sums can reach 3·10^9, so Go uses int64 throughout and Python exact integers. Time and state O(1); byte input and direct output replace the basic input wrappers. Portable os.Stdin.Read/os.Stdout.Write and direct integer conversion use fixed 4096-byte input and output buffers. Partial writes are handled before reusing the output buffer. The original simple Accepted source is preserved.

Compared with `2142_greedy.go`: time 0.031 s → 0.031 s; memory 1088 KB → 840 KB.

`2142_greedy_optimized.py`. Keep both necessary and sufficient mana checks: dual lands cover max(0,X-A)+max(0,Y-B), then total lands must cover X+Y+Z. After colored deficits are paid, any remaining land can supply neutral mana. Preserve both exact output phrases, including the all-zero instance. Sums can reach 3·10^9, so Go uses int64 throughout and Python exact integers. Time and state O(1); byte input and direct output replace the basic input wrappers. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `2142_greedy.py`: time 0.078 s → 0.125 s; memory 416 KB → 208 KB.

The optimized Java solution reads the six numbers byte by byte from
`System.in` instead of creating a `Scanner`, whose regular expressions
and locale data are the main cost of a program that makes two
comparisons; the sums still use `long`, since they reach 3 · 10⁹:
{2142_greedy_optimized.java}.

### Measured gains

Each optimized version has Accepted and meets a ranking or resource-improvement
admission criterion. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `2142_greedy_optimized.java`: time reduction +12.80%; memory reduction
  +76.67%; base: `2142_greedy.java`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2142_greedy_optimized.go`: time place 5/12, memory place 3/12 in this comparable sample.

`2142_greedy_optimized.py`: time place 66/79, memory place 1/79 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2142_greedy.cpp](2142_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.015 s | 124 KB | 11294928 |
| [2142_greedy.go](2142_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1088 KB | 11294929 |
| [2142_greedy.java](2142_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.125 s | 1560 KB | 11304055 |
| [2142_greedy.py](2142_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 416 KB | 11294930 |
| [2142_greedy.rs](2142_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.046 s | 228 KB | 11304056 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2142_greedy_optimized.java](2142_greedy_optimized.java) \* | Java 1.8 | greedy | O(1) | AC | 0.109 s | 364 KB | 11304424 |
| [2142_greedy_optimized.go](2142_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 840 KB | 11328343 |
| [2142_greedy_optimized.py](2142_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(1) | AC | 0.125 s | 208 KB | 11324931 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
