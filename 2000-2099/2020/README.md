# 2020. Clearing Two Opposing Traffic Queues

[Timus 2020](https://acm.timus.ru/problem.aspx?space=1&num=2020) · difficulty 162 · simulation

Original problem by Denis Dublennykh, prepared by Nick Burlakov, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two queues approach a junction from opposite directions, south and north.
Each car intends to go forward (`F`), turn left (`L`) or turn right (`R`).
Cars are listed from nearest to farthest, cannot overtake, and each crossing
takes one second. A car turning left must yield to an opposing front car
going forward or right. Two left turns can occur together, as can two
non-left maneuvers. In each second every front car allowed by these rules
crosses; its successor becomes eligible in the next second. No new cars arrive.
Find when both queues become empty.

Each queue initially contains between 1 and 1,000 cars.
Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line is the south queue and the second is the north queue.
Both strings use only `F`, `L`, `R` and list cars nearest-first.

## Output

Print the total number of seconds until all cars have crossed.

## Checking

Outputs are compared token by token.

## Examples

```
RLF
FF
```

```
4
```

```
L
L
```

```
1
```

## Solution

Keep indices `i`, `j` of the first unprocessed cars and a time counter.
While both queues are nonempty, read **both old heads** `a`, `b`.
The south car can move when `a != L` or `b == L`; symmetrically the north
car can move when `b != L` or `a == L`. Compute both flags before changing
either index. Advance exactly the permitted indices and add one second.

| South head | North head | Cars crossing this second |
| --- | --- | --- |
| `L` | `F` or `R` | north only |
| `F` or `R` | `L` | south only |
| `L` | `L` | both |
| `F` or `R` | `F` or `R` | both |

Once one queue is empty, the remaining cars face no opposing traffic and
take one second each. Add the total number of unprocessed cars to the counter.

For correctness, maintain that after `t` simulated seconds, the indices are
exactly the numbers of cars that have crossed in each queue. Initially both
are zero. The table is precisely the junction's priority rule applied to
the two current heads. Updating both from the same old state therefore
reproduces the next second and preserves the invariant. When a queue empties,
every remaining front car is permitted and leaves on its next second, so
the tail addition is exact. Thus the resulting counter is the required time.

At least one car crosses each simulated second: either one left turn waits
for a non-left car, or both cars move. The loop therefore terminates in
`O(s+t)` time for initial queue lengths `s`, `t`. Auxiliary state is `O(1)`;
including the input strings, space is `O(s+t)`. The answer lies between
`max(s,t)` and `s+t`, hence never exceeds 2,000.

In the first sample, second one clears south `R` and north `F`. South `L`
waits during second two while the next north `F` crosses. South `L` and
south `F` then take seconds three and four. In the second sample both left
turns cross during the same second.

Pitfalls:

- Decide both departures before advancing either queue; a newly exposed
  head acts next second.
- A left turn yields to a right turn as well as to a forward car.
- Two opposing left turns move together.
- When one queue ends, include all remaining cars in the time.

## Optimized solutions

The optimized C++ solution reads the two queues with `scanf` into global
`char` arrays of 1001 bytes, since a queue has at most 1000 cars,
instead of `std::string`s read through `iostream`; it walks them up to
their terminating zeros and prints with `printf`:
{2020_simulation_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `2020_simulation_optimized.cpp`: time reduction +0.00%; memory
  reduction +72.63%; base: `2020_simulation.cpp`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [2020_simulation.py](2020_simulation.py).
- [2020_simulation.rs](2020_simulation.rs).

All five versions scan the two strings with indices. Python adds Boolean
flags to the indices; the other versions use Boolean-to-integer conversion
or conditional increments. Ordinary integer types easily hold the answer.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2020_simulation.cpp](2020_simulation.cpp) | G++ 13.2 x64 | simulation | O(s + t) | AC | 0.015 s | 380 KB | 11292679 |
| [2020_simulation.go](2020_simulation.go) | Go 1.14 x64 | simulation | O(s + t) | AC | 0.031 s | 1116 KB | 11292686 |
| [2020_simulation.java](2020_simulation.java) | Java 1.8 | simulation | O(s + t) | AC | 0.093 s | 444 KB | 11307207 |
| [2020_simulation.py](2020_simulation.py) | Python 3.12 x64 | simulation | O(s + t) | AC | 0.062 s | 424 KB | 11292688 |
| [2020_simulation.rs](2020_simulation.rs) | Rust 1.75 x64 | simulation | O(s + t) | AC | 0.015 s | 228 KB | 11292699 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2020_simulation_optimized.cpp](2020_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(s + t) | AC | 0.015 s | 104 KB | 11307208 |
