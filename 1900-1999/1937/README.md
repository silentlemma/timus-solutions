# 1937. Two Cyclic Strings Forming a Palindrome

[Timus 1937](https://acm.timus.ru/problem.aspx?space=1&num=1937) · difficulty 1217 · suffix_structures

Original problem from Open Ural FU Championship 2012 | by Olga Soboleva (prepared by Egor Shchelkonogov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose an independent cyclic rotation of each of two strings A,B.
Their concatenation, rotated A followed by rotated B, must equal its
reverse. Find any two starting positions or determine that none exist.
Limits: 1 second, 64 MB.

## Input

Two lines of lowercase Latin letters: A of length n, then B of length m,
where 1≤m<n≤100000. A rotation starts at a chosen character and wraps
around to preserve the original cyclic order.

## Output

Print No if impossible. Otherwise print Yes and, on the next line,
starting positions in A and B, numbered from 1 and bounded by n and m.
Any pair producing a palindromic concatenation is valid.

## Checking

A checker verifies that the printed rotations really form a palindrome;
for `No` it decides independently that no pair exists. Any valid pair is
accepted.

## Examples

```
cdedab
bac
```

```
Yes
5 3
```

```
aaaa
bbb
```

```
No
```

## Solution

Use zero-based positions. Split a length-n rotation of A as U V with
|U|=m and |V|=L=n−m. Then U V Brot is a palindrome exactly when V is
a palindrome and Brot=reverse(U). This separates the middle condition
from rotation membership without trying all n·m pairs.

Let C=reverse(B), P=C+C[:-1]. Its length-m windows are exactly all
rotations of C. Build a suffix automaton of P. Scan the first n+m−1
characters of A+A, maintaining the longest suffix that occurs in P:
follow a character transition when possible; otherwise follow suffix
links until a transition exists, resetting matched length to that
state's maximum length. A match of length at least m certifies the
outer word U at start a=position−m+1. These positions cover all n starts.

Each automaton state stores maximum length, suffix link, transitions
and an occurrence endpoint f. To append a character, create a new state
and add missing transitions while walking suffix links. At the first
existing transition p→q, link to q if len(q)=len(p)+1. Otherwise clone q
with shortened length len(p)+1, copied transitions/link/endpoint, redirect
the affected suffix-link transitions to the clone, and link both q and
the new state to it. This preserves exactly the substring language of P.
The endpoint also certifies every suffix of a matched word, so its last
m characters begin at j=f−m+1 in P. Here 0≤j<m. Reversing C's rotation
at j gives B's rotation at (−j mod m); return a+1 and that position+1.

For the central condition, compute Manacher radii on A+A, using only
L's parity. Odd radii count matching pairs excluding the center; even
radii count pairs around the gap immediately before it. The middle
window at a+m is palindromic iff radius[a+m+floor(L/2)]≥floor(L/2).
Manacher reuses the mirror within the current rightmost palindrome and
extends beyond that boundary, giving linear total work. If no candidate
middle is palindromic, reject before building the automaton.
Every reported pair satisfies both necessary and sufficient conditions.
If the scan finds none, every possible rotation of A has been excluded.

O(n+m) time and space for the fixed 26-letter alphabet. Dense transitions
use O(26m) integers; the automaton has fewer than twice |P| states.
Suffix-link fallback work is amortized by successful character steps.
Java scans at most 26 sparse outgoing transitions, keeping the same bound.

Reverse B before rotation matching, then negate its recovered start.
Match at least m characters, including when the automaton knows a longer
suffix. The last possible start n−1 must be included. Repeated strings
can have several valid second indices. A palindromic middle and a matching
outer must occur at the same start. The strict inequality m<n guarantees
a nonempty middle, whose parity determines the radius convention.

## Language notes

C++, Go, Rust and Python use 32-bit dense transitions and state arrays;
Go int32 and Rust i32 avoid doubling the dominant allocation. Python's
array-based payload at m=99999 is 46,399,304 bytes, plus 800,000 bytes
for one radius array. Java uses primitive head/next/destination/letter
arrays, with at most 3|P|+1 transition slots and byte letters. This leaves
room for the JVM. All indices and encoded table offsets fit 32 bits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1937_suffix_structures.cpp](1937_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(n+m) | AC | 0.046 s | 46824 KB |
| [1937_suffix_structures.go](1937_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(n+m) | AC | 0.062 s | 49928 KB |
| [1937_suffix_structures.java](1937_suffix_structures.java) | Java 1.8 | suffix_structures | O(n+m) | AC | 0.218 s | 16404 KB |
| [1937_suffix_structures.py](1937_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(n+m) | AC | 0.796 s | 47932 KB |
| [1937_suffix_structures.rs](1937_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(n+m) | AC | 0.046 s | 46428 KB |
