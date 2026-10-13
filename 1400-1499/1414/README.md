# 1414. Astronomical Database

[Timus 1414](https://acm.timus.ru/problem.aspx?space=1&num=1414) · difficulty 431 · sorting, binary_search

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
- names contain digits, which sort before letters (test 07);
- the example shows the two indenting spaces as dots.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1414_sorting.cpp](1414_sorting.cpp) | G++ 13.2 x64 | sorting | O(Q log Q) | AC | 0.031 s | 5748 KB |
| [1414_sorting.go](1414_sorting.go) | Go 1.14 x64 | sorting | O(Q log Q) | AC | 0.031 s | 1868 KB |
| [1414_sorting.java](1414_sorting.java) | Java 1.8 | sorting | O(Q log Q) | AC | 0.156 s | 24264 KB |
| [1414_sorting.py](1414_sorting.py) | Python 3.12 x64 | sorting | O(Q log Q) | AC | 0.156 s | 19372 KB |
| [1414_sorting.rs](1414_sorting.rs) | Rust 1.75 x64 | sorting | O(Q log Q) | AC | 0.031 s | 6144 KB |
