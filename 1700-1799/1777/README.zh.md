# 1777. 阿宁迪利亚瓜人

[Timus 1777](https://acm.timus.ru/problem.aspx?space=1&num=1777) · 难度 128 · simulation

原题作者 Ivan Burmistrov，出自第十五届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

空地上有三堆大小不同的石头。每个人依次找出大小相差最小的两堆，并带来一堆恰好等于这个差的新石堆；所有石堆都留下。提问在找到两堆大小相等的那个人时结束。一共问了多少人？

## 输入

三个不同的大小 x₁、x₂、x₃（1 ≤ xᵢ ≤ 10¹⁸）。

## 输出

被问的人数。

## 样例

### 样例 1

输入：

```
11 5 9
```

输出：

```
3
```

## 解法

按原样模拟：把石堆排序，取相邻之差的最小值，若为 0 则停止，否则加入这么大的一堆。最小差的缩小方式与欧几里得算法中的数相似，所以过程很短：
找到的最长过程来自 10¹⁸ 附近三个相邻的斐波那契数，共问 85 人；在 10,000 个均匀随机生成的合法三元组样本中，平均问 3.7 人，中位数为 3。s 步时为 `O(s² log s)`。

样例中差为 2、4、6：第一个人带来一堆 2，第二个人又看到 9 和 11，再带来一堆 2，第三个人指出两堆 2。

注意事项：

- 找到相等两堆的那个人也要计入；
- 新堆可能与旧堆大小相同，这时下一个人就结束了；
- 大小可达 10¹⁸，需要 64 位整数。
- 随机样本的过程很短并不能确定最坏情况：测试 08 需要问 85 人。

在 90 个随机三元组上（包括斐波那契数的三元组），答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1777_simulation.cpp](1777_simulation.cpp) | G++ 13.2 x64 | simulation | O(s^2 log s) for s steps | AC | 0.015 s | 192 KB |
| [1777_simulation.go](1777_simulation.go) | Go 1.14 x64 | simulation | O(s^2 log s) for s steps | AC | 0.031 s | 1124 KB |
| [1777_simulation.java](1777_simulation.java) | Java 1.8 | simulation | O(s^2 log s) for s steps | AC | 0.125 s | 1712 KB |
| [1777_simulation.py](1777_simulation.py) | Python 3.12 x64 | simulation | O(s^2 log s) for s steps | AC | 0.093 s | 436 KB |
| [1777_simulation.rs](1777_simulation.rs) | Rust 1.75 x64 | simulation | O(s^2 log s) for s steps | AC | 0.062 s | 248 KB |
