# 1607. Taxi

[Timus 1607](https://acm.timus.ru/problem.aspx?space=1&num=1607) · difficulty 46 · implementation

Original problem by Denis Musin, from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Petya and a taxi driver haggle. Petya starts at a and raises the offer
by b each time; the driver starts at c and lowers the price by d each
time; they speak in turns, Petya first. Neither names a price past the
other's: the driver accepts Petya's offer instead of asking less than
it, and Petya accepts the driver's price instead of offering more than
it. How much does Petya pay? All numbers are from 1 to 10000.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

a, b, c and d.

## Output

The price of the ride.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
150 50 1000 100
```

Output:

```
450
```

## Solution

Play the haggle out. If a is already at least c, the driver takes it.
Otherwise Petya raises by b; if that reaches the driver's price, Petya
agrees to it. Then the driver lowers by d; if that reaches Petya's
offer, the driver agrees to the offer. The gap shrinks by at least 2 per
round, so at most about 5000 rounds are played: `O(max(1, c - a))`. The results
were compared with an independent implementation on 800 random
inputs.

Pitfalls:

- the side that would cross the other's price gives in at the other's
  price, so the answer is always a price that was actually named
  (tests 04 and 05);
- Petya can start above the driver's price; then no haggling happens and
  Petya pays a (test 02).

## Optimized solutions

The optimized Java solution parses the numbers byte by byte from
`System.in` instead of using `Scanner`: 316 KB instead of 1600 KB, with
the same time.

`1607_math.py`. Replace round-by-round bargaining by a closed formula. If a>=c return a. Otherwise q=(c-a-1)//(b+d) is the number of full rounds after which the parties are still apart; the next offer or reply agrees at min(a+(q+1)*b,c-q*d). Positive b,d make the division valid. This is the math variant; keep the simulation source separately. O(1) bounded-integer time and space. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1607_implementation.py`: time 0.093 s → 0.156 s; memory 416 KB → 200 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1607_math.py`: time place 97/97, memory place 1/97 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1607_implementation.cpp](1607_implementation.cpp) | G++ 13.2 x64 | implementation | O(max(1, c - a)) | AC | 0.015 s | 132 KB | 11288177 |
| [1607_implementation.go](1607_implementation.go) | Go 1.14 x64 | implementation | O(max(1, c - a)) | AC | 0.015 s | 1112 KB | 11288180 |
| [1607_implementation.java](1607_implementation.java) | Java 1.8 | implementation | O(max(1, c - a)) | AC | 0.140 s | 1600 KB | 11288188 |
| [1607_implementation.py](1607_implementation.py) | Python 3.12 x64 | implementation | O(max(1, c - a)) | AC | 0.093 s | 416 KB | 11288185 |
| [1607_implementation.rs](1607_implementation.rs) | Rust 1.75 x64 | implementation | O(max(1, c - a)) | AC | 0.031 s | 224 KB | 11288189 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1607_implementation_optimized.java](1607_implementation_optimized.java) \* | Java 1.8 | implementation | O(max(1, c - a)) | AC | 0.125 s | 316 KB | 11303763 |
| [1607_math.py](1607_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.156 s | 200 KB | 11324835 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
