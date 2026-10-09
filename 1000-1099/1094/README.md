# 1094. A one-line display with a wrapping cursor

[Timus 1094](https://acm.timus.ru/problem.aspx?space=1&num=1094) · difficulty 462 · simulation

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

## Language notes

- All five languages read one line and print all 80 characters, trailing
  spaces included.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1094_simulation.cpp](1094_simulation.cpp) | G++ 13.2 x64 | simulation | O(L) | AC | 0.015 s | 376 KB |
| [1094_simulation.go](1094_simulation.go) | Go 1.14 x64 | simulation | O(L) | AC | 0.015 s | 1092 KB |
| [1094_simulation.java](1094_simulation.java) | Java 1.8 | simulation | O(L) | AC | 0.093 s | 564 KB |
| [1094_simulation.py](1094_simulation.py) | Python 3.12 x64 | simulation | O(L) | AC | 0.078 s | 468 KB |
| [1094_simulation.rs](1094_simulation.rs) | Rust 1.75 x64 | simulation | O(L) | AC | 0.046 s | 204 KB |
