# 1670. Asterisk

[Timus 1670](https://acm.timus.ru/problem.aspx?space=1&num=1670) · difficulty 1904 · constructive

Original problem by Daniil Ayzenshteyn, from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The operation A * B writes sequence A after sequence B, and a chain of
stars is evaluated from left to right. An expression is a star chain of
sequences in parentheses, and an element of a sequence is a number or a
whole expression, flattened into it. Write the numbers 1 … N in
increasing order and add parentheses, commas and stars so that the
expression evaluates to the given permutation, or print `IMPOSSIBLE`.
The expression must have no spaces and at most 100 000 characters.

## Input

N (1 ≤ N ≤ 10 000), then the permutation.

## Output

The expression or `IMPOSSIBLE`.

## Examples

### Example 1

Input:

```
4
3 4 2 1
```

Output:

```
(1)*(2)*(3,4)
```

### Example 2

Input:

```
6
5 1 2 6 4 3
```

Output:

```
IMPOSSIBLE
```

## Solution

A sequence keeps its parts in order, and a chain s₁ * s₂ * … * s_k gives
s_k … s₂ s₁, its parts in reverse. Since the numbers are written in
increasing order, every part of an expression holds a range of
consecutive values, and the parts come out either with values rising
(a sequence, a direct join) or falling (a star chain, a skew join). These
are exactly the separable permutations, the ones that can be cut again
and again into blocks of consecutive values arranged up or down.

The blocks are found in one pass with a stack of blocks of consecutive
positions holding consecutive values. Each new number is a block; while
the top two blocks have touching value ranges, they join: the lower range
first is a direct join, the higher first a skew one. The permutation is
separable exactly when one block remains. Joining any two neighbours
whose ranges touch never hurts, since a separable arrangement stays
separable after the merge and an arrangement with a 2 4 1 3 or 3 1 4 2
pattern never reduces to one block.

The joins form a binary tree; a run of joins of the same kind is one
node with many parts, since both kinds are associative. A direct node is
written as (part,part,…) and a skew node as part*part*… listing its parts
from the smallest values up, each part in parentheses. Both the stack and
the writing take `O(N)`; the writing uses its own stack, as the tree can
be 10 000 levels deep.

Pitfalls:

- a single number at the top must still be written as (1) (test 03);
- the expression stays short: N − 1 separators, two parentheses per
  sequence and per number standing alone in a star chain, so at most
  about 5N characters besides the 38 894 digits of 1 … 10 000; the
  deepest alternating tree gives about 69 000 (gen4).

A checker parses the expression, checks the numbers and the length and
evaluates it. For every permutation of up to 6 numbers the answer is
`IMPOSSIBLE` exactly when it contains 2 4 1 3 or 3 1 4 2, and the answers
agree with an independent accepted implementation on larger inputs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1670_constructive.cpp](1670_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.031 s | 616 KB |
| [1670_constructive.go](1670_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 6768 KB |
| [1670_constructive.java](1670_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 5520 KB |
| [1670_constructive.py](1670_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.140 s | 4172 KB |
| [1670_constructive.rs](1670_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 1792 KB |
