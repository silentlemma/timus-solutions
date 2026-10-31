# 1613. For Fans of Statistics

[Timus 1613](https://acm.timus.ru/problem.aspx?space=1&num=1613) · difficulty 141 · binary_search

Original problem by Alexander Ipatov, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n cities (1 ≤ n ≤ 69 999) each carried some number of passengers, from 1
to 10⁹ − 1. For each of q queries (1 ≤ q ≤ 69 999) `l r x`, tell whether
some city numbered from l to r carried exactly x passengers. Print a
string of q characters, `1` for yes and `0` for no.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, the n counts, q, then q lines `l r x` with 1 ≤ l ≤ r ≤ n and
1 ≤ x < 10⁹.

## Output

The string of answers.

## Examples

### Example 1

Input:

```
5
1234567 666666 3141593 666666 4343434
5
1 5 3141593
1 5 578202
2 4 666666
4 4 7135610
1 1 1234567
```

Output:

```
10101
```

## Solution

Sort the pairs (count, city number). The cities with count x then form
one block, sorted by number. For a query, a binary search finds the
first pair not less than (x, l): the answer is yes if its count is x and
its city is at most r. `O((n + q) log n)`.

Pitfalls:

- the answer is one string without separators;
- the city must be found at or after l, not merely somewhere with count
  x (test 04).

## Optimized solutions

The optimized C++ solution parses the numbers by hand from a 4 KB buffer
instead of `scanf` and packs each pair into one `uint64_t`: the count,
below 10⁹ < 2³⁰, above 17 bits for the city number, since
`n ≤ 69 999 < 2¹⁷`. A fixed array of these keys is sorted as plain
numbers, a query is one `lower_bound` for `(x << 17) + l` followed by a
comparison with `(x << 17) + r`, and each answer goes out with `putchar`
instead of into a `std::string`: {1613_binary_search_optimized.cpp}.

The optimized Go solution parses the numbers byte by byte from a
`bufio.Reader` instead of a `bufio.Scanner` with a 1 MB buffer and
`strconv.Atoi`, and replaces the four `int` slices of counts, cities and
order with one `uint64` slice of packed pairs: the count, below
10⁹ < 2³⁰, above 17 bits for the city number, since `n ≤ 69 999 < 2¹⁷`.
A query is one `sort.Search` for `(x << 17) + l` and a comparison with
`(x << 17) + r`, and the answers go straight into the `bufio.Writer`:
{1613_binary_search_optimized.go}.

The optimized Java solution parses the numbers by hand from a 64 KB
buffer instead of `StreamTokenizer` and packs each pair into one `long`,
the count above 17 bits for the city number (`n ≤ 69 999 < 2¹⁷`).
Sorting a plain `long` array needs no `int[]` object per city and no
comparator, and a query is one `Arrays.binarySearch` for
`(x << 17) | l`: {1613_binary_search_optimized.java}.

The optimized Python solution reads the input in 8 KB chunks and
converts the tokens chunk by chunk instead of splitting the whole input
at once. It packs each pair into one integer, the count above 17 bits
for the city number (`n ≤ 69 999 < 2¹⁷`), so that the sorted list holds
plain integers instead of tuples, and collects the answers in a
`bytearray` instead of a list of strings:
{1613_binary_search_optimized.py}.

The optimized Rust solution parses the numbers by hand from a 4 KB
buffer instead of reading the whole input, up to about 2 MB, into a
`String`; the sorted pairs and the binary search are the same:
{1613_binary_search_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1613_binary_search_optimized.cpp`: time reduction +81.87%; memory
  reduction +18.18%; base: `1613_binary_search.cpp`.

- `1613_binary_search_optimized.go`: time reduction +25.81%; memory
  reduction +74.47%; base: `1613_binary_search.go`.

- `1613_binary_search_optimized.java`: time reduction +30.13%; memory
  reduction +45.22%; base: `1613_binary_search.java`.

- `1613_binary_search_optimized.py`: time reduction +31.78%; memory
  reduction +83.68%; base: `1613_binary_search.py`.

- `1613_binary_search_optimized.rs`: time reduction +0.00%; memory
  reduction +79.96%; base: `1613_binary_search.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1613_binary_search.cpp](1613_binary_search.cpp) | G++ 13.2 x64 | binary_search | O((n + q) log n) | AC | 0.171 s | 748 KB | 11288259 |
| [1613_binary_search.go](1613_binary_search.go) | Go 1.14 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 5876 KB | 11288261 |
| [1613_binary_search.java](1613_binary_search.java) | Java 1.8 | binary_search | O((n + q) log n) | AC | 0.156 s | 3388 KB | 11304478 |
| [1613_binary_search.py](1613_binary_search.py) | Python 3.12 x64 | binary_search | O((n + q) log n) | AC | 0.343 s | 26612 KB | 11288262 |
| [1613_binary_search.rs](1613_binary_search.rs) | Rust 1.75 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 3692 KB | 11288265 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1613_binary_search_optimized.cpp](1613_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O((n + q) log n) | AC | 0.031 s | 612 KB | 11304474 |
| [1613_binary_search_optimized.go](1613_binary_search_optimized.go) | Go 1.14 x64 | binary_search | O((n + q) log n) | AC | 0.046 s | 1500 KB | 11304475 |
| [1613_binary_search_optimized.java](1613_binary_search_optimized.java) | Java 1.8 | binary_search | O((n + q) log n) | AC | 0.109 s | 1856 KB | 11304479 |
| [1613_binary_search_optimized.py](1613_binary_search_optimized.py) \* | Python 3.12 x64 | binary_search | O((n + q) log n) | AC | 0.234 s | 4344 KB | 11304476 |
| [1613_binary_search_optimized.rs](1613_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 740 KB | 11304477 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
