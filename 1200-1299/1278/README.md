# 1278. "… Connecting people"

[Timus 1278](https://acm.timus.ru/problem.aspx?space=1&num=1278) · difficulty 988 · constructive

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sound processor knows two commands, one per memory cell. `CALL X`
pushes the next cell's address on a stack of 100 cells and jumps to cell
X. `BELL&RET` sounds once, then returns to the address on top of the
stack, or stops if the stack is empty. Execution starts at cell 0. Write
a program of at most 100 commands, with a single `BELL&RET` as the last
one, that sounds exactly K times (1 ≤ K ≤ 10⁹).

Time limit: 1 second. Memory limit: 64 MB.

## Input

K.

## Output

The program, one command per line, cell 0 first.

## Checking

Many programs work, so the checker accepts any: it checks the form of
every line and that every call points forward. It then counts the
bells made from each cell, from the last one up, and checks the stack
depth and the total.

## Examples

### Example 1

Input:

```
4
```

Output:

```
CALL 1
CALL 2
BELL&RET
```

### Example 2

Input:

```
1
```

Output:

```
BELL&RET
```

## Solution

Let bells(i) be the number of sounds made when the processor runs from
cell i until that run returns. The last cell gives bells = 1. A command
`CALL X` at cell i first runs from X and then from i + 1, so
bells(i) = bells(X) + bells(i + 1). Two choices of X are enough:

- `CALL i+1` doubles: bells(i) = 2 · bells(i + 1);
- a call of the last cell adds one: bells(i) = bells(i + 1) + 1.

Going up from the last cell, start at 1 and follow the binary digits of
K after the leading one: double for each digit, and add one more for
each digit 1. K below 2³⁰ needs at most 29 doublings and 29 additions,
59 cells with the bell. Every call points forward, so the stack holds
at most one address per cell. `O(log K)`.

Pitfalls:

- with K = 1 the program is `BELL&RET` alone (test 02);
- a call to the same or an earlier cell runs into itself forever and
  overflows the stack, so no call may point backwards;
- the program is read from cell 0, so the cells built from the bottom
  up are printed in reverse.

Every K up to 299 was also run on a literal model of the processor, and
the checker passes the answers for all tests.

## Language notes

- All languages walk the binary digits of K the same way.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1278_constructive.cpp](1278_constructive.cpp) | G++ 13.2 x64 | constructive | O(log K) | AC | 0.015 s | 192 KB |
| [1278_constructive.go](1278_constructive.go) | Go 1.14 x64 | constructive | O(log K) | AC | 0.031 s | 1096 KB |
| [1278_constructive.java](1278_constructive.java) | Java 1.8 | constructive | O(log K) | AC | 0.109 s | 1656 KB |
| [1278_constructive.py](1278_constructive.py) | Python 3.12 x64 | constructive | O(log K) | AC | 0.093 s | 448 KB |
| [1278_constructive.rs](1278_constructive.rs) | Rust 1.75 x64 | constructive | O(log K) | AC | 0.015 s | 244 KB |
