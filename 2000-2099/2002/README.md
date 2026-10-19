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

Use a hash map from name to a record containing its stored password and
online flag. For each request, perform a noninserting lookup. Apply the
first matching row of the table, append its response and change only the
fields specified by that successful operation.

For login, existence is checked first, then password equality, and only
then the online flag. A wrong password must therefore report the
password error even when the account is already online. Duplicate
registration never overwrites a password or resets the flag. Logout
changes only online to offline. Missing lookups never create accounts.

Inductively, after zero requests the map is the required empty registry.
Assuming it correctly represents all accounts after a prefix, the next
lookup finds precisely the specified account or its absence. The ordered
conditions choose the required response and perform exactly the
permitted update, preserving the invariant. This proves every output and
subsequent state.

Let `L≤30` bound token length. Expected time is `O(n L)` with hash maps,
and memory is `O(n L)` including input and responses. A conservative
collision worst case is `O(n² L)`, still small for at most 100 requests.
All five ports use the same transition order.

Do not check already-online before password validity. Do not log in
automatically on registration. A failed login, logout or duplicate
registration must not alter the database. Compare full strings
case-sensitively; quotes, backslashes and command-like names are
ordinary token characters. Emit one canonical line, without echoing the
name or password.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2002_implementation.cpp](2002_implementation.cpp) | G++ 13.2 x64 | implementation | O(n L) | AC | 0.015 s | 516 KB |
| [2002_implementation.go](2002_implementation.go) | Go 1.14 x64 | implementation | O(n L) | AC | 0.046 s | 1124 KB |
| [2002_implementation.java](2002_implementation.java) | Java 1.8 | implementation | O(n L) | AC | 0.109 s | 684 KB |
| [2002_implementation.py](2002_implementation.py) | Python 3.12 x64 | implementation | O(n L) | AC | 0.093 s | 576 KB |
| [2002_implementation.rs](2002_implementation.rs) | Rust 1.75 x64 | implementation | O(n L) | AC | 0.046 s | 460 KB |
