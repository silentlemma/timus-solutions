# 1614. 国家项目“有轨电车”

[Timus 1614](https://acm.timus.ru/problem.aspx?space=1&num=1614) · 难度 846 · constructive

原题作者 Alexander Ipatov（创意来自 Magaz Asanov），出自 2008 年 3 月 29 日第十二届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

城市里有 2n 个电车站（1 ≤ n ≤ 100）。要铺设恰好 n 条线路，每条是恰好
2n 个车站组成的序列（车站可以重复），使任意两个车站都在某条线路上相邻：
乘客可以从一个站直达另一个站而不在中间停靠。输出这些线路；若做不到则输出
`-1`。任何正确的方案都被接受。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

n。

## 输出

n 行，每行是一条线路的 2n 个车站。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
1 6 2 1 3 4
2 3 6 5 4 6
5 1 4 2 5 3
```

## 解法

车站对共有 n(2n − 1) 个，而 n 条各含 2n 个站的线路恰有 n(2n − 1) 个相邻
位置，所以每一对必须恰好出现一次。我们把 2n 个顶点的完全图分成 n 条经过
所有顶点的路径。这总是可以做到的。

把车站沿圆周编号为 0 … 2n − 1。线路 k 依次为 k、k + 1、k − 1、k + 2、
k − 2、…、k + n（模 2n）：它恰好经过每个车站一次，相邻的车站对交替具有模 2n
的和 2k + 1 与 2k，即所有对 {k − j, k + 1 + j} 和所有对 {k + j, k − j}。
任意两个不同车站的和模 2n 为某个 s，这一对属于线路 ⌊s / 2⌋，因此 n 条线路覆盖了
所有车站对。`O(n²)`。

易错点：

- n = 1 时只有一条连接两个车站的线路（测试 02）；
- 样例中的线路与此不同但同样正确，因此由检查器验证每一对都被覆盖。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1614_constructive.cpp](1614_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 128 KB |
| [1614_constructive.go](1614_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1260 KB |
| [1614_constructive.java](1614_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.156 s | 2012 KB |
| [1614_constructive.py](1614_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.109 s | 452 KB |
| [1614_constructive.rs](1614_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.046 s | 428 KB |
