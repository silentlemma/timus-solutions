# 1604. In the Country of Fools

[Timus 1604](https://acm.timus.ru/problem.aspx?space=1&num=1604) · difficulty 139 · greedy

Original problem by Alexander Ipatov (idea by Alexander Toropov), from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are k kinds of speed limit signs, nᵢ signs of kind i, at most
10000 signs in all. Place them all along a road so that drivers change
speed as often as possible: a change happens at the first sign and at
every sign that differs from the one before. Any best order is
accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

k, then n₁, …, nₖ, where 1 ≤ k ≤ 10000, each nᵢ is positive,
and their sum is at most 10000.

## Output

The kinds of the signs in road order.

## Examples

### Example 1

Input:

```
2
2 2
```

Output:

```
1 2 1 2
```

## Solution

Changing speed as often as possible means having as few equal
neighbours as possible. Let m be the largest count and n the total. The
other n − m signs split the m signs of the commonest kind into at most
n − m + 1 groups, so at least max(0, 2m − n − 1) neighbours are equal.

A greedy order reaches this bound: always place the kind with the most
signs left, unless it was the previous sign, in which case place the
kind with the second most. A heap gives both in `O(log k)`, so the whole
order takes `O(n log k)`.

The tests use a checker that counts the equal neighbours and compares
them with the bound. The bound itself was checked against an exhaustive
search over all orders of small sets of signs.

Pitfalls:

- equal neighbours are unavoidable exactly when 2m > n + 1, and the
  greedy puts them together at the end (test 05); at 2m = n + 1 they
  can still be avoided (tests 02 and 04);
- taking the commonest kind every time without looking at the previous
  sign repeats it; taking kinds in turn ignores the counts and can run
  out of other kinds too early (test 07).

## Optimized solutions

The optimized C++ solution packs a kind and its count into one `int`,
count·2¹⁴ + kind: both are at most 10000, below 2¹⁴ = 16384, so the two
fields never overlap, and comparing the packed numbers compares first
the counts and then the kinds, as with the pairs. The heap is a fixed
array of 10000 such numbers run by `std::push_heap` and `std::pop_heap`
instead of a `priority_queue` of pairs, and the kinds are printed with
`printf` as they come instead of being collected in a string:
{1604_greedy_optimized.cpp}.

The optimized Go solution writes its own heap over a slice of signs,
reserved for k entries, instead of `container/heap`, which turns every
pushed and popped sign into an `interface{}` value and allocates it. The
numbers are parsed byte by byte from the `bufio.Reader` instead of with
`fmt.Fscan`: {1604_greedy_optimized.go}.

The optimized Java solution passes the `PriorityQueue` an ordinary
`Comparator` class instead of a lambda, whose first use loads extra
machinery of the runtime. When a kind is placed, its array is taken out
of the heap anyway, so the solution lowers the count in that array and
puts it back instead of creating a new one for every sign. The kinds go
out through a `BufferedWriter` instead of a `StringBuilder`:
{1604_greedy_optimized.java}.

The optimized Python solution packs the heap entry (−count, kind) into
one integer, −count·(k + 1) + kind, instead of a tuple: the kind is from
1 to k, below the base k + 1, so the integers compare exactly like the
tuples, and `divmod` recovers both fields. It reads the input as bytes,
frees the list of tokens before the main loop, and writes the kinds in
chunks of 256 instead of keeping the whole order in memory:
{1604_greedy_optimized.py}.

The optimized Rust solution writes each kind through a `BufWriter` as it
is placed instead of collecting up to 10000 strings in a `Vec` and
joining them into one more string: {1604_greedy_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1604_greedy_optimized.cpp`: time reduction +0.00%; memory reduction
  +49.32%; base: `1604_greedy.cpp`.

- `1604_greedy_optimized.go`: time reduction +51.61%; memory reduction
  +49.27%; base: `1604_greedy.go`.

- `1604_greedy_optimized.java`: time reduction +19.87%; memory reduction
  +64.35%; base: `1604_greedy.java`.

- `1604_greedy_optimized.py`: time reduction +0.00%; memory reduction
  +42.12%; base: `1604_greedy.py`.

- `1604_greedy_optimized.rs`: time reduction -313.33%; memory reduction
  +56.70%; base: `1604_greedy.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1604_greedy.cpp](1604_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log k) | AC | 0.015 s | 292 KB | 11288133 |
| [1604_greedy.go](1604_greedy.go) | Go 1.14 x64 | greedy | O(n log k) | AC | 0.031 s | 2184 KB | 11288136 |
| [1604_greedy.java](1604_greedy.java) | Java 1.8 | greedy | O(n log k) | AC | 0.156 s | 3456 KB | 11288142 |
| [1604_greedy.py](1604_greedy.py) | Python 3.12 x64 | greedy | O(n log k) | AC | 0.093 s | 1776 KB | 11288140 |
| [1604_greedy.rs](1604_greedy.rs) | Rust 1.75 x64 | greedy | O(n log k) | AC | 0.015 s | 1044 KB | 11288144 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1604_greedy_optimized.cpp](1604_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n log k) | AC | 0.015 s | 148 KB | 11304457 |
| [1604_greedy_optimized.go](1604_greedy_optimized.go) | Go 1.14 x64 | greedy | O(n log k) | AC | 0.015 s | 1108 KB | 11304458 |
| [1604_greedy_optimized.java](1604_greedy_optimized.java) \* | Java 1.8 | greedy | O(n log k) | AC | 0.125 s | 1232 KB | 11304459 |
| [1604_greedy_optimized.py](1604_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(n log k) | AC | 0.093 s | 1028 KB | 11304460 |
| [1604_greedy_optimized.rs](1604_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(n log k) | AC | 0.062 s | 452 KB | 11304461 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
