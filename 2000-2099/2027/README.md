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

## Language notes

Ordinary signed integers cover all values and the one-step overflow
detection. C++ uses a string buffer, Go `strings.Builder`, Java
`StringBuilder`, and Rust `String`. Python uses `StringIO` rather than
retaining nearly a million separate number strings. All use buffered
input and execute the full tick budget without skipping cycles.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2027_simulation.cpp](2027_simulation.cpp) | G++ 13.2 x64 | simulation | O(HW + N + S + B) | AC | 0.031 s | 8132 KB |
| [2027_simulation.go](2027_simulation.go) | Go 1.14 x64 | simulation | O(HW + N + S + B) | AC | 0.093 s | 11016 KB |
| [2027_simulation.java](2027_simulation.java) | Java 1.8 | simulation | O(HW + N + S + B) | AC | 0.140 s | 21408 KB |
| [2027_simulation.py](2027_simulation.py) | Python 3.12 x64 | simulation | O(HW + N + S + B) | AC | 0.875 s | 21712 KB |
| [2027_simulation.rs](2027_simulation.rs) | Rust 1.75 x64 | simulation | O(HW + N + S + B) | AC | 0.031 s | 6264 KB |
