# 1030. The great-circle distance between a ship and an iceberg

[Timus 1030](https://acm.timus.ru/problem.aspx?space=1&num=1030) · difficulty 898 · geometry, parsing

Original problem by Evgeny Shtykov, from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A radio message gives the coordinates of a ship and of an iceberg on a
perfect sphere of diameter 6875 miles. Print the length of the shortest path
on the sphere between them, with two digits after the decimal point, and
add the line `DANGER!` if the printed distance is less than 100.00 miles.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The message always has exactly these lines (values vary):

```text
Message #<n>.
Received at <HH>:<MM>:<SS>.
Current ship's coordinates are
<X1>^<X2>'<X3>" <NL or SL>
and <Y1>^<Y2>'<Y3>" <EL or WL>.
An iceberg was noticed at
<X1>^<X2>'<X3>" <NL or SL>
and <Y1>^<Y2>'<Y3>" <EL or WL>.
===
```

`X1^X2'X3"` is X1 degrees, X2 minutes and X3 seconds of north (`NL`) or
south (`SL`) latitude, from 0 to 90 degrees; `Y1^Y2'Y3"` is the longitude,
east (`EL`) or west (`WL`), from 0 to 180 degrees.

## Output

```text
The distance to the iceberg: <s> miles.
```

with `<s>` printed with two decimals, followed by the line `DANGER!` when
`<s>` as printed is below 100.00.

## Checking

The output is compared token by token; numbers may differ by at most 0.01.

## Examples

### Example 1

Input:

```
Message #100.
Received at 00:10:20.
Current ship's coordinates are
12^30'00" NL
and 40^10'00" WL.
An iceberg was noticed at
12^10'00" NL
and 41^00'00" WL.
===
```

Output:

```
The distance to the iceberg: 52.78 miles.
DANGER!
```

### Example 2

Input:

```
Message #101.
Received at 01:11:21.
Current ship's coordinates are
55^45'20" NL
and 37^37'00" EL.
An iceberg was noticed at
59^56'30" NL
and 30^18'00" EL.
===
```

Output:

```
The distance to the iceberg: 342.61 miles.
```

## Solution

**Parsing.** Every coordinate is three integers followed by `NL`, `SL`, `EL`
or `WL`. Replace the characters `^`, `'` and `"` by spaces, split the text
into tokens and, at every token of the form `?L` with `?` among `N S E W`,
take the three previous tokens as degrees, minutes and seconds. The value
is `degrees + minutes / 60 + seconds / 3600`, negative for south and west.
The first two values are the ship, the last two the iceberg.

**Distance.** For latitudes `φ1, φ2` and longitudes `λ1, λ2` in radians, the
central angle `θ` between the points is given by the **haversine formula**

`hav θ = sin²((φ2 - φ1) / 2) + cos φ1 · cos φ2 · sin²((λ2 - λ1) / 2)`,

so `θ = 2 · asin(sqrt(hav θ))` and the distance is `R · θ` with
`R = 6875 / 2`. The spherical law of cosines,
`cos θ = sin φ1 sin φ2 + cos φ1 cos φ2 cos(λ2 - λ1)`, gives the same value but
loses precision for nearby points, where `cos θ` is very close to 1.

**The danger line.** It depends on the printed value: a distance of 99.996
miles is printed as `100.00` and is not dangerous. Compare the distance
rounded to hundredths with 100.00.

Pitfalls:

- longitudes on both sides of the 180th meridian (`179°59' E` and
  `179°59' W` are 2 minutes apart);
- clamp `hav θ` to 1 before `sqrt`/`asin`: rounding can push it above 1 for
  antipodal points;
- the threshold on the rounded value, not on the exact one.

## Language notes

The same parsing and formula everywhere; Python uses a regular expression,
Java prints with `Locale.US`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1030_geometry.cpp](1030_geometry.cpp) | G++ 13.2 x64 | geometry | O(length of the message) | AC | 0.015 s | 352 KB |
| [1030_geometry.go](1030_geometry.go) | Go 1.14 x64 | geometry | O(length of the message) | AC | 0.046 s | 1120 KB |
| [1030_geometry.java](1030_geometry.java) | Java 1.8 | geometry | O(length of the message) | AC | 0.093 s | 988 KB |
| [1030_geometry.py](1030_geometry.py) | Python 3.12 x64 | geometry | O(length of the message) | AC | 0.062 s | 516 KB |
| [1030_geometry.rs](1030_geometry.rs) | Rust 1.75 x64 | geometry | O(length of the message) | AC | 0.015 s | 288 KB |
