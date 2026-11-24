# 1023. Choosing the move limit that lets the second player win

[Timus 1023](https://acm.timus.ru/problem.aspx?space=1&num=1023) · difficulty 218 · games, number_theory

Original problem from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players take turns removing from 1 to `L` buttons from a pile of `K`
buttons; whoever takes the last button wins. The first player has chosen
`K` (`3 ≤ K ≤ 10^8`); now the second player chooses `L` with `2 ≤ L < K`.
Find the smallest `L` with which the second player wins against any play of
the first, or print 0 if there is none.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`K`.

## Output

The smallest winning `L`, or 0.

## Checking

Compare the exact answer tokens; whitespace formatting is immaterial.

- `1023_games_number_theory_optimized.java` (Java 1.8): 14 repository cases.

- `1023_games_number_theory_optimized.py` (PyPy 3.10 x64): 14 repository cases; 1003 additional source-bound comparisons.

## Examples

### Example 1

Input:

```
8
```

Output:

```
3
```

### Example 2

Input:

```
35
```

Output:

```
4
```

## Solution

With moves of `1..L`, losing positions for the player to move are
exactly multiples of `L + 1`, including the empty pile. From a positive
multiple every legal move leads to a non-multiple. From a non-multiple,
removing its remainder modulo `L + 1` leaves a multiple; this is a legal
move and never exceeds the pile. Induction therefore proves the claim.
The second player can force a win exactly when `(L + 1)` divides `K`.

We need the smallest divisor `d ≥ 3`, and the answer is `L = d − 1`.
The divisor `d = K` is always legal, so the answer is never zero for
valid input. The simple versions try every integer divisor `3..sqrt(K)`
in order. If none divides, the complementary smaller factor of a divisor
above the square root can only be 1 or 2. Thus the remaining answer uses
`d = K/2` if that is an integer at least 3, otherwise `d = K`.
In particular, `K = 4` must give `d = 4`, not 2. The first discovered
divisor is minimal, proving the result. Time `O(sqrt(K))`, auxiliary
space `O(1)`. All five original Accepted bases are retained unchanged.

## Optimized solutions

Keep the same smallest-legal-divisor game proof. The answer is d-1 for the smallest divisor d>=3 of K. Test3,4and5first; every remaining candidate is coprime to30, so the wheel gaps(4,2,4,2,4,6,2,6) enumerate exactly the remaining possible small factors. If none is found through sqrt(K), the only remaining choice is K/2when even, otherwise K. Python checks four successive wheel candidates per loop backedge: this preserves the search order and exact stopping conditions while reducing hot-loop/JIT overhead, without importing a JIT control module. Java retains its compact odd-divisor scan. Time O(sqrt(K)), constant state; all1003additional factor checks, including large primes and upper-bound composites, matched an independent direct-divisor oracle.

- `1023_games_number_theory_optimized.java`: 0.109 s / 392 KB; base `1023_games_number_theory.java`: 0.109 s / 1576 KB; relative change: time -0.0%, memory -75.1%.
- `1023_games_number_theory_optimized.py`: 0.140 s / 280 KB; base `1023_games_number_theory.py`: 0.078 s / 400 KB; relative change: time +79.5%, memory -30.0%.

`1023_games_number_theory_optimized.rs`. Keep the search for the least admissible divisor, including the even-number fallback. The bound d<=K/d avoids multiplying d by itself. Only the current divisor and the input value are needed: O(√K) time and O(1) auxiliary space. Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1023_games_number_theory.rs`: time 0.015 s → 0.015 s; memory 220 KB → 56 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1023_games_number_theory_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1023_games_number_theory.cpp](1023_games_number_theory.cpp) | G++ 13.2 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 128 KB | 11278278 |
| [1023_games_number_theory.go](1023_games_number_theory.go) | Go 1.14 x64 | games, number_theory | O(sqrt(K)) | AC | 0.031 s | 1072 KB | 11278279 |
| [1023_games_number_theory.java](1023_games_number_theory.java) | Java 1.8 | games, number_theory | O(sqrt(K)) | AC | 0.109 s | 1576 KB | 11278281 |
| [1023_games_number_theory.py](1023_games_number_theory.py) | Python 3.12 x64 | games, number_theory | O(sqrt(K)) | AC | 0.078 s | 400 KB | 11278280 |
| [1023_games_number_theory.rs](1023_games_number_theory.rs) | Rust 1.75 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 220 KB | 11278282 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1023_games_number_theory_optimized.java](1023_games_number_theory_optimized.java) | Java 1.8 | games, number_theory | O(sqrt(K)) time; O(1) space | AC | 0.109 s | 392 KB | 11308324 |
| [1023_games_number_theory_optimized.py](1023_games_number_theory_optimized.py) \* | PyPy 3.10 x64 | games, number_theory | O(sqrt(K)) time; O(1) space | AC | 0.140 s | 280 KB | 11309754 |
| [1023_games_number_theory_optimized.rs](1023_games_number_theory_optimized.rs) | Rust 1.75 x64 | games, number_theory | O(√K) | AC | 0.015 s | 56 KB | 11325081 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
