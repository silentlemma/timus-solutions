# 1940. Counting Years with No Small Proper Divisor

[Timus 1940](https://acm.timus.ru/problem.aspx?space=1&num=1940) · difficulty 835 · number_theory

Original problem from Open Ural FU Championship 2012 | by Ksenia Karpova (prepared by Egor Shchelkonogov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Consider the B years numbered A+1 through A+B, including the last year.
For a year n, try divisors 2,3,…,n−1 in order, spending one minute per
division. Stop after finding a divisor or spending k minutes. A year
is considered prime if no divisor was found, even when n is composite.
Count these years. If all proper candidates were exhausted sooner,
the year also passes. Limits: 1 second, 64 MB.

## Input

Three space-separated integers A,B,k, where 2≤A,B≤10^9 and 1≤k≤300.
The largest examined year is 2·10^9. Whitespace may include newlines.

## Output

One integer, the number of passing years in (A,A+B], between 0 and B.

## Checking

Compare the single integer token; whitespace is insignificant.

## Examples

```
23 7 3
```

```
2
```

## Solution

The last possible divisor within the time budget is y=k+1, not k.
Rejecting a multiple of a composite divisor adds nothing: a smaller
prime divisor would already reject it. Let p₁,…,p_s be the primes ≤y.

First count integers free of every p_i. Define φ(x,t) as the count of
integers in [1,x] divisible by none of the first t primes, including 1.
Then

φ(x,t)=φ(x,t−1)−φ(⌊x/p_t⌋,t−1).

The subtracted multiples correspond exactly to surviving quotients
after division by p_t. Cache each pair (x,t), shared between both ends.

There is one necessary exception. A prime n≤y passes, because dividing
by n itself is forbidden, but φ would remove it. Add these primes back:

answer = φ(A+B,s)−φ(A,s) + π(min(A+B,y))−π(min(A,y)).

Every excluded composite has a proper prime factor ≤y, so no other
exception exists. The artificial count of 1 cancels between the ends.
The open left and closed right endpoints follow from prefix subtraction.

To make the recursion fast, use b=min(s,6) small primes as a periodic
base. Their product W is at most 30030. Precompute the number of
survivors in every prefix of one period, then φ(x,b) is full periods
plus the remaining prefix, in constant time.

For higher levels, φ(0,t)=0. If 1≤x<p_t, only 1 survives. If
p_t≤x<p_t², no surviving composite can exist: its two smallest prime
factors would both exceed p_t. Thus φ(x,t)=1+π(x)−t. A sieve and prime
prefix counts through L=301² cover every such lookup. Larger states
use the recurrence. Each recursive step decreases t, so the base
and the two pruning rules establish correctness by induction.

Let N=A+B, s=π(k+1)≤62, b≤6, W≤30030 and L=301². There are O(√N)
distinct integer quotients ⌊X/d⌋ for either endpoint X; nested floor
division preserves this form. With memoization there are O(s√N)
states. Expected time is O(L log log L + bW + s√N), and space is
O(L+W+s√N), with recursion depth at most s. The fixed sieve and wheel
are small; no loop or array is proportional to B.

Count A+1 rather than A, include A+B, and test up to k+1. Do not treat
every composite as rejected: 25 passes for k=3. Do not remove a small
prime by testing it against itself. Consecutive k values can give the
same answer when the newly available divisor is composite. An unpruned
inclusion-exclusion over all subsets or scanning a billion years is
unnecessary.

## Language notes

Counts and endpoints fit signed 32-bit integers: N≤2·10^9, answer≤10^9.
Packed cache keys need 64 bits: shift x by six bits, then append t.
C++, Go and Rust use standard hash maps; Java uses a growing primitive
open-addressing map to avoid boxed cache entries. Python integers are
unbounded and wheel prefixes use unsigned-short arrays. All programs
use standard libraries and emit one integer with a final newline.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1940_number_theory.cpp](1940_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(s sqrt(N)) | AC | 0.031 s | 3596 KB |
| [1940_number_theory.go](1940_number_theory.go) | Go 1.14 x64 | number_theory | O(s sqrt(N)) | AC | 0.031 s | 8528 KB |
| [1940_number_theory.java](1940_number_theory.java) | Java 1.8 | number_theory | O(s sqrt(N)) | AC | 0.140 s | 6668 KB |
| [1940_number_theory.py](1940_number_theory.py) | Python 3.12 x64 | number_theory | O(s sqrt(N)) | AC | 0.171 s | 8424 KB |
| [1940_number_theory.rs](1940_number_theory.rs) | Rust 1.75 x64 | number_theory | O(s sqrt(N)) | AC | 0.031 s | 5564 KB |
