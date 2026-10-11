# 1240. A mage against a pack of monsters

[Timus 1240](https://acm.timus.ru/problem.aspx?space=1&num=1240) · difficulty 1414 · games

Original problem by Andrew Stankevich, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A hero stands on square 0 of a strip of squares 0 to N (N ≤ 10) with
HP_H hit points (≤ 100) and MP_H mana (≤ 50). A pack of N_M monsters of
HP_M hit points each (N_M, HP_M ≤ 10) starts on square N and acts as one
body: with H hit points left it holds ⌈H/HP_M⌉ monsters. Each turn the
hero spends one mana on a spell, then the pack moves:

- **Lightning bolt** removes L_P hit points from the pack, where P is its
  square;
- **Teleport** puts the pack on any square from 1 to N;
- **Heal** gives the hero dH hit points, up to HP_H.

The pack then moves min(V, P − 1) squares towards the hero, and if it
ends on square 1 it strikes for as many hit points as it has monsters.
The hero loses at zero hit points, or when out of mana with monsters
left. Find a winning sequence of spells or report that there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, HP_H, MP_H, HP_M, N_M, V, dH, then L_1 … L_N.

## Output

`DEFEATED`, or `VICTORIOUS` followed by one spell per line: `L`, `H` or
`T p`.

## Checking

Any winning sequence is accepted. The checker compares the verdict with
the expected answer and plays the spells: every one needs mana, the hero
must survive every strike, the pack must die from the last spell, and
nothing may follow.

## Examples

### Example 1

Input:

```
2 3 2 1 2 1 1
1 1
```

Output:

```
VICTORIOUS
L
L
```

### Example 2

Input:

```
2 3 2 3 1 1 1
1 1
```

Output:

```
DEFEATED
```

### Example 3

Input:

```
4 4 3 1 4 1 1
3 1 1 1
```

Output:

```
VICTORIOUS
L
T 2
L
```

### Example 4

Input:

```
1 6 5 1 4 1 3
1
```

Output:

```
VICTORIOUS
L
L
H
L
L
```

## Solution

Every spell costs one mana, so the game always ends and a state can be
solved from states with less mana. A state is the hero's hit points, the
mana, the pack's hit points and its square: up to 100 × 50 × 100 × 10.
But more hit points never hurt the hero: the same spells still work. So
for each mana m, pack hit points h and square p it is enough to know
`need[m][h][p]`, the fewest hit points with which the hero still wins,
and that is only 50 × 100 × 10 numbers.

For a spell, follow the pack to its next square q and add the strike `s`
it deals there:

- a bolt that kills the pack needs just 1 hit point; otherwise it needs
  `s + need[m−1][h − L_p][q]`;
- a teleport to t needs `s + need[m−1][h][q]` with q the square after
  moving from t;
- a heal needs the same `s + need[m−1][h][q]` after healing, which is
  impossible if that exceeds HP_H and otherwise asks for dH less.

`need` is the least over the spells, and infinite without mana. The hero
wins when `need[MP_H][N_M·HP_M][N] ≤ HP_H`; then the spells are replayed
forward, each time taking any spell whose requirement the current hit
points meet. `O(MP_H · N_M·HP_M · N²)`.

Pitfalls:

- after a teleport the pack moves at once, so it is never on the chosen
  square at the hero's next turn: test 05 sends it to square 10 so that
  it stands on 9, the only strong square;
- a pack already on square 1 moves zero squares and strikes again every
  turn;
- the strike counts the monsters left, ⌈H/HP_M⌉, not the hit points.

The verdicts were compared with an exhaustive search over full states on
800 random small battles, and every victory was replayed by the checker.

## Language notes

- Rust names the spells with an enum, Go and Python with letters, and C++
  and Java with -1 for a bolt, 0 for a heal and the target square for a
  teleport.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1240_games.cpp](1240_games.cpp) | G++ 13.2 x64 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.015 s | 448 KB |
| [1240_games.go](1240_games.go) | Go 1.14 x64 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.031 s | 1740 KB |
| [1240_games.java](1240_games.java) | Java 1.8 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.093 s | 876 KB |
| [1240_games.py](1240_games.py) | Python 3.12 x64 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.578 s | 1372 KB |
| [1240_games.rs](1240_games.rs) | Rust 1.75 x64 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.015 s | 592 KB |
