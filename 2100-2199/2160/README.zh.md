# 2160. 具有相同笛卡尔树的排列

[Timus 2160](https://acm.timus.ru/problem.aspx?space=1&num=2160) · 难度 1132 · combinatorics, trees

原题作者 Vadim Barinov，出自 2021 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两个排列等价，当它们都为空，或者它们的最小元素位于同一位置，且其左边部分和右边部分分别等价。求与给定排列等价的 1 … N 的排列个数，对 10⁹ + 7 取模。时间限制 2 秒，内存限制 256 MB。

## 输入

N（1 ≤ N ≤ 10⁵），然后是排列。

## 输出

等价排列的个数对 10⁹ + 7 取模。

## 样例

### 样例 1

输入：

```
3
2 1 3
```

输出：

```
2
```

### 样例 2

输入：

```
12
12 5 3 11 2 8 4 9 1 6 10 7
```

输出：

```
34650
```

## 解法

这个递归定义正是排列的笛卡尔树的形状：根是最小元素，左右子树由两边构造。所以问题是：用 1 … N 给一棵固定的二叉树标号，使每个节点都小于其子树中的所有节点，有多少种标号方式。

在这样的标号中，每棵大小为 s 的子树的根必须拿到其 s 个标号中最小的那个，概率为 1 / s，而且这些事件相互独立。因此答案是 N! 除以所有子树大小之积。笛卡尔树以及子树大小由常见的栈扫描得到：当更小的元素到来时，弹出的元素完成各自的子树，它们的大小累加到新元素的左孩子中。除法就是乘以模素数下的逆元。工作量 O(N)。

第一个样例中树的根为 1，有两个叶子，所以答案是 3! / (3 · 1 · 1) = 2。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2160_combinatorics_trees.cpp](2160_combinatorics_trees.cpp) | G++ 13.2 x64 | combinatorics, trees | O(N) | AC | 0.015 s | 1208 KB |
| [2160_combinatorics_trees.go](2160_combinatorics_trees.go) | Go 1.14 x64 | combinatorics, trees | O(N) | AC | 0.031 s | 5160 KB |
| [2160_combinatorics_trees.java](2160_combinatorics_trees.java) | Java 1.8 | combinatorics, trees | O(N) | AC | 0.109 s | 1196 KB |
| [2160_combinatorics_trees.py](2160_combinatorics_trees.py) | Python 3.12 x64 | combinatorics, trees | O(N) | AC | 0.125 s | 11584 KB |
| [2160_combinatorics_trees.rs](2160_combinatorics_trees.rs) | Rust 1.75 x64 | combinatorics, trees | O(N) | AC | 0.046 s | 3692 KB |
