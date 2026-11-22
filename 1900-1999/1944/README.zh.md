# 1944. 点优先的ASCII坐标图

[Timus 1944](https://acm.timus.ru/problem.aspx?space=1&num=1944) · difficulty 238 · implementation

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

绘制互异整数点的笛卡尔图，x向右增、y向上增，一格代表一个坐标对。
输入点用*，原点用+，x轴用-，y轴用|，其余用.。点覆盖坐标轴及
原点，坐标轴可完全被点遮住。绘制包含所有点与原点的最小矩形。
时限1秒，内存64 MB。

## 输入

n满足1≤n≤250，随后n对互异整数坐标，−100≤x,y≤100。无重复点。

## 输出

行从U=max(0,max y)向下至D=min(0,min y)，两端包含；列从
L=min(0,min x)到R=max(0,max x)。每行W=R−L+1个符号，共H=U−D+1行。
只输出图形。

## 评测方式

逐字节比较整个图，包括每个符号和换行，不能只比较空白分隔的词。
两份新发布程序各通过目标 Docker 编译器下全部 26 个仓库输入和 69 个独立额外输入。
重新读取每次额外运行的实际输出及退出码，与独立逐坐标定义的答案比较：先判断输入点，
再判断原点、坐标轴和背景。覆盖原点、单行单列、完全遮住的坐标轴、各象限、±100、
250 点、显式正号、CRLF 和 EOF。独立 Python 候选也通过这 69 次目标运行，
并在主机执行 2048 次，包括 3×3 网格所有非空子集；这 2048 次不是 C++ 或 Java
测试。三个候选均有对应精确源码的 Accepted，准入条件仍单独判断。

## 样例

```
8
-10 5
-7 3
-4 2
-9 4
0 1
6 -1
3 0
8 -3
```

```
*.........|........
.*........|........
...*......|........
......*...|........
..........*........
----------+--*-----
..........|.....*..
..........|........
..........|.......*
```

## 解法

四个边界先置零，再由输入点扩展。坐标(x,y)映射到row=U−y、
column=x−L，恰为0..H−1和0..W−1的双射，方向正确。

先用.填充H×W网格，每行的−L列置|。第U行填-，其−L列改+。
最后把每个输入点对应格改为*，按行下标递增输出。

初始点号覆盖背景；竖、横遍历恰好对应x=0及y=0，交点替换为+。
最后的星号遍历确保输入点优先，互异点映射也互异。边界从零开始
保证即使点都在同一象限仍包含原点，且任何更小边界都会丢失所需
坐标。故形状、符号、方向均正确，也覆盖仅一行或一列的情况。

时间及空间O(n+WH)，包括点及输出。W,H≤201，最大输出含换行
H(W+1)≤40602个ASCII字节，小于64 KiB。普通有符号整数足够表示下标。

两个坐标范围都包含零。行下标增大时y减小，不要互换行列偏移。
原点仅在没有输入点时是+；轴上的点仍为*。不能加标签、空格、
边框或额外边距。

## 优化解法

`1944_implementation_bitmask.java`. 固定掩码网格替代打包点排序，201 行每行四个 long。直接标点，输出框包含原点，再让置位星号覆盖坐标轴。掩码 6432 字节，完整输出至多 40602 字节，一次写出。K 为标记格、W/H 为输出尺寸，工作 O(N+WH+4H+K)，存储 O(201*4+WH)。重复点幂等。implementation_bitmask 以固定网格/完整输出换取旧稀疏排序与行复用；两者及教学源码均保留。

精确源码：Java 1.8 Accepted #11327417: 0.109 s / 440 KB。2026-11-20 保存的编译器组排名，时间然后内存：8/48; 1/48。严格收录采用低于 1024 KB 只看时间：前十或前 15%，同值共享名次，百分比向上取整。单独语言目标为两项第一，故保留星号。保留的旧版本有自己的配对指标 #11308715 (Java 1.8): 0.125 s / 476 KB，不混合测量或运行时。教学源码保持不变。

- `1944_implementation_bitmask.java`: 0.109 s / 440 KB; 保留教学版 `1944_implementation.java` (Java 1.8): 0.125 s / 844 KB.

`1944_implementation_sorting.rs`. 以互异点按 y 降、x 升排序，替代 W×H 绘图及完整输出缓冲。一次遍历输出坐标并推进点指针，先处理星号，再原点和轴。点用两个 i16，题定 [-100,100] 安全，边界始终含原点。O(n log n+WH) 时间、O(n) 空间，用排序换取不分配网格/整段输出。不同排序实现有独立文件名，保留简单网格版。

与 `1944_implementation.rs` 相比：时间 0.031 s → 0.015 s；内存 348 KB → 68 KB。

逐行绘制，不分配完整图。排序打包点坐标，使同一行的点相邻。先填背景及可见纵轴，需要时绘制横轴和原点，最后覆盖点，保持符号优先级和纵坐标递减顺序。复用行缓冲，空间取决于点数与行宽而非绘图面积。排序不能省去输出每格所需的时间。

- `1944_implementation_optimized.cpp`: 0.015 s / 116 KB; 基础版 `1944_implementation.cpp`: 0.015 s / 472 KB; 相对基础版的变化: 时间 -0.0%, 内存 -75.4%.
- `1944_implementation_optimized.java`: 0.125 s / 476 KB; 基础版 `1944_implementation.java`: 0.125 s / 844 KB; 相对基础版的变化: 时间 -0.0%, 内存 -43.6%.
- `1944_implementation_optimized.py`: 0.140 s / 332 KB; 基础版 `1944_implementation.py`: 0.093 s / 636 KB; 相对基础版的变化: 时间 +50.5%, 内存 -47.8%.

## 语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1944_implementation_sorting.rs`：没有足够可比的其他作者结果来证明排名；纳入依据为相对简单版本测得的改进。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1944_implementation.cpp](1944_implementation.cpp) | G++ 13.2 x64 | implementation | O(n+WH) | AC | 0.015 s | 472 KB | 11291904 |
| [1944_implementation.go](1944_implementation.go) | Go 1.14 x64 | implementation | O(n+WH) | AC | 0.031 s | 1420 KB | 11291906 |
| [1944_implementation.java](1944_implementation.java) | Java 1.8 | implementation | O(n+WH) | AC | 0.125 s | 844 KB | 11291912 |
| [1944_implementation.py](1944_implementation.py) | Python 3.12 x64 | implementation | O(n+WH) | AC | 0.093 s | 636 KB | 11291907 |
| [1944_implementation.rs](1944_implementation.rs) | Rust 1.75 x64 | implementation | O(n+WH) | AC | 0.031 s | 348 KB | 11291920 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1944_implementation_optimized.cpp](1944_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N log N+WH) | AC | 0.015 s | 116 KB | 11308709 |
| [1944_implementation_optimized.java](1944_implementation_optimized.java) | Java 1.8 | implementation | O(N log N+WH) | AC | 0.125 s | 476 KB | 11308715 |
| [1944_implementation_bitmask.java](1944_implementation_bitmask.java) \* | Java 1.8 | implementation, bitmask | O(N+WH+4H+K) time; fixed grid + O(WH) output | AC | 0.109 s | 440 KB | 11327417 |
| [1944_implementation_optimized.py](1944_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N log N+WH) | AC | 0.140 s | 332 KB | 11309399 |
| [1944_implementation_sorting.rs](1944_implementation_sorting.rs) \* | Rust 1.75 x64 | implementation, sorting | O(n log n+WH) time; O(n) space | AC | 0.015 s | 68 KB | 11325552 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
