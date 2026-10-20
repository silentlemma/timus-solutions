# 2178. 统计包含一组连续整数的区间

[Timus 2178](https://acm.timus.ru/problem.aspx?space=1&num=2178) · 难度 1459 · two_pointers

原题作者 Vadim Barinov，出自 2023 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

统计 N 个数的数组中有多少个区间，其中的值互不相同，并且以某种顺序构成一组连续整数。时间限制 1 秒，内存限制 512 MB。

## 输入

N（1 ≤ N ≤ 10⁵），然后是 a₁ … aₙ（1 ≤ aᵢ ≤ 10⁵）。

## 输出

这种区间的个数。

## 样例

### 样例 1

输入：

```
5
4 2 3 1 2
```

输出：

```
11
```

## 解法

区间 [l, r] 符合条件当且仅当其值互不相同且 max − min = r − l。互不相同是一个窗口条件：根据各值的最后出现位置，两次线性扫描就能求出每个位置不出现重复值的最远区间端点，所以每个起点 l 有终点的界 R(l)，每个终点也有起点的界。

其余部分是在数组上常见的分治。完全在一半内的区间递归统计；对跨过中点的区间，从中点向两侧分别求前缀最小值和最大值。按最小值和最大值所在位置分四种情况：

- 两者都在左侧：终点被确定为 l + max − min，检查它即可；
- 两者都在右侧：对称地，起点被确定；
- 最大值在左、最小值在右：条件变为 min(右部) + r = max(左部) + l，因此前缀最大值仍小于左侧最大值、前缀最小值小于左侧最小值的右端点构成一个窗口，随着 l 向左移动而单调移动；对窗口中键 min + r 计数即可回答每个 l；
- 最小值在左、最大值在右：同理，键为 max − r。

这些窗口还要用 R(l) 截断。每层都是线性工作量，总计 O(N log N)，很短的范围直接扫描。

样例中有 11 个区间符合条件，其中包括 [4, 2, 3, 1] 和 [3, 1, 2]。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2178_two_pointers.cpp](2178_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N log N) | AC | 0.046 s | 2488 KB |
| [2178_two_pointers.go](2178_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N log N) | AC | 0.062 s | 9076 KB |
| [2178_two_pointers.java](2178_two_pointers.java) | Java 1.8 | two_pointers | O(N log N) | AC | 0.156 s | 3168 KB |
| [2178_two_pointers.py](2178_two_pointers.py) | PyPy 3.10 x64 | two_pointers | O(N log N) | AC | 0.656 s | 18628 KB |
| [2178_two_pointers.rs](2178_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N log N) | AC | 0.046 s | 4680 KB |
