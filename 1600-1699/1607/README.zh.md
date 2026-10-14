# 1607. 出租车

[Timus 1607](https://acm.timus.ru/problem.aspx?space=1&num=1607) · 难度 46 · implementation

原题作者 Denis Musin，出自 2008 年 3 月 1 日第九届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Petya 和出租车司机讨价还价。Petya 从 a 开始，每次加价 b；司机从 c 开始，每次降价 d；两人轮流开价，Petya 先说。
谁都不会报出越过对方的价格：司机宁可接受 Petya 的报价也不会要价更低，Petya 宁可接受司机的价格也不会出价更高。
Petya 要付多少钱？所有数都在 1 到 10000 之间。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

a、b、c 和 d。

## 输出

车费。

## 样例

### 样例 1

输入:

```
150 50 1000 100
```

输出:

```
450
```

## 解法

把讨价过程模拟一遍。若 a 已不低于 c，司机直接接受。否则 Petya 加价 b，若达到司机的价格，Petya 就接受司机的价格；
接着司机降价 d，若达到 Petya 的报价，司机就接受这个报价。每轮差距至少缩小 2，所以最多约 5000 轮：`O(c − a)`。
结果已在 800 个随机输入上与独立实现对照。

注意事项：

- 将要越过对方价格的一方按对方的价格让步，所以答案总是真正报出过的价格（测试 04 和 05）；
- Petya 可能一开始就高于司机的价格，此时不必还价，Petya 付 a（测试 02）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1607_implementation.cpp](1607_implementation.cpp) | G++ 13.2 x64 | implementation | O(c - a) | AC | 0.015 s | 132 KB |
| [1607_implementation.go](1607_implementation.go) | Go 1.14 x64 | implementation | O(c - a) | AC | 0.015 s | 1112 KB |
| [1607_implementation.java](1607_implementation.java) | Java 1.8 | implementation | O(c - a) | AC | 0.140 s | 1600 KB |
| [1607_implementation.py](1607_implementation.py) | Python 3.12 x64 | implementation | O(c - a) | AC | 0.093 s | 416 KB |
| [1607_implementation.rs](1607_implementation.rs) | Rust 1.75 x64 | implementation | O(c - a) | AC | 0.031 s | 224 KB |
