# 1612. Tram Forum

[Timus 1612](https://acm.timus.ru/problem.aspx?space=1&num=1612) · difficulty 151 · strings

Original problem by Alexander Ipatov, prepared by Denis Musin, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A forum message of at most 10000 characters, small Latin letters,
spaces, line breaks and the marks `. , - : ! ?`, is written by a tram
driver if the word `tram` occurs in it more often than `trolleybus`, by
a trolleybus driver if the other way round, and by a bus driver
otherwise. Words are runs of letters. Who wrote it?

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The message.

## Output

`Tram driver`, `Trolleybus driver` or `Bus driver`.

## Examples

### Example 1

Input:

```
of course, tram is the best transport
in the world!
```

Output:

```
Tram driver
```

### Example 2

Input:

```
yes, yekaterinburg trams are the
best trams in the world, but
i like my trolleybus too.
```

Output:

```
Trolleybus driver
```

### Example 3

Input:

```
read forum.tr.ru every day!
you can learn much about tram 
drivers and trolleybus drivers.
```

Output:

```
Bus driver
```

## Solution

Split the message into words at every character that is not a letter,
count the words equal to `tram` and to `trolleybus`, and compare the
two counts: `O(n)`. The answers were compared with an independent
implementation on generated messages.

Pitfalls:

- only whole words count: `trams`, `tramway` or the `tr` in
  `forum.tr.ru` are not the word `tram` (examples 2 and 3);
- marks also separate words, so `tram-tram` holds two trams and
  `tram,trolleybus` one of each (tests 06 and 07);
- equal counts, zero included, mean a bus driver.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1612_strings.cpp](1612_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 156 KB |
| [1612_strings.go](1612_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1124 KB |
| [1612_strings.java](1612_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 840 KB |
| [1612_strings.py](1612_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 444 KB |
| [1612_strings.rs](1612_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 232 KB |
