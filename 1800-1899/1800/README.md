# 1800. Murphy's Law

[Timus 1800](https://acm.timus.ru/problem.aspx?space=1&num=1800) · difficulty 170 · math

Original problem by Alex Samsonov, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A toast, a thin segment of length l, is dropped butter side down from
height h, held level. It falls freely (g = 9.81 m/s²) and spins about
its centre at ω revolutions per minute in a vertical plane. Which side
touches the floor first? It is guaranteed not to touch while standing
upright.

## Input

l and h in centimetres and ω in revolutions per minute, whole numbers
from 1 to 1000.

## Output

"butter" or "bread".

## Examples

### Example 1

Input:

```
10 400 15
```

Output:

```
butter
```

### Example 2

Input:

```
10 500 15
```

Output:

```
bread
```

## Solution

After t seconds the centre is at h − g·t²/2 and the toast has turned by
ω·t, so its lower end is at gap(t) = h − g·t²/2 − (l/2)·|sin ωt|. The
answer depends only on the quarter turn in which gap first reaches
zero: in quarters 0 and 3 of a turn the butter faces down, in 1 and 2
the bread. So go through the quarters in order.

In an even quarter |sin ωt| grows, the lower end sinks faster than the
centre, and gap only decreases: the toast touches in it exactly when
gap ≤ 0 at its end. In an odd quarter the end rises back relative to
the centre, and gap may first fall, then rise, then fall again. Its
slope there is concave, since the third derivative is
(l/2)·ω³·cos ≤ 0. Find the peak of the slope by bisection on the
second derivative. If the slope at the peak is positive, a second
bisection finds where it turns positive, the local minimum of gap. The
quarter holds the first touch if that minimum or the value at its end
is at most zero. The centre reaches the floor within about 1.5
seconds, so there are at most about a hundred quarters. `O(ω)`.

In the first example the toast turns a quarter per second and lands
after about 0.9 s, at about 81°: butter. From 5 m it lands just past
90°: bread.

Pitfalls:

- the end of the toast may touch before the centre has fallen far: a
  long toast held low touches in the very first quarter;
- in an odd quarter gap is not monotone, so its value at the end of
  the quarter alone can miss a touch;
- the units: centimetres to metres, revolutions per minute to radians
  per second.

The answers agree with an independent accepted implementation, which
steps through time in microseconds, on 1548 inputs: 1500 random ones
and the extreme values.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1800_math.cpp](1800_math.cpp) | G++ 13.2 x64 | math | O(omega) | AC | 0.015 s | 376 KB |
| [1800_math.go](1800_math.go) | Go 1.14 x64 | math | O(omega) | AC | 0.031 s | 1084 KB |
| [1800_math.java](1800_math.java) | Java 1.8 | math | O(omega) | AC | 0.109 s | 1636 KB |
| [1800_math.py](1800_math.py) | Python 3.12 x64 | math | O(omega) | AC | 0.093 s | 592 KB |
| [1800_math.rs](1800_math.rs) | Rust 1.75 x64 | math | O(omega) | AC | 0.031 s | 236 KB |
