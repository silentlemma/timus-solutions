# 1600. Airport

[Timus 1600](https://acm.timus.ru/problem.aspx?space=1&num=1600) · difficulty 552 · geometry

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

The simple C++ version scales the decimal inputs to integers and computes the sign of the discriminant exactly. The simple Java version scales the decimal inputs to integers and computes the sign of the discriminant exactly.

The simple Rust version scales the decimal inputs to integers and computes the sign of the discriminant exactly.

## Optimized solutions

Python orders the objects by x and skips pairs whose separation on that axis cannot fall to the critical distance. Once an encounter is found, an integer upper bound on its time limits the scan. The sign of each remaining discriminant is computed exactly. Python 3.12 x64, submission 11322507. Time 0.203 → 0.078 s, memory 1492 → 1084 KB.

Java submission 11321903 took 0.125 s and used 1780 KB. The current simple version took 0.281 s and used 7020 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322335 · Go 1.14 x64 №11322334 · Java 1.8 №11322333 · Python 3.12 x64 №11322332 · Rust 1.75 x64 №11322336.

Go skips pairs that are moving apart. For pairs close to tangency it recomputes the discriminant from the original decimal values using rational arithmetic, then uses the stable entry-time formula.

C++ uses the cross product to compute the closest separation and rechecks near-tangent trajectories in quadruple precision.

Rust scales the decimal input to integers. It computes the discriminant exactly using 128-bit integers when every scaled input has magnitude at most 500,000,000, and uses arbitrary-precision integers otherwise.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1600_geometry.cpp](1600_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.328 s | 664 KB | 11322335 |
| [1600_geometry.go](1600_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.093 s | 2428 KB | 11322334 |
| [1600_geometry.java](1600_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.281 s | 7020 KB | 11322333 |
| [1600_geometry.py](1600_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.203 s | 1492 KB | 11322332 |
| [1600_geometry.rs](1600_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.234 s | 616 KB | 11322336 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1600_geometry_optimized.py](1600_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(n²) | AC | 0.078 s | 1084 KB | 11322507 |
| [1600_geometry_optimized.java](1600_geometry_optimized.java) \* | Java 1.8 | geometry | O(n²) | AC | 0.125 s | 1780 KB | 11321903 |
| [1600_geometry_optimized.go](1600_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(n²) | AC | 0.031 s | 1304 KB | 11322026 |
| [1600_geometry_optimized.cpp](1600_geometry_optimized.cpp) \* | G++ 13.2 x64 | geometry | O(n²) | AC | 0.031 s | 256 KB | 11321905 |
| [1600_geometry_optimized.rs](1600_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n²) | AC | 0.031 s | 560 KB | 11322367 |

\* The marked solutions can improve their target rankings.
