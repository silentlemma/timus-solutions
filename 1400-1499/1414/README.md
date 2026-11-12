# 1414. Astronomical Database

[Timus 1414](https://acm.timus.ru/problem.aspx?space=1&num=1414) · difficulty 430 · sorting, binary_search

Original problem by Pavel Egorov, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A database of star names starts with the single name "sun". Up to 10 000
operations follow, one per line: "+name" adds a name (it may be added
again later), "?prefix" asks for the names that start with the prefix.
Arguments are 1 to 20 lowercase Latin letters or digits. For each query
print the prefix and then the matching names in dictionary order,
without repeats, each indented by two spaces, at most the first 20.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The operations.

## Output

The answers to the queries.

## Examples

### Example 1

Input:

```
?e
+earth
+egg
?e
+eagle
+earth
?ea
```

Output:

```
e
e
  earth
  egg
ea
  eagle
  earth
```

## Solution

Keep the names in an ordered set. The names with a given prefix form a
contiguous run in dictionary order that starts where the prefix itself
would be inserted, so each query finds that place by binary search and
walks forward until a name no longer has the prefix or 20 names are
printed. C++, Java and Rust use their tree sets; Go and Python keep a
sorted array and insert into it, which moves at most 10 000 references
per addition. `O(Q log Q)` with tree sets.

Pitfalls:

- "sun" is in the base from the start (test 02);
- repeated additions must not repeat in the answer (test 03);
- only the first 20 names are printed (test 04);
- names contain digits, which sort before letters (test 12);
- the example shows the two indenting spaces as dots.

## Optimized solutions

The new C++ and Rust versions retain ordered sets and lower-bound prefix queries; the output cap stays twenty distinct names in dictionary order. They emit bounded output rather than retaining all query answers. C++ prints each line through C stdio. Rust pads each name to twenty bytes with zeros and stores these fixed arrays directly in BTreeSet: zero sorts before every valid digit or letter, preserving ordinary string order and proper-prefix order. Prefix matching compares only the given prefix length. One complete answer occupies at most 21+20·23=481 bytes, within its 512-byte buffer. Thus storage depends on the names, not cumulative output. The original String/set versions remain, and Go, Java and Python reuse admitted bases in the fast set.

The accepted G++ 13.2 x64 run takes 0.125 s versus 0.031 s for the base and uses 924 KB versus 5748 KB.

The accepted Rust 1.75 x64 run takes 0.062 s versus 0.031 s for the base and uses 292 KB versus 6144 KB.

The accepted base implementations [1414_sorting.go](1414_sorting.go), [1414_sorting.java](1414_sorting.java), [1414_sorting.py](1414_sorting.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1414_sorting.cpp](1414_sorting.cpp) | G++ 13.2 x64 | sorting | O(Q log Q) | AC | 0.031 s | 5748 KB | 11286098 |
| [1414_sorting.go](1414_sorting.go) | Go 1.14 x64 | sorting | O(Q^2) | AC | 0.031 s | 1868 KB | 11286100 |
| [1414_sorting.java](1414_sorting.java) \* | Java 1.8 | sorting | O(Q log Q) | AC | 0.156 s | 24264 KB | 11286104 |
| [1414_sorting.py](1414_sorting.py) \* | Python 3.12 x64 | sorting | O(Q^2) | AC | 0.156 s | 19372 KB | 11286103 |
| [1414_sorting.rs](1414_sorting.rs) | Rust 1.75 x64 | sorting | O(Q log Q) | AC | 0.031 s | 6144 KB | 11286105 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1414_sorting_optimized.cpp](1414_sorting_optimized.cpp) \* | G++ 13.2 x64 | sorting | O(Q log Q + output) | AC | 0.125 s | 924 KB | 11314978 |
| [1414_sorting_optimized.rs](1414_sorting_optimized.rs) \* | Rust 1.75 x64 | sorting | O(Q log Q + output) | AC | 0.062 s | 292 KB | 11314990 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
