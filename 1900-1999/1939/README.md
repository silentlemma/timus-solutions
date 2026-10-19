# 1939. A Deadline Between Passing and Braking

[Timus 1939](https://acm.timus.ru/problem.aspx?space=1&num=1939) · difficulty 837 · math

Original problem from Open Ural FU Championship 2012 | by Denis Dublennykh (prepared by Egor Shchelkonogov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A vehicle of length l and height h approaches a gate at constant speed v.
The grille initially has clearance H and may begin descending at speed x
at any instant. After noticing closure, the vehicle can release its
traction and decelerate at a until rest, or continue. Initially it is
far enough away to stop before the gate if braking immediately.
Decide whether a closure-start instant exists at which collision is
unavoidable, even with the best braking decision. Any touch is fatal.
Limits: 1 second, 64 MB.

## Input

First l,h,H with h<H, then v,x,a. All six values are positive integers
at most 1000. Lengths are centimetres, v and x centimetres/second,
and a centimetres/second². No present gate distance is supplied.

## Output

Crash if some possible closure-start time forces a collision;
otherwise Safe. Output is one word, with exactly this capitalization.

## Checking

Outputs are compared token by token.

## Examples

```
1 1 1000
1 1 1000
```

```
Safe
```

```
1000 1 2
1000 1 1
```

```
Crash
```

## Solution

Let d be the distance from the vehicle's front to the gate when closure
starts. The grille reaches height h after T=(H−h)/x. Immediate braking
stops the front after distance S=v²/(2a).

Stopping is safe precisely when d>S. Equality is insufficient: a front
parked on the gate plane will touch the descending grille. Continuing
is safe precisely when d+l<vT, because the rear must clear before T;
equality is also contact.

Delayed release cannot improve either limit. A delay δ≥0 increases
the final stopping distance to S+vδ. All permitted trajectories have
speed at most v, so none clears earlier than constant-speed travel.
Thus failure of both extreme choices implies failure of every delay.

If S+l<vT, every gap is covered: brake for d>S, continue for d≤S.
Otherwise choose d=S. Braking cannot stop strictly before the line,
and continuing cannot clear strictly before T. This instant is reachable
because the initial front distance exceeds S. Hence a forced crash
exists exactly when S+l≥vT. A single isolated bad instant still counts.

Multiply by positive 2ax to obtain the exact integer condition

x·(v²+2al) ≥ 2av·(H−h).

Print Crash when it holds, including equality. No division, square roots
or epsilon are needed. The vehicle length and the clearance loss H−h
both matter.

O(1) time and space, with a fixed number of arithmetic operations.

Use ≥ for Crash: both boundary choices touch the grille. Do not ignore
the rear, replace H−h by H, confuse stopping time with stopping distance,
or test just an unspecified current position. An arbitrary epsilon can
erase meaningful one-unit differences between large integer products.

## Language notes

The left side can reach 3,000,000,000, beyond signed 32-bit range; the
right side is at most 1,998,000,000. All operands are 64-bit before
multiplication: long long in C++, int64 in Go, long in Java, i64 in Rust.
Python uses arbitrary-size integers. Each program prints one word and LF.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1939_math.cpp](1939_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 380 KB |
| [1939_math.go](1939_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1092 KB |
| [1939_math.java](1939_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 404 KB |
| [1939_math.py](1939_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 408 KB |
| [1939_math.rs](1939_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 224 KB |
