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

`2002_implementation_optimized.rs`. Keep the same account HashMap and login-state machine, including error precedence. Read and process each command immediately; store byte names/passwords only for registered accounts and emit the fixed reply directly. Do not retain the command history or reply strings. Expected O(I+O) time for input/output bytes and O(A+T) storage for account data A and the largest current command T, with standard randomized hashing.

Compared with `2002_implementation.rs`: time 0.046 s → 0.015 s; memory 460 KB → 280 KB.

`2002_implementation_optimized.java`. Keep the same account map and error precedence, including checking the password before the already-online condition. Process one request and emit its reply immediately instead of retaining all commands, replies and the joined answer. Java stores one Account per registered name and uses fixed I/O buffers; Python uses byte keys/passwords without ASCII decoding and removes accumulated command/reply lists. Space is O(U) account records plus the current bounded-length request, where U<=n. With names/passwords at most 30 characters, expected hash-table processing is O(n), not a worst-case hashing guarantee. Failed commands leave state unchanged. Python flushes before os._exit(0); registration remains offline.

Compared with `2002_implementation.java`: time 0.140 s → 0.109 s; memory 664 KB → 640 KB.

`2002_implementation_optimized.py`. Keep the same account map and error precedence, including checking the password before the already-online condition. Process one request and emit its reply immediately instead of retaining all commands, replies and the joined answer. Java stores one Account per registered name and uses fixed I/O buffers; Python uses byte keys/passwords without ASCII decoding and removes accumulated command/reply lists. Space is O(U) account records plus the current bounded-length request, where U<=n. With names/passwords at most 30 characters, expected hash-table processing is O(n), not a worst-case hashing guarantee. Failed commands leave state unchanged. Python flushes before os._exit(0); registration remains offline.

Compared with `2002_implementation.py`: time 0.093 s → 0.109 s; memory 576 KB → 252 KB.

The optimized C++ solution reads the words with `scanf` into buffers of
31 bytes instead of `iostream` and answers every request at once instead
of storing all requests and replies first: 212 KB instead of 516 KB,
with the same time.

The optimized Go solution parses the requests by hand from a 1 KB
buffered reader instead of `fmt.Fscan` and answers each one at once
through a buffered writer, with no list of commands: 0.015 s instead of
0.046 s and 936 KB instead of 1124 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2002_implementation_optimized.java`: time place 26/249, memory place 29/249 in this comparable sample.

`2002_implementation_optimized.py`: time place 47/69, memory place 2/69 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [2002_implementation_optimized.java](2002_implementation_optimized.java) \* | Java 1.8 | implementation | O(n) expected | AC | 0.109 s | 640 KB | 11325028 |
| [2002_implementation_optimized.py](2002_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) expected | AC | 0.109 s | 252 KB | 11324845 |
| [2002_implementation_optimized.rs](2002_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | Expected O(I+O) time; O(A+T) space | AC | 0.015 s | 280 KB | 11325537 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
