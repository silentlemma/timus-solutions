# 1856. War and Peace

[Timus 1856](https://acm.timus.ru/problem.aspx?space=1&num=1856) · difficulty 3485 · games

Original problem by Fedor Fominykh, from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An army of liches is spread over all n garrisons. Each of two signal
spells sends the troops of every garrison i to a fixed garrison, aᵢ for
the first spell and bᵢ for the second, all at once. Every day at noon
Vidomina casts one of the spells, trying to gather the whole army in one
garrison, and every midnight Korbu casts one, trying to prevent it;
Vidomina starts. With both playing optimally, can the army be gathered?

## Input

n (2 ≤ n ≤ 1000), then the pairs aᵢ, bᵢ for every garrison.

## Output

"War" if Vidomina can gather the army, "Peace" otherwise.

## Examples

### Example 1

Input:

```
2
2 1
1 2
```

Output:

```
Peace
```

### Example 2

Input:

```
2
2 2
2 1
```

Output:

```
War
```

## Solution

The occupied garrisons form a set that the spells map forward, and it
never grows. The army can be gathered exactly when every pair of
garrisons can be forced together. If some pair (u, v) can be kept apart
forever, the troops starting there never meet. If every pair can be
forced together, Vidomina takes two occupied garrisons, follows the
strategy for that pair until they merge, and repeats with fewer
occupied garrisons each time.

So the game is played on pairs, at most 499 500 of them. A pair is won
for Vidomina when one of her spells either merges it or leaves Korbu
only replies that merge it or lead to pairs already won. Solve it
backwards: for every pair and each of her spells count Korbu's replies
that keep the pair apart, list for every pair the (pair, spell) moves
that can lead into it, and start from the pairs with a spell whose count
is zero. When a pair is won, every move leading into it loses one open
reply, and a count that drops to zero wins its pair. The answer is
"War" if all pairs are won. `O(n²)` time and memory.

In the first example both spells are permutations, so the two
garrisons never merge. In the second, the first spell sends both
garrisons to garrison 2 at once.

Pitfalls:

- Korbu's reply may itself merge a pair; such a reply is not open;
- gathering pair by pair works because the occupied set never grows,
  even though Korbu moves the other troops in between;
- the state space of whole sets is far too large; pairs are enough.

The answers agree with a game search over all sets of garrisons on
three hundred cases of up to six garrisons and with an independent
accepted implementation on the large tests. The Python solution runs on
PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1856_games.cpp](1856_games.cpp) | G++ 13.2 x64 | games | O(n^2) | AC | 0.093 s | 37828 KB |
| [1856_games.go](1856_games.go) | Go 1.14 x64 | games | O(n^2) | AC | 0.187 s | 56936 KB |
| [1856_games.java](1856_games.java) | Java 1.8 | games | O(n^2) | AC | 0.234 s | 38620 KB |
| [1856_games.py](1856_games.py) | PyPy 3.10 x64 | games | O(n^2) | AC | 0.500 s | 50420 KB |
| [1856_games.rs](1856_games.rs) | Rust 1.75 x64 | games | O(n^2) | AC | 0.140 s | 39544 KB |
