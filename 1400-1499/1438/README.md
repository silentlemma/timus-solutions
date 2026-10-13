# 1438. Time Limit Exceeded

[Timus 1438](https://acm.timus.ru/problem.aspx?space=1&num=1438) · difficulty 2918 · simulation

Original problem by Alexander Klepinin, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Run a program in a tiny language of at most 2000 lines. A nonblank line
holds a label, a command, or a label followed by a command. The commands are
`end`, `print x`, assignments `v = x`, `v = x op y` with op one of
`+ - * / % or and xor`, `v = not x`, `goto label` and
`if x cmp y goto label` with the six usual comparisons; x and y are
variables or numbers. Labels and keywords ignore letter case, variable
names do not. Values are 32-bit integers and never overflow.

Print what the program prints. If it is still running after ten million
commands, stop it and add the line "Program terminated. Variables
state:" followed by "name: value" for every variable assigned so far,
sorted by name.

Time limit: 1.5 seconds. Memory limit: 64 MB.

## Input

The program; operands need a separating space. Extra spaces are allowed
except between a label and its colon.

## Output

The printed values, then the report if the program was forcibly stopped.

## Examples

### Example 1

Input:

```
X = 5
      Y = 1
loop: Y = Y * X
      X = X - 1
      if X >= 1 goto LOOP
      Print Y
      y = Y - 5
      Print y
      end
```

Output:

```
120
115
```

### Example 2

Input:

```
value = 15
        value = not value
        value = value or 4
        print value
        value = 0
loop:   
        value = value - 1
        Value = value % 6
        ValueA = value % -6
        goto loop
```

Output:

```
-12
Program terminated. Variables state:
Value: 3
ValueA: 3
value: -2499999
```

## Solution

Compile first, run second. Split each line into tokens; a first token
ending in ":" is a label and points to the index of the next command,
so a line with only a label, or several such lines in a row, all lead
to the command that follows. Variables get slots in a value table, and
commands become records, arrays or enums (closures in Python). The run
is a plain loop over these commands with a counter; nothing is looked
up by name while the program runs.

The commands are told apart by their shape: a second token "=" means an
assignment, and the number of tokens after "=" distinguishes a copy,
`not` and a binary operation.
Division rounds towards zero, and the remainder is taken as
`(a mod b + |b|) mod |b|`, which is never negative: the second example
needs `% 6` and `% -6` to give 3 for a negative value. The report is
printed when exactly ten million commands ran and the last of them was
not `end`, even if that command was the last line. `O(L log L + K)` for
the program length L and the step limit K = 10⁷.

Pitfalls:

- a label alone on a line, or two in a row (test 03), and a label named
  like a keyword (test 11);
- variables whose names start with a keyword, like `ifi` (test 10);
- an assignment that was skipped leaves the variable out of the report
  (test 04);
- `end` as the ten millionth command is a normal stop, any other command
  there is not (tests 12, 13, 17);
- names are sorted by character codes, so upper case comes first (test
  16).

## Language notes

- Python runs under PyPy: the longest loops take about 1.6 s with
  CPython and about 0.4 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1438_simulation.cpp](1438_simulation.cpp) | G++ 13.2 x64 | simulation | O(L log L + K) | AC | 0.281 s | 1864 KB |
| [1438_simulation.go](1438_simulation.go) | Go 1.14 x64 | simulation | O(L log L + K) | AC | 0.125 s | 4840 KB |
| [1438_simulation.java](1438_simulation.java) | Java 1.8 | simulation | O(L log L + K) | AC | 0.421 s | 7320 KB |
| [1438_simulation.py](1438_simulation.py) | PyPy 3.10 x64 | simulation | O(L log L + K) | AC | 0.843 s | 8448 KB |
| [1438_simulation.rs](1438_simulation.rs) | Rust 1.75 x64 | simulation | O(L log L + K) | AC | 0.140 s | 2096 KB |
