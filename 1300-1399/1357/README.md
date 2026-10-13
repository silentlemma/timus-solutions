# 1357. Teakettle 1.0 for Dummies

[Timus 1357](https://acm.timus.ru/problem.aspx?space=1&num=1357) · difficulty 1187 · simulation

Original problem by Vladimir Yakovlev, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 500 students wake up at different moments of one day and share one
teakettle on a 400 W burner. A student who finds the burner free pours
200 ml of water at 20 °C and starts heating it. A student who finds the
kettle heating adds 200 ml at 20 °C, and the temperatures mix in
proportion to the masses. The kettle holds 1 litre, five portions; when
it is full, newcomers wait until it is free. Once the water reaches
100 °C, everyone in the kettle gets coffee and the kettle can be reused
at once. Water of mass m warms by P·Δt / (C·m) degrees in Δt seconds,
with C = 4190 J/(kg·K). For every student, print the moment of coffee.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N wake-up times `HH:MM:SS` in increasing order.

## Output

N lines with the coffee times in the same format.

## Examples

### Example 1

Input:

```
4
07:00:00
07:02:00
07:05:30
12:00:00
```

Output:

```
07:08:23
07:08:23
07:08:23
12:02:48
```

## Solution

Count the heat still missing before the kettle boils:
Q = C · Σ mᵢ · (100 − Tᵢ). Mixing does not change Q, since it is linear
in the masses, and the burner lowers it by P every second. Each portion
adds C · 0.2 kg · 80 K = 67 040 J, which the burner supplies in exactly
167.6 s. So a kettle started at moment s with k portions in it boils
at s + 167.6 · k, no matter when the later portions were added.

The simulation keeps the students in the kettle, a queue of waiting
students and the boiling moment. A newcomer before that moment joins
the kettle and moves the boiling moment 167.6 s later, or joins the
queue if the kettle is full. At the boiling moment, the kettle's
students are served, and up to five waiting students form the next
kettle, which starts right away. All times are kept in whole
milliseconds, where 167.6 s is exactly 167 600, so there is no rounding
error at all. `O(N)`.

The statement leaves three things open; the judge's tests follow these
conventions, as reported on the problem's discussion board:

- the answer is rounded up to a whole second: 10:00:00 and 10:00:01
  share a kettle boiling at 10:05:35.2, printed as `10:05:36` (test 05);
- a student who wakes up exactly when the water boils does not join
  that kettle and starts a new one (test 03);
- times after midnight continue from `00:00:00` (test 04).

The answers were compared with a simulation that follows the
temperatures and masses with exact fractions, as in the statement, on
400 random cases.

## Language notes

- All five solutions use the same integer simulation in milliseconds.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1357_simulation.cpp](1357_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.015 s | 208 KB |
| [1357_simulation.go](1357_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.015 s | 1224 KB |
| [1357_simulation.java](1357_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.171 s | 2236 KB |
| [1357_simulation.py](1357_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.078 s | 664 KB |
| [1357_simulation.rs](1357_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 248 KB |
