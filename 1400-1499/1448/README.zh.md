# 1448. 霍格沃茨的照明

[Timus 1448](https://acm.timus.ru/problem.aspx?space=1&num=1448) · 难度 581 · constructive

原题由 Alexander Mironenko（构思）和 Stanislav Vasiliev（题面与程序）完成，出自 2006 年 3 月 24–25 日第十届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

走廊里有一排 N 盏灯（1 ≤ N ≤ 10⁶），每盏要么全亮要么全灭。阿格斯·费尔奇想要
b%（0 ≤ b ≤ 100）的亮度并尽量均匀：输出 N 个由 0 和 1 组成的数字，使任意连续
L 盏灯中亮着的数量与 L b / 100 相差不超过 2。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

N，然后是 b。

## 输出

灯的排列。任何满足条件的排列都被接受。

## 样例

### 样例 1

输入:

```
10
33
```

输出:

```
0100100100
```

## 解法

第 i 盏灯（从 0 开始计）亮，当且仅当 ⌊(i + 1) b / 100⌋ 大于 ⌊i b / 100⌋。这样
前 k 盏中亮着 ⌊k b / 100⌋ 盏，从 l 到 r 的一段有 ⌊r b / 100⌋ − ⌊l b / 100⌋ 盏，
与 (r − l) b / 100 相差不到 1，远在允许的 2 之内。图案每 100 盏重复一次，因为 i
加 100 会让两个下取整都恰好加 b。`O(N)`。

注意事项：

- b = 0 和 b = 100 时整排只有一种数字（测试 02、03、05、gen1、gen2）；
- 一百万个数字要一次性输出，不能每个数字调用一次输出（gen1 到 gen7）；
- 样例中的排列只是众多正确答案之一。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1448_constructive.cpp](1448_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1164 KB |
| [1448_constructive.go](1448_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 2088 KB |
| [1448_constructive.java](1448_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 3036 KB |
| [1448_constructive.py](1448_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 2244 KB |
| [1448_constructive.rs](1448_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 2056 KB |
