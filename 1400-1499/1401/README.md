# 1401. Gamers

[Timus 1401](https://acm.timus.ru/problem.aspx?space=1&num=1401) · difficulty 159 · constructive

Original problem by Alex Samsonov, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Tile a 2ⁿ × 2ⁿ board, 1 ≤ n ≤ 9, with one cell removed by L-shaped
pieces of three cells. Print the board with 0 on the removed cell and
the number of the piece on every other cell, pieces numbered from 1 to
(4ⁿ − 1) / 3, or -1 if there is no tiling.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

n, then the row x and the column y of the removed cell,
1 ≤ x, y ≤ 2ⁿ; the top-left cell is (1, 1).

## Output

2ⁿ lines of 2ⁿ numbers. Any tiling is accepted.

## Examples

### Example 1

Input:

```
2
1 1
```

Output:

```
0 1 3 3
1 1 4 3
2 4 4 5
2 2 5 5
```

## Solution

A tiling always exists, by halving. Split the board into four quarters;
the removed cell lies in one of them. Put one piece on the three cells
around the middle of the board that belong to the other three quarters.
Now every quarter is a 2ⁿ⁻¹ × 2ⁿ⁻¹ board with exactly one cell taken,
which is the same task, and a 1 × 1 board needs nothing. The solutions
keep the squares still to do on a stack instead of recursing, each with
its taken cell, and give the pieces numbers in the order they are put
down. `O(4ⁿ)`.

Pitfalls:

- the answer is never -1;
- a 512 × 512 board prints 262 144 numbers, so the output is
  buffered (generated tests).

The tests are judged by a checker that asks for 0 at the removed cell
only and for every number from 1 to (4ⁿ − 1) / 3 on three cells forming
an L inside a 2 × 2 square.

## Optimized solutions

`1401_constructive_optimized.py`. Keep the recursive tromino tiling and array("I") rows, whose 4-byte cells hold labels up to 87381 for n<=9. A dedicated side==2 case writes the three cells directly while preserving the real or inherited hole. Larger squares recurse in reverse quadrant order, retaining the teaching stack version's piece labels. Board work/storage is O(4^n), recursion depth O(n), and output retains at most one decimal row. Flush before os._exit(0) inside main. This run is faster than the previous optimized run but uses more memory; report each run as its own time/memory pair.

Exact-source Python 3.12 x64 Accepted #11327426: 0.218 s / 2004 KB. Saved 2026-11-20 compiler-cohort comparison: time 19/157, memory 2/157. At 1024 KB or above strict admission requires both time and memory: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11307190 (Python 3.12 x64) was 0.312 s / 1744 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1401_constructive_optimized.py`: 0.218 s / 2004 KB; retained teaching base `1401_constructive.py`: 0.375 s / 10628 KB.

The C++ revision retains recursive tiling and reverse quadrant order, so tile labels remain unchanged. It splits each label into a low 16-bit cell and a high 8-bit cell instead of storing a 32-bit int. The maximum label is 87381, so 24 bits suffice; the 512 × 512 board uses 768 KiB. A fixed 16 KB numeric output buffer replaces printf per cell. Time and board storage remain O(4^n), with O(n) recursion depth.

Exact-source Accepted (G++ 13.2 x64, #11326640: 0.031 s / 888 KB); teaching base `1401_constructive.cpp`: 0.031 s / 3760 KB. The previous optimized measurement was 0.093 s / 1128 KB. In the saved 20 November 2026 comparison, time place is 53/427, memory place 2/427; below 1 MiB the policy evaluates the time rank only.

The optimized Go solution stores the board in `int32` cells instead of
64-bit `int`, since the piece numbers are at most (4⁹ − 1) / 3 = 87 381,
which halves the board, and formats each number with `strconv.AppendInt`
into one reused byte slice instead of creating a string for every cell:
{1401_constructive_optimized.go}.

The optimized Java solution recurses instead of pushing a `Square`
object for every square onto a stack: a call places the piece of one
square and descends into its quarters, at most n ≤ 9 calls deep, and the
quarters are visited in reverse order, so the pieces get the same
numbers as with the stack. It reads the input with `StreamTokenizer`
instead of `Scanner` and writes the board row by row through a
`BufferedWriter`, reusing one `StringBuilder` for a row, instead of
building the whole output first: {1401_constructive_optimized.java}.

The optimized Rust solution builds the board in the same way but writes
the numbers straight into a `BufWriter` instead of first formatting the
whole board into a `String` of up to about 1.5 MB:
{1401_constructive_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1401_constructive_optimized.cpp`: time reduction +0.00%; memory reduction +76.38%; base: `1401_constructive.cpp`.

- `1401_constructive_optimized.go`: time reduction +0.00%; memory
  reduction +54.86%; base: `1401_constructive.go`.

- `1401_constructive_optimized.java`: time reduction +38.42%; memory
  reduction +57.07%; base: `1401_constructive.java`.

- `1401_constructive_optimized.rs`: time reduction -48.39%; memory
  reduction +72.59%; base: `1401_constructive.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1401_constructive.cpp](1401_constructive.cpp) | G++ 13.2 x64 | constructive | O(4^n) | AC | 0.031 s | 3760 KB | 11286021 |
| [1401_constructive.go](1401_constructive.go) | Go 1.14 x64 | constructive | O(4^n) | AC | 0.031 s | 4732 KB | 11286022 |
| [1401_constructive.java](1401_constructive.java) | Java 1.8 | constructive | O(4^n) | AC | 0.203 s | 13044 KB | 11286024 |
| [1401_constructive.py](1401_constructive.py) | Python 3.12 x64 | constructive | O(4^n) | AC | 0.375 s | 10628 KB | 11286023 |
| [1401_constructive.rs](1401_constructive.rs) | Rust 1.75 x64 | constructive | O(4^n) | AC | 0.031 s | 4276 KB | 11286025 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1401_constructive_optimized.cpp](1401_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(4^n) | AC | 0.031 s | 888 KB | 11326640 |
| [1401_constructive_optimized.go](1401_constructive_optimized.go) | Go 1.14 x64 | constructive | O(4^n) | AC | 0.031 s | 2136 KB | 11305934 |
| [1401_constructive_optimized.java](1401_constructive_optimized.java) \* | Java 1.8 | constructive | O(4^n) | AC | 0.125 s | 5600 KB | 11305935 |
| [1401_constructive_optimized.py](1401_constructive_optimized.py) \* | Python 3.12 x64 | constructive | O(4^n) board work/storage; O(n) recursion | AC | 0.218 s | 2004 KB | 11327426 |
| [1401_constructive_optimized.rs](1401_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(4^n) | AC | 0.046 s | 1172 KB | 11307191 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
