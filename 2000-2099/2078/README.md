# 2078. Bowling score bounds from frame totals

[Timus 2078](https://acm.timus.ru/problem.aspx?space=1&num=2078) · difficulty 277 · dp

Original problem by Alexander Krasnoselskikh, prepared by Oleg Dolgorukov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A bowling game has ten frames. In frames 1 to 9 a player rolls at 10
pins up to twice; knocking all of them down with the first roll is a
strike (the second roll is skipped), with both rolls a spare. A strike
adds the next two rolls to the frame's score, a spare the next one. The
last frame gives a third roll after a strike or a spare, with fresh pins
whenever all are down, and earns no bonus itself. Only the number of
pins knocked down in each frame is known. Find the least and the
greatest possible score. The limits are 2 seconds and 256 MB.

## Input

Ten numbers: the pins of frames 1 to 9 (0 to 10 each) and of the last
frame (0 to 30).

## Output

The least and the greatest score.

## Examples

### Example 1

Input:

```
10 2 4 8 3 8 1 9 8 7
```

Output:

```
60 62
```

### Example 2

Input:

```
2 4 6 8 10 10 8 6 4 2
```

Output:

```
60 86
```

## Solution

The pins themselves give the same sum for every way to split the frames
into rolls; only the bonuses differ, and they look at most two rolls
ahead. So a DP runs from the last frame to the first, keeping for every
pair (x, y) of the first two rolls from the current frame on the least
and the greatest score of the frames from there to the end.

For the last frame every valid roll sequence with the right total is
tried: two rolls when they leave pins standing, otherwise a third roll
on fresh pins (or on the rest of the pins after a strike and a partial
second roll). Its pair is its first two rolls, and its score is its
total.

A frame with fewer than 10 pins can be split as (r, t − r) for any r,
and its pair is exactly those two rolls. A frame with 10 pins is either
a strike, whose pair is (10, x) for the next frame's pair (x, y) and
whose bonus is x + y, or a spare (r, 10 − r) with bonus x. The answer is
the extreme over the pairs of the first frame; there are at most 121
pairs, so the work is tiny.

In the first example the first frame is a strike or a spare, followed by
a frame of 2 pins: as a strike it adds both rolls of that frame (2
points), as a spare with a 0 first roll it adds nothing, hence 60 and
62.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2078_dp.cpp](2078_dp.cpp) | G++ 13.2 x64 | dp | O(1) | AC | 0.015 s | 136 KB |
| [2078_dp.go](2078_dp.go) | Go 1.14 x64 | dp | O(1) | AC | 0.031 s | 1144 KB |
| [2078_dp.java](2078_dp.java) | Java 1.8 | dp | O(1) | AC | 0.125 s | 1664 KB |
| [2078_dp.py](2078_dp.py) | Python 3.12 x64 | dp | O(1) | AC | 0.093 s | 708 KB |
| [2078_dp.rs](2078_dp.rs) | Rust 1.75 x64 | dp | O(1) | AC | 0.046 s | 232 KB |
