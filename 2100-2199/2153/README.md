# 2153. Largest party of distinct roles and which recruit would help

[Timus 2153](https://acm.timus.ru/problem.aspx?space=1&num=2153) · difficulty 960 · dp, bitmask

Original problem by Valentin Zuev, from the Ural School Programming Contest 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n guild members has a non-empty set of the four qualifications
warrior, mage, cleric and rogue. A party gives distinct members distinct
roles from their qualifications. Find the largest party, and if it has
fewer than four members, list the qualifications for which hiring one
person with only that qualification would make the largest party
bigger. The limits are 0.5 seconds and 256 MB.

## Input

n, 1 ≤ n ≤ 15, then each member's qualifications as a subsequence of
"WMCR".

## Output

The largest size, and if it is below 4, a line "Looking for" with the
qualifications in the order warrior, mage, cleric, rogue.

## Examples

### Example 1

Input:

```
1
W
```

Output:

```
1
Looking for mage cleric rogue
```

### Example 2

Input:

```
2
M
CR
```

Output:

```
2
Looking for warrior cleric rogue
```

### Example 3

Input:

```
4
WMCR
WMCR
WMCR
WMCR
```

Output:

```
4
```

### Example 4

Input:

```
1
WMCR
```

Output:

```
1
Looking for warrior mage cleric rogue
```

## Solution

There are only 16 sets of roles. A DP over the members keeps which role
sets can be filled by distinct members so far: a member either stays
out or takes one free role of the set. Going through the sets in
decreasing order inside one member's step keeps the member from taking
two roles. The largest party is the largest reachable set.

A newcomer with only qualification r makes the party bigger exactly
when some largest set does not use r: that set plus the newcomer is
larger, and if every largest set used r, a bigger party would contain a
reachable set of the old maximum size without r. So the
advertisement lists the roles outside the intersection of all largest
reachable sets. The work is O(16 · 4 · n).

In the second example the largest parties are {mage, cleric} and
{mage, rogue}; their intersection is {mage}, so warriors, clerics and
rogues are wanted.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2153_dp_bitmask.cpp](2153_dp_bitmask.cpp) | G++ 13.2 x64 | dp, bitmask | O(64 n) | AC | 0.015 s | 448 KB |
| [2153_dp_bitmask.go](2153_dp_bitmask.go) | Go 1.14 x64 | dp, bitmask | O(64 n) | AC | 0.031 s | 1168 KB |
| [2153_dp_bitmask.java](2153_dp_bitmask.java) | Java 1.8 | dp, bitmask | O(64 n) | AC | 0.078 s | 392 KB |
| [2153_dp_bitmask.py](2153_dp_bitmask.py) | Python 3.12 x64 | dp, bitmask | O(64 n) | AC | 0.109 s | 640 KB |
| [2153_dp_bitmask.rs](2153_dp_bitmask.rs) | Rust 1.75 x64 | dp, bitmask | O(64 n) | AC | 0.046 s | 244 KB |
