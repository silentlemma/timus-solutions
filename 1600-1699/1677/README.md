# 1677. Monkey at the Keyboard

[Timus 1677](https://acm.timus.ru/problem.aspx?space=1&num=1677) · difficulty 1586 · strings

Original problem by Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every second a monkey types one of the first N letters, each equally
likely. Find the expected number of seconds until a given word appears
in the typed text, rounded down.

## Input

N (1 ≤ N ≤ 26), then the word: lowercase letters among the first N, at
most 30000 of them.

## Output

The expected time, rounded down (it is an integer anyway).

## Examples

### Example 1

Input:

```
2
aa
```

Output:

```
6
```

### Example 2

Input:

```
2
ba
```

Output:

```
4
```

## Solution

The answer is the sum of N^k over all k such that the first k letters
of the word equal its last k letters (its borders), the whole word
included. For aa with N = 2 that is 2 + 4 = 6, for ba just 4.

A betting argument shows why. Before each second a new gambler arrives
with 1 coin and bets everything, at fair odds N to 1, that the next
letter is the first letter of the word; if it wins, it bets all on the
second letter, and so on. The game is fair, so at the moment the word
first appears the gamblers' total winnings minus the coins they brought
has expectation zero. At that moment the gamblers still in play are
exactly those who started at a border of the word, holding N^k each for a
border of length k, and every second brought one coin. So the expected
time equals the sum of N^k.

The borders come from the prefix function: the longest border of the
word, the longest border of that, and so on. The sum, written in base N,
has digits 0 and 1 only, so it is built by Horner's rule from the top
digit down; it has up to about 42 500 decimal digits. `O(L²)` limb
operations for the number, `O(L)` for the borders.

Pitfalls:

- the answer is a huge exact integer (test 05), so big-number arithmetic
  is needed; doubles are useless here;
- with N = 1 the time is just the length of the word (test 03).

The answers match an exact solution of the waiting-time equations on all
words up to length 5 over up to three letters, and an independent
accepted implementation.

## Language notes

- C++ and Rust do the arithmetic themselves in base 10⁹ limbs: each step
  multiplies by N and adds one digit.
- Python lifts the limit on converting huge integers to text with
  sys.set_int_max_str_digits(0).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1677_strings.cpp](1677_strings.cpp) | G++ 13.2 x64 | strings | O(L^2) | AC | 0.218 s | 408 KB |
| [1677_strings.go](1677_strings.go) | Go 1.14 x64 | strings | O(L^2) | AC | 0.078 s | 6000 KB |
| [1677_strings.java](1677_strings.java) | Java 1.8 | strings | O(L^2) | AC | 0.953 s | 5976 KB |
| [1677_strings.py](1677_strings.py) | Python 3.12 x64 | strings | O(L^2) | AC | 0.328 s | 26416 KB |
| [1677_strings.rs](1677_strings.rs) | Rust 1.75 x64 | strings | O(L^2) | AC | 0.156 s | 776 KB |
