# 2208. 带修改时在区间中找两个有公因数的数

[Timus 2208](https://acm.timus.ru/problem.aspx?space=1&num=2208) · 难度 935 · number_theory, segment_tree

原题作者 Konstantin Rychkov，出自 2023 年大学学术中学生信息学奥林匹克。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个由 N 个 2 到 10⁶ 之间的数组成的数组接受 Q 次操作：修改一个元素，或者在区间 [l, r] 中给出两个位置，使其上的数不互质，若没有则输出 −1。任何正确的位置对都可接受。时间限制 2 秒，内存限制 256 MB。

## 输入

N 和 Q（2 ≤ N ≤ 10⁵，1 ≤ Q ≤ 10⁵），然后是数组，然后是操作「1 l r」和「2 p x」。

## 输出

对每个区间查询输出一对位置或 −1。

## 样例

### 样例 1

输入：

```
5 4
2 3 4 5 6
1 1 5
1 2 4
2 3 6
1 2 4
```

输出：

```
1 3
-1
2 3
```

## 解法

两个数不互质当且仅当它们有公共质因数，而不超过 10⁶ 的数至多有 7 个不同的质因数。对每个位置 i，设 prev(i) 为与位置 i 上的数共享某个质因数的最大的 j < i，即它的各个质因数在之前最后一次出现的位置。

区间 [l, r] 中存在合法的一对，当且仅当其中某个 i 满足 prev(i) ≥ l，此时 (prev(i), i) 就是这样一对。在 prev 值上建线段树，查询时下降到区间中第一个 prev 达到 l 的 i ≥ l。

在 p 处修改，只会改变 p 本身的 prev，以及对 p 失去或获得的每个质因数，该质因数在 p 之后下一次出现的位置的 prev。每个质数用有序结构保存它的出现位置（C++ 中用平衡集合，Go、Java 和 Rust 中用预先收集的、该质数可能出现的所有位置上的树状数组），然后重新计算至多 15 个受影响的位置。

Python 版本在小质数上节省时间：不超过 100 的 25 个质数变成一个能放进机器字的位掩码，树节点还记录其中是否已有两个元素共享小质数。由于 101 · 103 · 107 > 10⁶，一个数至多有两个大于 100 的质因数，只有它们使用 prev 树。这些质因数的所有出现位置（包括修改将产生的）预先通过一次排序编号，当前存在的位置保存在带有多层 30 位字摘要的位集中，用几次字运算即可找到前一个出现位置。查询时从左往右遍历区间对应的树节点，携带已经过部分的掩码按位或，并进入第一个含有这样一对的节点向下查找。

样例中 2 和 4 有公因数 2，区间 3, 4, 5 中没有这样的对，修改后 3 和 6 有公因数 3。

在筛出到 10⁶ 的最小质因数之后，每次操作的时间复杂度为 O(log(N + Q))。

## 各语言说明

- Python 在 PyPy 下运行：在 CPython 3.12 下它在第 34 个测试点超时（2.046 秒），而在 PyPy 3.10 下以 1.64 秒通过。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2208_number_theory_segment_tree.cpp](2208_number_theory_segment_tree.cpp) | G++ 13.2 x64 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 0.937 s | 76668 KB |
| [2208_number_theory_segment_tree.go](2208_number_theory_segment_tree.go) | Go 1.14 x64 | number_theory, segment_tree | O((N + Q) 7 log(N + Q)) | AC | 0.578 s | 121460 KB |
| [2208_number_theory_segment_tree.java](2208_number_theory_segment_tree.java) | Java 1.8 | number_theory, segment_tree | O((N + Q) 7 log(N + Q)) | AC | 0.906 s | 61776 KB |
| [2208_number_theory_segment_tree.py](2208_number_theory_segment_tree.py) | PyPy 3.10 x64 | number_theory, segment_tree | O((N + Q) 7 log(N + Q)) | AC | 1.640 s | 48276 KB |
| [2208_number_theory_segment_tree.rs](2208_number_theory_segment_tree.rs) | Rust 1.75 x64 | number_theory, segment_tree | O((N + Q) 7 log(N + Q)) | AC | 0.375 s | 61924 KB |
