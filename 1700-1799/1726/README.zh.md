# 1726. 串门

[Timus 1726](https://acm.timus.ru/problem.aspx?space=1&num=1726) · 难度 120 · sorting

原题作者 Denis Dublennykh，出自 2009 年乌拉尔地区团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

委员会的 n 名成员住在网格城市的街道交叉口，沿街道走最短路互相拜访。每人拜访每人的频率相同。求平均步行距离，向下取整。

## 输入

第一行是 n（2 ≤ n ≤ 10⁵），接下来 n 行，每行是坐标 x 和 y（1 ≤ x, y ≤ 10⁶）。

## 输出

两名成员住所之间的平均距离，向下取整。

## 样例

### 样例 1

输入：

```
3
10 10
20 20
10 20
```

输出：

```
13
```

## 解法

沿街道的最短路长度为 |dx| + |dy|，所以所有点对的总和分解为 |x_i − x_j| 之和与 |y_i − y_j| 之和。
把 x 排序：第 i 个值（从 0 开始）不小于它之前的 i 个值，所以贡献 i·x_i 减去它们的和，这个和用累计量维护。
y 同理。对 n(n − 1)/2 个点对的平均值就是总和除以点对数并向下取整。`O(n log n)`。

样例中距离为 20、10 和 10，平均值为 40/3，向下取整为 13。

注意事项：

- 当一半房子在一个远角、另一半在对面远角时，总和约达 5·10¹⁵，需要 64 位整数；
- 直接比较所有点对约需 5·10⁹ 步，太多了。

在 300 张小型随机地图上，平均值与对所有点对求和的结果一致；在大测试上与一个独立的已通过实现一致。

## 优化解法

优化的 C++ 解法把坐标存放在静态 `int` 数组中（坐标不超过 10⁶，放得下），而不是
`long long` 向量；2·10⁵ 个数从用 `fread` 读入的 4 KB 块中手动解析，而不是每个数
调用一次 `scanf`；求和仍用 `long long`：{1726_sorting_optimized.cpp}。

优化的 Go 解法从 64 KB 的带缓冲 reader 中手动解析 2·10⁵ 个数，而不是用
`fmt.Fscan`——后者正是简单程序中慢的部分：{1726_sorting_optimized.go}。

优化的 Python 解法每批读入约 64 KB 的行，存入 32 位整数数组（坐标不超过 10⁶，放
得下），而不是把输入的每个词保留为字节串、再建两个 Python 整数列表。它还不用
Python 循环计算每个和：排好序后，`n` 个值中的第 `i` 个（从 0 开始）不小于它前面
的 `i` 个、不大于它后面的 `n − 1 − i` 个，所以它以权重 `2i − (n − 1)` 计入总和；
对排好序的值和权重的 `range` 调用 `sum(map(mul, …))`，整个过程都在 C 中执行：
{1726_sorting_optimized.py}。

优化的 Rust 解法从 4 KB 的块中手动解析数字，而不是把整个输入读成字符串；坐标用
`u32` 而不是 `i64` 存储（坐标不超过 10⁶，放得下）；求和用 `u64`：
{1726_sorting_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1726_sorting_optimized.cpp`: 时间降低 +91.23%; 内存降低 +49.43%; 基础版本: `1726_sorting.cpp`.

- `1726_sorting_optimized.go`: 时间降低 +70.51%; 内存降低 +37.78%; 基础版本: `1726_sorting.go`.

- `1726_sorting_optimized.py`: 时间降低 +0.00%; 内存降低 +70.45%; 基础版本: `1726_sorting.py`.

- `1726_sorting_optimized.rs`: 时间降低 +0.00%; 内存降低 +79.09%; 基础版本: `1726_sorting.rs`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1726_sorting.cpp](1726_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.171 s | 1756 KB | 11304062 |
| [1726_sorting.go](1726_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.156 s | 4404 KB | 11304355 |
| [1726_sorting.java](1726_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.125 s | 2092 KB | 11304357 |
| [1726_sorting.py](1726_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.187 s | 20644 KB | 11304063 |
| [1726_sorting.rs](1726_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 4744 KB | 11304064 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1726_sorting_optimized.cpp](1726_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 888 KB | 11304358 |
| [1726_sorting_optimized.go](1726_sorting_optimized.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.046 s | 2740 KB | 11304362 |
| [1726_sorting_optimized.py](1726_sorting_optimized.py) \* | Python 3.12 x64 | sorting | O(n log n) | AC | 0.187 s | 6100 KB | 11304360 |
| [1726_sorting_optimized.rs](1726_sorting_optimized.rs) \* | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 992 KB | 11304361 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
