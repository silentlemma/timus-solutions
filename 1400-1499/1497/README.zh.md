# 1497. 切割正方形

[Timus 1497](https://acm.timus.ru/problem.aspx?space=1&num=1497) · 难度 304 · implementation

原题作者 Alexander Toropov，出自 2006 年 10 月 14 日第十三届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一张 N × N 的方格纸（3 ≤ N ≤ 1000）被切成黑块（格子 1）和白块（格子 0），两块都
按边连通。两块拼在一起放在桌上。能否在不让任何一块离开桌面的情况下，把其中一块移
到离另一块很远的地方？输出 "Yes" 或 "No"。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，然后是 N 行，每行 N 个字符 0 或 1。

## 输出

"Yes" 或 "No"。

## 样例

### 样例 1

输入:

```
5
10001
10001
10001
11111
11111
```

输出:

```
Yes
```

### 样例 2

输入:

```
5
11011
11011
10001
11111
11111
```

输出:

```
No
```

## 解法

移开一块等于把另一块朝相反方向移开，所以只需移动黑块。若没有任何一列中白格位于黑
格上方，黑块就能直接向上滑出；向下、向左、向右同理。斜向滑动不会带来新的可能：两
块之间的每条边都必须背离运动方向，这样组成该斜向的两个轴向滑动也都畅通。所以只需
检查四个方向，每个方向扫描一遍。`O(N²)`。

注意事项：

- 被另一块包围的一块永远出不来（测试 03、gen2）；
- 只要有一个钩子，哪怕只有一格长，两块就会卡住（测试 05、07、gen4）；
- 阶梯形切口虽然边朝向两个方向，仍能沿某条轴滑开（测试 04、gen1）。

## 优化解法

`1497_implementation_optimized.cpp`. 保留四个单调方向标志。SSE2 每次比较十六个单元并将行块转为位掩码；移位检测水平变化，进位连接相邻块，上一行掩码检测垂直变化。末尾不足十六位的块被屏蔽，行数组增加填充，所有向量读取均在数组内。x64 目标包含 SSE2，无需 AVX。16 KiB 输入缓冲替代逐字符标准输入。时间 O(N²)，辅助空间 O(N)，保留提前否定。

精确源代码 Accepted #11326995：0.015 s / 92 KB。2026-11-20 保存的 G++ 13.2 样本：时间排名 1/46，内存排名 1/46。教学源代码保留。

C++ 和 Go 一趟检查四个方向。横向相邻格颜色不同时，该轴上只允许黑块远离白块的方向。纵向相邻格以同样方式限制另一轴。保留四个标志，全部失效即可停止。只需保存上一行和当前行，空间 O(N)。

保留的已接受基础实现 [1497_implementation.go](1497_implementation.go), [1497_implementation.java](1497_implementation.java), [1497_implementation.py](1497_implementation.py), [1497_implementation.rs](1497_implementation.rs) 在保存的比较中满足严格快速版本收录：所需指标前十名或前 15%。直接复用，不创建相同副本；其他教学源代码保留。星号表示单独的语言排名目标。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1497_implementation.cpp](1497_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.031 s | 868 KB | 11287233 |
| [1497_implementation.go](1497_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.046 s | 2192 KB | 11287234 |
| [1497_implementation.java](1497_implementation.java) \* | Java 1.8 | implementation | O(N^2) | AC | 0.109 s | 2952 KB | 11287236 |
| [1497_implementation.py](1497_implementation.py) \* | Python 3.12 x64 | implementation | O(N^2) | AC | 0.109 s | 4276 KB | 11287235 |
| [1497_implementation.rs](1497_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.031 s | 2116 KB | 11287237 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1497_implementation_optimized.cpp](1497_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N²) | AC | 0.015 s | 92 KB | 11326995 |
| [1497_implementation_optimized.go](1497_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(N²) | AC | 0.031 s | 904 KB | 11310460 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
