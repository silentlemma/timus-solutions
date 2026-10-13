# 1433. Diamonds

[Timus 1433](https://acm.timus.ru/problem.aspx?space=1&num=1433) · difficulty 264 · bruteforce

Original problem by Pavel Egorov and Stanislav Vasiliev, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two regular tetrahedra of the same size have each face painted R, G, B
or Y. The colours are listed in the same order for both: the base, the
front left face, the front right face and the back face. Print "equal"
if one tetrahedron can be turned to look exactly like the other, and
"different" otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Two lines of four letters.

## Output

"equal" or "different".

## Examples

### Example 1

Input:

```
RGRB
GRRB
```

Output:

```
equal
```

## Solution

A turn of a tetrahedron permutes its four faces, and the turns give
exactly the 12 even permutations: a turn about an axis through a corner
moves three faces in a cycle, a half turn about an axis through two
opposite edges swaps two pairs, and an odd permutation, such as one
swap, would be a mirror image. So try all 24 orders of the faces, keep
those with an even number of inversions, and check whether one of them
turns the first colouring into the second. `O(1)`.

Pitfalls:

- mirror images are different: with four distinct colours, swapping two
  faces is not a turn (tests 03, 11);
- with a repeated colour every arrangement of the same colours is equal,
  since swapping the two equal faces fixes the parity (tests 05, 07, 08,
  12).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1433_bruteforce.cpp](1433_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 360 KB |
| [1433_bruteforce.go](1433_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1084 KB |
| [1433_bruteforce.java](1433_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1568 KB |
| [1433_bruteforce.py](1433_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 440 KB |
| [1433_bruteforce.rs](1433_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 224 KB |
