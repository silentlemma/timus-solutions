# 1019. 直线多次重涂后最长的白色区间

[Timus 1019](https://acm.timus.ru/problem.aspx?space=1&num=1019) · 难度 465 · sorting, dsu

原题出自 Ural State University Internal Contest '99 #2。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

数轴上的线段 `[0, 10^9]` 为白色。随后依次进行 `N` 次重涂（`1 ≤ N ≤ 5000`）：第 `i` 次把从 `a_i` 到 `b_i`
（`0 < a_i < b_i < 10^9`，整数）的线段涂成白色或黑色。求结果中最长的白色区间；长度相同时取最左边的。

时间限制：2 秒。内存限制：64 MB。

## 输入

先是 `N`，然后 `N` 行 `a b c`，其中 `c` 为 `w`（白）或 `b`（黑）。

## 输出

最长白色区间的两端 `x y`（`x < y`）。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
4
2 999999998 b
100 500 w
500 900 w
300 310 b
```

输出：

```
310 900
```

### 样例 2

输入：

```
1
1 999999999 w
```

输出：

```
0 1000000000
```

## 解法

收集 0、10⁹ 及所有涂色端点，排序去重。相邻坐标之间颜色一致，按输入顺序直接涂这些段，再从左向右合并连续白段。比较实际坐标长度而非段数，仅在严格变长时更新，便保留最左的并列答案。至多 2N+1 段，排序 O(N log N) 后直接涂色耗时 O(N²)，空间 O(N)。N ≤ 5000 时至多 50005000 次段赋值。Python 用 bytearray 切片涂色，内部复制由原生代码执行，因此同一简单算法现已在五种语言全部通过。相接白段应合并，必须加入边界 0、10⁹；未被涂过的前缀 [0,min a) 保证白区间存在。

## 优化解法

DSU 版本逆序处理涂色。后继结构找到尚未被后续操作赋值的第一段，赋值后将其连接到下一段，每段最多涂一次。排序与端点查找共耗时 O(N log N)，空间 O(N)。Accepted 的 Go 源码使用 592 KB、0.031 秒，直接涂色为 1784 KB、0.031 秒，内存减少 66.8%。保留原有 Accepted C++、Python DSU。Python DSU 为 3560 KB、0.078 秒，新简单版本为 5 464 KB、0.093 秒。虽两项指标更差，仍保留更简单的算法用于教学。C++ DSU 使用 212 KB，直接版为 208 KB；0.031 到 0.015 秒只差一个计时刻度，因此快速集合的收录依据是保存的排名规则，不宣称已证明 30% 时间收益。

## 各语言说明

简单的直接涂色现已在五种语言全部获得 Accepted。DSU 是另一算法，使用独立文件名。新的 Go DSU 使用标准句柄和紧凑基本类型数组。保留全部旧文件及其历史 Accepted 指标。星号只标记选入快速集合但尚未达到该语言目标排名的源码。

逆序处理染色操作，用并查集跳过已经确定最终颜色的小段。通过的提交 11324217 用时 0.109 秒、占用 644 KB；简单版用时 0.203 秒、占用 3960 KB。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1019_sorting.cpp](1019_sorting.cpp) | G++ 13.2 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 208 KB | 11278218 |
| [1019_sorting.go](1019_sorting.go) | Go 1.14 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 1784 KB | 11278227 |
| [1019_sorting.java](1019_sorting.java) \* | Java 1.8 | sorting | O(N^2) after sorting | AC | 0.203 s | 3960 KB | 11278235 |
| [1019_sorting.py](1019_sorting.py) | Python 3.12 x64 | sorting | O(N²) after sorting | AC | 0.093 s | 5 464 KB | 11314812 |
| [1019_sorting.rs](1019_sorting.rs) \* | Rust 1.75 x64 | sorting | O(N^2) after sorting | AC | 0.046 s | 692 KB | 11278240 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1019_dsu_sorting.cpp](1019_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.015 s | 212 KB | 11278221 |
| [1019_dsu_sorting.go](1019_dsu_sorting.go) \* | Go 1.14 x64 | dsu, sorting | O(N log N) | AC | 0.031 s | 592 KB | 11314801 |
| [1019_dsu_sorting.py](1019_dsu_sorting.py) \* | Python 3.12 x64 | dsu, sorting | O(N log N) | AC | 0.078 s | 3560 KB | 11278231 |
| [1019_dsu_sorting.java](1019_dsu_sorting.java) | Java 1.8 | dsu, sorting | O(N log N) | AC | 0.109 s | 644 KB | 11324217 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
