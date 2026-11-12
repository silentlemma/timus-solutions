# 1236. Recovering an XOR key from a shifted message

[Timus 1236](https://acm.timus.ru/problem.aspx?space=1&num=1236) · difficulty 499 · math

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

## Optimized solutions

Let P be the plaintext, K the key, S the shorter ciphertext and L the longer one. The added leading space gives `K[0] = L[0] XOR space`. At index i, `S[i] = P[i] XOR K[i]` and `L[i+1] = P[i] XOR K[i+1]`. Their XOR cancels P[i], so `K[i+1] = K[i] XOR S[i] XOR L[i+1]`. Each key byte is emitted as soon as it is recovered. C++, Go, Java and Rust store only the shorter ciphertext in a 10000-byte array and use 4096-byte input and output blocks. Java expands signed bytes with mask 255. The scan takes O(N) time. Python reuses its base implementation.

The accepted Java 1.8 run takes 0.125 s versus 0.109 s for the base and uses 408 KB versus 1756 KB.

The accepted Rust 1.75 x64 run takes 0.046 s versus 0.015 s for the base and uses 208 KB versus 368 KB.

The accepted base implementations [1236_math.py](1236_math.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

Original Go/Python use library hex conversion; the new C++/Go/Java/Rust variants parse digits and stream the recurrence. Java masks stored bytes with255. Python retains its original library implementation.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1236_math.cpp](1236_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 376 KB | 11283792 |
| [1236_math.go](1236_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1364 KB | 11283795 |
| [1236_math.java](1236_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 1756 KB | 11283798 |
| [1236_math.py](1236_math.py) \* | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 488 KB | 11283796 |
| [1236_math.rs](1236_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 368 KB | 11283799 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1236_math_optimized.cpp](1236_math_optimized.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 76 KB | 11315388 |
| [1236_math_optimized.go](1236_math_optimized.go) \* | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 824 KB | 11315392 |
| [1236_math_optimized.java](1236_math_optimized.java) \* | Java 1.8 | math | O(N) | AC | 0.125 s | 408 KB | 11315395 |
| [1236_math_optimized.rs](1236_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 208 KB | 11315404 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
