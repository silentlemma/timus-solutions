# 2104. 把双面纸条对折到只剩一种颜色

[Timus 2104](https://acm.timus.ru/problem.aspx?space=1&num=2104) · 难度 375 · games

原题作者 Nikita Sivukhin，出自 2016 年乌拉尔联邦大学青少年锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

1 × n 的纸条每格两面都涂有颜色 A 或 B。Alice 和 Bob 轮流操作，Alice 先手；每次把纸条对折（仅当长度为偶数时），向内或向外折。若某次操作后纸条两面都只剩一种颜色，A 表示 Alice 获胜，B 表示 Bob 获胜，与谁折的无关。若轮到的人不能折且无人获胜，则平局。双方都最优时谁获胜？时间限制 2 秒，内存限制 64 MB。

## 输入

n ≤ 5·10⁵，然后是由 A 和 B 组成的两面字符串。

## 输出

`Alice`、`Bob` 或 `Draw`。

## 样例

### 样例 1

输入：

```
4
BBAA
BABB
```

输出：

```
Bob
```

### 样例 2

输入：

```
3
AAA
BBB
```

输出：

```
Draw
```

### 样例 3

输入：

```
2
AA
BB
```

输出：

```
Alice
```

## 解法

对折把右半放到左半的上面或下面。一种折法外侧为上面一侧的左半和上面一侧右半的反转；另一种外侧为下面一侧右半的反转和下面一侧的左半。折到里面的面再也看不到。所以每个局面至多两种走法，每次长度减半，游戏至多 log₂ n ≈ 19 层。

在这棵树上做普通的极小极大即可：每次对折后检查新纸条是否只剩一种颜色；否则换另一方递归，长度为奇数则平局。Alice 取对自己最好的结果，Bob 取对自己最好的结果，一旦某个走法获胜就停止。第 k 层至多 2ᵏ 张长为 n / 2ᵏ 的纸条，所以工作量 O(n log n)。

第一个样例中 Alice 的两种折法留下的纸条 Bob 都能折成 B/B，所以 Bob 获胜。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2104_games.cpp](2104_games.cpp) | G++ 13.2 x64 | games | O(n log n) | AC | 0.031 s | 3832 KB |
| [2104_games.go](2104_games.go) | Go 1.14 x64 | games | O(n log n) | AC | 0.046 s | 8076 KB |
| [2104_games.java](2104_games.java) | Java 1.8 | games | O(n log n) | AC | 0.125 s | 14932 KB |
| [2104_games.py](2104_games.py) | Python 3.12 x64 | games | O(n log n) | AC | 0.265 s | 3968 KB |
| [2104_games.rs](2104_games.rs) | Rust 1.75 x64 | games | O(n log n) | AC | 0.015 s | 2132 KB |
