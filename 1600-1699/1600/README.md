# 1600. Airport

[Timus 1600](https://acm.timus.ru/problem.aspx?space=1&num=1600) · difficulty 555 · geometry

Original problem by Vladimir Yakovlev, from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Up to 500 objects fly in straight lines at constant speed in space; all
start farther apart than a critical distance d. Find the first moment
when some pair comes within distance d, printed as `ALARM!` and then the
time to three decimals with the pair, or `OK` if that never happens. If
several pairs meet at that moment, any of them may be printed.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n and d, then the position and velocity of each object, six numbers.

## Output

`OK`, or `ALARM!` and then the time and the two object numbers.

## Examples

### Example 1

Input:

```
2 1.0
1.0 1.0 -1.0 0.0 0.0 10.0
0.0 0.0 4.0 2.0 0.0 0.0
```

Output:

```
ALARM!
0.500 1 2
```

## Solution

Seen from one object of a pair, the other moves along the line p + v·t,
where p and v are the differences of positions and velocities. They are
at distance d when |p + v·t|² = d², a quadratic equation:
(v·v)t² + 2(p·v)t + (p·p − d²) = 0. With equal velocities, or a negative
discriminant, the pair never meets. Otherwise the smaller root is the
moment they first come within d; since every pair starts apart, a
negative root means they are flying away from each other. The earliest
moment over all pairs is the answer: `O(n²)`, about 125000 pairs.

The tests use a checker that accepts any pair meeting at the right time,
within the rounding to three decimals. The times were checked against a
bisection on the distance before the closest approach.

Pitfalls:

- a pair that only touches distance d at its closest approach still
  raises the alarm: the discriminant is then exactly 0 (test 04);
- the time can be large when the relative speed is tiny, almost
  10⁶ seconds in test 07, so it must not be bounded in advance;
- with half the discriminant, b = p·v and b² − a·c, there is no factor
  4 to carry around.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1600_geometry.cpp](1600_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.015 s | 272 KB |
| [1600_geometry.go](1600_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.015 s | 1156 KB |
| [1600_geometry.java](1600_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.109 s | 1068 KB |
| [1600_geometry.py](1600_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.156 s | 928 KB |
| [1600_geometry.rs](1600_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.062 s | 328 KB |
