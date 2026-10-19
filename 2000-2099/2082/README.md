# 2082. Restore the betting since the bot's last turn

[Timus 2082](https://acm.timus.ru/problem.aspx?space=1&num=2082) · difficulty 6136 · simulation

Original problem by Igor Chevdar.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A Texas hold'em hand is played by 2 to 9 players with an ante, a small
and a big blind (with two players the dealer posts the small blind).
Bets go round the table street by street (preflop, flop, turn, river);
the actions are fold, check, call, bet and raise, and a player short of
chips may go all in. A bot knows the start of the hand, every action up
to its previous turn, and now the current stacks of all players, but not
the bets. Restore every action since the bot's previous turn, or the
hand's start on its first turn, including street changes. The answer is
guaranteed to be unique. The limits are 2 seconds and 256 MB.

## Input

The blinds and the ante, the number of players, the dealer and the bot,
the current street, the names and initial stacks, the known actions in
the format of the output, and the current stacks.

## Output

The number of restored actions, then the actions: `dealing <street>`,
`<name> folds`, `checks`, `calls <amount>`, `bets <amount>` or
`raises <amount> to <total>`.

## Examples

### Example 1

Input:

```
10 20 2
5 3 4
preflop
PhilIvey 500
TomDwan 500
ViktorBlom 500
Grobot 500
Ziigmund 500
0
498 478 438 488 478
```

Output:

```
3
PhilIvey folds
TomDwan calls 20
ViktorBlom raises 40 to 60
```

### Example 2

Input:

```
10 20 2
5 3 4
flop
PhilIvey 500
TomDwan 500
ViktorBlom 500
Grobot 500
Ziigmund 500
3
PhilIvey folds
TomDwan calls 20
ViktorBlom raises 40 to 60
498 478 438 438 478
```

Output:

```
4
Grobot calls 50
Ziigmund folds
TomDwan folds
dealing flop
```

### Example 3

Input:

```
10 20 2
5 3 4
flop
PhilIvey 500
TomDwan 500
ViktorBlom 500
Grobot 500
Ziigmund 500
7
PhilIvey folds
TomDwan calls 20
ViktorBlom raises 40 to 60
Grobot calls 50
Ziigmund folds
TomDwan folds
dealing flop
498 478 338 438 478
```

Output:

```
2
Grobot checks
ViktorBlom bets 100
```

### Example 4

Input:

```
50 100 10
2 2 1
preflop
Grobot 2500
ViktorBlom 2000
0
2390 1890
```

Output:

```
1
ViktorBlom calls 50
```

## Solution

A small table model is replayed. It keeps every stack, the bet of each
player on the current street, the current bet, who has folded, and who
still has to act; a bet or raise above the current bet makes every other
player who is in the hand and has chips act again. The ante and the blinds are
posted first (a player who cannot cover them pays all their chips), the
preflop starts after the big blind and the other streets after the
dealer, and a street ends when nobody has to act; then the model deals
the next street.

After the known actions the model continues on its own. At each turn the
acting player's chip loss so far, the difference between the model's
stack and the reported one, tells what was paid. Nothing paid means a
check when the player's bet already matches, and a fold otherwise; a
payment on an empty street is a bet; a new total above the current bet is
a raise to that total; otherwise it is a call, an all-in one if the
stack runs out. The only subtle point is a street that ends before the
bot's turn: on it nobody can raise after the bot, so a player pays at
most the amount to call there, and the rest of the chip loss belongs to
the next street. The replay stops when the bot is to act on the current
street with all stacks matching. This takes O(k + m) time for k known
and m restored actions.

In the first example the bot posts the small blind, so PhilIvey, TomDwan
and ViktorBlom act before it; besides the ante of 2 the stacks show that
PhilIvey paid nothing (a fold), TomDwan called 20 and ViktorBlom raised
by 40 to 60.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2082_simulation.cpp](2082_simulation.cpp) | G++ 13.2 x64 | simulation | O(k + m) | AC | 0.015 s | 492 KB |
| [2082_simulation.go](2082_simulation.go) | Go 1.14 x64 | simulation | O(k + m) | AC | 0.031 s | 1232 KB |
| [2082_simulation.java](2082_simulation.java) | Java 1.8 | simulation | O(k + m) | AC | 0.125 s | 976 KB |
| [2082_simulation.py](2082_simulation.py) | Python 3.12 x64 | simulation | O(k + m) | AC | 0.093 s | 1172 KB |
| [2082_simulation.rs](2082_simulation.rs) | Rust 1.75 x64 | simulation | O(k + m) | AC | 0.015 s | 248 KB |
