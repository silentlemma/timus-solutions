# 1897. Alice and Bob and a string

[Timus 1897](https://acm.timus.ru/problem.aspx?space=1&num=1897) · difficulty 5381 · suffix_structures

Original problem by Oleksandr Kulkov, from Petrozavodsk Summer 2018, Moscow IPT Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A game position is a substring t of a fixed string s, possibly empty.
A move prepends one lowercase letter and appends another, provided
the resulting string is still a substring of s. A player unable to
move loses; both players choose optimally.

Among the distinct starting strings that win for the player to move,
find the k-th in lexicographic order. The empty string comes first,
and a proper prefix precedes its extensions. Different occurrences
of the same substring count only once. The limits are 1 second and
256 MB.

## Input

The first line contains s, with 1 ≤ |s| ≤ 100 000, using only lowercase
English letters. The second contains k, with 1 ≤ k ≤ 10¹⁰.

## Output

Print the requested string, or `no solution` if fewer than k winning
strings exist. Print `-` when the answer is the empty string.

## Checking

Outputs are compared token by token.

## Examples

### Example 1

Input:

```
abac
3
```

Output:

```
b
```

### Example 2

Input:

```
rndstr
1
```

Output:

```
-
```

### Example 3

Input:

```
abc
10
```

Output:

```
no solution
```

## Solution

### Compress the game by centers

Every move adds two letters, preserving the center and length parity
of an occurrence. For an even-length occurrence, let c be the gap
before position c; for an odd one, c is the center character. With
parity e equal to 0 or 1 and radius d, the substring starts at c − d
and has length 2d + e.

For each center, read successive pairs of letters outwards. Build a
trie of these pair sequences: one root represents the empty string,
and odd-length roots are grouped by their center character. Identical
prefixes represent identical substrings, so a game move is one trie
step. Mark a terminal whenever a center reaches a text boundary.

Compress paths, retaining roots, branching nodes and every terminal,
including terminals with one child. There are only `O(n)` such nodes,
since there are `O(n)` center sequences. A terminal occurrence is not
an extra game move or a reason to stop: other occurrences may extend.
Retaining terminals records exactly where the occurrence set changes.

To construct the compressed tries efficiently, preprocess suffix arrays
and LCP range-minimum queries for s and its reversal. The common prefix
of two center sequences is the minimum of the matching left-outward
and right-outward lengths, capped by their available radii. Compare
their next letter pairs if necessary. Sort centers with these constant-
time comparisons and build each compressed trie from adjacent LCPs
using a depth stack.

### Evaluate compressed edges

A position wins exactly when some next position loses. Suppose an
edge runs from radius L to radius R and the child outcome is W(R).
Its internal positions have one possible next step, hence
W(d) = W(R) XOR ((R − d) mod 2), for L < d ≤ R. Evaluate explicit
nodes bottom-up using the first position on each outgoing edge.

### Assign each string to a suffix

Assign each distinct substring to its occurrence whose starting suffix
has the smallest suffix-array rank. In suffix-array order, these owners
give the usual blocks of new prefixes: lengths exceeding the LCP with
the previous suffix. Within one block, increasing length is exactly
lexicographic order.

Along a compressed edge, the occurrence centers do not change. Each
radius step prepends the same letter to every occurrence, preserving
their suffix order. Thus one representative center c owns the whole
edge. Find representatives bottom-up: at a node's radius, compare its
terminal centers with the representatives of its child groups.

An edge with radii L < d ≤ R contributes starts p = c − d in the
interval [c − R, c − L − 1]. The outcome alternates with d, so its
winning strings contribute 1 at every other start in this interval.
Use separate difference arrays for even and odd starts. A winning
odd root contributes its one-character string at its representative
start. Handle the empty root separately.

Prefix-summing the difference arrays gives the winning count owned by
each suffix. Scan suffixes in suffix-array order to locate the block
containing rank k. For its start p, scan the compressed edges again:
each edge can contribute at most one radius, d = c − p, and therefore
one length 2d + e. Keep winning candidates, include its odd-root point
if applicable, sort their lengths and select the remaining rank.

Every distinct substring belongs to exactly one trie position and one
suffix owner. Edge parity computes its game result, the range additions
count it once, and the final owner/length order is lexicographic.
Therefore the selected string has the required rank.

Counting-sort suffix-array doubling, LCP preprocessing and center-path
sorting take `O(n log n)` time. The compressed game and ownership counts
take linear time; sorting the selected owner's lengths costs at most
`O(n log n)`. Total time and sparse-table storage are `O(n log n)`.

In the first example the winners are the empty string, `a`, `b` and
`ba`, so the third is `b`. In the second, the empty position can move
to the terminal string `rn` and is winning. In the third, only the
empty string and `b` win, fewer than ten choices.

Pitfalls:

- one game step changes the radius by 1 and the length by 2;
- keep all terminal drops when compressing, even with one child;
- a boundary occurrence does not forbid moves from other occurrences;
- use suffix rank, not the earliest text position, for ownership;
- count strings rather than occurrences and use 64-bit counts;
- place a winning empty string before every nonempty candidate.

## Language notes

Short center prefixes are packed into integer keys to reduce
comparisons. C++, Go, Java and Rust store the LCP tables in arrays of
primitive types.

The Python solution runs on PyPy and takes another route, through a
suffix automaton of the reversal of s, whose reversed suffix links form
the suffix tree of s and so give the lexicographic order. A string that occurs once can only
grow until its occurrence meets the nearer end of s, so its outcome
follows from a parity; for repeated strings the outcomes of the lengths
of each automaton state are kept in bitsets of linear total size, with
shared runs for very repetitive strings. The winning strings are then
counted down the suffix tree to find the k-th. It takes 0.69 s of the
1 s on the judge; earlier versions, with the center tries and then with
a first automaton, exceeded the time limit on the judge's tests 73 and
107.

The answers agree with a full search of the game on 25 534 rank queries.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1897_suffix_structures.cpp](1897_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(n log n) | AC | 0.171 s | 28008 KB |
| [1897_suffix_structures.go](1897_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(n log n) | AC | 0.468 s | 92856 KB |
| [1897_suffix_structures.java](1897_suffix_structures.java) | Java 1.8 | suffix_structures | O(n log n) | AC | 0.468 s | 36316 KB |
| [1897_suffix_structures.py](1897_suffix_structures.py) | PyPy 3.10 x64 | suffix_structures | O(n log n) | AC | 0.687 s | 74404 KB |
| [1897_suffix_structures.rs](1897_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(n log n) | AC | 0.453 s | 45932 KB |
