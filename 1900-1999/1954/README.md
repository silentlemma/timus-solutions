# 1954. Five Palindromes with Parity-Aware Factorization

[Timus 1954](https://acm.timus.ru/problem.aspx?space=1&num=1954) · difficulty 3575 · dp

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Kirill Borozdin).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Split the entire given string into exactly five nonempty contiguous
palindromes, retaining the original character order. A palindrome equals
its reversal. Any valid split is allowed. Limits: 1 second, 64 MB.

## Input

One string s of lowercase English letters, 5≤n=|s|≤100000.

## Output

Print `NO` if no split exists. Otherwise print `YES` and then the five
palindromes, one per line. Concatenating them must reproduce s exactly.

## Checking

A checker verifies that `YES` or `NO` is right and, for `YES`, that the
five printed words are nonempty palindromes forming the string; any
valid split is accepted.

## Examples

```
aaabbcdcaa
```

```
YES
aa
a
bb
cdc
aa
```

```
spaaaaaaarta
```

```
NO
```

```
abacdcxyxzpz
```

```
NO
```

## Solution

First find the minimum odd number r of palindrome parts. Exactly five
parts are possible if and only if r≤5. Necessity is immediate. For
sufficiency, r is 1,3 or 5. While r<5, the string contains at least two
characters more than the number of parts. Either some part has length
at least three or two parts have length two. In the first case split a
palindrome P into its first character, nonempty middle and last character;
all three are palindromes. In the second split both two-character
palindromes into their individual characters. Either operation adds
exactly two parts, keeps every part nonempty, and preserves concatenation.
Repeat at most twice. The assumption n≥5 is essential to this argument.

Keep two costs E[i],O[i] for each prefix: the minimum even/odd number of
parts. Initially E[0]=0 and O[0]=∞. For each palindromic suffix s[j:i],
update O[i] from E[j]+1 and E[i] from O[j]+1, recording j for restoration.
Appending a palindrome flips parity. Every partition has such a last
suffix, so these transitions are necessary and sufficient. Costs above
five can all be represented by the sentinel six: future steps only add
parts. A single unrestricted minimum is insufficient because the minimum
even and odd counts can differ or one parity can be impossible.

An eertree represents each distinct palindrome by a node. Its character
edge adds equal letters on both sides; its suffix link leads to its
longest proper palindromic suffix. Two roots of lengths −1 and 0 handle
odd and even lengths. When appending a character, follow suffix links
until it can surround the current suffix; reuse or create the resulting
node and its suffix link. There are at most n+2 nodes. Store 26 transitions
per node to obtain deterministic access for this fixed alphabet.

Enumerating all suffix palindromes is quadratic on a uniform string.
Group consecutive suffix nodes with equal length difference
d[v]=len[v]−len[link[v]], and jump to the next group with a series link.
For a group leader v at position i, the new predecessor is
b=i−len[series[v]]−d[v]. Initialize both group costs from E[b],O[b].
If link[v] has the same difference, take componentwise minima with its
remembered group costs. Keep the corresponding predecessor index too.
Each group then updates E[i],O[i] by adding one and flipping parity.

The periodic series invariant explains reuse: the earlier group at
i−d[v] has exactly the same predecessor positions except the new b.
Thus remembering the minimizing position preserves both the minimum and
a genuine suffix-palindrome witness. Do not clear group data at every
character and do not shift the stored predecessor by d[v]. Process only
group leaders; there are O(log n) per prefix. The standard series lemma
and construction are described in the [eertree paper](https://arxiv.org/pdf/1506.04862),
Section 4. The parity pair applies the same minimum operation independently
to each component.

If O[n]>5 print NO. Otherwise follow recorded prefix indices, alternating
parity, to recover a minimum odd partition. Reverse it and apply the
two-part-increment operations proved above until exactly five parts remain.
Every restored edge is a nonempty suffix palindrome; the chain starts at
prefix zero, so the pieces reconstruct the entire input.

O(n log n) time and O(26n)=O(n) space, including transition storage and
predecessors. Construction and final output/refinement are linear for
the fixed alphabet. The logarithmic term is the number of series groups.

Exactly five is not equivalent to at most five without tracking parity.
For example, an even alternating string has only odd-length palindromes
and cannot have five parts. Empty middle pieces are forbidden; only split
outer characters from a part of length at least three. Preserve the
predecessor attached to a cached minimum. Allocate two roots in addition
to n nodes, and keep arrays indexed by the prefix length, including zero.

## Language notes

All versions use only the standard library. Python stores transitions and
indices in typed arrays and costs in bytearrays, avoiding one dictionary
and many boxed integers per node. Java uses flat arrays and BufferedReader.
C++, Go and Rust allocate the node capacity once. Root lengths require a
signed type. The final five substrings have total length n; no quadratic
sequence of string concatenations is needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1954_dp.cpp](1954_dp.cpp) | G++ 13.2 x64 | dp | O(n log n) | AC | 0.031 s | 15368 KB |
| [1954_dp.go](1954_dp.go) | Go 1.14 x64 | dp | O(n log n) | AC | 0.046 s | 33204 KB |
| [1954_dp.java](1954_dp.java) | Java 1.8 | dp | O(n log n) | AC | 0.140 s | 17020 KB |
| [1954_dp.py](1954_dp.py) | Python 3.12 x64 | dp | O(n log n) | AC | 0.656 s | 14836 KB |
| [1954_dp.rs](1954_dp.rs) | Rust 1.75 x64 | dp | O(n log n) | AC | 0.031 s | 30280 KB |
