# 2081. Decreasing times behind a faulty dial

[Timus 2081](https://acm.timus.ru/problem.aspx?space=1&num=2081) · difficulty 721 · greedy

Original problem by Pavel Egorov, prepared by Ivan Burmistrov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A timer shows MM:SS on a seven-segment dial drawn with `_`, `|` and `.`,
but some lit segments may fail to show (a shown segment is always
right). Given n readings, restore times from 00:00 to 59:59, strictly
decreasing, each consistent with its reading. Any valid answer is
accepted. The limits are 2 seconds and 256 MB.

## Input

n ≤ 100, then three lines of 17 characters per reading: the four digits
take columns 1–3, 5–7, 11–13 and 15–17.

## Output

n lines MM:SS.

## Checking

A checker verifies the format, the strict decrease and that every
shown segment belongs to the chosen digit.

## Examples

### Example 1

Input:

```
2
._..._........._.
|...._|.*...|.._|
|_|.._..*...|.|..
....._....._..._.
|.|...|.*.|.|.._.
|.|.|_..*.|_|.._.
```

Output:

```
03:12
00:05
```

## Solution

A digit fits a cell when every shown character equals the character of
the digit at that place. For each reading the four cells give a table
of fitting digits. Going through the readings in order, take the
largest time that fits and is below the previous answer, scanning down
from it.

This never fails when some answer exists: by induction the greedy value
of each reading is at least the value in that answer, because the
answer's value fits and is below the previous answer value, which is at
most the greedy previous value. The scan takes at most 3600 steps per
reading.

In the example the first reading fits 09:48 as well as 03:12, so the
output may differ from the sample.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2081_greedy.cpp](2081_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 392 KB |
| [2081_greedy.go](2081_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 1272 KB |
| [2081_greedy.java](2081_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.187 s | 2448 KB |
| [2081_greedy.py](2081_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 564 KB |
| [2081_greedy.rs](2081_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.031 s | 256 KB |
