# 2151. Recognizing a winning or nearly winning mahjong hand

[Timus 2151](https://acm.timus.ru/problem.aspx?space=1&num=2151) · difficulty 904 · bruteforce, greedy

Original problem by Ivan Sychev, from the Ural School Programming Contest 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Tiles have a suit a, b or c and a number from 1 to 9. A hand of 14 tiles
wins when it splits into four triples and one pair, where a triple is
three equal tiles or three consecutive numbers of one suit and a pair is
two equal tiles. A hand is nearly winning when replacing exactly one
tile makes it win. Classify a hand as Tsumo, Tenpai or Noten. The limits
are 1 second and 256 MB.

## Input

14 tiles such as 1a or 9c, at most four of each kind.

## Output

Tsumo, Tenpai or Noten.

## Examples

### Example 1

Input:

```
1a 2a 3a 6a 7a 8a 5b 5b 5b 9c 8c 7c 1c 1c
```

Output:

```
Tsumo
```

### Example 2

Input:

```
1a 2a 3a 6a 7a 8a 5b 5b 5b 9c 8c 7c 1c 1b
```

Output:

```
Tenpai
```

## Solution

Count the tiles of each of the 27 kinds. To test whether a hand wins,
note first that triples stay inside a suit, so exactly one suit has a
number of tiles ≡ 2 modulo 3 and holds the pair, and the other suits
are ≡ 0. Try every kind of that suit with at least two tiles as the
pair. The rest must split into triples, which a greedy pass decides:
going up from the lowest number, a count c leaves c mod 3 tiles that
cannot be in equal triples, because three equal sequences are the same
as three equal triples, so exactly c mod 3 sequences must start there.

A hand is Tenpai if it does not win but wins after removing one tile
of some kind and adding one of a different kind; a replacement may
create a fifth tile of a kind. That is at most 27 · 26 checks of a
27-element greedy test.

In the second example the hand has 1c and 1b where a pair is needed, so
replacing one of them by the other completes it.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2151_bruteforce_greedy.cpp](2151_bruteforce_greedy.cpp) | G++ 13.2 x64 | bruteforce, greedy | O(27^3) | AC | 0.015 s | 400 KB |
| [2151_bruteforce_greedy.go](2151_bruteforce_greedy.go) | Go 1.14 x64 | bruteforce, greedy | O(27^3) | AC | 0.031 s | 1100 KB |
| [2151_bruteforce_greedy.java](2151_bruteforce_greedy.java) | Java 1.8 | bruteforce, greedy | O(27^3) | AC | 0.109 s | 492 KB |
| [2151_bruteforce_greedy.py](2151_bruteforce_greedy.py) | Python 3.12 x64 | bruteforce, greedy | O(27^3) | AC | 0.078 s | 652 KB |
| [2151_bruteforce_greedy.rs](2151_bruteforce_greedy.rs) | Rust 1.75 x64 | bruteforce, greedy | O(27^3) | AC | 0.015 s | 216 KB |
