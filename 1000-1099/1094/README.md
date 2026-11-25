# 1094. A one-line display with a wrapping cursor

[Timus 1094](https://acm.timus.ru/problem.aspx?space=1&num=1094) · difficulty 466 · simulation

Original problem by Stanislav Vasiliev, from the USU Open Collegiate Programming Contest, March 2001, Senior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A display shows one line of 80 characters, at first all spaces, with the
cursor at the leftmost position. Pressing a character key writes it at
the cursor, replacing what was there, and moves the cursor one position
right; `<` and `>` move the cursor without writing. Whenever the cursor
goes past the left or the right edge, it jumps to the leftmost position.
Given one line of up to 10000 keys, print the display at the end.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

One line of keys: letters, digits, `:;-!?.,`, spaces, `<` and `>`.

## Output

The 80 characters of the display.

## Checking

The output must be equal to the expected text; only trailing whitespace at
the very end is ignored.

## Examples

### Example 1

Input:

```
>><<<Look for clothes at the <<<<<<<<<<<<<<<second floor. <<<<<<<Fresh pizza and <<<<<<<<<<<<<<<<hamburger at a shop right to <<<<<<<<<<<<<the entrance. Call <<<<<<<<<< 123<-456<-8790 <<<<<<<<<<<<<<<<to order <<<<<<<<<<<<<<<<<computers< and office<<<<<<< chairs.
```

Output:

```
Look for second hamburger at computer and chairs.790                            
```

## Acceptance update

Refreshed files: [1094_simulation_parsing_optimized.rs](1094_simulation_parsing_optimized.rs). Their new exact-source Accepted results are listed in the solution tables. Earlier comparison measurements and rankings for these files refer to preceding source snapshots and are retained as historical evidence. The cached audit confirms qualifying coverage in every available language. Teaching versions are retained for clarity; a source that also serves as the fast version must meet the performance criterion.

## Solution

Keep an array of 80 characters and the cursor position. For `<` and `>`
move the cursor; for any other key write it and move right. After every
key, a cursor outside `0 … 79` is set back to 0. `O(L)` for `L` keys.

Pitfalls:

- the left edge also sends the cursor to the leftmost position, which is
  the same as staying there: `<` at position 0 keeps the cursor at 0;
- after writing the 80th position the cursor wraps to the first one, and
  so does `>` from the last position;
- spaces are ordinary keys and must not be skipped, so the line is read
  whole, with only the line break removed;
- the line may be empty, and then the display stays blank.

The answers were checked against a separate simulation that stores the
written cells in a dictionary.

## Optimized solutions

The new C++, Go and Rust sources consume keys incrementally and keep only the 80 display cells and cursor, instead of retaining the entire input line. A left move at zero stays at zero; a right move or write at the last cell wraps to zero. Spaces remain ordinary writes. Stop at the first line ending or EOF and print all 80 cells, including trailing blanks. Time stays O(L), auxiliary storage O(80) with a bounded Go input buffer. C++/Rust use C-runtime character I/O, Rust with a C entry point; Go uses standard handles. All simple sources remain; Java/Python reuse their admitted bases.

The accepted base implementations [1094_simulation.java](1094_simulation.java), [1094_simulation.py](1094_simulation.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1094_simulation_parsing_optimized.rs`. Process terminal commands in bounded blocks instead of checking the input refill path for every byte; preserve cursor movement and wrapping.

Accepted #11328989 (Rust 1.75 x64): **0.015 s / 52 KB**. Archived comparison: `1094_simulation_optimized.rs` (Rust 1.75 x64) — 0.031 s / 52 KB (#11315266).

## Language notes

These notes describe the simple implementations.

- All five languages read one line and print all 80 characters, trailing
  spaces included.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1094_simulation.cpp](1094_simulation.cpp) | G++ 13.2 x64 | simulation | O(L) | AC | 0.015 s | 376 KB | 11279111 |
| [1094_simulation.go](1094_simulation.go) | Go 1.14 x64 | simulation | O(L) | AC | 0.015 s | 1092 KB | 11279112 |
| [1094_simulation.java](1094_simulation.java) | Java 1.8 | simulation | O(L) | AC | 0.093 s | 564 KB | 11279114 |
| [1094_simulation.py](1094_simulation.py) | Python 3.12 x64 | simulation | O(L) | AC | 0.078 s | 468 KB | 11279113 |
| [1094_simulation.rs](1094_simulation.rs) | Rust 1.75 x64 | simulation | O(L) | AC | 0.046 s | 204 KB | 11279115 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1094_simulation_optimized.cpp](1094_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(L) | AC | 0.001 s | 76 KB | 11315263 |
| [1094_simulation_optimized.go](1094_simulation_optimized.go) | Go 1.14 x64 | simulation | O(L) | AC | 0.015 s | 276 KB | 11315265 |
| [1094_simulation_optimized.rs](1094_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(L) | AC | 0.031 s | 52 KB | 11315266 |
| [1094_simulation_parsing_optimized.rs](1094_simulation_parsing_optimized.rs) | Rust 1.75 x64 | simulation, parsing | O(L) | AC | 0.031 s | 48 KB | 11330213 |
