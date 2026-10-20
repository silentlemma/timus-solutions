# 2201. A chat server where every gl and hf changes the luck of its readers

[Timus 2201](https://acm.timus.ru/problem.aspx?space=1&num=2201) · difficulty 1097 · parsing, prefix_sums

Original problem by Vadim Barinov, from the University Academic School Olympiad in Informatics 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A game server processes N chat commands: join, quit, online count, a
public message, a private message, and two comparison commands for the
admin. Messages are made of the pairs "gl" and "hf", and every reader
who is online multiplies their luck by A for each "gl" and divides it by
B for each "hf"; authors are not affected. Print the server's reply to
each command, including the comparisons of two players' luck. The
limits are 2.5 seconds and 256 MB.

## Input

N, M, A and B, 1 ≤ N ≤ 86400, 2 ≤ M ≤ 10, 1 ≤ A, B ≤ 10⁹, then N log
lines "[hh:mm:ss] NICK: /command".

Timestamps strictly increase within one day. Nicknames have 1–8 Latin
letters, digits or underscores. Only online players may issue commands,
except for joining; initially only admin is online, and admin never quits.
Messages contain at most M characters, and private messages cannot target
their author. Compared unequal luck values differ by a factor of at least
1.0001; equal luck values are also possible.

## Output

The server's reply to each command.

## Examples

### Example 1

Input:

```
18 4 2 4
[00:00:23] admin: /online
[00:01:02] j0e: /j
[00:01:15] j0e: /s hfhf
[00:01:17] j0e: /q
[00:01:18] admin: /write<j0e> hfhf
[00:03:25] Tea_: /join
[00:04:11] j0e: /join
[00:07:54] Tea_: /j
[00:08:30] admin: /say glgl
[00:08:37] admin: /write<j0e> hfhf
[00:09:00] Tea_: /compare<j0e>
[00:13:41] admin: /c<j0e>-<Tea_>
[00:13:44] j0e: /quit
[00:13:57] admin: /compare<j0e>
[00:27:49] j0e: /j
[00:28:01] j0e: /s hfhf
[00:30:19] admin: /compare<j0e>
[00:30:43] admin: /compare<Tea_>-<j0e>
```

Output:

```
There are 1 players on the server
Successful
j0e: hfhf
Successful
admin (to j0e): hfhf
Successful
Successful
Failed: Tea_ is already on the server
admin: glgl
admin (to j0e): hfhf
Failed: you have no such rights
Tea_ is a lucky guy
Successful
Failed: j0e is not on the server
Successful
j0e: hfhf
j0e is a lucky guy
Their luck is equal
```

## Solution

A player's luck is A^g / B^f, where g and f count the pairs the player
has read, so it is enough to keep the two counts. Public messages reach
everyone online at once, so they go into two running totals, and each
player stores counts relative to them: on joining the totals are
subtracted, on leaving they are added back, and the author of a public
message subtracts its own pairs. For two online players the totals then
cancel, and the difference of luck is described by two integers
Δg and Δf. Private messages change only the recipient's counts.

Equality is decided exactly. Write A = r^s and B = q^t with
the largest possible exponents. If A^Δg = B^Δf with A, B > 1, both are
powers of one integer, and then r = q, so equality holds exactly when
r = q and s·Δg = t·Δf, or when Δg = Δf = 0 for unrelated bases; a base
of 1 simply drops out. Only when the lucks differ is the sign of
Δg·ln A − Δf·ln B used. The ratio guarantee makes its absolute value
at least ln(1.0001), safely above double-precision rounding error under
the count bounds. The pitfall is losing this small difference after
large cancellation (test gen13), or treating equal powers as unequal
because their pair counts differ (test 16). A ratio closer to 1 than
1.0001 cannot be used as an unequal-comparison test.

The rest is careful parsing: short and long command names, the reply
texts, and the order of the checks for comparisons.

Each command takes O(1) apart from reading its line, so the whole log
takes linear time.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2201_parsing_prefix_sums.cpp](2201_parsing_prefix_sums.cpp) | G++ 13.2 x64 | parsing, prefix_sums | O(N) | AC | 0.078 s | 4176 KB |
| [2201_parsing_prefix_sums.go](2201_parsing_prefix_sums.go) | Go 1.14 x64 | parsing, prefix_sums | O(N) | AC | 0.109 s | 16820 KB |
| [2201_parsing_prefix_sums.java](2201_parsing_prefix_sums.java) | Java 1.8 | parsing, prefix_sums | O(N) | AC | 0.203 s | 10020 KB |
| [2201_parsing_prefix_sums.py](2201_parsing_prefix_sums.py) | Python 3.12 x64 | parsing, prefix_sums | O(N) | AC | 0.328 s | 16696 KB |
| [2201_parsing_prefix_sums.rs](2201_parsing_prefix_sums.rs) | Rust 1.75 x64 | parsing, prefix_sums | O(N) | AC | 0.078 s | 11700 KB |
