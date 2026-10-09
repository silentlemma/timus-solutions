# 1102. Splitting a line into the words of a strange dialogue

[Timus 1102](https://acm.timus.ru/problem.aspx?space=1&num=1102) · difficulty 176 · strings

Original problem by Katya Ovechkina, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dialogue is any sequence of the words `out`, `output`, `puton`, `in`,
`input` and `one`, written without spaces. For each of `N` lines
(`N ≤ 1000`, lowercase letters, `4 · 10^6` letters in all) print `YES` if
it is a dialogue and `NO` otherwise.

Time limit: 1 second. Memory limit: 16 MB.

## Input

`N`, then `N` lines.

## Output

`YES` or `NO` for each line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
puton
inonputin
oneputonininputoutoutput
oneininputwooutoutput
outpu
utput
```

Output:

```
YES
NO
YES
NO
NO
NO
```

## Solution

Read forwards, the words overlap badly: `out` starts `output`, `in`
starts `input`, and `output` + `one` reads like `out` + `puton` + `e`.
Read backwards, they become `tuo`, `tuptuo`, `notup`, `ni`, `tupni` and
`eno`, and none of these is the beginning of another. So at every point
at most one word can end there, and cutting the line greedily from its
end, one word at a time, either uses up the whole line or proves that no
split exists. `O(L)` for `L` letters.

Pitfalls:

- a forward greedy that always takes the longest word fails: `outputon`
  is `out` + `puton`, but taking `output` first leaves `on`;
- the lines are long and the memory limit is only 16 MB, so copies of the
  whole input must be avoided.

The answers were checked against a forward dynamic programming over
prefixes, on every dialogue of up to three words, on near misses and on
random spoiled lines.

## Language notes

- Python matches the reversed line with the regular expression
  `(?:tuo|tuptuo|notup|ni|tupni|eno)*+`; the possessive `*+` keeps no
  states to backtrack to, which is safe because the split is unique.
- Java reads the input byte by byte and keeps only the last six letters
  with a forward DP over them, since a line of four million letters as a
  `String` would not fit in 16 MB.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1102_strings.cpp](1102_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.156 s | 5768 KB |
| [1102_strings.go](1102_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.078 s | 11448 KB |
| [1102_strings.java](1102_strings.java) | Java 1.8 | strings | O(L) | AC | 0.421 s | 476 KB |
| [1102_strings.py](1102_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.140 s | 8328 KB |
| [1102_strings.rs](1102_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 7760 KB |
