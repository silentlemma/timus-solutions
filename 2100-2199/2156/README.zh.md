# 2156. 把圆周上的差值分成相等的两半

[Timus 2156](https://acm.timus.ru/problem.aspx?space=1&num=2156) · 难度 656 · math, constructive

原题作者 Semyon Trifochkin，出自 2020 年乌拉尔团队程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 位有趣度为 a₁ … aₙ 的朋友围坐在圆桌旁，邻座 i 与 i + 1（最后一对为 n 与 1）之间谈话的有趣度为 |aᵢ − aᵢ₊₁|。把 n 段谈话分成两个非空集合，使总有趣度相等，或者输出 NO。任何合法划分都可接受。时间限制 1 秒，内存限制 256 MB。

## 输入

n（3 ≤ n ≤ 10⁵），然后是 a₁ … aₙ（1 ≤ aᵢ ≤ 10⁹）。

## 输出

YES，然后依次是第一个集合和第二个集合的大小及编号，或者 NO。

## 评测方式

检查器验证两个集合非空、划分了所有谈话且和相等。

## 样例

### 样例 1

输入：

```
3
1 2 3
```

输出：

```
YES
2
1 2
1
3
```

## 解法

答案总是 YES。沿圆桌绕一圈，有符号差值 aᵢ − aᵢ₊₁ 之和为 0。所以数值下降（aᵢ > aᵢ₊₁）的谈话与数值上升的谈话总有趣度相同，而相等邻座之间的谈话有趣度为 0，可以放到任一边。

若数值不全相等，则至少有一次下降和一次上升，两个集合都非空。若全部相等，每段谈话的有趣度都是 0，一段对其余 n − 1 段即可。工作量 O(n)。

样例中数值只在从 3 回到 1 时下降，所以谈话 3（有趣度 2）与谈话 1 和 2（各为 1）平衡。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2156_math_constructive.cpp](2156_math_constructive.cpp) | G++ 13.2 x64 | math, constructive | O(n) | AC | 0.093 s | 2668 KB |
| [2156_math_constructive.go](2156_math_constructive.go) | Go 1.14 x64 | math, constructive | O(n) | AC | 0.125 s | 9912 KB |
| [2156_math_constructive.java](2156_math_constructive.java) | Java 1.8 | math, constructive | O(n) | AC | 0.140 s | 9008 KB |
| [2156_math_constructive.py](2156_math_constructive.py) | Python 3.12 x64 | math, constructive | O(n) | AC | 0.140 s | 21040 KB |
| [2156_math_constructive.rs](2156_math_constructive.rs) | Rust 1.75 x64 | math, constructive | O(n) | AC | 0.046 s | 9448 KB |
