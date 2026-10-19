# 1996. Minimum low-bit edits for a byte substring

[Timus 1996](https://acm.timus.ru/problem.aspx?space=1&num=1996) · difficulty 1240 · strings

Original problem by Denis Dublennykh, prepared by Oleg Dolgorukov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An image is a sequence of `n` bytes and a message contains `m` bytes.
Only the least significant bit of each image byte may be flipped. Make
the message appear as one contiguous block, minimizing the total number
of flips. Among equally cheap placements choose the earliest start. The
seven higher bits of every byte stay fixed. Bounds: `1≤n,m≤250000`; time
2 seconds, memory 64 MB.

## Input

The first line gives `n m`. The next two lines contain the image and
message respectively. Each byte is an eight-character binary token, most
significant bit first, separated by spaces.

## Output

Print `No` if no placement exists. Otherwise print `Yes`, followed by
the minimum flip count and the one-based starting byte on the next line.

## Checking

Outputs are compared token by token.

## Examples

```
3 2
11110001 11110001 11110000
11110000 11110000
```

```
Yes
1 2
```

```
3 1
11110000 11110001 11110000
11110000
```

```
Yes
0 1
```

In the first case both starts have matching higher bits. The first needs
two flips, while the second needs one, so the answer starts at byte 2.
In the second case bytes 1 and 3 both need zero flips; byte 1 wins the
tie.

## Solution

Let `A[i]` and `B[j]` be the input byte values. First run KMP on
`A[i]>>1` and `B[j]>>1`. Its occurrences are exactly the feasible
starts: changing the low bit cannot repair a mismatch in the remaining
seven bits, while equal higher bits can always be completed by the low
bit. After each occurrence restore the prefix-function state so
overlapping matches are retained. If `m>n` or there are no occurrences,
return `No`.

Write `a[i]=A[i]&1`, `b[j]=B[j]&1`. Let `P` be prefix sums of `a`, and
let `q=sum(b)`. Reverse `b` and convolve it with `a`, obtaining `C`. At
zero-based start `s`, `C[s+m-1]=sum(a[s+j]·b[j])`. The identity `x xor
y=x+y−2xy` for bits gives the exact cost

`P[s+m]−P[s]+q−2·C[s+m−1]`.

Evaluate this only at feasible starts, in increasing order. Replace the
answer only for a strictly smaller cost, which proves the required tie
rule. No changes outside the selected block are useful.

### Exact transform in C++, Go, Java and Rust

Use an NTT modulo `998244353=119·2^23+1` with primitive root 3. Pad both
arrays to the next power of two `L≥n+m−1`; here `L≤524288`, so the
needed roots exist. Two forward transforms, pointwise multiplication and
one inverse recover the convolution. Every integer coefficient is
between 0 and `m≤250000`, below the modulus, so its modular
representative is the exact count. There is no floating rounding or
probabilistic equality test. Products use 64-bit arithmetic; sums of two
residues fit signed 32 bits. With at most 32 feasible starts, literal
low-bit comparisons replace the transform.

### Exact integer multiplication in Python

Use base `R=2^18`. Pack `X=sum(a[i]R^i)` and `Y=sum(b[m−1−j]R^j)`. Their
product has the same convolution as its base-`R` digits. Each
coefficient is at most 250000, strictly below 262144, so carries never
mix neighboring coefficients. Four bits are packed into nine bytes with
a 16-entry table. Convert the product back to little-endian bytes and
extract each 18-bit digit. Its bit offset modulo eight is 0, 2, 4 or 6,
so three bytes always suffice. Padding the final four-bit group adds
only zero digits.

For at most 2048 feasible starts, pack the low bits one per binary digit
and compute masked XOR/popcount directly. The mask removes bytes beyond
the message length; reversal puts the first byte at the least
significant position. With a fixed cap this branch is linear in the
input length. Uniform higher-bit sequences have a direct occurrence-list
shortcut. Both shortcuts preserve the same cost and tie rule.

### Complexity

The four NTT ports take `O(n+m+L log L)` time and `O(n+m+L)` memory,
hence `O((n+m) log(n+m))` and `O(n+m)`. For Python let `M(u,v)` be the
cost of multiplying integers of at most `u` and `v` bits: time is
`O(n+m+M(18n,18m))`, with linear stored data plus multiplication
workspace. This is an integer-multiplication bound, rather than an FFT
bound for Python.

Match all seven immutable bits, not just the low-bit pattern. Reverse
the message before convolution and read coefficient `s+m−1`. Search only
feasible starts and keep the first equal-cost result. Leading zeroes
belong to a byte token. All-zero products, maximum coefficients,
overlapping matches, `m>n`, and one-window cases are valid.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1996_strings.cpp](1996_strings.cpp) | G++ 13.2 x64 | strings | O((n+m) log(n+m)) | AC | 0.156 s | 7028 KB |
| [1996_strings.go](1996_strings.go) | Go 1.14 x64 | strings | O((n+m) log(n+m)) | AC | 0.156 s | 22660 KB |
| [1996_strings.java](1996_strings.java) | Java 1.8 | strings | O((n+m) log(n+m)) | AC | 1.000 s | 11184 KB |
| [1996_strings.py](1996_strings.py) | Python 3.12 x64 | strings | O(n+m+M(18n,18m)) | AC | 1.421 s | 35828 KB |
| [1996_strings.rs](1996_strings.rs) | Rust 1.75 x64 | strings | O((n+m) log(n+m)) | AC | 0.125 s | 17348 KB |
