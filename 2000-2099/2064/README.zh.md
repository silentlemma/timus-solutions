# 2064. 许多锯齿中的最高点

[Timus 2064](https://acm.timus.ru/problem.aspx?space=1&num=2064) · 难度 976 · math, prefix_sums

原题作者 Nikita Sivukhin（由 Alexey Danilyuk 和 Nikita Sivukhin 整理），出自 2015 年乌拉尔地区团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 只毛毛虫在时刻 0 从地面出发。第 i 只以每分钟 1 厘米的速度向上爬 tᵢ 分钟，然后以同样的速度下滑 tᵢ 分钟回到地面，如此无限重复。对 q 个时刻中的每一个，求最高的毛毛虫所在的高度。时间限制 3 秒，内存限制 64 MB。

## 输入

毛毛虫数 n（1 ≤ n ≤ 10⁶），然后是 n 个 tᵢ（1 ≤ tᵢ ≤ 10⁹），再是时刻数 q（1 ≤ q ≤ 10⁶），以及 q 个时刻 x，每行一个，1 ≤ x ≤ 10⁶。

## 输出

对每个时刻，单独一行输出最大高度。

## 评测方式

按记号逐个比较输出。

## 样例

### 样例 1

输入：

```
4
1 3 2 1
12
1
2
3
4
5
6
7
8
9
10
11
12
```

输出：

```
1
2
3
2
1
2
1
2
3
2
1
0
```

## 解法

在时刻 x，参数为 t 的毛毛虫位于高度 t − |x − c|，其中 c 是离 x 最近的 t 的奇数倍：它的图像是一排高度为 t 的“帐篷”，顶点在 t, 3t, 5t, …，底脚在偶数倍处。换句话说，高度就是 x 到最近的 2t 的倍数的距离。时刻 x 的答案是所有帐篷的最高点，即对所有帐篷取 h − |x − c| 的最大值；不覆盖 x 的帐篷在那里的值至多为 0，不会胜出。

设 X 为最大的时刻。t ≥ X 的毛毛虫在所有时刻都还在往上爬，高度为 x，这正是顶点在 X、高度为 X 的帐篷给出的值。对 t < X，离时刻 x ≤ X 最近的帐篷顶点不会超过 2X。于是把帐篷放进数组：height[c] 是顶点在 c 的最高帐篷，对每个不同的 t 依次走 c = t, 3t, 5t, … 直到 2X 来填写。总共 O(X log X) 步。

然后 best[x] = 对 c 取 height[c] − |x − c| 的最大值，这是斜率为 1 的距离变换：从左到右扫一遍取 best[x] = max(height[x], best[x − 1] − 1) 处理左边的帐篷，再从右到左扫一遍处理右边的帐篷。每个时刻的答案直接从数组读出。使用排序时，时间 O(n log n + X log X + q)，内存 O(n + X + q)。

样例中，帐篷在奇数时刻高 1，在 2, 6, 10, … 高 2，在 3, 9, 15, … 高 3。时刻 12 最近的顶点 10、11、13、14、15 都给出 0，所以答案是 0。

注意事项：

- 同一个 t 可能出现很多次：只有不同的值才重要；
- 比所有时刻都高的毛毛虫也要计入，高度为 x；
- 顶点在最大时刻之后的帐篷对它之前的时刻有影响。

## 各语言说明

所有语言读入两百万个数都需要快速输入。Python 解答用大小为 T = 10⁶ + 1 的标记数组代替排序，在 PyPy 上运行，采用 JIT 擅长处理的简单循环；CPython 在最大的测试上约需六秒。把整个输入切分成单词会让 PyPy 用掉超过 64 MB，所以数字从小块输入中逐位解析，存放在 array 数组中，答案也分小批输出。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2064_math_prefix_sums.cpp](2064_math_prefix_sums.cpp) | G++ 13.2 x64 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.453 s | 33928 KB |
| [2064_math_prefix_sums.go](2064_math_prefix_sums.go) | Go 1.14 x64 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.562 s | 33868 KB |
| [2064_math_prefix_sums.java](2064_math_prefix_sums.java) | Java 1.8 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.468 s | 53828 KB |
| [2064_math_prefix_sums.py](2064_math_prefix_sums.py) | PyPy 3.10 x64 | math, prefix_sums | O(n + T + X log X + q) | AC | 0.875 s | 18808 KB |
| [2064_math_prefix_sums.rs](2064_math_prefix_sums.rs) | Rust 1.75 x64 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.265 s | 64076 KB |
