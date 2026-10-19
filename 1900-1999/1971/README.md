# 1971. Classifying a Dynamic Product Without Overflow

[Timus 1971](https://acm.timus.ru/problem.aspx?space=1&num=1971) · difficulty 674 · number_theory

Original problem by Denis Dublennykh, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A frame of width W and height H costs W·H operations before optional
effects. Each enabled named option multiplies that cost by its integer
factor k. Hardware performs p operations per second, so the frame rate
is p divided by the resulting frame cost. All options start enabled.
After each option switch or resolution change, classify the frame rate.

Print Slideshow below 10 FPS, Perfect at 60 FPS or above, and So-so
otherwise. Report the initial state too. Limits: 2 seconds, 64 MB.

## Input

n, 0≤n≤100000, followed by n lines containing an option name and factor
2≤k≤100. Names consist of 1…10 lowercase Latin letters. Then W,H,p with
320≤W≤2560, 200≤H≤1600, 1≤p≤10⁹. Next is m, 1≤m≤100000, followed by m
commands: On s, Off s, or Resolution w h with the same dimension bounds.
On always names a disabled option, Off an enabled one. Hardware power p
never changes.

## Output

m+1 lines: initial classification and one after each command, using
exactly Slideshow, So-so or Perfect. Equality at 10 belongs to So-so;
equality at 60 belongs to Perfect.

## Checking

Outputs are compared token by token.

## Examples

```
1
vsync 10
640 480 10000000
2
Off vsync
Resolution 320 240
```

```
Slideshow
So-so
Perfect
```

## Solution

### Keep an exact factorization, not the entire product

There are only 25 primes at most 100. Precompute the factorization of
every allowed factor. For each prime q, maintain the total exponent E[q]
over enabled options. Turning an option on adds its factorization; turning
it off subtracts it. A resolution change leaves all exponents untouched.
The map from option names to factors is permanent.

These exponents stay exact even when the product is enormous. Capping
the stored product would lose information needed when many options are
later disabled; floating logarithms can misclassify exact FPS boundaries.

### Evaluate only as far as the lower threshold

Let A=W·H and L=floor(p/(10A)). If L=0, even the empty product gives
less than 10 FPS, so output Slideshow. Otherwise start a temporary
product Q=1 and expand the stored prime powers. Before multiplying by q,
check Q>floor(L/q). If true, the actual option product is greater than L,
so output Slideshow immediately. Otherwise multiply and continue.

This early exit changes no stored exponent. If all prime powers were
consumed, Q is the exact option product and FPS is at least 10. Output
Perfect precisely when Q≤floor(p/(60A)); otherwise output So-so.

Since A≥64000 and p≤10⁹, L≤1562. Each successful multiplication is by
at least two, so there are at most ten successful multiplications and
one failing attempt, regardless of how large E[q] is. Scanning the 25
prime counters is also constant work. Huge exponent values never cause
long inner loops.

### Correctness and bounds

Prime exponents represent exactly the product of enabled options at the
start. Adding or subtracting an option preserves this invariant, while
resolution changes do not affect it. During a query Q is a prefix of
that factorization. A failed bound test proves the complete product is
greater than L, exactly the condition p<10A·product. If no test fails,
the full product was computed exactly; comparison with floor(p/(60A))
is exactly the upper FPS test. Thus all three categories, including both
equalities, are correct after every update.

The largest exponent is at most 600000, 60A≤245760000, and the temporary
product never exceeds 1562. All arithmetic except encoded names fits
signed 32 bits. With the fixed factor bound and expected constant-time
hash lookup, total time is `O(n+m)`. Space is `O(n+m)` including buffered
input/output, or `O(n)` for the maintained state itself.

In the sample, the initial frame costs 640·480·10=3072000 operations:
10⁷/3072000<10, giving Slideshow. Disabling the option reduces the cost
to 307200 and gives about 32.55 FPS, so So-so. At 320×240 the cost is
76800 and the rate about 130.21 FPS, giving Perfect.

Print m+1 answers. Preserve the exact exponent counts even after early
classification; queries must not subtract factors from the stored state.
Never divide a previously capped product on Off. Handle n=0 as product
one, and use integer inequalities at 10 and 60. A resolution change
keeps p fixed. Read long inputs without building millions of temporary
tokens, and retain distinct names even when one is a prefix of another.

## Language notes

Python reads lines and stores byte-string keys. C++ and Go use buffered
streams; Rust keeps one input string and borrows name slices from it.
Java uses a byte buffer and encodes names as base-27 digits 1…26 in a
long: lengths at most ten fit, and nonzero digits preserve prefixes.
Java scans the 25 primes on updates; other versions store sparse factors.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1971_number_theory.cpp](1971_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n+m) | AC | 0.093 s | 7212 KB |
| [1971_number_theory.go](1971_number_theory.go) | Go 1.14 x64 | number_theory | O(n+m) | AC | 0.328 s | 12744 KB |
| [1971_number_theory.java](1971_number_theory.java) | Java 1.8 | number_theory | O(n+m) | AC | 0.187 s | 14272 KB |
| [1971_number_theory.py](1971_number_theory.py) | Python 3.12 x64 | number_theory | O(n+m) | AC | 0.375 s | 16372 KB |
| [1971_number_theory.rs](1971_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n+m) | AC | 0.046 s | 10220 KB |
