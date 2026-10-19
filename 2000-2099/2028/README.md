# 2028. Generate a triangular-sum grid program

[Timus 2028](https://acm.timus.ru/problem.aspx?space=1&num=2028) · difficulty 880 · constructive

Original problem by Kirill Borozdin, from the Ural Regional Team Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Output a fixed program in the grid language described below. When that
program receives one integer `n`, for every `1 ≤ n ≤ 100`, it must
output exactly one integer `1+2+…+n` and halt normally. Any valid
program is accepted. The generator itself does not receive `n`. Its only
input is the line `Good luck!`, which may be ignored. Generator limits:
1 second, 64 MB.

The generated program is an `H×W` grid with `1 ≤ H,W ≤ 100`. It has one
current register and 26 memory registers `A`…`Z`, all initially zero.
The pointer starts in the top-left cell facing right. Each tick executes
one instruction, then moves one cell in the resulting direction, without
wrapping.

| Instruction | Meaning |
| --- | --- |
| `^`, `>`, `v`, `<` | Set direction up, right, down, left respectively. |
| `.` | Do nothing. |
| `A`…`Z` | Swap the current register with the named memory register. |
| `?` | Read into the current register; repeated reads after the one input reuse `n`. |
| `!` | Output the current value, then clear it to zero. |
| `+`, `-` | Add or subtract one from the current value. |
| `@` | Turn counterclockwise for zero, clockwise for any nonzero value. |
| `#` | Halt immediately, without movement. |

A current value of absolute value greater than 100000 causes `OVERFLOW
ERROR` before movement. Moving outside the grid causes `RUNTIME ERROR`.
Completing 1000000 ticks without a halt or earlier error causes `TIME
LIMIT EXCEEDED`. The required program must avoid all these errors;
printing the correct number before an error is insufficient.

## Input

Exactly the single line `Good luck!`. This belongs to the generator. The
generated program's separate input is the one integer `n`.

## Output

Print `H W` and then exactly `H` instruction rows of width `W`. Use only
the operators above. The resulting program must solve every allowed
target input, not just one value.

## Checking

A checker runs the printed program for every n from 1 to 100 and accepts
it when each run prints exactly the right sum once and halts normally.
The program in the official example only shows the format and is not a
correct answer, so the stored example output is marked `format_only` and
is not checked.

## Examples

```
Good luck!
```

```
4 6
?A?v>v
>..>@A
-...A!
^A.+<#
```
This official example illustrates only the output format. Its program
does not solve the task: on target input 1 it outputs 2 instead of 1.
Our generators output the correct program below, so their output
intentionally differs from this illustration.

## Solution

```text
6 11
>?v........
.>>.......v
..@A+AB+B-<
..B........
..-........
.^@A!#.....
```
Use register `A` as the accumulated sum and `B` as a temporary counter.
The current register holds an outer count `q`, initially `n`. For each
`q = n,n-1,…,1`, add `q` units to `A`, restore `q` from `B`, then
decrement it. When the count becomes zero, swap `A` into the current
register, output it and halt.

The inner macro is `-B+BA+A`. It decreases the current value by one,
increments `B` through a swap, increment and swap back, then similarly
increments `A`. Thus after `j` iterations the state is current `q-j`, `B
= j`, and `A = old_sum+j`. At `j=q`, the current value is zero, `B=q`,
and the entire `q` has been added to `A`. The exit `B-` restores `q`,
clears `B`, and leaves `q-1` in the current register.

In zero-based coordinates, the inner `@` is at `(2,2)` and is approached
moving left. Nonzero turns upward into the top side of the inner
rectangle; zero turns downward to `B-`. The body is traversed right to
left, so its printed order is reversed. The outer `@` at `(5,2)` is
approached downward. Nonzero turns left into `^` and the return
corridor, reaching `(1,1)` and `(1,2)` before the next inner loop. Zero
turns right into `A!#`. The input at `(0,1)` is visited only once.

The outer invariant is current `q`, `B=0`, and `A` equal to the sum of
already completed values `n` down to `q+1`. The inner invariant above
proves that one outer iteration adds exactly `q` and restores the
invariant for `q-1`. Eventually `q=0`, so `A` is `1+…+n`; the only
output occurs on the final exit and is followed by normal termination.
All values remain between 0 and 5050, and every traversed cell is inside
the 6×11 grid.

Let `S=n(n+1)/2`. There are three initial ticks, 18 ticks per added
unit, eight between consecutive outer iterations, and six on the final
exit. The exact total is `3+18S+8(n-1)+6 = 18S+8n+1`, at most 91701 for
`n=100`, below the million-tick limit.

The generator prints a fixed 66-cell program, so its time and space are
`O(1)`. The emitted program runs in `O(n²)` time and uses `O(1)`
registers. These are different execution stages: computing a formula in
the generator would not supply a working grid program.

Pitfalls:

- Keep the format-only official example, but never treat it as a correct
  solution.
- The host input is not `n`; every target value must be handled by the
  emitted program.
- Memory letters swap values. The inner macro must restore the current
  counter after each increment.
- Check the approach direction at both `@` cells and reverse the printed
  inner body.
- Require one correct output followed by a normal halt; errors after
  output remain invalid.

## Language notes

All five generators print the same literal instruction rows with named
height and width constants. They may ignore their input. Fixed output is
the required construction: the printed program implements the loop
algorithm for all target values. Dots are actual no-op instructions, so
preserve row widths and directions exactly.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2028_constructive.cpp](2028_constructive.cpp) | G++ 13.2 x64 | constructive | O(1) | AC | 0.001 s | 356 KB |
| [2028_constructive.go](2028_constructive.go) | Go 1.14 x64 | constructive | O(1) | AC | 0.001 s | 1024 KB |
| [2028_constructive.java](2028_constructive.java) | Java 1.8 | constructive | O(1) | AC | 0.078 s | 304 KB |
| [2028_constructive.py](2028_constructive.py) | Python 3.12 x64 | constructive | O(1) | AC | 0.046 s | 248 KB |
| [2028_constructive.rs](2028_constructive.rs) | Rust 1.75 x64 | constructive | O(1) | AC | 0.001 s | 184 KB |
