# 2029. Distance to an arbitrary disk state

[Timus 2029](https://acm.timus.ru/problem.aspx?space=1&num=2029) · difficulty 601 · math

Original problem by Nikita Sivukhin and Édouard Lucas, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are three pegs `A`, `B`, `C` and `n` disks of distinct sizes 1
through `n`. Initially every disk is on `A`, with smaller disks above
larger ones. A move takes one top disk to another peg, which must be
empty or have a larger disk on top. Find the minimum moves to a given
target assignment. String position `i`, numbered from one, specifies the
peg of disk size `i`: the smallest disk is written first. The order
within each peg is determined by size, so every string over `A,B,C` is a
valid state.

Constraints: `1 ≤ n ≤ 50`, 1 second, 64 MB. The statement guarantees any
existing answer is at most `10^18`; in fact all allowed states are
reachable and need at most `2^n-1` moves.

## Input

The first line contains `n`, the second exactly `n` uppercase letters
`A`, `B`, `C`.

## Output

Print the minimum number of moves. The format permits `-1` for an
unreachable state, but the proof below shows that every legal input here
is reachable.

## Checking

Outputs are compared token by token.

## Examples

```
1
A
```

```
0
```

```
4
BBBB
```

```
15
```

```
7
BCCBABC
```

```
95
```

## Solution

Consider a subproblem where all `m` smaller disks start on one peg `s`.
Inspect disk `m`, the largest remaining disk. If its target peg is also
`s`, leave it in place and solve the smaller subproblem with the same
start peg. Otherwise let its target be `d` and the remaining peg be `u`.
Transfer all `m-1` smaller disks from `s` to `u`, move disk `m` to `d`,
then solve the smaller target starting from corner `u`. The first two
parts cost `(2^(m-1)-1)+1 = 2^(m-1)`.

Why is this optimal? First recall the whole-tower transfer cost
`T(m)=2^m-1`. Before the first move of disk `m`, every smaller disk must
form a tower on the third peg, requiring at least `T(m-1)` moves. After
its last move onto the destination, another `T(m-1)` moves are needed
for the smaller tower. One largest-disk move and the usual recursive
construction give `T(m)=2T(m-1)+1`.

The construction for an arbitrary target inductively uses at most `2^m-1` moves:
either only smaller disks move, or the transfer and largest move cost `2^(m-1)`
followed by at most `2^(m-1)-1` moves. This also proves reachability.

Smaller-disk moves remain legal regardless of the largest disk's
location, since all of them fit on it or on a bare peg. If the largest
disk visits the same peg twice, remove its moves between those visits
while keeping every smaller-disk move. The result is still legal and
strictly shorter, with the same ending state. Thus its peg route in an
optimal solution is simple. If its start and target agree, it never
moves. If they differ, the only simple alternatives are one direct move
or two through `u`. The two-move route `s→u→d` first requires the
smaller tower from `s` to `d`, then from `d` to `s`, plus two largest
moves: at least `2T(m-1)+2 = 2^m` moves. This is already worse than the
direct construction. Hence the largest disk moves exactly once when its
target differs, and the recurrence above is optimal.

Implement the recurrence iteratively. Start with `source = A` and answer
zero, scanning string indices from `n-1` down to 0. If the target at
index `i` differs from `source`, add `2^i` and replace `source` with the
third peg. Otherwise do nothing. Encode pegs as 0, 1, 2; for distinct
pegs the third is `3-source-target`. Here `source` is the start corner
of the remaining smaller subproblem.

The first sample already equals the start, giving zero. The second
transfers a whole four-disk tower, giving `2^4-1=15`. For `BCCBABC`, the
largest-first scan adds `64+16+8+4+2+1=95`; disk 6 already matches its
current subproblem's source.

Time is `O(n)` and the scan uses `O(1)` state. Buffered input storage is
`O(n)`. No move sequence or exponential state graph is constructed by
the submitted programs.

Pitfalls:

- The input is smallest first, while the calculation runs largest first.
- Update the source peg of the smaller subproblem only when adding a
  contribution.
- Do not restrict the target to one fixed optimal route from an all-`A`
  to an all-`B` tower.
- Use an integer 64-bit shift. `2^50-1 = 1125899906842623` exceeds 32-bit range.
- The generic unreachable case never occurs for a valid assignment in
  this problem.

## Language notes

C++ uses `1LL`, Go `int64(1)`, Java `1L`, and Rust `1_u64` before
shifting. Python integers are exact. Peg indices fit ordinary integers;
Rust's unsigned third-peg calculation is safe inside the distinct-peg
branch. No floating-point powers are needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2029_math.cpp](2029_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 436 KB |
| [2029_math.go](2029_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1080 KB |
| [2029_math.java](2029_math.java) | Java 1.8 | math | O(n) | AC | 0.093 s | 400 KB |
| [2029_math.py](2029_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 484 KB |
| [2029_math.rs](2029_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 232 KB |
