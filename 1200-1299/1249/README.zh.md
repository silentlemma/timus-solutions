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
2 3
1 1 1
1 0 1
```

输出：

```
No
```

### 样例 2

输入：

```
3 4
1 1 0 1
1 1 0 1
0 0 0 1
```

输出：

```
Yes
```

## 解法

若某个 2 × 2 窗口恰有三个暗格，它们属于同一连通块，该块不可能是
实心矩形。反过来，不是实心矩形的按边连通块，其边界必有向内凹的角，
孔洞周围也如此；该角对应一个恰有三个暗格的 2 × 2 窗口。因此只需排除这些窗口。

保留相邻行，在最后一格到达时检查每个2×2窗口。基础本地版显式检查格子，Python用整数位集表示行。读取O(NM)，行状态为O(M)项或Python O(M)位加当前输入行。最大3000×3000图若每像素一字节需9000000字节，超过4 MiB；小图可放下，甚至最大位压缩图也可能放下。因此并非任何整图都不能保存，流式处理避免最坏非压缩存储。仅角接触不连接分量。

以下五份仅修正不准确内存注释，保留可执行代码及有意义说明。

`1249_implementation.cpp` (#11283966); `1249_implementation.go` (#11283967); `1249_implementation.java` (#11283977); `1249_implementation.rs` (#11283979); `1249_implementation_parsing_optimized.go` (#11329324).

## 优化解法

`1249_implementation_optimized.rs`. 保留 2×2 和为三的禁形检测。以一行字节及保存的左、左上格替代两行，检查窗口后才更新本列。提前 No、最终 Yes 不变。O(NM) 时间、O(M) 存储。

与 `1249_implementation.rs` 相比：时间 0.031 s → 0.625 s；内存 224 KB → 68 KB。

相邻两行中，`B = previous AND current` 标记上下均为 1 的列，
`S = previous XOR current` 标记恰有一个 1 的列。禁用窗口恰是满列旁边有单格列，
故 `(B AND (S >> 1)) OR (S AND (B >> 1))` 同时检查两种顺序。

Python 将原来的四格表达式分解为此形式，并用一次转换移除行内空白。
C++ 将列压入 64 位字，采用有界输入缓冲区，并行检查字内窗口，再单独检查
相邻字之间的窗口；只保留前一行压缩数据与当前字。C++ 每行逻辑检查为
`O(ceil(M/64))`，但读取输入仍需 `O(N M)`，行存储为 `O(M/64)` 个字。
Python 保存 `O(M)` 位以及当前输入行。

保留成对记录：C++ 0.531 s/208 KB→0.078 s/128 KB（时间降85.3%、内存降38.5%）；Python 0.218 s/1532 KB→0.125 s/3684 KB（时间降42.7%、内存升）。快速Python不能仅按时间准入：3684 KB≥1024，必须比较内存。精确编译器参照允许2060.8 KB，故时间虽过，内存未过，星号保留。未变基础Python 1532 KB通过两项并覆盖语言，无单独加速准入例外。

`1249_implementation_parsing_optimized.go`以整数解析维度，将输入块直接解码到当前字节行，再与上一行检查窗口。固定8192输入字节，处理补充/EOF，避免每像素一次字节助手调用。fastPrint只支持字符串，用复用缓冲写固定Yes/No及换行，无数字输出转换；数值函数仅用于输入。几何判定不变。

下列Go Accepted配对属于修订注释前的历史源码。

Accepted #11329324 (Go 1.14 x64): **0.031 s / 820 KB**.

## 各语言说明

Python 与独立连通块遍历及包围矩形检查器比较了 75,254 个小图，
包括行列均不超过四的所有二值图。两个实际程序均在 Docker 中通过仓库的 14 组输入，
包含 3000 × 3000 大图。另检查了 C++ 与 Python 在字边界处的四种缺角方向及对角接触。

旧11月2日筛选排名已由精确源码缓存和统一[标准](../../RATING_CRITERIA.md)取代：优化C++、基础Java只按时间达标；Go解析器历史版本只看时间，对两名精确编译器对手中的第二名达标，基础Go未过时间。两份Rust以同语言回退达标，并非空表自动通过。基础C++保留教学。历史哈希数值准入与修订字节新Accepted是两件事。

上述源码修订均已取得各自的 Accepted。解答表列出与最终源码对应的提交编号及同次运行的时间和内存；较早的观察对应此前的修订。所有有教学价值的简单实现均保留。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1249_implementation.cpp](1249_implementation.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.562 s | 188 KB | 11331141 |
| [1249_implementation.go](1249_implementation.go) | Go 1.14 x64 | implementation | O(N M) | AC | 0.062 s | 1052 KB | 11331015 |
| [1249_implementation.java](1249_implementation.java) | Java 1.8 | implementation | O(N M) | AC | 0.125 s | 476 KB | 11331046 |
| [1249_implementation.py](1249_implementation.py) | Python 3.12 x64 | implementation | O(N M) | AC | 0.218 s | 1532 KB | 11283970 |
| [1249_implementation.rs](1249_implementation.rs) | Rust 1.75 x64 | implementation | O(N M) | AC | 0.046 s | 216 KB | 11331109 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1249_implementation_optimized.cpp](1249_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.078 s | 128 KB | 11308213 |
| [1249_implementation_optimized.py](1249_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N M) | AC | 0.125 s | 3684 KB | 11308214 |
| [1249_implementation_optimized.rs](1249_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(NM) time; O(M) space | AC | 0.625 s | 68 KB | 11325546 |
| [1249_implementation_parsing_optimized.go](1249_implementation_parsing_optimized.go) | Go 1.14 x64 | implementation, parsing | O(nm) time; O(m) row state + bounded input buffer | AC | 0.062 s | 816 KB | 11331016 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
