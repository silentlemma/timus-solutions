# 2066. 三个数能组成的最小值

[Timus 2066](https://acm.timus.ru/problem.aspx?space=1&num=2066) · 难度 28 · bruteforce

原题作者 Kirill Borozdin，出自 2015 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

三个非负整数可以按任意顺序排列，相邻两数之间放一个 +、− 或 × 号；乘法优先，不能用括号和单目负号。求这样的表达式可能的最小值。时间限制 1 秒，内存限制 64 MB。

## 输入

数 a ≤ b ≤ c，0 ≤ a，每行一个，c ≤ 100。

## 输出

最小值。

## 评测方式

按记号逐个比较输出。

## 样例

### 样例 1

输入：

```
1
2
3
```

输出：

```
-5
```

## 解法

顺序只有 6 种，符号组合只有 9 种，所以程序尝试全部 54 个表达式。按通常的优先级计算 x op₁ y op₂ z：若只有第二个符号是 ×，先算 y × z；否则从左到右计算。

搜索的结果总是同一种形式：最小的数减去 b + c 与 b × c 中较大的那个，即 a − max(b + c, b × c)。从最小的数中减去尽可能多的量显然最好，而只有当 b 或 c 为 0 或 1 时 b + c 才大于 b × c。检查全部 176 851 个输入验证了这个公式，但直接搜索不需要任何证明。

样例中 1 − 2 × 3 = −5。

## 各语言说明

没有特别需要注意的地方。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2066_bruteforce.cpp](2066_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 184 KB |
| [2066_bruteforce.go](2066_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1080 KB |
| [2066_bruteforce.java](2066_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.140 s | 1632 KB |
| [2066_bruteforce.py](2066_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 532 KB |
| [2066_bruteforce.rs](2066_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.062 s | 224 KB |
