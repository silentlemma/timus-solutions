# 1992. Share learning and undo histories

[Timus 1992](https://acm.timus.ru/problem.aspx?space=1&num=1992) · difficulty 372 · trees, simulation

Original problem by Egor Shchelkonogov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Initially entity 1 has no learned programs and no undo history. Maintain
ordered learning histories under `n` commands, with program identifiers
from `1` through `m`. Learning appends a program and clears that
entity's undo history. Undo removes the last learned program and records
it; redo restores the most recently undone program. Copying creates a
new entity with both current sequences copied. Queries ask for the last
learned program, or `basic` when none is learned.

The bounds are `1≤n,m≤500000`. All commands are valid: referenced
entities already exist, a newly learned program is not currently learned
by that entity, undo has a program to remove, and redo has a record to
restore. A rolled-back program may be learned again. Time limit: 2
seconds; memory limit: 64 MB.

## Input

The first line contains `n m`, followed by `n` commands:

- `learn c p`: learn program `p`, `1≤p≤m`, and clear the undo history of
  entity `c`.
- `rollback c`: undo its last learned program.
- `relearn c`: restore its most recent rollback.
- `clone c`: copy both histories into the next new entity.
- `check c`: query its last learned program.

New entity identifiers increase in creation order, starting after the
initial identifier 1. Copying does not change the source entity.

## Output

For every `check`, in order, print the program identifier or lowercase
`basic` on its own line. If there are no queries, the output is empty.

## Checking

Outputs are compared token by token.

## Examples

Input:

```
9 10
learn 1 5
learn 1 7
rollback 1
check 1
clone 1
relearn 2
check 2
rollback 1
check 1
```

Output:

```
5
7
basic
```

After the first rollback, entity 1 knows program 5 and can redo 7.
Copying preserves both parts. Entity 2 restores 7 while entity 1 remains
unchanged, then the final rollback leaves entity 1 basic.

## Solution

Give each entity two stack heads: `A` for learned programs, most recent
first, and `R` for undone programs, most recent rollback first. All
stacks share one global pool. A node stores `(program, previous)` and is
immutable after creation; index 0 means an empty stack. To push `p` onto
head `h`, allocate a fresh node `(p,h)` and return its index. Popping
reads the node's `previous` index.

Commands act as follows:

- Learn: `A=push(p,A)`, `R=0`.
- Rollback: remember `t=A`, then `A=previous[t]`, `R=push(value[t],R)`.
- Relearn: remember `t=R`, then `R=previous[t]`, `A=push(value[t],A)`.
- Clone: copy the two integer head indices to the new entity.
- Check: print `value[A]` if `A` is nonzero, otherwise `basic`.

Clearing undo history only replaces its head with zero; do not erase
shared nodes. Old nodes may still be reachable from another entity. A
clone shares the underlying immutable tails, while future changes
replace only its own heads. No traversal, list copy or
program-membership set is needed; command validity is guaranteed.

For any nonzero head `h`, define its represented sequence as `value[h]`
followed by the sequence at `previous[h]`; head zero represents the
empty sequence. A new push has exactly the old sequence with its new
element on top. Since existing nodes never change, copying a head
preserves its complete sequence forever, regardless of later updates to
another head.

Induct on commands. Initially both heads represent empty histories.
Learn pushes the requested program and removes the redo sequence.
Rollback moves exactly the top learned program to redo; relearn performs
the inverse move. Clone preserves both represented sequences, and check
reads their correct learned top. Therefore the two represented stacks
always equal the specified histories and every printed answer is
correct.

Each learn, rollback or relearn creates one node; clone and check create
none. There are at most `n` nodes and `n+1` entities. Four arrays of
length `n+2` store values, predecessor indices and the two head tables.
All numbers fit 32 bits. At maximum size their element storage is
`4·4·(500000+2)=8000032` bytes, about 7.63 MiB.

Stack work per command is `O(1)`, total `O(n)` with bounded command
tokens; memory is `O(n)`. Let `I` be input bytes and `B` output bytes.
Go and Rust also retain `I`; C++, Go, Python and Rust buffer `B`. Java
streams output through a buffered writer, using a reusable digit array
instead of allocating a string per numeric answer. In these formats
`B≤7n`, so the total remains linear.

Python uses compact `array('i')` storage and reads one command at a
time; tuples or copied lists for every history would consume too much
memory. Go uses 32-bit arrays and a byte-token reader compatible with
1.14. Java uses `int` arrays and buffered byte input. Rust uses `u32`
node indices, converted when indexing vectors. Copying ordinary lists on
every clone can require quadratic time and memory, especially when many
entities copy a deep history.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1992_trees.cpp](1992_trees.cpp) | G++ 13.2 x64 | trees | O(n) | AC | 0.156 s | 13608 KB |
| [1992_trees.go](1992_trees.go) | Go 1.14 x64 | trees | O(n) | AC | 0.062 s | 32780 KB |
| [1992_trees.java](1992_trees.java) | Java 1.8 | trees | O(n) | AC | 0.171 s | 10724 KB |
| [1992_trees.py](1992_trees.py) | Python 3.12 x64 | trees | O(n) | AC | 0.609 s | 14972 KB |
| [1992_trees.rs](1992_trees.rs) | Rust 1.75 x64 | trees | O(n) | AC | 0.078 s | 13340 KB |
