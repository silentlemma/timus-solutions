# 1084. 拴着的山羊能吃到的正方形菜园面积

[Timus 1084](https://acm.timus.ru/problem.aspx?space=1&num=1084) · 难度 151 · geometry

原题作者 Irina Danilina，出自 2001 年 3 月 4 日斯维尔德洛夫斯克州第三届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一只山羊用长为 `r` 的绳子拴在边长为 `a` 的正方形菜园中心的木桩上（两者都是 1 到 100 的整数）。它会吃掉所有够得
着的东西，但不会离开菜园。求被吃掉的面积，保留小数点后三位。

时间限制：1 秒。内存限制：64 MB。

## 输入

`a` 和 `r`。

## 输出

被吃掉的面积。

## 评测方式

数值按绝对误差 0.0011 比较：答案以三位小数输出，最后一位可能相差 1。

## 样例

### 样例 1

输入：

```
10 6
```

输出：

```
95.091
```

## 题解

被吃掉的部分是正方形与以其中心为圆心、半径为 `r` 的圆的交集。设 `h = a/2`。

- `r ≤ h`：圆完全在正方形内，面积为 `πr²`。
- `r² ≥ 2h²`：绳子够得着四个角，整个正方形 `a²` 都被吃掉。
- 否则每条边从圆上切下一个弓形。距圆心为 `h` 的弓形面积是 `r²·arccos(h/r) − h·√(r² − h²)`，而且由于圆够不到
  四个角，四个弓形互不重叠。面积为 `πr² − 4·弓形`。

`O(1)`。

注意事项：

- 中间情形需要两个边界：当 `r` 不小于半条对角线时，弓形会重叠，公式会多减；
- 判断 `r² ≥ 2h²` 比较的是平方，避免了对 2 开方。

答案与对被吃部分的高度 `min(a, 2√(r² − x²))` 关于 `x` 用辛普森法则做的数值积分（在公式变化处分段）做了核对。

## 优化解法

优化的 Java 解法从由 `System.in` 填充的 4 KB 缓冲区中手工解析两个整数，而不是创
建 `Scanner`，这样 JVM 不必加载扫描器及其正则表达式；公式和用 `String.format` 输
出的方式不变：{1084_geometry_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1084_geometry_optimized.java`: 时间降低 +25.60%; 内存降低 +49.11%; 基础版本: `1084_geometry.java`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1084_geometry.cpp](1084_geometry.cpp).
- [1084_geometry.go](1084_geometry.go).
- [1084_geometry.rs](1084_geometry.rs).

- C++ 用 `acos(-1)` 得到 `π`，因为 `M_PI` 不属于标准 C++。
- Java 用 `Locale.US` 格式化答案，以得到小数点。

## 题解代码

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1084_geometry.cpp](1084_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 148 KB | 11279033 |
| [1084_geometry.go](1084_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB | 11279034 |
| [1084_geometry.java](1084_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1792 KB | 11279036 |
| [1084_geometry.py](1084_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.062 s | 376 KB | 11279035 |
| [1084_geometry.rs](1084_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 268 KB | 11279037 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1084_geometry_optimized.java](1084_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 912 KB | 11304545 |
