# 1207. 过两点且平分其余点的直线

[Timus 1207](https://acm.timus.ru/problem.aspx?space=1&num=1207) · 难度 117 · geometry

原题作者 Pavel Atnashev，出自 2002 年 3 月乌拉尔国立大学团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

平面上有偶数个 `4 ≤ N ≤ 10000` 个点，坐标为绝对值不超过 `10⁶` 的整数，任意三点
不共线。选出其中两点，使过这两点的直线把其余的点分成数量相等的两半。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

第一行是 `N`，接下来 `N` 行，每行是一个点的坐标 `x y`。

## 输出

所选两点的编号。

## 评测方式

满足条件的点对很多，所以只要是两个不同的点，且它们的直线两侧各有 `(N − 2)/2`
个点，就判为正确。

## 样例

### 样例 1

输入：

```
4
0 0
1 0
0 1
1 1
```

输出：

```
1 4
```

## 解法

取最低的点，若有两点同样低则取左边那个。其余所有点都在它上方或同一高度的右侧，
处在半圈之内，所以只用叉积的符号就能按绕它的角度排序，不需要浮点数。按这个顺序，
排在第 `k` 个之前的点都在从最低点到第 `k` 个点的直线的一侧，排在之后的都在另一
侧。其余共有 `N − 1` 个点，从零开始编号时位于 `(N − 2)/2` 处的那个点前后各有
`(N − 2)/2` 个点。`O(N log N)`。

注意事项：

- 如果任意选择基准点，射线可能跨越超过半圈的范围，破坏顺序；
- 叉积可达 `4·10¹²`，超出 32 位；
- 比较函数在元素与自身比较时必须返回“相等”，否则有些排序例程会拒绝它。

每个答案都通过统计两侧的点数检查过，另一份独立解答在所有测试上也能通过同一个
评测程序。

## 优化解法

优化的 Java 解法把坐标存放在 `int` 数组中（绝对值不超过 `10⁶`），用手写的堆排序
对基本类型的下标数组排序，而不是用 lambda 对装箱的 `Integer` 下标排序；叉积用
`long` 计算；输入按 4 KB 分块手动解析，而不是用 `BufferedReader` 和
`StringTokenizer`：{1207_geometry_optimized.java}。

优化的 Python 解法为每个点只计算一次整数键，再按键排序，而不是调用 `O(N log N)`
次 Python 比较函数。键是 `−dx/dy` 乘以 `2⁴²` 后向下取整，其中 `dx`、`dy` 是相对
基准点的偏移；`−dx/dy` 随相对基准点的角度增大而增大。偏移的绝对值不超过
`2·10⁶`，所以两个不同的分数至少相差 `1/(2·10⁶)²`，而 `2⁴²` 大于 `(2·10⁶)²`，因
此取整后的键仍然互不相同且顺序不变；与基准点同高的点得到一个比其余所有键都小的
键。坐标逐行读入 32 位整数数组：{1207_geometry_optimized.py}。

优化的 Rust 解法逐行读取输入，而不是保存整段文本和其中所有数字组成的向量；每个点
以两个 `i32` 坐标加编号存入一个结构体（坐标绝对值不超过 `10⁶`），先把所有点平移
一次使基准点位于原点，再用 `sort_unstable_by` 按 `i64` 叉积排序：
{1207_geometry_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1207_geometry_optimized.java`: 时间降低 +36.26%; 内存降低 +88.53%; 基础版本: `1207_geometry.java`.

- `1207_geometry_optimized.py`: 时间降低 +33.57%; 内存降低 +49.37%; 基础版本: `1207_geometry.py`.

- `1207_geometry_optimized.rs`: 时间降低 -48.39%; 内存降低 +56.39%; 基础版本: `1207_geometry.rs`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1207_geometry.cpp](1207_geometry.cpp).

- Python 用 `functools.cmp_to_key` 排序；Java 用 `Long.compare` 的 lambda 对装箱的
  下标排序。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1207_geometry.cpp](1207_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 296 KB | 11283603 |
| [1207_geometry.go](1207_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.046 s | 1512 KB | 11283604 |
| [1207_geometry.java](1207_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.171 s | 5544 KB | 11283609 |
| [1207_geometry.py](1207_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.140 s | 3516 KB | 11283608 |
| [1207_geometry.rs](1207_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 908 KB | 11283610 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1207_geometry_optimized.java](1207_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.109 s | 636 KB | 11304352 |
| [1207_geometry_optimized.py](1207_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(N log N) | AC | 0.093 s | 1780 KB | 11304354 |
| [1207_geometry_optimized.rs](1207_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 396 KB | 11304353 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
