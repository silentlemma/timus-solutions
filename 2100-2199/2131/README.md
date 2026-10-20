# 2131. Shortest substring of all marked names and no other name, over time

[Timus 2131](https://acm.timus.ru/problem.aspx?space=1&num=2131) · difficulty 5575 · suffix_structures

Original problem by Mikhail Rubinchik, prepared by Alexander Kulkov, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Team names appear in a standings table one by one; some are marked with
"+" as the coach's teams, and the first name is a marked favourite.
After each new name, find the shortest string that occurs in every
marked name present and in no unmarked name present, printed as the
positions l … r of an occurrence in the favourite name; among the
shortest choose the smallest l, and print "−1 −1" if there is none. The
limits are 2 seconds and 256 MB.

## Input

n, then the n distinct names in order of appearance, lowercase letters
and "_", with a "+" after the marked ones; the total length is at most
2 · 10⁵.

## Output

l and r, or −1 −1, after every name.

## Examples

### Example 1

Input:

```
6
mit_kotiki+
sjtu_koty+
itmo_first
msu_koshki
mipt_alot
spbsu_kot
```

Output:

```
0 0
2 2
4 4
5 6
4 6
-1 -1
```

## Solution

Every candidate is a substring of the favourite. A substring stays
valid from the start until one of two moments: the first unmarked name
that contains it appears, or the first marked name that does not
contain it appears. So each substring has an expiration time, and the
answer after name t is the best substring whose expiration is later
than t.

A suffix automaton of all names together groups the substrings into
states whose strings occur in exactly the same names. For every state
collect, through its subtree of suffix links:

- the earliest end position in the favourite, if it occurs there;
- the first unmarked name containing it;
- the set of marked names containing it, merged small into large, and
  its smallest missing member, which only grows towards the root.

The best string of a state is its shortest one, of length one more than
its suffix link's, ending at the earliest favourite position. Store it
under the state's expiration time, take suffix minima over the times
and read the answer for every moment. The work is O(S log S) for the
total length S, dominated by the set merges.

In the example the first answer is a single letter, "m", the start of
the favourite; when "itmo_first" arrives the shortest choice becomes the
"k" at position 4, later "ot" and then "kot", and once "spbsu_kot"
appears nothing works.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2131_suffix_structures.cpp](2131_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(S log S) | AC | 0.343 s | 80288 KB |
| [2131_suffix_structures.go](2131_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(S log S) | AC | 0.328 s | 110800 KB |
| [2131_suffix_structures.java](2131_suffix_structures.java) | Java 1.8 | suffix_structures | O(S log S) | AC | 0.421 s | 93620 KB |
| [2131_suffix_structures.py](2131_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(S log S) | AC | 1.609 s | 148908 KB |
| [2131_suffix_structures.rs](2131_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(S log S) | AC | 0.218 s | 73324 KB |
