# 1958. Sort by Value-Length Cyclic Swaps

[Timus 1958](https://acm.timus.ru/problem.aspx?space=1&num=1958) · difficulty 3577 · constructive

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Olga Soboleva (prepared by Denis Dublennykh).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Sort a permutation p of 1…n using the following operation. Choose a value
a, 1≤a≤n, locate its current zero-based position k, and swap p[k] with
p[(k+a) mod n]. The argument is a value, not an array index. Produce at
most 10⁶ operations, or report impossibility. Limits: 1 second, 64 MB.

## Input

First n, 1≤n≤500. Then n integers forming a permutation of 1…n.

## Output

If sorting is impossible, print `Impossible`. Otherwise print m,
0≤m≤10⁶, then m lines containing the chosen arguments in execution order.
Any valid sequence is accepted; minimizing m is unnecessary. The construction
below proves that every legal input is sortable, so never prints `Impossible`.

## Checking

A checker performs the printed operations and accepts any sequence
within the limit that sorts the permutation.

## Examples

```
5
1 3 5 2 4
```

```
3
4
3
3
```

## Solution

The last position n−1 is a useful buffer. If it contains a<n, operation a
swaps it with index (n−1+a) mod n=a−1, placing a in its final position.
Repeat this until the last value is n; call this a flush.

Within a flush, each operation fixes a different value permanently: another
operation b targets b−1, a different index. Therefore the flush ends with
n in the buffer after at most n−1 calls. Start by flushing once.

Now the permutation has a correct suffix including n. If it is already
sorted, stop. Otherwise find value 1 and repeatedly perform operation 1
until it reaches the last position. These are ordinary forward adjacent
swaps, with no wraparound. Flush again, and repeat.

### Why the suffix grows

Suppose indices k…n−1 were correct before the round, with k>0. Value 1 lies
strictly before this suffix. Moving it right to the buffer shifts every
suffix value one position left: value k+1 is at k−1, k+2 at k, …, n at n−2.

During the following flush, the only way to bring n into the last position
is to fix n−1, targeting n−2. Before that, n−1 must enter the buffer by fixing
n−2; continuing backward, the flush must pass through k,k+1,…,n−1. None of
these values can be displaced from a position already fixed in this flush.
Consequently all these values are fixed, including the new value k at k−1.
The correct suffix grows by at least one position.

Every round therefore makes progress and sorting always succeeds. The
initial flush uses at most n−1 calls. Each of at most n−1 rounds has at
most n−1 moves of value 1 and n−1 flush calls. In total:

m≤(n−1)+2(n−1)²=(n−1)(2n−1)≤498501<10⁶.

For n=1 or an already sorted input, the answer is zero. Each loop iteration
is one real permitted operation, not a compressed sequence.

O(n²) time, including locating 1 once per round and printing the calls.
Stored operations require O(n²) memory; the working permutation is O(n).
Do not confuse value a with index k, use one-based positions in the modulo,
or assume a=n changes the permutation: it is a valid no-op. A flush only
uses a<n. The goal is the increasing order 1…n, not a cyclic rotation.

## Language notes

C++, Go and Rust store the operation sequence in a vector/slice. Java 8
uses a preallocated primitive int array sized by the proven bound, avoiding
boxed integers. Python retains integer references and writes output in
4096-call blocks, avoiding one huge list of decimal strings. Rust uses
only the standard library. All native arithmetic fits ordinary integers.
Resource tests select CPython.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1958_constructive.cpp](1958_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 1416 KB |
| [1958_constructive.go](1958_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 7624 KB |
| [1958_constructive.java](1958_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.109 s | 9216 KB |
| [1958_constructive.py](1958_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.234 s | 6288 KB |
| [1958_constructive.rs](1958_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.078 s | 4964 KB |
