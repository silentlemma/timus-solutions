# 1758. 再谈秃顶 2

[Timus 1758](https://acm.timus.ru/problem.aspx?space=1&num=1758) · 难度 2764 · backtracking

原题作者 Ekaterina Vasilyeva，出自 2010 年 3 月 13 日第十一届乌拉尔国立大学公开个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

酒馆编号为 1 到 n。从 1 号酒馆出发，只有当两个编号中一个整除另一个时才能从一家走到另一家，且不能重复访问。求访问酒馆尽可能多的路线。

## 输入

n（2 ≤ n ≤ 50）。

## 输出

最长路线中的酒馆数，然后按路线顺序输出这些酒馆。任何最长路线都可以。

## 样例

### 样例 1

输入：

```
9
```

输出：

```
7
1 9 3 6 2 4 8
```

## 解法

这是整除图中的最长简单路径，一般情况下是难题，但输入只有 49 种。解答里存着事先用穷举搜索求出的最长路线表，
输出长度增长处不超过 n 的最大 n' 对应的条目：n' 的路线对 n 仍然是路线，而在两个增长点之间最优长度不变。表中有 26 条，回答为 `O(1)`。

搜索从路线最后一家酒馆向所有可能方向延伸，当最好情况也无法超过记录时剪枝。
最好情况是：从最后一家经由空闲酒馆能到达的空闲酒馆数，减去其中至多一个空闲邻居的酒馆中除一个以外的全部——它们中只能访问一个，而且只能放在最后。
把记录初始化为已知长度后，完整搜索能证明不存在更长的路线；每个 n 最多需要半分钟，所以是事先完成的，而不是在一秒的限制内。

n = 9 时路线 1 9 3 6 2 4 8 漏掉了 5 和 7：它们都只与 1 号相连，而 1 号已被起点占用。

注意事项：

- 大于 n / 2 的素数 p 只与 1 相连，所以只能作为第二家，而路线也就在此结束；
- 路线必须从 1 号出发，但可以在任意处结束；
- 贪心路线在 n 很小时就已达不到最优长度。

对 2 到 50 的每个 n，长度都与一个独立的已通过实现一致，检查器验证路线本身。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1758_backtracking.cpp](1758_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.015 s | 376 KB |
| [1758_backtracking.go](1758_backtracking.go) | Go 1.14 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.031 s | 1128 KB |
| [1758_backtracking.java](1758_backtracking.java) | Java 1.8 | backtracking | O(1) with a table of 26 walks | AC | 0.140 s | 1752 KB |
| [1758_backtracking.py](1758_backtracking.py) | Python 3.12 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.078 s | 412 KB |
| [1758_backtracking.rs](1758_backtracking.rs) | Rust 1.75 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.062 s | 228 KB |
