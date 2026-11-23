# 1185. 与多边形城堡保持指定距离的最短城墙

[Timus 1185](https://acm.timus.ru/problem.aspx?space=1&num=1185) · 难度 301 · geometry

原题作者 Sergey Volchenkov 和 Roman Elizarov，出自 2001–2002 年 ACM ICPC 东北欧区域赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

城堡是一个简单多边形，有 `3 ≤ N ≤ 1000` 个按顺时针给出的整点顶点。求环绕城堡、
处处与城堡距离不小于 `L` 英尺的最短闭合城墙的长度，四舍五入到整英尺。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N` 和 `L`，然后是各顶点。

## 输出

以英尺为单位的长度，误差不超过 8 英寸。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
9 100
200 400
300 400
300 300
400 300
400 400
500 400
500 200
350 200
200 200
```

输出：

```
1628
```

## 解法

最短城墙是凸的，必定围住城堡的凸包，且恰为到凸包距离等于 `L` 的
点集。沿凸包的每条边，城墙在距离 `L` 处平行延伸，长度等于该边长。在凸包的每个
顶点，它沿半径为 `L` 的圆弧转过该处的外角，而凸多边形外角之和恰为一整圈。所以
长度等于凸包周长加上 `2πL`。

凸包用 Andrew 单调链求：将点排序，分别构造下链和上链，去掉不向左拐的点（包括
共线点）。四舍五入到最近的英尺，误差至多 6 英寸。`O(N log N)`。

注意事项：

- 城堡不一定是凸的，所以它自身的周长太长；凹进去的部分由凸包的边跨过，样例
  就是如此；
- 直边中间的顶点不能破坏凸包，所以要去掉共线点；
- 答案要四舍五入，而不是截断。

答案已在 200 个随机城堡和所有测试上与另一份独立编写的解答比对。

## 优化解法

`1185_geometry_optimized.java`. 保留单调链凸包、周长加 2πL，并仅在最后取整。每点压成一个 long：有符号 x 占高32位，y 翻转符号位后在低半部保持有符号顺序，基本类型排序得到同样字典序。凸包用一个 int 下标数组替代坐标对象和临时列表。叉积仍以 long 精确计算，只有边长用 hypot。空间 O(N)。设基本类型排序代价为 S(N)，凸包扫描额外 O(N)；Java8 通常 O(N log N)，最坏情况保守允许二次排序，而不保证严格对数界。

与 `1185_geometry.java` 相比：时间 0.140 s → 0.109 s；内存 3144 KB → 556 KB。

Go 版本先给两个坐标各加 10 000，再打包到一个 32 位整数中，x 在高位。对整数排序就得到字典序。沿两个方向扫描该顺序，两条单调链共用一个栈。周长仍需加上偏移项 2πL。

已通过评测的基础实现 [1185_geometry.cpp](1185_geometry.cpp), [1185_geometry.java](1185_geometry.java), [1185_geometry.py](1185_geometry.py), [1185_geometry.rs](1185_geometry.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1185_geometry_parsing_optimized.go`. 词元转换及数值输出按实际类型专门化，移除未使用的通用分支，保留算法和注释。

Accepted #11328893 (Go 1.14 x64): **0.015 s / 1072 KB**. 历史对照: `1185_geometry.go` (Go 1.14 x64) — 0.031 s / 1204 KB (#11283369).

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1185_geometry_implementation_parsing_optimized.rs`. 采用有界原生读取及完整原生写出、Windows 二进制描述符和 C 入口。纯数字输入直接从字节转为有符号整数，不分配词元；依赖行边界的输入保留完整行。 点使用原地不稳定排序；相同点在不变的凸包算法中可互换。

Accepted #11329170 (Rust 1.75 x64): **0.015 s / 124 KB**. 历史对照: `1185_geometry.rs` (Rust 1.75 x64) — 0.031 s / 264 KB (#11283379).

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1185_geometry_optimized.java`：在该可比样本中，时间名次 5/27，内存名次 1/27。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1185_geometry.cpp](1185_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 236 KB | 11283368 |
| [1185_geometry.go](1185_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1204 KB | 11283369 |
| [1185_geometry.java](1185_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 3144 KB | 11283377 |
| [1185_geometry.py](1185_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 752 KB | 11283372 |
| [1185_geometry.rs](1185_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 264 KB | 11283379 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1185_geometry_optimized.go](1185_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 824 KB | 11310857 |
| [1185_geometry_optimized.java](1185_geometry_optimized.java) | Java 1.8 | geometry | O(N+S(N)) | AC | 0.109 s | 556 KB | 11325011 |
| [1185_geometry_parsing_optimized.go](1185_geometry_parsing_optimized.go) | Go 1.14 x64 | geometry, parsing | O(N log N) | AC | 0.015 s | 1072 KB | 11328893 |
| [1185_geometry_implementation_parsing_optimized.rs](1185_geometry_implementation_parsing_optimized.rs) | Rust 1.75 x64 | geometry, implementation, parsing | O(N log N) | AC | 0.015 s | 124 KB | 11329170 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
