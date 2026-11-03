# 2078. Bowling score bounds from frame totals

[Timus 2078](https://acm.timus.ru/problem.aspx?space=1&num=2078) · difficulty 275 · dp, simulation

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

## Checking

Compare the exact answer tokens; whitespace formatting is immaterial.

- `2078_dp_simulation.go` (Go 1.14 x64): 14 repository cases; 14 additional source-bound comparisons.

- `2078_dp_simulation.java` (Java 1.8): 14 repository cases; 444 additional source-bound comparisons.

- `2078_dp_simulation.py` (PyPy 3.10 x64): 14 repository cases.

- `2078_dp_simulation.rs` (Rust 1.75 x64): 14 repository cases.

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
tried: two rolls without a strike or spare, otherwise a third roll
on fresh pins (or on the rest of the pins after a strike and a partial
second roll). Its pair is its first two rolls, and its score is its
total.

A frame with fewer than 10 pins can be split as (r, t − r) for any r,
and its pair is exactly those two rolls. A frame with 10 pins is either
a strike, whose pair is (10, x) for the next frame's pair (x, y) and
whose bonus is x + y, or a spare (r, 10 − r) with bonus x. The answer is
the extreme over the pairs of the first frame; there are at most 121
pairs, so the work is O(1).

In the first example the first frame is a strike or a spare, followed by
a frame of 2 pins: as a strike it adds both rolls of that frame (2
points), as a spare it adds nothing if that frame starts with 0, hence
60 and 62.

## Optimized solutions

Keep the readable backward DP. The chronological dp_simulation variants track pending bonuses for the next two rolls: only (0,0),(1,0),(1,1),(2,1) are reachable. Store minimum and maximum score for each. For an open/spare two-roll frame of total t, extra score is b*t+(a-b)*first; since a>=b, its extrema occur at the allowed endpoints for the first roll. A strike consumes the old first bonus, shifts the second and adds its own next-two-roll bonuses. In the last frame no new bonuses are created; rack-reset rules give the allowed extrema, including totals above 20 forcing the first two rolls to be 10. These transitions cover every legal roll sequence. Four score states replace 121 future-roll pairs: O(F) time and constant score storage. Different input/output representations have their own Accepted receipts.

- `2078_dp_simulation.go`: 0.031 s / 312 KB; base `2078_dp.go`: 0.031 s / 1144 KB; relative change: time -0.0%, memory -72.7%.
- `2078_dp_simulation.java`: 0.109 s / 416 KB; base `2078_dp.java`: 0.125 s / 1660 KB; relative change: time -12.8%, memory -74.9%.
- `2078_dp_simulation.py`: 0.140 s / 276 KB; base `2078_dp.py`: 0.093 s / 708 KB; relative change: time +50.5%, memory -61.0%.
- `2078_dp_simulation.rs`: 0.031 s / 68 KB; base `2078_dp.rs`: 0.031 s / 224 KB; relative change: time -0.0%, memory -69.6%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `2078_dp.cpp`; covering source `2078_dp.cpp`; time/memory places 1/1, other-author entries 42/42.

- Go: preferred teaching base `2078_dp.go`; covering source `2078_dp_simulation.go`; time/memory places 1/1, other-author entries 2/2.

- Java: preferred teaching base `2078_dp.java`; covering source `2078_dp_simulation.java`; time/memory places 1/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `2078_dp.py`; covering source `2078_dp_simulation.py`; time/memory places 153/2, other-author entries 158/158.

- Rust: preferred teaching base `2078_dp.rs`; covering source `2078_dp_simulation.rs`; time/memory places 2/1, other-author entries 1/1.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2078_dp.cpp](2078_dp.cpp) | G++ 13.2 x64 | dp | O(1) | AC | 0.015 s | 116 KB | 11309235 |
| [2078_dp.go](2078_dp.go) | Go 1.14 x64 | dp | O(1) | AC | 0.031 s | 1144 KB | 11294529 |
| [2078_dp.java](2078_dp.java) | Java 1.8 | dp | O(1) | AC | 0.125 s | 1660 KB | 11309236 |
| [2078_dp.py](2078_dp.py) | Python 3.12 x64 | dp | O(1) | AC | 0.093 s | 708 KB | 11294532 |
| [2078_dp.rs](2078_dp.rs) | Rust 1.75 x64 | dp | O(1) | AC | 0.031 s | 224 KB | 11309237 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2078_dp_simulation.go](2078_dp_simulation.go) | Go 1.14 x64 | dp, simulation | O(F) time; O(1) score state | AC | 0.031 s | 312 KB | 11309759 |
| [2078_dp_simulation.java](2078_dp_simulation.java) | Java 1.8 | dp, simulation | O(F) time; O(1) score state | AC | 0.109 s | 416 KB | 11309301 |
| [2078_dp_simulation.py](2078_dp_simulation.py) \* | PyPy 3.10 x64 | dp, simulation | O(F) time; O(1) score state | AC | 0.140 s | 276 KB | 11309738 |
| [2078_dp_simulation.rs](2078_dp_simulation.rs) \* | Rust 1.75 x64 | dp, simulation | O(F) time; O(1) score state | AC | 0.031 s | 68 KB | 11309708 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
