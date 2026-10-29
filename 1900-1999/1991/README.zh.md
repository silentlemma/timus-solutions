# 1991. 统计剩余供给与未消除目标

[Timus 1991](https://acm.timus.ru/problem.aspx?space=1&num=1991) · 难度 48 · implementation

原题作者 Denis Dublennykh（由 Egor Shchelkonogov 整理）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 `n` 个独立组，每组恰有 `k` 个目标。第 `i` 组得到 `a_i` 单位供给，每单位只能使用一次，消除本组一个目标，且总能成功。组间不能交换供给。各组尽可能消除目标后，求未使用供给总数和剩余目标总数。

限制：`1≤n,k≤10000`，`0≤a_i≤100000`。时间限制 1 秒，内存限制 64 MB。

## 输入

第一行是 `n k`，第二行是 `n` 个供给数量。

## 输出

两个整数：先输出未使用供给总数，再输出剩余目标总数。

## 评测方式

按记号逐个比较输出。

## 样例

输入：

```
4 5
2 7 5 0
```

输出：

```
2 8
```

各组的 `(剩余供给,剩余目标)` 分别为 `(0,3)`、`(2,0)`、`(0,0)`、`(0,5)`，总和为 `(2,8)`。

## 解法

每组用 min(aᵢ, k) 份补给消灭 min(aᵢ, k) 个目标。因此当 aᵢ > k 时剩下 aᵢ − k 份
未用的补给，否则剩下 k − aᵢ 个目标。把这些数按组相加即可。`O(n)`。

注意事项：

- 补给不能在组之间转移，所以一组可能有多余的补给，而另一组还有目标：只比较
  总数是错的；
- 未用补给的总数可达 10 000 · 99 999 ≈ 10⁹，仍在 32 位有符号整数范围内。

## 优化解法

优化的 C++ 解法用 `scanf` 和 `printf` 代替 `iostream`：132 KB，而不是 448 KB。总数
的计算不变。

## 各语言说明

没有特别需要注意的地方。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1991_implementation.cpp](1991_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 448 KB | 11292383 |
| [1991_implementation.go](1991_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1236 KB | 11292384 |
| [1991_implementation.java](1991_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 472 KB | 11303526 |
| [1991_implementation.py](1991_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 1380 KB | 11292385 |
| [1991_implementation.rs](1991_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 480 KB | 11292387 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1991_implementation_optimized.cpp](1991_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 132 KB | 11303652 |
