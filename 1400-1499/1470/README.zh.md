# 1470. 不明飞行物

[Timus 1470](https://acm.timus.ru/problem.aspx?space=1&num=1470) · 难度 253 · fenwick

原题作者 Dmitry Zhukov，出自 2006 年 8 月彼得罗扎沃茨克夏季集训的乌拉尔国立大学与奥廖尔国立技术大学比赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个由 N × N × N 个单位扇区组成的立方体（1 ≤ N ≤ 128，坐标从 0 到 N − 1）开始时
是空的。记录每行一条。"1 x y z K" 把扇区 (x, y, z) 中的物体数改变 K
（−20000 ≤ K ≤ 20000）；任何扇区都不会变成负数。"2 x1 y1 z1 x2 y2 z2" 询问长方
体 x1 ≤ x ≤ x2、y1 ≤ y ≤ y2、z1 ≤ z ≤ z2 中有多少物体。"3" 结束输入。记录至多
100002 条。

时间限制：2 秒。内存限制：64 MB。

## 输入

N，然后是各条记录，最后一条是 "3"。

## 输出

每个询问的答案各占一行。

## 评测方式

精确比较完整输出，包括空格和换行。

## 样例

### 样例 1

输入:

```
2
2 1 1 1 1 1 1
1 0 0 0 1
1 0 1 0 3
2 0 0 0 0 0 0
2 0 0 0 0 1 0
1 0 1 0 -2
2 0 0 0 1 1 1
3
```

输出:

```
0
1
4
2
```

## 解法

树状数组可以推广到任意维：单元 (i, j, w) 保存一块扇区的和，这块扇区的下标结束于
i、j、w，长度分别等于它们的最低位。修改时 i 向上走，在其内部 j 和 w 也向上走；
求 [1, x] × [1, y] × [1, z] 的前缀和时三者都向下走。每条路径每个坐标轴至多 8 步，
所以一次修改或前缀求和至多访问 8³ 个单元。长方体的和由八个角的容斥得到，下侧的角要减一。
树占 (N + 1)³ 个 64 位单元，约 17 MB。每条记录 `O(log³ N)`。

注意事项：

- 坐标从 0 开始，而树状数组从 1 开始，所以每个下标都要加一（测试 03、04）；
- 所有扇区的物体总数可达 2·10⁹，八角公式的中间结果会超出 32 位，所以和要用 64
  位（gen4）；
- 询问可能出现在任何修改之前，修改量也可能为 0（测试 01、02）。

## 优化解法

保留三维 Fenwick 树，但节点和改存 32 位。扇区值非负，因此节点不超过合法总质量，后者小于有符号 32 位上限。前缀求和及容斥中间式仍使用足够宽的算术。更新范围与查询符号不变，只减少树存储。Python 还逐条读取操作，不保存全部输入词元和答案。

- `1470_fenwick_optimized.cpp`: 0.359 s / 8144 KB; 基础版 `1470_fenwick.cpp`: 0.375 s / 16552 KB; 相对基础版的变化: 时间 -4.3%, 内存 -50.8%.
- `1470_fenwick_optimized.go`: 0.140 s / 10320 KB; 基础版 `1470_fenwick.go`: 0.156 s / 20044 KB; 相对基础版的变化: 时间 -10.3%, 内存 -48.5%.
- `1470_fenwick_optimized.java`: 0.187 s / 12064 KB; 基础版 `1470_fenwick.java`: 0.281 s / 20908 KB; 相对基础版的变化: 时间 -33.5%, 内存 -42.3%.
- `1470_fenwick_optimized.py`: 0.734 s / 16836 KB; 基础版 `1470_fenwick.py`: 0.890 s / 61120 KB; 相对基础版的变化: 时间 -17.5%, 内存 -72.5%.
- `1470_fenwick_optimized.rs`: 0.046 s / 11476 KB; 基础版 `1470_fenwick.rs`: 0.125 s / 19804 KB; 相对基础版的变化: 时间 -63.2%, 内存 -42.1%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1470_fenwick.cpp`; 覆盖实现 `1470_fenwick_optimized.cpp`; 时间/内存名次 60/1, 其他作者记录 89/89.

- Go: 优先教学基础版 `1470_fenwick.go`; 覆盖实现 `1470_fenwick.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1470_fenwick.java`; 覆盖实现 `1470_fenwick_optimized.java`; 时间/内存名次 1/1, 其他作者记录 3/3.

- Python/PyPy: 优先教学基础版 `1470_fenwick.py`; 覆盖实现 `1470_fenwick_optimized.py`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Rust: 优先教学基础版 `1470_fenwick.rs`; 覆盖实现 `1470_fenwick_optimized.rs`; 时间/内存名次 1/1, 其他作者记录 2/2.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1470_fenwick.cpp](1470_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(log^3 N) per record | AC | 0.375 s | 16552 KB | 11286549 |
| [1470_fenwick.go](1470_fenwick.go) | Go 1.14 x64 | fenwick | O(log^3 N) per record | AC | 0.156 s | 20044 KB | 11286550 |
| [1470_fenwick.java](1470_fenwick.java) | Java 1.8 | fenwick | O(log^3 N) per record | AC | 0.281 s | 20908 KB | 11286552 |
| [1470_fenwick.py](1470_fenwick.py) | PyPy 3.10 x64 | fenwick | O(log^3 N) per record | AC | 0.890 s | 61120 KB | 11286551 |
| [1470_fenwick.rs](1470_fenwick.rs) | Rust 1.75 x64 | fenwick | O(log^3 N) per record | AC | 0.125 s | 19804 KB | 11286553 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1470_fenwick_optimized.cpp](1470_fenwick_optimized.cpp) \* | G++ 13.2 x64 | fenwick | O(log^3 N) per operation | AC | 0.359 s | 8144 KB | 11308809 |
| [1470_fenwick_optimized.go](1470_fenwick_optimized.go) | Go 1.14 x64 | fenwick | O(log^3 N) per operation | AC | 0.140 s | 10320 KB | 11308810 |
| [1470_fenwick_optimized.java](1470_fenwick_optimized.java) | Java 1.8 | fenwick | O(log^3 N) per operation | AC | 0.187 s | 12064 KB | 11308811 |
| [1470_fenwick_optimized.py](1470_fenwick_optimized.py) | PyPy 3.10 x64 | fenwick | O(log^3 N) per operation | AC | 0.734 s | 16836 KB | 11308813 |
| [1470_fenwick_optimized.rs](1470_fenwick_optimized.rs) | Rust 1.75 x64 | fenwick | O(log^3 N) per operation | AC | 0.046 s | 11476 KB | 11308812 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
