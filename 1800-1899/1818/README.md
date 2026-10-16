# 1818. Fair Fishermen

[Timus 1818](https://acm.timus.ru/problem.aspx?space=1&num=1818) · difficulty 1925 · number_theory

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n fishermen share a catch one by one. The i-th to wake up throws away
aᵢ fishes so that the rest splits evenly into n parts, takes one part
and leaves the other n − 1 parts, not knowing that others have already
taken theirs. Given every aᵢ, find the smallest possible catch, at
least one fish.

## Input

n (2 ≤ n ≤ 2000), then a₁, …, aₙ (0 ≤ aᵢ ≤ n − 1).

## Output

The smallest catch.

## Examples

### Example 1

Input:

```
2
1 1
```

Output:

```
3
```

### Example 2

Input:

```
3
1 0 2
```

Output:

```
19
```

## Solution

If fisherman k finds Fₖ fishes, the condition is Fₖ ≡ aₖ (mod n), and
the next one finds Fₖ₊₁ = (Fₖ − aₖ)/n · (n − 1). Once Fₖ ≡ aₖ, Fₖ ≥ aₖ
holds by itself, since aₖ < n.

Adding t to the catch adds t·((n − 1)/n)^(k−1) to Fₖ. For t = s·nʲ this
is a multiple of n for the first j fishermen, so their conditions
survive, while fisherman j + 1 gets s·(n − 1)ʲ ≡ s·(−1)ʲ more. So the
catch is fixed digit by digit in base n: at step j pick the only
s in [0, n) that fixes fisherman j + 1, add s·nʲ to the catch and
s·(n − 1)ʲ to what that fisherman finds, then move on to the next. The
catches that work are exactly one residue modulo nⁿ, so the answer is
that residue, or nⁿ when it is 0.

The numbers grow to about n·log₁₀ n ≈ 6600 digits, so all solutions
use big integers: the library ones in Go, Java and Python, and a small
base-10⁹ type in C++ and Rust with only the operations needed here:
multiply-add, subtract, divide and remainder by a small number.
`O(n² log n)` bit operations.

For the second example: fisherman 1 needs X ≡ 1 (mod 3), so X = 1 and
fisherman 1 finds 1, leaving 0 for fisherman 2, who needs 0: fine,
s = 0. Fisherman 3 also gets 0 but needs 2; adding s·9 to X gives
fisherman 3 s·4 ≡ s more, so s = 2 and X = 19.

Pitfalls:

- residue 0 means nⁿ fishes, not 0: someone caught at least one;
- (n − 1)ʲ alternates between 1 and −1 modulo n, so the digit flips
  sign on odd steps;
- what each fisherman finds must be kept exactly, not modulo n: the
  division by n mixes in higher digits.

The answers agree with a brute force for n up to 5 and with an
independent accepted implementation on random tests up to n = 2000.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1818_number_theory.cpp](1818_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^2 log n) | AC | 0.031 s | 1032 KB |
| [1818_number_theory.go](1818_number_theory.go) | Go 1.14 x64 | number_theory | O(n^2 log n) | AC | 0.046 s | 5716 KB |
| [1818_number_theory.java](1818_number_theory.java) | Java 1.8 | number_theory | O(n^2 log n) | AC | 0.250 s | 5244 KB |
| [1818_number_theory.py](1818_number_theory.py) | Python 3.12 x64 | number_theory | O(n^2 log n) | AC | 0.109 s | 2064 KB |
| [1818_number_theory.rs](1818_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^2 log n) | AC | 0.046 s | 320 KB |
