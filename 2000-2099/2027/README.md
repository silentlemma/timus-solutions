# 2027. Execute a bounded register grid

[Timus 2027](https://acm.timus.ru/problem.aspx?space=1&num=2027) · difficulty 541 · simulation

Original problem by Kirill Borozdin, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Interpret a rectangular grid of instructions. The machine has one
current integer register and 26 memory registers named `A` through `Z`,
all initially zero. Its pointer starts in the top-left cell, facing
right. A tick executes that cell's instruction, then moves one cell in
the resulting direction. The grid does not wrap.

| Instruction | Effect before movement |
| --- | --- |
| `^`, `>`, `v`, `<` | Set direction to up, right, down, left respectively. |
| `.` | Do nothing. |
| `A`…`Z` | Swap the current value with the named memory register. |
| `?` | Overwrite the current register with the next input number. After exhaustion, reuse the last number on every read. |
| `!` | Output the current value, then reset the current register to zero. |
| `+`, `-` | Increase or decrease the current value by one. |
| `@` | Turn counterclockwise if the current value is zero; otherwise turn clockwise, including for negative values. |
| `#` | Halt immediately, without moving. |

After an instruction, a current value outside `[-100000,100000]` causes
`OVERFLOW ERROR`. If the subsequent movement leaves the grid, stop with
`RUNTIME ERROR`. If 1000000 ticks finish without a halt or either error,
stop with `TIME LIMIT EXCEEDED`. Preserve all numbers already output.
Operation and overflow come before movement, and both precede the
tick-budget error. In particular, a halt on tick 1000000 succeeds.

Grid dimensions satisfy `1 ≤ H,W ≤ 100`. There are `1 ≤ N ≤ 100000`
input integers, each of absolute value at most 100000. Ignoring unused
input is allowed. Limits: 2 seconds, 64 MB.

## Input

Read `H W`, then `H` instruction rows of exactly `W` characters. Only
the instructions above occur. Next read `N`, followed by the `N`
integers, one per line.

## Output

Write one integer per executed `!`, each on its own line. If an error
occurs, append its exact message on a separate line. A normal halt
appends nothing; output may be empty.

## Checking

Outputs are compared token by token.

## Examples

```
4 6
?A?v>v
>..>@A
-...A!
^A.+<#
2
2
3
```

```
5
```

```
2 4
?!>v
##^<
1
0
```

```
0
TIME LIMIT EXCEEDED
```

```
1 4
??!#
1
1
```

```
1
```

## Solution

Read each integer as a decimal token: consume an optional `+` or `-`,
accumulate its digits, then apply the sign. Use this for dimensions,
the input count and input values before simulating.

Directly simulate the machine, storing row, column, direction, current
value, memory, input cursor and output buffer. Encode directions
clockwise as right, down, left, up. At `@`, add one modulo four for
nonzero, or subtract one modulo four for zero. Keep the input cursor at
the last valid index after the final number has been read.

For each of at most 1000000 ticks, fetch and execute the instruction.
Return immediately at `#`. Otherwise check the value bound, move by the
direction's row/column offset, and check the board boundary. Return
immediately on the first error. If the loop finishes, append the
time-limit message. Output buffering preserves earlier values even when
a later error occurs. No cycle detection is needed: a cycle may still
emit many values, so simply stopping on a repeated location would be
wrong.

Correctness follows by induction over ticks. Initially the stored
registers, pointer, direction, unread input and empty output match the
machine. Each instruction performs the specified update: swaps retain
both values, reads select the next number or the last repeated number,
and output occurs before clearing. Direction changes precede movement.
Therefore the next state and output prefix agree. The bound and boundary
checks occur at the specified phases, giving the same first error; `#`
stops before movement. After the millionth completed tick, the only
remaining termination is the time limit. Thus the entire output,
including any terminal error, is exact.

In the first sample, the loop transfers units through register `A` and
outputs 5. The second outputs zero, clears the register and enters a
loop that cannot reach a halt, so it also reports the time limit. The
third reads the only input twice; the second read repeats 1, which is
printed before halting.

Let `S ≤ 1000000` be the executed ticks and `B` the output length in
characters. Time is `O(HW + N + S + B)`. With input and output buffers,
space is `O(HW + N + B)`; the 27 registers and pointer state use
constant space. Streaming output could reduce the output-storage term,
but must preserve every output before an error.

Pitfalls:

- Accept an explicit `+` on integers, including the input count. Test `028`
  uses `+1`; treating the sign as a digit makes the count negative.
- A register letter swaps values; it does not copy. `!` clears the
  current value.
- Read past the input by repeating the final number; unused numbers are
  harmless.
- A negative current value still turns clockwise at `@`.
- Do not wrap at edges or move after `#`. Overflow wins over leaving the grid.
- Execute the millionth instruction and its movement before deciding the
  time limit.
- Preserve large output streams; an immediate halt need not print even a
  newline.

The teaching Python interpreter reads the grid as characters and uses match to dispatch each instruction. It keeps row and column separately. The input iterator converts a token with int when ? requests it. next(values, last) repeats the last input after exhaustion. StringIO collects the output and any terminal message. A halt returns immediately. Other ticks execute the instruction, check overflow, then move and check the boundary. For N input tokens, T executed ticks and B output bytes, time is O(HW + N + T + B) and space is O(HW + N + B).

## Optimized solutions

`2027_simulation_optimized.java`. Keep the exact interpreter operation order and tick/error semantics. Store the grid in one byte array; consume input numbers only when ? executes, retaining the last value for repeated reads after exhaustion. Stream ! outputs and terminal error messages rather than storing all numbers and the growing answer. Halt still precedes movement; overflow precedes bounds checking; the tick limit is checked only after completing the millionth instruction and movement. Negative current values turn clockwise at @. For T executed ticks, time O(HW+T), storage O(HW+26) plus fixed buffers, independent of unused input count and output length.

Compared with `2027_simulation.java`: time 0.156 s → 0.14 s; memory 21 392 KB → 552 KB.

C++, Go and Rust keep the interpreter semantics but compile the H×W character grid once to byte opcodes, with a zero boundary frame and four linear direction offsets. A tick starts inside the grid, and a single step can reach at most the surrounding frame. The frame uses the reserved zero opcode, so checking the destination detects an exit before the next tick. Input values are read only when ? executes; after exhaustion repeat the last source value, independently of register exchanges and the current accumulator. Output is streamed through fixed buffers (Rust uses C character I/O), rather than retaining the input list and the potentially long output. Every executed instruction checks overflow before movement and checks leaving the board immediately after movement. These errors still precede TIME LIMIT EXCEEDED on tick 1,000,000; # halts before movement, while tick1,000,001 is never executed. For T≤1,000,000 executed instructions, time O(HW+T), space O(HW) plus fixed I/O buffers and26 registers; it does not grow with the number of input values or output lines. The simple interpreters remain unchanged; Java/Python reuse admitted baseline files.

The accepted Rust 1.75 x64 run takes 0.078 s versus 0.031 s for the base and uses 72 KB versus 6264 KB.

The accepted base implementations [2027_simulation.java](2027_simulation.java), [2027_simulation.py](2027_simulation.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`2027_simulation_optimized.java`: time place 4/34, memory place 2/34 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2027_simulation.cpp](2027_simulation.cpp) | G++ 13.2 x64 | simulation | O(HW + N + S + B) | AC | 0.031 s | 8132 KB | 11293002 |
| [2027_simulation.go](2027_simulation.go) | Go 1.14 x64 | simulation | O(HW + N + S + B) | AC | 0.093 s | 11016 KB | 11298002 |
| [2027_simulation.java](2027_simulation.java) \* | Java 1.8 | simulation | O(HW + N + S + B) | AC | 0.156 s | 21392 KB | 11325568 |
| [2027_simulation.py](2027_simulation.py) \* | Python 3.12 x64 | simulation | O(HW + N + S + B) | AC | 0.875 s | 21712 KB | 11298005 |
| [2027_simulation.rs](2027_simulation.rs) | Rust 1.75 x64 | simulation | O(HW + N + S + B) | AC | 0.031 s | 6264 KB | 11298006 |
| [2027_implementation.py](2027_implementation.py) | Python 3.12 x64 | implementation | O(HW + N + T + B) | AC | 0.937 s | 20624 KB | 11315921 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2027_simulation_optimized.cpp](2027_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(HW + T) | AC | 0.015 s | 144 KB | 11315741 |
| [2027_simulation_optimized.go](2027_simulation_optimized.go) | Go 1.14 x64 | simulation | O(HW + T) | AC | 0.031 s | 920 KB | 11315743 |
| [2027_simulation_optimized.rs](2027_simulation_optimized.rs) \* | Rust 1.75 x64 | simulation | O(HW + T) | AC | 0.078 s | 72 KB | 11315747 |
| [2027_simulation_optimized.java](2027_simulation_optimized.java) | Java 1.8 | simulation | O(HW+T) | AC | 0.14 s | 552 KB | 11325034 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
