# 1739. Faryuks

[Timus 1739](https://acm.timus.ru/problem.aspx?space=1&num=1739) · difficulty 1790 · bitmask

Original problem by Alex Samsonov, from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

You are inside a plantation and want to carry out n fruits. Each exit
through the gate may carry any set of fruits, but the alarm stays quiet
only if their total aroma is a whole multiple of 256. Fruits may be
carried back in freely. A deodorant lowers one fruit's aroma by 25%
and a perfume raises one fruit's aroma by 10%; each can be used once in
all, possibly both on the same fruit, and the effect ends when the
fruit passes the gate. Get all the fruits out with the fewest exits and
print the plan, or report that it is impossible.

## Input

n (1 ≤ n ≤ 12), then the n aromas, integers from 1 to 1000.

## Output

`IMPOSSIBLE`, or the number of actions and then the actions:
`take k a1 … ak`, `return s b1 … bs`, `dearomatize p` and
`aromatize q`, at most 20 000 of them. Any plan with the fewest exits
is accepted.

## Examples

### Example 1

Input:

```
3
36 56 200
```

Output:

```
4
take 2 2 3
return 1 3
aromatize 3
take 2 1 3
```

### Example 2

Input:

```
1
100
```

Output:

```
IMPOSSIBLE
```

## Solution

Fruits can be carried back in at no cost, so an exit may take any set
of fruits, already outside or not; only the fruits still inside matter,
and a larger set is never worse. For every way of spraying (none, the
deodorant on fruit i, the perfume on fruit j, or both) list the sets
whose total aroma passes and keep only those not contained in another
one. Aromas are multiplied by 1000, so that 3/4, 11/10 and 33/40 of
them stay whole. The Python, Java and Rust solutions also drop a set
that a set needing fewer sprays contains, which leaves far fewer moves.

Then a dynamic program over the fruits still inside and the sprays used
gives the fewest exits: from a state, an exit with a listed set of an
unused spray kind removes the set from the fruits inside. Replaying the
choices gives the plan: return the needed fruits that are outside,
spray, take. `O(4·2ⁿ·M + n²·2ⁿ)` for M candidate sets before
pruning.

In the first example 56 + 200 = 256 leaves first; then the 200 comes
back, gets the perfume to become 220 and leaves with the 36:
36 + 220 = 256.

Pitfalls:

- a sprayed aroma may not be whole: 0.75·101 and 1.1·36 are fractions,
  and the total must be a whole multiple of 256;
- both sprays may go on one fruit, giving 33/40 of its aroma;
- one fruit alone passes only if its aroma is already 256, 512 or 768:
  no spray turns another aroma from 1 to 1000 into a multiple of 256.

The fewest exits match a breadth-first search over all sets and sprays
with exact fractions on 200 random cases of up to 7 fruits, and an
independent accepted implementation on the large tests; the checker
replays every plan. The Python solution runs on PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1739_bitmask.cpp](1739_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.203 s | 256 KB |
| [1739_bitmask.go](1739_bitmask.go) | Go 1.14 x64 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.218 s | 3188 KB |
| [1739_bitmask.java](1739_bitmask.java) | Java 1.8 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.203 s | 5132 KB |
| [1739_bitmask.py](1739_bitmask.py) | PyPy 3.10 x64 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.250 s | 7292 KB |
| [1739_bitmask.rs](1739_bitmask.rs) | Rust 1.75 x64 | bitmask | O(4·2ⁿ·M + n²·2ⁿ) | AC | 0.031 s | 960 KB |
