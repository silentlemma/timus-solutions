# 1887. Frequent Flyer Card

[Timus 1887](https://acm.timus.ru/problem.aspx?space=1&num=1887) · difficulty 1068 · probability

Original problem by Eugene Kurpilyanskiy, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A card number has n random digits x₁, …, xₙ, each uniform from 0 to 9,
and a check digit ((∏ (aᵢxᵢ² + bᵢxᵢ + cᵢ)) mod 11) mod 10. Cards are
generated until ten of them have pairwise different check digits. What
is the expected number of generated cards? Print −1 if some check digit
can never appear.

## Input

n (2 ≤ n ≤ 25), then the lines a₁ … aₙ, b₁ … bₙ and c₁ … cₙ (all from 0
to 9).

## Output

The expected number of cards with absolute or relative error at most 10⁻⁶, or −1.

## Examples

### Example 1

Input:

```
13
0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1
```

Output:

```
29.2896825397
```

### Example 2

Input:

```
13
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
```

Output:

```
-1
```

## Solution

First find the distribution of the check digit. The product is taken
modulo 11, so a DP over the 11 residues follows it factor by factor:
each digit xᵢ multiplies the residue by aᵢxᵢ² + bᵢxᵢ + cᵢ with chance
1/10. Residue r gives check digit r mod 10, so residues 0 and 10 both
give 0. If some digit has probability 0, print −1; the DP only adds
positive terms, so such a zero is exact.

Then collect the ten digits, each card showing digit d with probability
p_d. Let E(S) be the expected number of further cards once the digits
in S have been seen. A card either shows a new digit d, with chance
p_d, or repeats, so E(S) = (1 + Σ_{d∉S} p_d·E(S ∪ {d})) / Σ_{d∉S} p_d,
over all 2¹⁰ sets from the full one down. The denominator is summed
over the missing digits rather than taken as 1 minus the seen ones, so
a small probability keeps its precision. The answer is E(∅).
`O(n·10·11 + 2¹⁰·10)`.

In the first example every factor is xᵢ + 1, from 1 to 10, so the
product is a uniform nonzero residue and every check digit has
probability 1/10. The answer is the classic 10·(1 + 1/2 + … + 1/10) ≈
29.2897.

Pitfalls:

- the check digit is (product mod 11) mod 10, so a product of 10 gives
  the digit 0, together with 0 itself;
- a single factor that is always 0 makes every check digit 0;
- products of squares give only quadratic residues modulo 11, so some
  inputs make digits impossible and need −1.

The expectations agree with exact inclusion–exclusion over all sets of
digits and with an independent accepted implementation on 48 random
inputs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1887_probability.cpp](1887_probability.cpp) | G++ 13.2 x64 | probability | O(n + 2^10 * 10) | AC | 0.015 s | 220 KB |
| [1887_probability.go](1887_probability.go) | Go 1.14 x64 | probability | O(n + 2^10 * 10) | AC | 0.031 s | 1228 KB |
| [1887_probability.java](1887_probability.java) | Java 1.8 | probability | O(n + 2^10 * 10) | AC | 0.156 s | 1880 KB |
| [1887_probability.py](1887_probability.py) | Python 3.12 x64 | probability | O(n + 2^10 * 10) | AC | 0.078 s | 636 KB |
| [1887_probability.rs](1887_probability.rs) | Rust 1.75 x64 | probability | O(n + 2^10 * 10) | AC | 0.046 s | 272 KB |
