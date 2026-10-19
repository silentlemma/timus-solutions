# 2040. New palindrome values after each letter

[Timus 2040](https://acm.timus.ru/problem.aspx?space=1&num=2040) · difficulty 861 · strings

Original problem by Mikhail Rubinchik, prepared by Kirill Borozdin, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For every nonempty prefix of a word, report how many new distinct
nonempty palindrome substring values appeared when its last letter was
appended. Equal strings at different positions are one value;
occurrences are not counted separately.

## Input

One word consisting only of lowercase `a` and `b`, of length
`1≤n≤5000000`. Time limit: 0.5 seconds. Memory limit: 100 MB. The
official note guarantees a sufficiently fast C++ solution, but
explicitly makes no such guarantee for other languages, including Java.

## Output

Exactly `n` digits in order, without spaces. Digit `i` is the number of
distinct nonempty palindromes in the prefix of length `i` minus that
number in the previous prefix. The first digit is `1`. The argument
below proves that every digit is `0` or `1`.

## Checking

Outputs are compared token by token.

## Examples

```
abbbba
```

```
111111
```

The newly introduced values are respectively `a`, `b`, `bb`, `bbb`,
`bbbb` and `abbbba`, so all six digits are one. This is not true for
every binary word: `aababbaa` produces `11111110`. Its last letter
introduces no new palindrome value.

## Solution

### At most one new palindrome

A new substring must end at the new last position. Suppose two new
palindromic suffixes were different, with `|U|>|V|`. Since both are
palindromes, suffix `V` of palindrome `U` is also a prefix of `U`. That
occurrence ends earlier, contradicting that `V` is new. Thus at most one
value is new, and it can only be the longest palindromic suffix. There
are at most `n` distinct nonempty palindrome nodes in total.

### A binary palindromic tree

Each node represents one palindrome. Store its length, a suffix link to
its longest proper palindromic suffix, and two labeled transitions: `c`
leads from `P` to `cPc`. Two roots represent length zero and an
artificial length minus one. The artificial root allows a length-one
palindrome; its self-link ends every failed extension search. Node zero
is this root, node one is the empty root, and zero transition entries
mean absent edges; real palindrome nodes start at two.

Maintain `last`, the longest palindrome suffix of the processed prefix.
At position `p` with character `c`, follow links from `last` until a
node `P` satisfies `p-1-length(P)≥0` and the character there equals `c`.
The imaginary root always satisfies it. Suffix links enumerate
candidates in decreasing length, so the first match gives the new
longest palindrome suffix `cPc`.

If that transition exists, its value occurred before: output zero and
reuse the node. Otherwise create exactly one node, set its length to
`length(P)+2`, add the transition, and output one. A new length-one node
links to the empty root. For a longer new node, follow links starting
from `link(P)` with the same extension test; the matched node's `c`
transition is the new suffix link. Every proper palindrome suffix has a
proper palindromic suffix of `P` as its interior, so this finds the
longest one. Its target already exists, because there cannot be two new
palindromes at this position.

Every palindrome's interior appeared before its last letter. Together
with the unique representation `cPc`, this proves that edges identify
exactly the previously seen palindrome values. Inductively, the two
searches maintain the longest suffix and every new suffix link
correctly. A newly created node is exactly a new distinct value, so the
emitted digits solve the task.

### Why both searches are linear in total

Let `F_i` be the longest suffix palindrome length after `i` letters,
with `F_0=0`. The first search starts at `F_(i-1)` and ends at `F_i-2`;
every link step decreases length by at least one. Its number of steps is
at most `F_(i-1)+2-F_i`. Summing telescopes to at most `2n`.

For the second search let `G_i` be the length of the longest proper
palindrome suffix of the current longest palindrome, and `G_0=-1`. A
proper suffix `W` of the new longest, if of length at least two, has an
interior which is a palindrome suffix of the previous prefix. Since
`|W|<F_i≤F_(i-1)+2`, that interior is a proper suffix of the old
longest, so `G_i≤G_(i-1)+2`. Length-zero and length-one suffixes obey
the same bound. The second search begins at a length at most `G_(i-1)`
and finishes at `G_i-2`. Its cost is therefore at most `G_(i-1)+2-G_i`.
On steps where this search is unnecessary its zero cost also satisfies
that nonnegative bound. The sum is again `O(n)`. Constant-time binary
transitions give total tree work `O(n)`, including node creation.

### Representation and resources

C++ uses four 32-bit fields per node, not four machine-sized
indices. For `n=5000000` the node buffers contain at most
`16(n+2)=80000032` bytes; input, output and runtime memory must also
fit. Python uses four typed integer arrays, not millions of Python node
objects, and writes its result bytearray without making another full
copy.

Java uses four unsigned three-byte fields per node, or `12(n+2)` bytes.
All node IDs and `length+1` are below `2^23`; storing length plus one
encodes the artificial root as zero. It also reuses the input bytes for
output: the bit of value four is absent in both ASCII `a` and `b`. Set
it when a new palindrome is created, mask it out for subsequent
character comparisons, and only after processing the whole word convert
these marks to `0`/`1` in place. No later palindrome comparison then
needs the original letters. Output only the original word's range,
excluding whitespace and unused buffer capacity.

The tree, the input and the answer take O(n) memory; Java reserves a
fixed input buffer of 5 000 002 bytes. Read and write the whole digit
string as bytes, not millions of separately formatted numbers.

The Python solution runs under PyPy: under CPython 3.12 it exceeds the
time limit on the judge's test 9, while PyPy 3.10 is accepted in 0.375 s
with 92 MB of the 100 MB. Go and Rust read the word into one buffer of
fixed size, mark the answer in it like the others and keep the tree in
four arrays of 32-bit integers, about 85 MB in all; earlier versions of
them did not compile on the judge.

Count distinct values, not occurrences, and exclude the empty
palindrome. A missing edge creates one answer digit; merely finding
another occurrence does not. Reset the candidate to the parent's suffix
link for the second search. Keep the imaginary root’s logical length at
minus one; packed storage uses an explicit offset. Avoid 64-bit indices
per field, UTF-16 copies of the whole input, and an extra copy of the
Python output. Small all-one examples cannot replace tests with zero
digits and long suffix-link failures.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2040_strings.cpp](2040_strings.cpp) | G++ 13.2 x64 | strings | O(n+N) | AC | 0.125 s | 88880 KB |
| [2040_strings.go](2040_strings.go) | Go 1.14 x64 | strings | O(n+N) | AC | 0.109 s | 87324 KB |
| [2040_strings.java](2040_strings.java) | Java 1.8 | strings | O(n+N) | AC | 0.390 s | 69240 KB |
| [2040_strings.py](2040_strings.py) | PyPy 3.10 x64 | strings | O(n+N) | AC | 0.375 s | 93844 KB |
| [2040_strings.rs](2040_strings.rs) | Rust 1.75 x64 | strings | O(n+N) | AC | 0.109 s | 83068 KB |
