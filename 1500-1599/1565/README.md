# 1565. The Duel for Three

[Timus 1565](https://acm.timus.ru/problem.aspx?space=1&num=1565) · difficulty 1785 · games

Original problem by Sergey Pupyrev, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three duellists A, B and C hit with probabilities 1, b and c (b ≠ c),
and a hit kills. A fair lot sets the order, and they take turns in that
order, skipping the dead, until only one is left; each shot may go at
either opponent or into the air. A always shoots the most accurate
living opponent. B and C choose the shot that gives them the best
chance to survive, and on a tie shoot the strongest opponent. Print the
survival chances of A, B and C with at least five digits after the
point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The three accuracies.

## Output

The three chances on one line.

## Examples

### Example 1

Input:

```
1.0 0.8 0.5
```

Output:

```
0.30000 0.17778 0.52222
```

## Solution

Each of the 6 orders is solved apart and the results are averaged. Once
someone dies, two are left and shoot in turn; if the first to shoot
hits with p and the other with q, the first wins with

p + (1 − p)(1 − q)·p + … = p / (p + q − p·q).

While all three live, A's turn ends that phase at once, as A never
misses and kills the stronger of B and C. So from any turn the phase
lasts at most two more shots, and the chances follow by recursion over
the turns: a shooter compares shooting each opponent (hit with its
accuracy, then the duel that is left, starting with the next living
shooter; miss, then the next turn) with shooting into the air (the next
turn), and takes the best own chance. The ties are broken as the
statement says, then by A, B, C and the air, with a tolerance of 10⁻¹².
Everything takes constant time. The results agree with an independent
program on about 420 inputs.

Pitfalls:

- shooting into the air can be best: in the example, while all three
  live, C always shoots into the air and lets A and B shoot first;
- B or C may never hit or never miss, and a perfect B or C is the one A
  shoots first (tests 02–05);
- the next shooter after a hit skips the dead one, which decides who
  opens the remaining duel.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1565_games.cpp](1565_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 204 KB |
| [1565_games.go](1565_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.015 s | 1128 KB |
| [1565_games.java](1565_games.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 2012 KB |
| [1565_games.py](1565_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 724 KB |
| [1565_games.rs](1565_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.015 s | 256 KB |
