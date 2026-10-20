# 2144. 把密封盒子排成一个有序队列

[Timus 2144](https://acm.timus.ru/problem.aspx?space=1&num=2144) · 难度 222 · sorting

原题作者 Ivan Smirnov，出自 2019 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 n 个盒子，每个盒子里是一排固定的手办尺寸，不能重新排列也不能倒过来。判断能否把盒子按某种顺序摆放，使所有尺寸合起来构成一个不降序列。时间限制 0.5 秒，内存限制 256 MB。

## 输入

n（1 ≤ n ≤ 100），然后对每个盒子给出 kᵢ（1 ≤ kᵢ ≤ 100）及其尺寸（1 ≤ aᵢⱼ ≤ 10⁴）。

## 输出

YES 或 NO。

## 样例

### 样例 1

输入：

```
3
2 1 2
3 7 7 7
1 5
```

输出：

```
YES
```

### 样例 2

输入：

```
2
2 1 3
1 2
```

输出：

```
NO
```

## 解法

每个盒子内部必须不降。此后只有它的第一个尺寸 f 和最后一个尺寸 l 有关系，合法顺序要求每个盒子的 l 不超过下一个盒子的 f。

在任何合法顺序中，第一个尺寸都不降，因为 f ≤ l ≤ 下一个盒子的 f。在第一个尺寸同为 f 的盒子中，除最后一个外都有 l ≤ f，即 l = f。因此只要存在合法顺序，按 (f, l) 排序就能得到一个，只需检查这个顺序中的相邻盒子。工作量 O(Σ kᵢ + n log n)。

第一个样例中盒子 (1, 2)、(5, 5) 和 (7, 7) 按此顺序正好衔接；第二个样例中 (1, 3) 和 (2, 2) 重叠。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2144_sorting.cpp](2144_sorting.cpp) | G++ 13.2 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 192 KB |
| [2144_sorting.go](2144_sorting.go) | Go 1.14 x64 | sorting | O(sum k + n log n) | AC | 0.031 s | 1328 KB |
| [2144_sorting.java](2144_sorting.java) | Java 1.8 | sorting | O(sum k + n log n) | AC | 0.187 s | 6900 KB |
| [2144_sorting.py](2144_sorting.py) | Python 3.12 x64 | sorting | O(sum k + n log n) | AC | 0.062 s | 1140 KB |
| [2144_sorting.rs](2144_sorting.rs) | Rust 1.75 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 336 KB |
