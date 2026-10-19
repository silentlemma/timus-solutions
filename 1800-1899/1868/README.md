# 1868. Prediction Contest

[Timus 1868](https://acm.timus.ru/problem.aspx?space=1&num=1868) · difficulty 158 · implementation

Original problem by Denis Dublennykh, from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

At the world finals the first four teams win gold medals, the next four
silver and the next four bronze. Several veterans made forecasts of the
form "team X wins a medal of kind Y", and Vadik pays five dollars to
each veteran with the most right guesses. Given the twelve medallists
in order of their places and all the forecasts, how much does Vadik
pay?

## Input

Twelve team names from the first place to the twelfth, then n
(1 ≤ n ≤ 100) and n forecasts. A forecast starts with its number of
guesses kᵢ, followed by kᵢ lines "team : medal" with the medal "gold",
"silver" or "bronze". No forecast gives a team two medals or a medal
to more than four teams. Names are 1 to 30 Latin letters, underscores,
dots and commas.

## Output

The amount Vadik pays, in dollars.

## Examples

### Example 1

Input:

```
Zhejiang_U
U_of_Michigan_at_Ann_Arbor
Tsinghua_U
St._Petersburg_SU
Nizhny_Novgorod_SU
Saratov_SU
Friedrich_Alexander_U
Donetsk_National_U
Jagiellonian_U_in_Krakow
Moscow_SU
Ural_SU
U_of_Waterloo
3
6
Moscow_SU : gold
St._Petersburg_SU_of_ITMO : gold
Warsaw_U : gold
Tsinghua_U : gold
Nizhny_Novgorod_SU : silver
Saratov_SU : silver
6
Warsaw_U : gold
Saratov_SU : gold
Tsinghua_U : gold
Donetsk_National_U : silver
St._Petersburg_SU_of_ITMO : silver
Ural_SU : bronze
6
Zhejiang_U : gold
Tsinghua_U : gold
Shanghai_Jiao_Tong_U : gold
Fudan_U : gold
Moscow_SU : silver
Nizhny_Novgorod_SU : silver
```

Output:

```
15
```

## Solution

Names contain no spaces, so the input is a stream of words: twelve
names, then for each guess a name, a colon and a medal. A dictionary
from the twelve names to their medals (place 1–4 gold, 5–8 silver,
9–12 bronze) tells whether a guess is right; a team missing from it
won nothing. Count the right guesses of every veteran, and pay five
dollars for each veteran with the largest count. `O(n·k)` dictionary
lookups.

In the example each veteran has three right guesses, so all three win
and Vadik pays 15 dollars.

Pitfalls:

- the medal comes from the place: the names are in order, so the
  first four are gold, and so on;
- a forecast may name teams that won no medal at all;
- names are case-sensitive and may consist of dots and commas only;
- when nobody guessed anything right, every veteran ties with zero and
  is paid.

The amounts agree with an independent accepted implementation on 150
random contests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1868_implementation.cpp](1868_implementation.cpp) | G++ 13.2 x64 | implementation | O(n k) | AC | 0.015 s | 444 KB |
| [1868_implementation.go](1868_implementation.go) | Go 1.14 x64 | implementation | O(n k) | AC | 0.015 s | 1220 KB |
| [1868_implementation.java](1868_implementation.java) | Java 1.8 | implementation | O(n k) | AC | 0.093 s | 1196 KB |
| [1868_implementation.py](1868_implementation.py) | Python 3.12 x64 | implementation | O(n k) | AC | 0.078 s | 692 KB |
| [1868_implementation.rs](1868_implementation.rs) | Rust 1.75 x64 | implementation | O(n k) | AC | 0.015 s | 536 KB |
