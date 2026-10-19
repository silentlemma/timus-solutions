# 2112. 检查射击比赛日志并推测队伍

[Timus 2112](https://acm.timus.ru/problem.aspx?space=1&num=2112) · 难度 818 · dsu, greedy, simulation

原题作者 Ivan Sychev，出自 2019 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 名玩家组成隐藏的四人队伍进行比赛。每名玩家的状态为 3（健康）、2（受伤）、1（濒死）或 0（死亡），初始为 3。日志中有三类事件：击中身体或头部使目标状态降低 1 或 2（不低于 0），医疗包使使用者恢复到 3，复活使队友从 1 变为 2。只有状态为 3 或 2 的玩家可以行动，并且只能复活濒死的队友。如果没有任何四人分组能使日志合法，输出 "FAKE"，否则输出 "CORRECT" 和任意一种合法分组。时间限制 1 秒，内存限制 256 MB。

## 输入

n（4 ≤ n ≤ 1000，能被 4 整除），n 个互不相同的名字，然后是 m（0 ≤ m ≤ 10⁴）以及事件 "X HIT Y IN BODY"、"X HIT Y IN HEAD"、"X USES MEDKIT" 和 "X REVIVE Y"。

## 输出

"FAKE"，或者 "CORRECT" 以及 n / 4 行、每行四个名字。

## 评测方式

检查器接受任何合法分组。

## 样例

### 样例 1

输入：

```
8
Shroud
Forsen
Wycc
Ragyra
BeastQT
Lirik
Asmadey
Ninja
12
Wycc HIT Shroud IN BODY
Shroud HIT Wycc IN HEAD
Ragyra REVIVE Wycc
Wycc USES MEDKIT
Lirik HIT BeastQT IN BODY
Asmadey HIT BeastQT IN BODY
Asmadey REVIVE BeastQT
Ragyra HIT Forsen IN HEAD
Shroud REVIVE Forsen
BeastQT HIT Shroud IN HEAD
Wycc HIT Forsen IN HEAD
Ninja HIT BeastQT IN HEAD
```

输出：

```
CORRECT
Wycc Ragyra BeastQT Asmadey
Lirik Ninja Shroud Forsen
```

### 样例 2

输入：

```
8
Shroud
Forsen
Wycc
Ragyra
BeastQT
Lirik
Asmadey
Ninja
8
Shroud HIT Wycc IN HEAD
Shroud HIT Ragyra IN HEAD
Shroud HIT BeastQT IN HEAD
Shroud HIT Asmadey IN HEAD
Lirik REVIVE Wycc
Lirik REVIVE Ragyra
Lirik REVIVE BeastQT
Lirik REVIVE Asmadey
```

输出：

```
FAKE
```

### 样例 3

输入：

```
4
Shroud
Forsen
Wycc
Ragyra
3
Shroud HIT Wycc IN HEAD
Wycc HIT Shroud IN HEAD
Wycc HIT Shroud IN BODY
```

输出：

```
FAKE
```

## 解法

状态与分组无关，所以直接模拟日志。行动者处于状态 1 或 0 的事件是伪造的，复活一个不处于状态 1 的目标也是伪造的。击中任何人都允许，甚至击中自己。

与分组唯一的联系是：复活意味着两名玩家在同一队。用并查集合并他们。每个得到的组必须能放进一支队伍，所以超过四人的组说明是伪造的。然后把组装进四人队：

- 四人组本身就是一队；
- 每个三人组需要一名单人，如果单人比三人组少，日志就是伪造的；
- 两人组两两配对；
- 剩下的一个两人组再取两名单人，由于 n 能被四整除，这样的单人一定存在；
- 其余单人每四人组成一队。

借助名字的哈希，模拟和装队共需 O(n + m)。

第三个样例中 Wycc 被爆头后处于濒死状态却还在开枪，所以日志是伪造的。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2112_dsu_greedy_simulation.cpp](2112_dsu_greedy_simulation.cpp) | G++ 13.2 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.031 s | 644 KB |
| [2112_dsu_greedy_simulation.go](2112_dsu_greedy_simulation.go) | Go 1.14 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.046 s | 2824 KB |
| [2112_dsu_greedy_simulation.java](2112_dsu_greedy_simulation.java) | Java 1.8 | dsu, greedy, simulation | O(n + m) | AC | 0.156 s | 4712 KB |
| [2112_dsu_greedy_simulation.py](2112_dsu_greedy_simulation.py) | Python 3.12 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.109 s | 1140 KB |
| [2112_dsu_greedy_simulation.rs](2112_dsu_greedy_simulation.rs) | Rust 1.75 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.046 s | 1280 KB |
