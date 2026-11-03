# 1656. 远方王国的军队

[Timus 1656](https://acm.timus.ru/problem.aspx?space=1&num=1656) · 难度 206 · constructive

原题作者 Vladimir Yakovlev（创意来自 Magaz Asanov），出自 NEERC 2008 东部分区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把 n² 名给定身高的士兵排成 n × n 的方阵，使每一行、每一列最高的人站在中间，从中间到两端身高都不增加。

## 输入

奇数 n（3 到 9），然后是 n² 个 170 到 200 的身高。

## 输出

方阵，n 行，每行 n 个身高。任何合法排列都被接受。

## 评测方式

检查尺寸、原身高多重集及全部向外单调不等式，接受任意合法网格。

## 样例

### 样例 1

输入：

```
3
170
170
180
175
170
175
175
170
175
```

输出：

```
170 175 170
175 180 175
170 175 170
```

## 解法

按格子到中心行和中心列距离的二元组（较小者，较大者）给格子排序，把最高的士兵分给排名最靠前的格子。
在距中心为 a 的一行中，距离为 b 的格子排名在 b < a 时为 (b, a)，之后为 (a, b)：无论哪种情况排名都随 b
增大而增大，所以在中间两侧身高都向外不增加。列由对称性同理。排名相同的格子互为镜像，不会位于同一条线的
同一侧。`O(n² log n)`；Go 的稳定排序：`O(n² log² n)`。

易错点：

- “向两端不增加”允许身高相等（测试 02）；
- 合法排列很多，所以检查器验证规则和身高集合。

程序给出的方阵在 90 支随机军队上都能通过检查器。

## 优化解法

统计有界身高值，避免排序坐标元组。离中心曼哈顿距离较小的格子获得不小的身高；沿行列向外每步都增加距离，故满足限制。每格填一次，相等身高允许。Python 将身高计数展开为字节数组，利用距离层前缀偏移逐行输出，不保存完整网格。保留简单坐标排序构造。

- `1656_constructive_optimized.cpp`: 0.001 s / 108 KB; 基础版 `1656_constructive.cpp`: 0.001 s / 180 KB; 相对基础版的变化: 时间 -0.0%, 内存 -40.0%.
- `1656_constructive_optimized.java`: 0.078 s / 472 KB; 基础版 `1656_constructive.java`: 0.156 s / 4188 KB; 相对基础版的变化: 时间 -50.0%, 内存 -88.7%.
- `1656_constructive_optimized.py`: 0.109 s / 268 KB; 基础版 `1656_constructive.py`: 0.046 s / 436 KB; 相对基础版的变化: 时间 +137.0%, 内存 -38.5%.

## 语言说明

使用 2026 年 11 月 1–2 日保存的快照。C++ 要求时间和内存同时进入前 15% 或前 10 名；其他语言族要求两项均第一。相同结果共享名次，无竞争记录的样本只表示形式覆盖。

- C++: 优先教学基础版 `1656_constructive.cpp`; 覆盖实现 `1656_constructive.cpp`; 时间/内存名次 1/1, 其他作者记录 48/48.

- Go: 优先教学基础版 `1656_constructive.go`; 覆盖实现 `1656_constructive.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 优先教学基础版 `1656_constructive.java`; 覆盖实现 `1656_constructive_optimized.java`; 时间/内存名次 1/1, 其他作者记录 2/2.

- Python/PyPy: 优先教学基础版 `1656_constructive.py`; 覆盖实现 `1656_constructive_optimized.py`; 时间/内存名次 9/2, 其他作者记录 13/13.

- Rust: 优先教学基础版 `1656_constructive.rs`; 覆盖实现 `1656_constructive.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

简单表包含优先教学源码和保留的 Accepted 替代实现。各语言族的优先基础版见语言说明。

### 简单版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1656_constructive.cpp](1656_constructive.cpp) | G++ 13.2 x64 | constructive | O(n² log n) | AC | 0.001 s | 180 KB | 11308831 |
| [1656_constructive.go](1656_constructive.go) | Go 1.14 x64 | constructive | O(n² log² n) | AC | 0.031 s | 1152 KB | 11288581 |
| [1656_constructive.java](1656_constructive.java) | Java 1.8 | constructive | O(n² log n) | AC | 0.156 s | 4188 KB | 11288583 |
| [1656_constructive.py](1656_constructive.py) | Python 3.12 x64 | constructive | O(n² log n) | AC | 0.046 s | 436 KB | 11308832 |
| [1656_constructive.rs](1656_constructive.rs) | Rust 1.75 x64 | constructive | O(n² log n) | AC | 0.031 s | 220 KB | 11308833 |

### 优化版本

| 解法 | 语言 | 方法 | 复杂度 | 结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1656_constructive_optimized.cpp](1656_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N^2+H) | AC | 0.001 s | 108 KB | 11308068 |
| [1656_constructive_optimized.java](1656_constructive_optimized.java) | Java 1.8 | constructive | O(N^2+H) | AC | 0.078 s | 472 KB | 11308073 |
| [1656_constructive_optimized.py](1656_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(N^2+H) time, O(N^2+H+N) compact bytes/counts; H31 | AC | 0.109 s | 268 KB | 11309461 |

\* Accepted；尚未达到排名目标，此实现仍可继续优化。
