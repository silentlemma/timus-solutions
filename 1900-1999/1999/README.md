# 1999. Shifting the numeric language of a decimal automaton

[Timus 1999](https://acm.timus.ru/problem.aspx?space=1&num=1999) · difficulty 5674 · constructive

Original problem by Denis Dublennykh, prepared by Eugene Kurpilyansky.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A deterministic automaton reads a nonnegative decimal integer from left
to right. Leading zeroes do not change the number's verdict. Its first
state is initial and nonterminal, so an empty identifier is rejected.
Construct an automaton accepting exactly the numbers obtained by adding
`k` to the old accepted numbers. The result must also reject the empty
identifier and handle leading zeroes consistently.

The old automaton has `1≤n≤100` states and `1≤k≤8`. Output at most 25600
states. Time limit 1 second, memory 64 MB. The construction below always
fits under these assumptions, so `Impossible` is unnecessary.

## Input

First `k`, then `n`, then `n` terminal flags, each 0 or 1. Each of the
next `n` rows contains the destination states for digits 0 through 9,
using one-based numbering. State 1 is initial.

## Output

Print `Success` and a new automaton in the same format without `k`. Any
correct automaton with at most 25600 states is accepted; it need not be
minimal or use the example's numbering. The statement also allows
`Impossible` when no automaton exists, but the construction proves
existence here.

## Checking

A checker builds the product of the printed automaton and the old one
shifted by k and verifies that they accept the same numbers, the size
limit and the treatment of the empty identifier; any valid automaton is
accepted.

## Examples

```
3
4
0 0 1 0
1 2 4 4 4 4 4 4 4 4
4 2 4 4 4 4 4 4 3 4
4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4
```

```
Success
5
0 0 0 0 1
1 2 3 4 4 4 4 4 4 4
4 2 3 4 4 4 4 4 4 4
4 5 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4
4 4 4 4 4 4 4 4 4 4
```

The old machine accepts 18, 118, 1118, and so on, with optional leading
zeroes. Adding 3 gives 21, 121, 1121, and so on, which the displayed
five-state machine accepts. Our construction has eight reachable states
for this input and recognizes exactly the same language.

## Solution

Let `δ` be the old transition function and `T` its terminal flags. For a
processed prefix `s` of numeric value `v`, keep a state `(q,r,b)`:

- `q` is the old state after reading `s`.
- If `v>0`, `r` is the old state after reading `v−1` padded with zeroes
  to the length of `s`; otherwise `r` is a special invalid value `n`.
- `b` is the required acceptance verdict for the current prefix viewed
  as a new identifier.

The initial state is `(0,n,0)` in zero-based internal numbering. Append
digit `d`. The next normal state is `q'=δ(q,d)`. For the predecessor
state, if `d>0` set `r'=δ(q,d−1)`; otherwise keep it invalid if `r` is
invalid, or set `r'=δ(r,9)`. This follows from `10v−1=10(v−1)+9` when
`v>0`.

The next acceptance bit is determined from the previous `q,r` and the
current digit:

- If `d≥k`, set `b'=T[δ(q,d−k)]`.
- If `d<k` and `r` is valid, set `b'=T[δ(r,d+10−k)]`.
- Otherwise the new value is below `k`, so set `b'=0`.

These are exactly the no-borrow and borrow cases of subtracting a single
digit. Induction proves the two state invariants and that `b'` accepts
precisely when the new number minus `k` is nonnegative and accepted by
the old machine. Zero padding is harmless by the given old-language
convention. In particular, an old accepted zero is read as a nonempty
zero string, not as an empty identifier. The new empty string and all
numbers below `k` are rejected.

There are at most `2n(n+1)≤20200` tuples: `n` normal states, `n+1`
predecessor states and two verdict bits. Enumerate only reachable tuples
in BFS order and assign the first tuple state 1. A dense identifier
table indexed by `2·(q·(n+1)+r)+b` avoids hashing. Use `b` as the
terminal flag and emit all ten transitions. All-zero prefixes retain an
invalid predecessor and a false verdict; general leading zeroes preserve
the language because subtraction produces the same padded old number.

### Complexity

With decimal alphabet fixed, time and memory are `O(n²)`, including the
output transition table. There are at most 20200 reachable states and
202000 output transitions. Only small state indices are used; no
identifier is converted to a bounded machine integer.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1999_constructive.cpp](1999_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.031 s | 840 KB |
| [1999_constructive.go](1999_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 7720 KB |
| [1999_constructive.java](1999_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.109 s | 5124 KB |
| [1999_constructive.py](1999_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.187 s | 6440 KB |
| [1999_constructive.rs](1999_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 2444 KB |
