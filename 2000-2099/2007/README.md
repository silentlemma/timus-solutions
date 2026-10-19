# 2007. The Smallest String After All Letter Operations

[Timus 2007](https://acm.timus.ru/problem.aspx?space=1&num=2007) · difficulty 1922 · strings, greedy

Original problem by Ilya Kuchumov, from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a string and a multiset of letter modifiers, use every modifier
exactly once, in any order. A modifier `c` either inserts `c` anywhere,
including either end, or deletes one currently present `c`. Inserted
letters may later be deleted. Find the lexicographically smallest
obtainable final string. A shorter proper prefix is smaller. It is
guaranteed that no sequence using all modifiers produces the empty
string.

## Input

Two nonempty lines: the original string `S` and the modifiers `T`. Both
contain only lowercase Latin letters and each has length at most 100000.
The order of modifiers in the input imposes no restriction. Time 0.5
seconds, memory 64 MB.

## Output

The smallest obtainable string, nonempty by the guarantee. Its length is
at most `|S|+|T|`.

## Checking

Outputs are compared token by token.

## Examples

```
abc
bbc
```

```
ab
```

Delete `c` with its modifier and consume the two `b` modifiers by
inserting and deleting one extra `b`. This leaves `ab`.

## Solution

### Greedy rule

At a state let `R[c]` count remaining original letters and `K[c]`
remaining modifiers. An empty completion is possible exactly when every
`K[c]≥R[c]` and `K[c]−R[c]` is even: delete the originals, then consume
surplus equal-letter pairs by insertion followed by deletion. If this
holds, stop immediately; no extension beats the current prefix.

Otherwise choose the smallest feasible next letter. It can be an
inserted letter with positive modifier count, or an original occurrence
whose preceding original prefix can all be deleted within the available
per-letter counts. Prefer the earliest such original occurrence on
equality with insertion, delete its preceding prefix, and keep it. If
insertion is smaller, consume that modifier and output it.

### Why the tie rule is correct

Remaining original letters preserve their relative order; other
surviving letters are inserted. An inserted letter later deleted
consumes a neutral pair of equal modifiers. These operations can be
reordered into this description without changing the result.

Suppose the selected original `c` occurs after prefix `X`, with suffix
`Z`. Every letter of `X` is greater than `c`: each position of `X` is
itself accessible, and an earlier `c` would have been chosen. No
available modifier is smaller than `c`. If an answer keeps a later
original `c`, swap which occurrence survives; deleting that later copy
instead preserves counts and the result. Thus the earliest original is
sufficient.

Compare keeping this `c` with inserting `c` first. Consider any
completion after the insertion. If all originals in `X` are deleted and
the original `c` survives, keep it for the first output instead and
insert `c` at its former output location. This preserves the result and
modifier usage. If that original `c` is deleted, keep it first and use
the two freed `c` modifiers as a neutral pair. Again the same result is
obtainable after deleting `X` early.

If some original of `X` survives, the output before its first surviving
letter consists only of inserted letters, all at least `c`. The
continuation has an initial run `c^r` followed by a larger letter. These
`r` letters were inserted, so `r≤K[c]−1`, since the initial insertion
already spent one modifier. Keeping the original leaves all `K[c]`
modifiers of `c`, because `X` contains none. It can output `r+1` further
copies of `c` and then complete legally by keeping the suffix and
inserting any remaining modifiers. This is strictly smaller than the
insertion-first continuation.

Therefore keeping the original is never worse. The smallest feasible
next character, this tie rule and the empty-completion test prove the
algorithm by induction on the remaining operations and originals.

### Efficient implementation

For each letter store its original positions, a consumed-position count
`head[c]`, and a sentinel `n=|S|`. Set `cut[c]=head[c]+K[c]`. Its first
undeletable occurrence is at `positions[c][cut[c]]`, or `n` beyond the
list. Let `r` be the minimum of these positions. The next original
occurrence of any letter is accessible exactly when its position is at
most `r`, including `r` itself.

Deleting a prefix letter decrements `K` and increments `head`, leaving
`cut` unchanged. Keeping a letter increments its `cut`; inserting
decrements it. Also `delta[c]=cut[c]−initial_frequency[c]=K[c]−R[c]`. A
bit mask records negative or odd deltas, so the stopping test needs only
an update of the chosen letter. Other masks record present original
letters and available modifiers.

Cache the smallest accessible original until an original is kept. An
insertion is chosen only for a strictly smaller letter `c`, which has no
original in the currently reachable prefix. Decreasing its quota cannot
move the first undeletable occurrence before its first remaining
occurrence, which is beyond `r`. Thus the cached choice remains valid
throughout an insertion run. If the current original has no matching
modifier, it is the only accessible original and needs no search.

There are at most `n+1` original queries, each inspecting at most `A=26`
letters; every original is consumed once and at most `m=|T|` insertions
occur. Time `O(A n+m+A)`, hence `O(n+m)` for this fixed alphabet. Memory
`O(n+m+A)` including the output. No data structure proportional to the
number of operation sequences is stored.

## Language notes

Using every modifier is mandatory, but neutral pairs need not remain in
the answer. Test for an empty completion before selecting another
letter. The initial guarantee does not prevent an empty suffix later.
Prefer originals on equal letters, include the first undeletable
position in the accessible range, and invalidate the cache after keeping
an original. Bounds-check `cut` before indexing; modifier counts and
original counts differ. All five ports use position arrays, 26-bit masks
and iterative loops; bit-scan operations are called only on nonzero
masks.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2007_strings_greedy.cpp](2007_strings_greedy.cpp) | G++ 13.2 x64 | strings, greedy | O(n + m) | AC | 0.015 s | 1580 KB |
| [2007_strings_greedy.go](2007_strings_greedy.go) | Go 1.14 x64 | strings, greedy | O(n + m) | AC | 0.031 s | 7340 KB |
| [2007_strings_greedy.java](2007_strings_greedy.java) | Java 1.8 | strings, greedy | O(n + m) | AC | 0.125 s | 3008 KB |
| [2007_strings_greedy.py](2007_strings_greedy.py) | Python 3.12 x64 | strings, greedy | O(n + m) | AC | 0.359 s | 5864 KB |
| [2007_strings_greedy.rs](2007_strings_greedy.rs) | Rust 1.75 x64 | strings, greedy | O(n + m) | AC | 0.015 s | 2156 KB |
