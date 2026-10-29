# 1319. 旅馆

[Timus 1319](https://acm.timus.ru/problem.aspx?space=1&num=1319) · 难度 39 · implementation, math

原题作者 Stanislav Vasiliev，出自 2004 年 3 月 11–16 日在叶卡捷琳堡举行的第八届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

旅馆的信件架是一个 N × N 的格子块（1 ≤ N ≤ 100），沿对角线编号：1 号在右上角，每条对角线从上往下编号，
各条对角线依次向左下角推进，左下角是 N²。输出编好号的表格。

时间限制：1 秒。内存限制：64 MB。

## 输入

整数 N。

## 输出

N 行，每行 N 个用空格分隔的数。

## 样例

### 样例 1

输入：

```
3
```

输出：

```
4 2 1
7 5 3
9 8 6
```

## 解法

同一条对角线上的格子，列号 − 行号相同。让这个差从 N − 1 递减到 −(N − 1)，每条对角线内按行从上到下，
得到的正是编号顺序。`O(N²)`。

注意事项：

- 第一条对角线是右上角的单个格子，不是主对角线（测试 01）；
- N = 1 时只有一个格子，写 1（测试 02）。

## 优化解法

**公式**（C++、Java、Rust）。不保存表格：每个格子里的数根据它的位置直接算出，每
一行算好就输出。第 `r` 行第 `c` 列的格子所在的对角线有 `len = N − |c − r|` 个格
子。在主对角线上或其上方（`c ≥ r`），它之前的对角线共有
`1 + 2 + … + (len − 1) = len·(len − 1)/2` 个数，而该格子是本对角线上的第 `r + 1`
个，所以其中的数是 `len·(len − 1)/2 + r + 1`。在主对角线下方则从末尾倒数：后面的
对角线和本对角线剩下的部分给出 `N² − len·(len + 1)/2 + c + 1`。Java 和 Rust 还逐
字节读取 `N`。Java 为 0.062 s，而不是 0.093 s；508 KB，而不是 2008 KB。C++ 和
Rust 时间不变，内存更少：124 KB，而不是 244 KB；200 KB，而不是 364 KB。

Python 也实现了这个公式，每行一算出就输出：296 KB，而不是 888 KB，但时间从
0.046 s 增加到 0.078 s。

## 各语言说明

- 简单解法都以同样的方式填表，最后输出。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1319_implementation.cpp](1319_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.015 s | 244 KB | 11284938 |
| [1319_implementation.go](1319_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.001 s | 1188 KB | 11284939 |
| [1319_implementation.java](1319_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.093 s | 2008 KB | 11284941 |
| [1319_implementation.py](1319_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.046 s | 888 KB | 11284940 |
| [1319_implementation.rs](1319_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.001 s | 364 KB | 11284942 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1319_math.cpp](1319_math.cpp) | G++ 13.2 x64 | math | O(N^2) | AC | 0.001 s | 124 KB | 11303594 |
| [1319_math.java](1319_math.java) | Java 1.8 | math | O(N^2) | AC | 0.062 s | 508 KB | 11303596 |
| [1319_math.py](1319_math.py) \* | Python 3.12 x64 | math | O(N^2) | AC | 0.078 s | 296 KB | 11303740 |
| [1319_math.rs](1319_math.rs) | Rust 1.75 x64 | math | O(N^2) | AC | 0.001 s | 200 KB | 11303597 |

\* 未进入当前评测机上该语言解法的前 10 名或前 15%，可能还能进一步优化。
