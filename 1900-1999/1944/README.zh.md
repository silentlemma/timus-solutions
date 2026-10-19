# 1944. 点优先的ASCII坐标图

[Timus 1944](https://acm.timus.ru/problem.aspx?space=1&num=1944) · difficulty 239 · implementation

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

完整图形按行列精确比较，空格不能代替背景点。每行以换行结束。

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

## 各语言说明

Python用bytearray，Go用字节切片，C++用string，Java用char数组，
Rust用字节向量。Java追加整行字符内容，不是数组对象表示。所有
符号均为ASCII；直接输出已有末尾换行的图，避免额外空行。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1944_implementation.cpp](1944_implementation.cpp) | G++ 13.2 x64 | implementation | O(n+WH) | AC | 0.015 s | 472 KB |
| [1944_implementation.go](1944_implementation.go) | Go 1.14 x64 | implementation | O(n+WH) | AC | 0.031 s | 1420 KB |
| [1944_implementation.java](1944_implementation.java) | Java 1.8 | implementation | O(n+WH) | AC | 0.125 s | 844 KB |
| [1944_implementation.py](1944_implementation.py) | Python 3.12 x64 | implementation | O(n+WH) | AC | 0.093 s | 636 KB |
| [1944_implementation.rs](1944_implementation.rs) | Rust 1.75 x64 | implementation | O(n+WH) | AC | 0.031 s | 348 KB |
