# 1573. Alchemy

[Timus 1573](https://acm.timus.ru/problem.aspx?space=1&num=1573) · difficulty 108 · math

Original problem by Alexander Ipatov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Sandro has three bags of different reagents: B blue, R red and Y yellow
(1 … 100 each). A potion needs one reagent of each color in its recipe,
all colors different. Count the sets of reagents that make the potion.

Time limit: 1 second. Memory limit: 64 MB.

## Input

B, R and Y, then a positive K and the K different colors of the recipe
(Blue, Red or Yellow).

## Output

The number of ways.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
2 3 5
3
Red
Yellow
Blue
```

Output:

```
30
```

## Solution

Each color of the recipe takes one reagent from its own bag, and the
choices are independent, so the answer is the product of the sizes of
the bags the recipe names. It is at most 100³ = 10⁶. `O(K)`.

Pitfalls:

- the input lists the bags as blue, red, yellow, while the example's
  recipe lists red first;
- only the colors in the recipe count (tests 02, 03).

## Optimized solutions

`1573_math_optimized.java`. Keep the product of independent choices from the distinct required color bags. Initials B/R/Y identify the promised Blue/Red/Yellow tokens; skip the rest without allocating recipe strings. A 1024-byte input buffer and raw numeric output reduce runtime overhead. At most three factors of at most 100 fit int; O(K) work for K recipe colors and fixed auxiliary storage. The combinatorial argument and simple source remain unchanged.

Exact-source Java 1.8 Accepted #11327456: 0.093 s / 344 KB. Saved 2026-11-20 compiler-cohort comparison: time 12/82, memory 2/82. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11304267 was 0.109 s / 328 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1573_math_optimized.java`: 0.093 s / 344 KB; retained teaching base `1573_math.java`: 0.125 s / 1628 KB.

The optimized C++ solution reads with `scanf` instead of `iostream` and
picks the bag by the first letter of the color, since Blue, Red and
Yellow start with different letters, instead of looking the name up in a
`std::map` of strings. A color goes into a buffer of 7 bytes, enough for
the longest name, Yellow, and the product is kept in `int`, which holds
it since it is at most 10⁶: {1573_math_optimized.cpp}.

The optimized Rust solution keeps the three bag sizes in three variables
and selects one with a `match` on the color name instead of building a
`HashMap`: {1573_math_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1573_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +69.23%; base: `1573_math.cpp`.

- `1573_math_optimized.rs`: time reduction -206.67%; memory reduction
  +45.10%; base: `1573_math.rs`.

`1573_math_optimized.py`. Keep multiplication of the available counts for the distinct recipe colors. Map the three ASCII byte names Blue, Red and Yellow directly to their integer bag counts, avoiding decoded input and text keys. There are O(K) multiplications and O(K) token storage, with K<=3 and product at most 10^6 under the statement limits. This changes representation and runtime overhead, not the combinatorial rule. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1573_math.py`: time 0.078 s → 0.109 s; memory 452 KB → 232 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1573_math_optimized.py`: time place 34/51, memory place 1/51 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math.cpp](1573_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 416 KB | 11287812 |
| [1573_math.go](1573_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 1084 KB | 11287815 |
| [1573_math.java](1573_math.java) | Java 1.8 | math | O(K) | AC | 0.125 s | 1628 KB | 11287819 |
| [1573_math.py](1573_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.078 s | 452 KB | 11287817 |
| [1573_math.rs](1573_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.015 s | 408 KB | 11287824 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math_optimized.cpp](1573_math_optimized.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 128 KB | 11304264 |
| [1573_math_optimized.java](1573_math_optimized.java) \* | Java 1.8 | math | O(K) time; O(1) auxiliary space | AC | 0.093 s | 344 KB | 11327456 |
| [1573_math_optimized.rs](1573_math_optimized.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 224 KB | 11304268 |
| [1573_math_optimized.py](1573_math_optimized.py) \* | PyPy 3.10 x64 | math | O(K) | AC | 0.109 s | 232 KB | 11324919 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
