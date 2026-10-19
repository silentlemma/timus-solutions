# 1846. GCD 2010

[Timus 1846](https://acm.timus.ru/problem.aspx?space=1&num=1846) · 难度 155 · segment_tree

原题作者 Alexey Samsonov，出自 2010 年 8 月彼得罗扎沃茨克夏季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个正整数多重集开始时为空。每次操作加入一个数，或删除集合中某个数的一个副本。每次操作后输出整个多重集的最大公约数；空多重集的最大公约数规定为 1。

## 输入

q（1 ≤ q ≤ 10⁵），然后是 q 行 "+ x" 或 "- x"，其中 1 ≤ x ≤ 10⁹。只会删除存在的数。

## 输出

每次操作后的最大公约数，每行一个。

## 样例

### 样例 1

输入：

```
5
+ 8
+ 6
+ 8
- 8
- 8
```

输出：

```
8
2
2
2
6
```

## 解法

最大公约数无法"撤销"，所以删除需要借助数据结构。在按操作编号建立的线段树中，给每次加入分配一个自己的叶子，并为每个值保存一个存放它的叶子的栈。
加入 x 时把 x 写进这次操作的叶子；删除 x 时清空它的栈顶叶子，写入 0，由于 gcd(a, 0) = a，这不会改变任何最大公约数。
每个内部节点保存其子节点的最大公约数，所以根就是多重集的最大公约数，根为 0 表示多重集为空，此时输出 1。
更新一个叶子要重新计算它的祖先；一旦某个节点的值没有变化就可以停止向上，因为更上面的值也不会变。`O(q log q log x)`。

在样例中，叶子保存 8、6、8，所以最大公约数为 2。删除两个 8 会清空两个叶子，只剩下 6。

注意事项：

- 空多重集输出 1 而不是 0；
- 相等的数可能被加入多次并一次删除一个；
- 时限只有半秒，提前停止向上和快速读入都很重要；Python 版本在 PyPy 上运行。

在三十个最多 10⁵ 次操作的随机文件上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1846_segment_tree.cpp](1846_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(q log q log x) | AC | 0.171 s | 8616 KB |
| [1846_segment_tree.go](1846_segment_tree.go) | Go 1.14 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 14000 KB |
| [1846_segment_tree.java](1846_segment_tree.java) | Java 1.8 | segment_tree | O(q log q log x) | AC | 0.140 s | 10080 KB |
| [1846_segment_tree.py](1846_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(q log q log x) | AC | 0.250 s | 37060 KB |
| [1846_segment_tree.rs](1846_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(q log q log x) | AC | 0.046 s | 12328 KB |
