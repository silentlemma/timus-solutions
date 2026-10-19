# 2082. 恢复机器人上一回合以来的下注

[Timus 2082](https://acm.timus.ru/problem.aspx?space=1&num=2082) · 难度 6131 · simulation

原题作者 Igor Chevdar。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一手德州扑克由 2 到 9 名玩家进行，有前注、小盲和大盲（两人时由庄家下小盲）。下注按街（翻牌前、翻牌、转牌、河牌）逐轮绕桌进行；动作有弃牌、过牌、跟注、下注和加注，筹码不足的玩家可以全下。机器人知道这手牌的开始、直到它上一回合为止的所有动作，以及现在所有玩家的当前筹码，但不知道下注。恢复从机器人上一回合到当前回合的所有动作，包括换街。保证答案唯一。时间限制 2 秒，内存限制 256 MB。

## 输入

盲注和前注，玩家数、庄家和机器人，当前街，名字和初始筹码，按输出格式给出的已知动作，以及当前筹码。

## 输出

恢复的动作数，然后是各动作：`dealing <street>`、`<name> folds`、`checks`、`calls <amount>`、`bets <amount>` 或 `raises <amount> to <total>`。

## 样例

### 样例 1

输入：

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

输出：

```
3
PhilIvey folds
TomDwan calls 20
ViktorBlom raises 40 to 60
```

### 样例 2

输入：

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

输出：

```
4
Grobot calls 50
Ziigmund folds
TomDwan folds
dealing flop
```

### 样例 3

输入：

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

输出：

```
2
Grobot checks
ViktorBlom bets 100
```

### 样例 4

输入：

```
50 100 10
2 2 1
preflop
Grobot 2500
ViktorBlom 2000
0
2390 1890
```

输出：

```
1
ViktorBlom calls 50
```

## 解法

重放一个小的牌桌模型。它保存每个人的筹码、每个玩家在当前街的下注、当前注额、谁已弃牌以及谁还需行动；高于当前注额的下注或加注会让所有仍在局中且有筹码的人重新行动。先收前注和盲注（付不起的就付全部），翻牌前从大盲之后开始，其余各街从庄家之后开始，没人需要行动时一街结束，模型发下一街。

已知动作之后模型自行继续。每一步，行动玩家迄今损失的筹码——模型筹码与报告筹码之差——说明他付了多少。没付钱时，若他的下注已等于当前注额则是过牌，否则是弃牌；在空街上付钱是下注；付到超过当前注额是加注到新总额；其余是跟注，筹码用完时为全下跟注。唯一的细节是在机器人回合之前就结束的街：在那里没人能在机器人之后加注，所以玩家在那条街最多付跟注额，其余损失属于下一街。当轮到机器人在当前街行动且所有筹码都吻合时重放停止。整体与动作数成线性。

第一个样例中机器人下小盲，所以 PhilIvey、TomDwan 和 ViktorBlom 在它之前行动；除去前注 2，筹码显示 PhilIvey 没付钱（弃牌），TomDwan 跟注 20，ViktorBlom 加注 40 到 60。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2082_simulation.cpp](2082_simulation.cpp) | G++ 13.2 x64 | simulation | O(k) | AC | 0.015 s | 492 KB |
| [2082_simulation.go](2082_simulation.go) | Go 1.14 x64 | simulation | O(k) | AC | 0.031 s | 1232 KB |
| [2082_simulation.java](2082_simulation.java) | Java 1.8 | simulation | O(k) | AC | 0.125 s | 976 KB |
| [2082_simulation.py](2082_simulation.py) | Python 3.12 x64 | simulation | O(k) | AC | 0.093 s | 1172 KB |
| [2082_simulation.rs](2082_simulation.rs) | Rust 1.75 x64 | simulation | O(k) | AC | 0.015 s | 248 KB |
