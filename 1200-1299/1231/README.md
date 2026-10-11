# 1231. A Turing machine that plays a counting-out game

[Timus 1231](https://acm.timus.ru/problem.aspx?space=1&num=1231) · difficulty 2192 · constructive

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tape holds n minuses (1 ≤ n ≤ 200), unknown in advance, with `#` in
every other cell. The minuses stand in a circle; starting from the first,
every k-th minus still standing is crossed out, until one is left. Given
k (1 ≤ k ≤ 200), print the control table of a Turing machine that, for
any n, turns every minus except that one into `+`.

The machine starts in state 1 on the leftmost minus. A row of the table
`state symbol new-state new-symbol move` says what to do on reading a
symbol in a state; the move is `<`, `>` or `=`, and the machine halts
when no row matches. It may write `+`, `#` and `A`–`Z`, cells of the
minuses may only hold `-` and `+`, the remaining minus must never change,
and the head must end on it. Limits: at most 1 000 000 steps, fewer than
10 000 rows, states from 1 to 30 000, at most 5000 cells on each side of
the start.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The integer k.

## Output

The number of rows p (1 < p < 10 000), then the p rows, each as five
items separated by single spaces.

## Checking

Any table is accepted that works for every n. The reference checker runs
it for each n from 1 to 200 and checks the steps, the written symbols,
the minus left and the final position of the head.

## Examples

The statement shows only the format: for k = 2 it gives a five-row
table that crosses out the second minus, which is correct only for
n = 2.

## Solution

The machine does not have to simulate the game: k is known when the
table is printed, so the program solves the game itself for every n with
the Josephus recurrence `pos(n) = (pos(n−1) + k) mod n` and builds the
answers into the table.

- **Counting.** State i means "the head is on cell i". On `-` it moves
  right into state i+1, so on reaching the `#` after the minuses the
  state is n+1 and n is known.
- **Seeking.** That row steps back onto the last minus and enters the
  state "d cells left to go", with d = n−1−pos(n); these states walk left
  until d is 0, and the head is on the minus that stays.
- **Crossing.** Five fixed states step past it, turn everything to its
  right into `+` up to the `#`, walk back over it, cross out everything
  to its left and finally move right over the `+` signs back to it, where
  no row matches and the machine halts.

That is 609 rows and at most 6n steps. `O(N)` with `N = 200`.

Pitfalls:

- the survivor's cell must keep its `-`, so the sweeps pass over it and
  write the same `-` back;
- n = 1 must work too: the machine then crosses nothing and stops on the
  only minus.

The checker runs the table for every n and compares the minus left with
the one the game leaves.

## Language notes

- All languages print the same table, row by row, in the same order.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1231_constructive.cpp](1231_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 152 KB |
| [1231_constructive.go](1231_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 1172 KB |
| [1231_constructive.java](1231_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.093 s | 576 KB |
| [1231_constructive.py](1231_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.062 s | 604 KB |
| [1231_constructive.rs](1231_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 240 KB |
