# 1873. GOV 编年史

[Timus 1873](https://acm.timus.ru/problem.aspx?space=1&num=1873) · 难度 365 · implementation

原题作者 Mikhail Rubinchik，出自 2011 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

题面按比赛逐场讲述了 Alarm 队（后来的 Team.GOV）的漫长历史，以及阵容的每次变化。队员编号为 0 到 13。给出队员编号，输出该队员代表这支队伍参加了多少场比赛。最后一次乌拉尔锦标赛的热身赛不计入。

## 输入

队员编号，0 到 13。

## 输出

该队员代表队伍参加的比赛场数。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
1
```

输出：

```
21
```

### 样例 2

输入：

```
11
```

输出：

```
0
```

## 解法

所有工作都在于仔细阅读故事；程序只是查表。按顺序的比赛及阵容：

| 比赛 | 队员 |
| --- | --- |
| Alarm：校赛、四分之一决赛、半决赛、乌拉尔、鞑靼斯坦 | 0, 1, 2 |
| 2008 年秋季校赛 | 1, 2 |
| 四分之一决赛 | 1, 2, 3 |
| 半决赛 | 1, 2, 4 |
| 乌拉尔锦标赛选拔赛 | 1, 2, 5 |
| 乌拉尔锦标赛 | 1, 5 |
| 四分之一决赛、校赛、半决赛 | 1, 2, 6 |
| 代际之战 | 1, 6, 7 |
| 乌拉尔锦标赛选拔赛 | 5, 6 |
| 乌拉尔锦标赛 | 1, 5, 6 |
| 校赛、四分之一决赛、全西伯利亚竞赛、半决赛 | 1, 8, 9 |
| 最后一次乌拉尔锦标赛 | 1, 3, 10 |
| SWERC | 1, 12, 13 |

相加得到 0 到 13 号队员的比赛场数：5, 21, 12, 2, 1, 4, 6, 1, 4, 4, 1, 0, 1, 1。`O(1)`。

注意事项：

- 11 号队员只参加了热身赛，所以答案为 0；
- 有些比赛只有两人参加：2008 年校赛缺 3 号，一次乌拉尔锦标赛缺 2 号，一次选拔赛缺 1 号；
- 故事结尾的 SWERC 也要算。

对全部十四名队员，表格与一个独立的已通过实现一致。

## 优化解法

`1873_implementation_optimized.java`. Java 保留简单版本所述的算法和数据结构。固定字节缓冲区与 FastInput 替代 Scanner 及其正则表达式、区域设置处理。整数记号直接解析；需要字符串时仍进行 UTF-8 解码，十进制记号仍显式转换为数值。仅在需要前瞻时保存一个记号，输出算法不变。这样减少通用解析开销；表中列出算法工作量，输入扫描与字节数成正比，并使用有界输入缓冲区。

与 `1873_implementation.java` 相比：时间 0.109 s → 0.093 s；内存 1584 KB → 460 KB。

Go 和 Python 保留相同的十四项参赛次数表。Go 直接用固定字节缓冲区读取编号，并复用缓冲区输出答案。Go 通过 syscall.Read 和 syscall.Write 使用标准句柄，重试中断调用并完成部分写入。PyPy 版本用无缓冲二进制流读取编号并输出预编码答案，避免文本格式化。

通过评测的 PyPy 3.10 x64 版本耗时 0.14 秒，基础版为 0.078 秒，内存为 208 KB，基础版为 388 KB。

已通过评测的基础实现 [1873_implementation.cpp](1873_implementation.cpp), [1873_implementation.java](1873_implementation.java), [1873_implementation.rs](1873_implementation.rs) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。保留教学算法。复查的基础代码行使用其自身新精确源代码 Accepted 的指标与 ID；这些检查不算优化。

`1873_implementation_optimized.java`：在该可比样本中，时间名次 4/28，内存名次 1/28。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1873_implementation.cpp](1873_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 112 KB | 11325583 |
| [1873_implementation.go](1873_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1072 KB | 11290961 |
| [1873_implementation.java](1873_implementation.java) \* | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1584 KB | 11290964 |
| [1873_implementation.py](1873_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 388 KB | 11290962 |
| [1873_implementation.rs](1873_implementation.rs) \* | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 240 KB | 11290966 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1873_implementation_optimized.go](1873_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 288 KB | 11311200 |
| [1873_implementation_optimized.py](1873_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(1) | AC | 0.14 s | 208 KB | 11311240 |
| [1873_implementation_optimized.java](1873_implementation_optimized.java) \* | Java 1.8 | implementation | O(1) | AC | 0.093 s | 460 KB | 11324804 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
