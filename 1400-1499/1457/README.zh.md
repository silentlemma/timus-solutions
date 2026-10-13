# 1457. 供暖管道

[Timus 1457](https://acm.timus.ru/problem.aspx?space=1&num=1457) · 难度 69 · math

原题作者 Nikita Rybak、Dmitry Kovalioff 与 Ilya Grebnov，出自 Timus Top Coders: Second Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一条笔直的供暖管道经过 N 个地点（1 ≤ N ≤ 1000）的下方，位置为 P[i]
（0 ≤ P[i] ≤ 10⁶）。走一段距离所花的力气与距离的平方成正比。求管道上到各地点平均
力气最小的点，小数点后至少六位。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是 N 个位置。

## 输出

最优的点。

## 样例

### 样例 1

输入:

```
3
7 4 5
```

输出:

```
5.333333
```

## 解法

(x − P[i])² 的平均值是关于 x 的抛物线，导数 2 (x − 平均值) 在各位置的算术平均处
为零，所以答案就是总和除以 N。总和不超过 10⁹，32 位有符号整数放得下。`O(N)`。

注意事项：

- 当平均值恰好以 5 结尾（如 1/128）时，各语言保留六位小数的舍入可能不同（测试
  05）；在要求精度内的答案都被接受。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1457_math.cpp](1457_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 144 KB |
| [1457_math.go](1457_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1120 KB |
| [1457_math.java](1457_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 2612 KB |
| [1457_math.py](1457_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 504 KB |
| [1457_math.rs](1457_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 252 KB |
