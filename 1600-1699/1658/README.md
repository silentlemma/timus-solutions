# 1658. Sum of Digits

[Timus 1658](https://acm.timus.ru/problem.aspx?space=1&num=1658) · difficulty 203 · dp

Original problem by Vladimir Yakovlev (idea by Stanislav Vasilyev), from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each of t queries, given the sum s₁ of the digits of a positive
integer and the sum s₂ of their squares, print the smallest such integer,
or `No solution` if there is none with at most 100 digits.

## Input

t (at most 10000), then t pairs s₁ s₂ (1 ≤ s₁, s₂ ≤ 10000).

## Output

The smallest number for each query, or `No solution`.

## Checking

Compare output tokens; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
9 81
12 9
6 10
7 9
```

Output:

```
9
No solution
1122
111112
```

## Solution

The smallest number has the fewest digits, and among those it is the
smallest string. It never contains a zero: a zero adds a digit without
changing either sum, so it would not be shortest. With at most 100
digits the sums stay within 900 and 8100, so larger queries have no
answer.

Except in Python, a table of the fewest nonzero digits for every pair (s₁, s₂) up to
900 × 8100 comes from one pass over the table: each cell is one more
than the best cell reached by taking away a digit d and d². The answer
is then built greedily: the first digit is the smallest d after which
the rest still needs exactly one digit fewer, and so on. The digits come
out sorted, so each search can start from the previous digit.
`O(S₁ · S₂ · 9)` for the table, `O(100)` per query.

Pitfalls:

- the table has 7.3 million cells, so it is kept in bytes;
- a sum of squares below the sum of digits, or above nine times it, is
  impossible; the table handles that with no special case;
- s₁ = 900 with s₂ = 8100 is a hundred nines, one digit more is already
  too long (test 02).

The answers match an independent accepted implementation on 80 000
queries.

## Optimized solutions

The digit-moment DP retains only feasible parity-compatible states instead of a rectangular table containing impossible sums. Balance and maximum-square-sum bounds determine each compressed row; transition values still represent minimum required digits, and reconstruction follows valid digit transitions. The Python bitset variant performs many transitions together with exact shifts and OR operations, not floating arithmetic. Its normalization removes zero padding without discarding a feasible state. No precomputed answer table is introduced.

Here C is the number of feasible compressed states, T the number of queries and K the digit-length bound; the factor 9 counts nonzero digits.

- `1658_dp_optimized.cpp`: 0.046 s / 3292 KB; base `1658_dp.cpp`: 0.125 s / 9572 KB; relative change: time -63.2%, memory -65.6%.
- `1658_dp_optimized.go`: 0.062 s / 4488 KB; base `1658_dp.go`: 0.203 s / 12960 KB; relative change: time -69.5%, memory -65.4%.
- `1658_dp_optimized.java`: 0.156 s / 9148 KB; base `1658_dp.java`: 0.265 s / 14280 KB; relative change: time -41.1%, memory -35.9%.
- `1658_bitmask_dp.py`: 1.031 s / 12680 KB; base `1658_dp.py`: 1.578 s / 23432 KB; relative change: time -34.7%, memory -45.9%.
- `1658_dp_optimized.rs`: 0.031 s / 2800 KB; base `1658_dp.rs`: 0.156 s / 9532 KB; relative change: time -80.1%, memory -70.6%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1658_dp.cpp`; covering source `1658_dp_optimized.cpp`; time/memory places 5/3, other-author entries 87/87.

- Go: preferred teaching base `1658_dp.go`; covering source `1658_dp.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1658_dp.java`; covering source `1658_dp.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1658_dp.py`; covering source `1658_bitmask_dp.py`; time/memory places 2/1, other-author entries 2/2.

- Rust: preferred teaching base `1658_dp.rs`; covering source `1658_dp_optimized.rs`; time/memory places 1/1, other-author entries 2/2.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1658_dp.cpp](1658_dp.cpp) | G++ 13.2 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.125 s | 9572 KB | 11308834 |
| [1658_dp.go](1658_dp.go) | Go 1.14 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.203 s | 12960 KB | 11288594 |
| [1658_dp.java](1658_dp.java) | Java 1.8 | dp | O(S₁ · S₂ · 9) | AC | 0.265 s | 14280 KB | 11308836 |
| [1658_dp.py](1658_dp.py) | Python 3.12 x64 | dp | O(K · S₁ · S₂ · 9) | AC | 1.578 s | 23432 KB | 11288595 |
| [1658_dp.rs](1658_dp.rs) | Rust 1.75 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.156 s | 9532 KB | 11308837 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1658_dp_optimized.cpp](1658_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(9C+TK) | AC | 0.046 s | 3292 KB | 11308098 |
| [1658_dp_optimized.go](1658_dp_optimized.go) | Go 1.14 x64 | dp | O(9C+TK) | AC | 0.062 s | 4488 KB | 11308100 |
| [1658_dp_optimized.java](1658_dp_optimized.java) | Java 1.8 | dp | O(9C+TK) | AC | 0.156 s | 9148 KB | 11308105 |
| [1658_bitmask_dp.py](1658_bitmask_dp.py) \* | Python 3.12 x64 | bitmask, dp | O(9C+TK) | AC | 1.031 s | 12680 KB | 11308153 |
| [1658_dp_optimized.rs](1658_dp_optimized.rs) | Rust 1.75 x64 | dp | O(9C+TK) | AC | 0.031 s | 2800 KB | 11308108 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
