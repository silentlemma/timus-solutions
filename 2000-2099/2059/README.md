# 2059. Compare palindrome frequencies

[Timus 2059](https://acm.timus.ru/problem.aspx?space=1&num=2059) · difficulty 1487 · strings

Original problem by Mikhail Rubinchik, from the Palindromic Contest of July 11, 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For two words A and B, look at every distinct palindrome occurring in
either of them. Count the palindromes that occur more often in A, those
that occur equally often in both, and those that occur more often in B.
Occurrences may overlap, and case matters. The limits are 1 second and
64 MB.

## Input

The number of tests T, then two lines with A and B for each test. Each
word is nonempty and at most 200 000 characters long; the whole input is
at most 8 MB.

## Output

For test i, the line `Case #i: x y z` with the three counts.

## Checking

A checker compares the three numbers of every case; spacing between them
does not matter.

## Examples

```
3
abacab
abccab
faultydogeuniversity
hasnopalindromeatall
abbacabbaccab
youmayexpectedstrongsamplesbutnow
```

```
Case #1: 4 1 2
Case #2: 8 3 9
Case #3: 13 0 15
```

In the first pair, `a,aba,aca,bacab` occur more often in `abacab`; `b`
appears twice in both words; `c` and `cc` occur more often in `abccab`.
This gives `4 1 2`. The second pair has 20 distinct palindromes in the
union, split as `8+3+9`; the third has 28, split as `13+0+15`. Frequency
counts must include overlaps: `aaaa` contains `aa` three times, and
comparing `aaaa` with `aaa` gives `4 0 0`.

## Solution

### One shared palindrome tree

Create an eertree whose real nodes represent distinct palindromes. Two
auxiliary roots have lengths `−1` and `0`. A transition labeled `c`
extends palindrome `P` to `cPc`; from the odd root it creates the
one-letter palindrome `c`. Each node stores its length, its longest
proper palindromic suffix `link`, and sparse children.

Scan `A` left to right. From the previous longest palindromic suffix,
follow suffix links until the next letter can be placed on both ends.
Follow the matching transition, creating it if missing. A new node's
proper suffix is found by the same search beginning from its parent's
suffix link. Check the current word's left boundary before accessing the
preceding character.

Then scan `B` with the same nodes and transitions but restart the active
suffix at the empty root and use `B`'s own boundary. This shares equal
palindromes across words without introducing palindromes crossing the
word boundary. The compiled versions keep two counters per node,
initially zero. At each position increment only the counter of the
current longest suffix, for the word being scanned.

### Recover all occurrence counts

Process real nodes in decreasing creation order. Add both counters of
`v` to the corresponding counters of `link[v]`. After the additions,
compare the two counters of `v` and increment exactly one of `x,y,z`.
The two roots are never classified.

Python uses the equivalent signed difference instead of two counters:
add `+1` while scanning `A` and `−1` while scanning `B`, then propagate
that difference along suffix links in the same reverse order. Its sign
selects `x,y,z`. Subtraction commutes with propagation, so the result is
exactly the comparison of the two full occurrence counts.

A transition identifies its palindrome uniquely: its inner palindrome
and its two equal outer characters determine the string. Therefore a
shared node is precisely one distinct palindrome, not one occurrence.
Only the longest palindromic suffix can be newly created at a position:
every shorter palindromic suffix also occurs earlier as a prefix of that
longest palindrome. Thus the joint tree has at most `|A|+|B|+2` nodes,
and a new node's proper suffix already has an older node ID.

For any fixed ending position, every palindromic occurrence ending there
appears exactly once on the longest suffix's suffix-link chain. We
initially place one mark at that chain's top. Propagating counters sends
the mark once to every ancestor, so each node receives exactly one mark
for every ending position of its palindrome. Different ending positions
remain separate even when their occurrences overlap. Decreasing node IDs
process every child before its parent, since all suffix links lead to
older nodes; this proves the final counters for both words. Every real
node was created in at least one word, so equal counters are
automatically positive. The final classification counts exactly the
required distinct strings.

### Several tests and implementation details

Reuse allocated node arrays across tests. Reset the two roots' child
heads and counters, then initialize every newly assigned node slot,
including its child head and both counters. Old unreachable slots cannot
affect the new tree. Python resets one difference counter per node,
stores length plus one in `span`, prefixes each word with a zero sentinel,
and uses direct byte-indexed transitions for the two roots. The
single-letter pair is a mathematical base case:
equal letters give `0 1 0`, different letters give `1 0 1`.

Python also handles pairs of unary words or pairs of alternating
period-two words directly. In an alternating word, each starting letter
determines a family of odd palindromes whose frequencies decrease by one
as their lengths grow by two. Equal two-letter alphabets share those
families; different alphabets
can share only single-letter palindromes. If neither word contains a
palindrome of length two or three, only single letters need counting:
every longer palindrome has such a central palindrome. For identical
words, Python builds only one tree and counts its real nodes, all tied.
It also reuses the previous answer for a repeated pair, or swaps `x,z`
when the pair is reversed. These shortcuts preserve the same counts and
do not change the worst-case complexity.

Sparse child lists need at most one scan per transition lookup. If `σ`
is the character alphabet size, a pair takes `O(σ(|A|+|B|))` time;
suffix-link searches have linear total work by the usual length-decrease
amortization, since one extension increases the relevant suffix lengths
by at most two. Count propagation is linear. For a fixed byte alphabet,
this is `O(|A|+|B|)` per pair. Only `O(|A|+|B|)` node slots are live.
Compiled versions allocate the maximum `400002` slots once; Python grows
to the largest observed pair. Initialization is paid once, not for every
tiny test. All counts fit signed 32-bit integers.

C++ streams words as lines. Python retains the input in `BytesIO` and
reads its words as lines. Go and Java retain an input buffer bounded by
8 MiB; Rust also retains the input. Output is buffered in
bounded chunks, so nearly two million tiny pairs do not create an
in-memory list of all answers. Python uses packed arrays and reuses them
between tests.

Do not rebuild unrelated trees and compare node numbers, because IDs are
not string identities between separate trees. Do not keep `A`'s active
suffix when starting `B`. Mark only the longest suffix and then
propagate; incrementing its entire suffix chain as well would
double-count. Use reverse topological order, exclude the empty roots,
count overlaps, and distinguish frequency comparison from mere presence.
Reset both word counters when recycling a slot. The total 8 MB limit
matters in addition to the individual string lengths.
With Python's signed counter, zero means equal frequencies, not absence:
only created real nodes are classified. Test `002`, for example, compares
`abba` with itself and requires `0 4 0`. The generator must emit LF even
on Windows: CRLF expansion makes `max_many_single_letters` and
`max_many_varied_single_letters` exceed the total input limit.

## Language notes

The Python solution runs under PyPy: under CPython 3.12 it exceeds the
time limit on the judge's test 2, while PyPy 3.10 is accepted in 0.75 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2059_strings.cpp](2059_strings.cpp) | G++ 13.2 x64 | strings | O(n + m) | AC | 0.250 s | 12020 KB |
| [2059_strings.go](2059_strings.go) | Go 1.14 x64 | strings | O(n + m) | AC | 0.218 s | 20668 KB |
| [2059_strings.java](2059_strings.java) | Java 1.8 | strings | O(n + m) | AC | 0.296 s | 24520 KB |
| [2059_strings.py](2059_strings.py) | PyPy 3.10 x64 | strings | O(n + m) | AC | 0.750 s | 30004 KB |
| [2059_strings.rs](2059_strings.rs) | Rust 1.75 x64 | strings | O(n + m) | AC | 0.125 s | 22364 KB |
