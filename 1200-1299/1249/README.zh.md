# 1249. 所有暗区都是矩形吗？

[Timus 1249](https://acm.timus.ru/problem.aspx?space=1&num=1249) · 难度 221 · implementation

原题作者 Nikita Shamgunov 和 Leonid Volkov，出自 2003 年 3 月 15 日乌拉尔国立大学公开团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定最多 3000 行、3000 列的 `N × M` 二值图像，判断每个按公共边相连的 1 连通块是否都是轴对齐的实心矩形。仅角接触不算连通。时间限制：2.5 秒；内存限制：4 MB。

## 输入

先给出 `N M`，随后 `N` 行，每行 `M` 个用空格分隔的 0 或 1。

## 输出

每个连通块均为实心矩形时输出 `Yes`，否则输出 `No`。

## 评测方式

按标记比较 `Yes` 或 `No`，大小写必须一致；空白格式不影响结果。

## 样例

### 样例 1

输入：

```
2 2
0 1
1 1
```

输出：

```
No
```

### 样例 2

输入：

```
3 3
0 0 1
1 1 0
1 1 0
```

输出：

```
Yes
```

## 解法

若某个 2 × 2 窗口恰有三个暗格，它们属于同一连通块，该块不可能是
实心矩形。反过来，不是实心矩形的按边连通块，其边界必有向内凹的角，
孔洞周围也如此；该角对应一个恰有三个暗格的 2 × 2 窗口。因此只需排除这些窗口。

只保留相邻两行，在窗口最后一个格子到达时检查。简单原生版本直接检查四格；
简单 Python 用整数位集表示行，并结合奇偶性与至少两格为 1 的条件。
输入时间为 `O(N M)`，行存储为 `O(M)`；存整幅图像或全部输入文本会超过内存限制。
仅对角接触的块仍然分开。五份原始 Accepted 源码全部逐字节保留。

## 优化解法

相邻两行中，`B = previous AND current` 标记上下均为 1 的列，
`S = previous XOR current` 标记恰有一个 1 的列。禁用窗口恰是满列旁边有单格列，
故 `(B AND (S >> 1)) OR (S AND (B >> 1))` 同时检查两种顺序。

Python 将原来的四格表达式分解为此形式，并用一次转换移除行内空白。
C++ 将列压入 64 位字，采用有界输入缓冲区，并行检查字内窗口，再单独检查
相邻字之间的窗口；只保留前一行压缩数据与当前字。C++ 每行逻辑检查为
`O(ceil(M/64))`，但读取输入仍需 `O(N M)`，行存储为 `O(M/64)` 个字。
Python 保存 `O(M)` 位以及当前输入行。

C++ 从 0.531 秒 / 208 KB 降至 0.078 秒 / 128 KB，时间减少 85.3%，内存减少 38.5%。
Python 从 0.218 秒 / 1532 KB 变为 0.125 秒 / 3684 KB，时间减少 42.7%，但实测内存峰值增大。
因此 Python 仅按时间改善准入；两个新版本都有各自的 Accepted，并非每项资源都更优。

## 各语言说明

Python 与独立连通块遍历及包围矩形检查器比较了 75,254 个小图，
包括行列均不超过四的所有二值图。两个实际程序均在 Docker 中通过仓库的 14 组输入，
包含 3000 × 3000 大图。另检查了 C++ 与 Python 在字边界处的四种缺角方向及对角接触。

排名快照为 2026 年 11 月 2 日。C++ 在 61 个筛选后的其他作者记录中，时间第 5、
内存第 1，达到目标。Python 对一个记录为时间第 1、内存第 2，因此保留星号。
原 Java 对四个记录两项均第 1。Go、Rust 的筛选比较样本为空，形式覆盖不证明竞争优势。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1249_implementation.cpp](1249_implementation.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.531 s | 208 KB | 11283966 |
| [1249_implementation.go](1249_implementation.go) | Go 1.14 x64 | implementation | O(N M) | AC | 0.093 s | 1096 KB | 11283967 |
| [1249_implementation.java](1249_implementation.java) | Java 1.8 | implementation | O(N M) | AC | 0.156 s | 452 KB | 11283977 |
| [1249_implementation.py](1249_implementation.py) | Python 3.12 x64 | implementation | O(N M) | AC | 0.218 s | 1532 KB | 11283970 |
| [1249_implementation.rs](1249_implementation.rs) | Rust 1.75 x64 | implementation | O(N M) | AC | 0.031 s | 224 KB | 11283979 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1249_implementation_optimized.cpp](1249_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.078 s | 128 KB | 11308213 |
| [1249_implementation_optimized.py](1249_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N M) | AC | 0.125 s | 3684 KB | 11308214 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
