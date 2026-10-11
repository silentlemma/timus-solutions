# 1236. Recovering an XOR key from a shifted message

[Timus 1236](https://acm.timus.ru/problem.aspx?space=1&num=1236) · difficulty 498 · math

Original problem by Elena Kruchkova, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Messages are encoded byte by byte as `E[i] = K[i] xor C[i]` with a secret
key K. The same clear text of N bytes (1 ≤ N ≤ 10 000) was sent twice:
once as it is and once with one space (byte 32) put in front. Given both
encoded messages, recover the first N + 1 bytes of the key.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Two lines of hexadecimal digits: the encoded message of N bytes, then the
one of N + 1 bytes.

## Output

The N + 1 key bytes in the same hexadecimal form.

## Examples

### Example 1

Input:

```
05262C5269143F314C2A69651A264B
610728413B63072C52222169720B425E
```

Output:

```
41434D2049435043204E454552432732
```

## Solution

Call the encoded messages S (short) and L (long). The long text starts
with the known space, so `K[0] = L[0] xor 32`. After that, byte i + 1 of
the long message and byte i of the short one hide the same clear byte
C[i]:

```text
C[i] = S[i] xor K[i],   K[i+1] = L[i+1] xor C[i] = L[i+1] xor S[i] xor K[i]
```

Each key byte gives the next one, so a single pass recovers all N + 1.
`O(N)`.

Pitfalls:

- every byte prints as two uppercase digits, with a leading zero below
  16 (test gen3).

## Language notes

- Go and Python decode and encode hexadecimal with library functions;
  C++, Java and Rust convert the digit pairs themselves.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1236_math.cpp](1236_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 376 KB |
| [1236_math.go](1236_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1364 KB |
| [1236_math.java](1236_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 1756 KB |
| [1236_math.py](1236_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 488 KB |
| [1236_math.rs](1236_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 368 KB |
