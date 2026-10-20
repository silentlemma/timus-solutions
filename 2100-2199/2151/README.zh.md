# 2151. 判断麻将手牌是和牌还是听牌

[Timus 2151](https://acm.timus.ru/problem.aspx?space=1&num=2151) · 难度 862 · bruteforce, greedy

原题作者 Ivan Sychev，出自 2020 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每张牌有花色 a、b 或 c 和数字 1 到 9。14 张牌的手牌若能分成四组三张和一对，就是和牌：三张组是三张相同的牌或同一花色的三个连续数字，对子是两张相同的牌。若恰好替换一张牌就能和牌，则为听牌。把手牌判定为 Tsumo、Tenpai 或 Noten。时间限制 1 秒，内存限制 256 MB。

## 输入

14 张形如 1a 或 9c 的牌，每种至多四张。

## 输出

Tsumo、Tenpai 或 Noten。

## 样例

### 样例 1

输入：

```
1a 2a 3a 6a 7a 8a 5b 5b 5b 9c 8c 7c 1c 1c
```

输出：

```
Tsumo
```

### 样例 2

输入：

```
1a 2a 3a 6a 7a 8a 5b 5b 5b 9c 8c 7c 1c 1b
```

输出：

```
Tenpai
```

## 解法

统计 27 种牌各有几张。判断是否和牌时，先注意三张组不会跨越花色，所以恰好有一种花色的张数 ≡ 2 (mod 3) 并包含对子，其他花色 ≡ 0。把该花色中至少有两张的每种牌依次当作对子尝试。剩下的牌必须能分成三张组，这由一次贪心扫描判定：从最小的数字往上，数量 c 中有 c mod 3 张不能进入相同的三张组，因为三个相同的顺子等价于三个刻子，所以恰好要有 c mod 3 个顺子从这里开始。

若手牌不是和牌，但去掉某种牌的一张、加入另一种牌的一张后能和牌，就是听牌；替换后可能出现某种牌的第五张。这至多是 27 · 26 次对 27 个元素的贪心检查。

第二个样例中在需要对子的地方手牌有 1c 和 1b，所以把其中一张换成另一张即可和牌。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2151_bruteforce_greedy.cpp](2151_bruteforce_greedy.cpp) | G++ 13.2 x64 | bruteforce, greedy | O(27^3) | AC | 0.015 s | 400 KB |
| [2151_bruteforce_greedy.go](2151_bruteforce_greedy.go) | Go 1.14 x64 | bruteforce, greedy | O(27^3) | AC | 0.031 s | 1100 KB |
| [2151_bruteforce_greedy.java](2151_bruteforce_greedy.java) | Java 1.8 | bruteforce, greedy | O(27^3) | AC | 0.109 s | 492 KB |
| [2151_bruteforce_greedy.py](2151_bruteforce_greedy.py) | Python 3.12 x64 | bruteforce, greedy | O(27^3) | AC | 0.078 s | 652 KB |
| [2151_bruteforce_greedy.rs](2151_bruteforce_greedy.rs) | Rust 1.75 x64 | bruteforce, greedy | O(27^3) | AC | 0.015 s | 216 KB |
