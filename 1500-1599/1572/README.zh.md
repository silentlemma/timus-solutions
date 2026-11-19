# 1572. 叶卡捷琳诺扎沃茨克大井

[Timus 1572](https://acm.timus.ru/problem.aspx?space=1&num=1572) · 难度 146 · geometry

原题作者 Alexander Ipatov 和 Alex Samsonov，出自 2007 年 10 月第十四届斯维尔德洛夫斯克州中学生团体程序设计公开赛（USU Junior Contest）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

井口和至多 100 个井盖都是圆（类型 1，尺寸为半径）、正方形（类型 2）或正三角形（类型 3，尺寸为边长），尺寸为
1 … 100 的整数。扁平的井盖可以在空间中任意旋转和移动。求能扔进井里的井盖数。

时间限制：1 秒。内存限制：64 MB。

## 输入

井的类型和尺寸，然后是 N（1 ≤ N ≤ 100）以及每个井盖的类型和尺寸。

## 输出

能穿过的井盖数。

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。

## 样例

### 样例 1

输入:

```
2 10
3
3 20
1 5
2 11
```

输出:

```
2
```

### 样例 2

输入:

```
1 5
2
2 10
1 6
```

输出:

```
1
```

## 解法

把井盖竖起来径直往下推，它与井口平面的交线是自身的一组平行弦，所以只要在某个方向上它最长的弦能放进井口，
它就能穿过。最好的方向对圆是直径 2r，对正方形是边长 a，对三角形是高 a·√3/2（平行于高的弦）。井口能容纳的
线段最长为：圆的直径 2R、正方形的对角线 A·√2、三角形的边长 A。

把这些长度平方再乘以 4 都是整数：井盖为 16r²、4a²、3a²，井口为 16R²、8A²、4A²，所以比较是精确的，恰好碰到
边的井盖也能穿过。`O(N)`。对任意形状和尺寸的每一对井口和井盖，答案都与一个独立程序一致。

注意事项：

- 圆的尺寸是半径，不是直径；
- 三角形靠高而不是边穿过，所以边长 16 的三角形仍能放进边长 10 的正方形井（测试 06）；
- 尺寸相等也能穿过：边长 10 的正方形能穿过半径 5 的圆（第二个样例），所以浮点比较要小心。

## 优化解法

`1572_geometry_optimized.py`. 保留 NARROWEST/WIDEST 系数下精确平方弦比较，含相等。逐盖读取、检验缩放整数平方即丢弃，无盖列表。O(n) 时间、常数几何状态及词缓冲。刷新单个答案后退出 PyPy，保留几何教学推导。

与 `1572_geometry.py` 相比：时间 0.093 s → 0.14 s；内存 384 KB → 264 KB。

`1572_geometry_optimized.rs`. 保留 NARROWEST/WIDEST 形状系数的精确平方弦比较，包含相等情形。直接读每个盖，比较其 u64 缩放平方后丢弃，不保存全量解析向量；直接输出替代格式化。O(n) 时间、O(1) 辅助空间，保留清晰几何推导和基础源。

与 `1572_geometry.rs` 相比：时间 0.031 s → 0.046 s；内存 228 KB → 60 KB。

优化的 Java 解法从由 `System.in` 填充的 4 KB 缓冲区中手工解析数字，而不是创建
`Scanner`，这样 JVM 不必加载扫描器及其正则表达式；比较长度平方的方法不变：
{1572_geometry_optimized.java}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1572_geometry_optimized.java`: 时间降低 +44.29%; 内存降低 +80.86%; 基础版本: `1572_geometry.java`.

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1572_geometry_optimized.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1572_geometry.cpp](1572_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 128 KB | 11287799 |
| [1572_geometry.go](1572_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1072 KB | 11287801 |
| [1572_geometry.java](1572_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.140 s | 1776 KB | 11287805 |
| [1572_geometry.py](1572_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 384 KB | 11287803 |
| [1572_geometry.rs](1572_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 228 KB | 11287810 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1572_geometry_optimized.java](1572_geometry_optimized.java) | Java 1.8 | geometry | O(N) | AC | 0.078 s | 340 KB | 11304529 |
| [1572_geometry_optimized.rs](1572_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n) time; O(1) space | AC | 0.046 s | 60 KB | 11325506 |
| [1572_geometry_optimized.py](1572_geometry_optimized.py) \* | PyPy 3.10 x64 | geometry | O(n) time; O(1) state plus bounded token buffers | AC | 0.14 s | 264 KB | 11325701 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
