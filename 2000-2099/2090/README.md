# 2090. Crosswalk or traffic light: where each one wins

[Timus 2090](https://acm.timus.ru/problem.aspx?space=1&num=2090) · difficulty 4821 · math, probability

Original problem by Egor Shchelkonogov, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A pedestrian walks with speed v along Marx street towards its crossing
with Engels street and has to reach the opposite corner. One way is to
cross Marx at a crosswalk (no light) at distance d before the crossing
and then cross Engels at the light; the other is to cross both streets
at the light, in either order. The light shows green to Engels walkers
for t₁, yellow for t₂, then green to Marx walkers for t₃ and yellow for
t₄, and repeats; a street is entered only on green. The phase at the
start is uniformly random. Find the probability that the crosswalk is
strictly faster and the probability that the light is strictly faster.
The limits are 1 second and 64 MB.

## Input

v, then d, w₁ (the width of Engels) and w₂ (the width of Marx), then
t₁ … t₄; all from 1 to 10⁶, with w₁ ≤ v t₂ and w₂ ≤ v t₄.

## Output

The two probabilities with an absolute error of at most 10⁻⁹.

## Examples

### Example 1

Input:

```
1
10 1 1
4 1 4 1
```

Output:

```
0.4 0.1
```

## Solution

Both ways walk the same distance d along Marx; the crosswalk way also
crosses Marx first, so it reaches the far corner w₂/v later than the
other way reaches the near corner, and then waits for the Engels green.
Let b = w₂/v and T = t₁ + t₂ + t₃ + t₄. The arrival phase θ of the light
way is uniform too. Represent one cycle as [−t₄, T − t₄), so the final
yellow and the following Engels green form one interval [−t₄, t₁).

- θ in [−t₄, t₁ − b): the crosswalk way reaches the far corner at θ + b,
  enters Engels before its green ends, and finishes first. The light way
  must still wait for the Marx green at t₁ + t₂. This winning interval
  has length t₁ + t₄ − b, which is positive because b ≤ t₄.
- θ in [t₁ − b, t₁): the crosswalk way misses the Engels green and waits
  for the next cycle. The light way crosses Engels and then Marx, finishing
  by t₁ + t₂ + b ≤ T, so it wins. This interval has length b.
- θ in [t₁, T − t₄), the Engels yellow or Marx green: both ways finish
  crossing Marx by T and cross Engels at T, a tie. Here the bounds
  w₁/v ≤ t₂ and b ≤ t₄ ensure that neither route misses that green.

Pitfall (test 05): b can exceed t₁. Then t₁ − b is negative, so part of
the light's winning interval lies in the final yellow; the crosswalk does
not always win during that phase. Individual phase boundaries have zero
probability.

So the probabilities are (v (t₁ + t₄) − w₂) / (v T) and w₂ / (v T) with
T as above. They are rational, so they are printed by exact
integer long division, rounded to 12 decimal places, with trailing zeros
removed.

In the example v = 1, w₂ = 1 and T = 10: the crosswalk wins with
probability (4 + 1 − 1) / 10 = 0.4 and the light with 1/10 = 0.1.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2090_math_probability.cpp](2090_math_probability.cpp) | G++ 13.2 x64 | math, probability | O(1) | AC | 0.015 s | 384 KB |
| [2090_math_probability.go](2090_math_probability.go) | Go 1.14 x64 | math, probability | O(1) | AC | 0.031 s | 1120 KB |
| [2090_math_probability.java](2090_math_probability.java) | Java 1.8 | math, probability | O(1) | AC | 0.093 s | 412 KB |
| [2090_math_probability.py](2090_math_probability.py) | Python 3.12 x64 | math, probability | O(1) | AC | 0.109 s | 488 KB |
| [2090_math_probability.rs](2090_math_probability.rs) | Rust 1.75 x64 | math, probability | O(1) | AC | 0.015 s | 244 KB |
