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

逐行绘制，不分配完整图。排序打包点坐标，使同一行的点相邻。先填背景及可见纵轴，需要时绘制横轴和原点，最后覆盖点，保持符号优先级和纵坐标递减顺序。复用行缓冲，空间取决于点数与行宽而非绘图面积。排序不能省去输出每格所需的时间。

- `1944_implementation_optimized.cpp`: 0.015 s / 116 KB; 基础版 `1944_implementation.cpp`: 0.015 s / 472 KB; 相对基础版的变化: 时间 -0.0%, 内存 -75.4%.
- `1944_implementation_optimized.java`: 0.125 s / 476 KB; 基础版 `1944_implementation.java`: 0.125 s / 844 KB; 相对基础版的变化: 时间 -0.0%, 内存 -43.6%.
- `1944_implementation_optimized.py`: 0.140 s / 332 KB; 基础版 `1944_implementation.py`: 0.093 s / 636 KB; 相对基础版的变化: 时间 +50.5%, 内存 -47.8%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1944_implementation.cpp`; 覆盖实现 `1944_implementation_optimized.cpp`; 时间/内存名次 1/1, 其他作者记录 50/50.

- Go: 优先教学基础版 `1944_implementation.go`; 覆盖实现 `1944_implementation.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1944_implementation.java`; 覆盖实现 `1944_implementation.java`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Python/PyPy: 优先教学基础版 `1944_implementation.py`; 覆盖实现 `1944_implementation_optimized.py`; 时间/内存名次 11/1, 其他作者记录 11/11.

- Rust: 优先教学基础版 `1944_implementation.rs`; 覆盖实现 `1944_implementation.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

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
| [1944_implementation_optimized.py](1944_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N log N+WH) | AC | 0.140 s | 332 KB | 11309399 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
