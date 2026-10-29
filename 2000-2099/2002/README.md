# 2002. Test Task

[Timus 2002](https://acm.timus.ru/problem.aspx?space=1&num=2002) · difficulty 72 · implementation

Original problem by Kirill Borozdin, from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Simulate a registry of user accounts, initially empty. A request
registers a name and password, logs in with a password, or logs out by
name. Every request must emit exactly the specified response, testing
errors in their prescribed order. Registration creates an offline
account. Failed requests leave all existing passwords and sessions
unchanged.

## Input

An integer `1≤n≤100`, followed by `n` requests: `register name
password`, `login name password`, or `logout name`. Names and passwords
are case-sensitive, nonempty strings of length at most 30, with ASCII
codes 33–126. Thus tokens have no whitespace, but may contain
punctuation or be equal to command words. Time limit 0.5 seconds, memory
64 MB.

## Output

One response line per request. Preserve the exact English spelling,
colon, spaces and punctuation below. For each command, test its table
rows from top to bottom.

| Condition | Response | Change |
| --- | --- | --- |
| register: name exists | `fail: user already exists` | none |
| register: otherwise | `success: new user added` | store password, offline |
| login: name missing | `fail: no such user` | none |
| login: wrong password | `fail: incorrect password` | none |
| login: already online | `fail: already logged in` | none |
| login: otherwise | `success: user logged in` | online |
| logout: name missing | `fail: no such user` | none |
| logout: already offline | `fail: already logged out` | none |
| logout: otherwise | `success: user logged out` | offline |

## Checking

The repository compares output character by character after removing all
trailing whitespace from the complete output. Trailing spaces and extra
blank lines at the end are ignored; whitespace elsewhere must match.

## Examples

```
6
register vasya 12345
login vasya 1234
login vasya 12345
login anakin C-3PO
logout vasya
logout vasya
```

```
success: new user added
fail: incorrect password
success: user logged in
fail: no such user
success: user logged out
fail: already logged out
```

Registration stores `12345` and leaves the account offline. The wrong
password fails without changing it. Correct login succeeds, an unknown
name fails, the first logout succeeds and the next logout fails because
the account is already offline.

## Solution

Keep a hash map from a name to its password and an online flag. For
every request, look the name up and check the conditions of the table
from the top; the first one that holds gives the reply and the only
change. `O(n·L)` for names of length L ≤ 30.

Pitfalls:

- for login, a wrong password is reported before "already logged in";
- registration does not log the user in;
- failed requests change nothing, and a lookup never creates an account;
- names and passwords are compared exactly, case included.

## Optimized solutions

The optimized C++ solution reads the words with `scanf` into buffers of
31 bytes instead of `iostream` and answers every request at once instead
of storing all requests and replies first: 212 KB instead of 516 KB,
with the same time.

The optimized Go solution parses the requests by hand from a 1 KB
buffered reader instead of `fmt.Fscan` and answers each one at once
through a buffered writer, with no list of commands: 0.015 s instead of
0.046 s and 936 KB instead of 1124 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2002_implementation.cpp](2002_implementation.cpp) | G++ 13.2 x64 | implementation | O(n L) | AC | 0.015 s | 516 KB | 11292443 |
| [2002_implementation.go](2002_implementation.go) | Go 1.14 x64 | implementation | O(n L) | AC | 0.046 s | 1124 KB | 11292444 |
| [2002_implementation.java](2002_implementation.java) | Java 1.8 | implementation | O(n L) | AC | 0.140 s | 664 KB | 11303527 |
| [2002_implementation.py](2002_implementation.py) | Python 3.12 x64 | implementation | O(n L) | AC | 0.093 s | 576 KB | 11292445 |
| [2002_implementation.rs](2002_implementation.rs) | Rust 1.75 x64 | implementation | O(n L) | AC | 0.046 s | 460 KB | 11292448 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2002_implementation_optimized.cpp](2002_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n L) | AC | 0.015 s | 212 KB | 11303656 |
| [2002_implementation_optimized.go](2002_implementation_optimized.go) | Go 1.14 x64 | implementation | O(n L) | AC | 0.015 s | 936 KB | 11303790 |
