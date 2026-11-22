# 1424. 小巴

[Timus 1424](https://acm.timus.ru/problem.aspx?space=1&num=1424) · 难度 697 · greedy

原题作者 Dmitry Kovalioff、Ilya Grebnov 与 Nikita Rybak（创意来自 Sergey Sofronov），出自 Timus Top Coders: First Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一辆有 M 个座位（M ≤ 1000）的小巴从 1 号站开到 N 号站（N ≤ 100 000），只跑一
趟。K 个人（K ≤ 50 000）想乘车，第 i 人从 S[i] 站到 F[i] 站，不论远近都付 P。司
机可以拒绝任何人。输出最大利润以及应搭载的人的编号，顺序任意；任何最优方案都可
以。

时间限制：1 秒。内存限制：64 MB。

## 输入

N、M、K 和 P，然后 K 行 S F。

## 输出

利润，然后是要搭载的人。

## 样例

### 样例 1

输入:

```
6 2 6 9
1 4
2 6
1 5
2 3
4 6
3 6
```

输出:

```
36
1 5 6 4
```

## 解法

每位乘客付钱相同，所以要在车上同时不超过 M 人的前提下尽量多载人；在某站空出的座
位可以在同一站被占用。按顺序经过各站。在每一站，行程在此结束的人下车，在此等候
的人全部上车，只要车上多于 M 人，就拒绝去得最远的那位，当作从未搭载。

拒绝最远的乘客是安全的：在某站之后车上的人中，任何最优方案都至少要放弃超出的那
么多人；把被保留的长行程换成被拒绝的短行程，绝不会让后面的站更拥挤，因为短行程
先结束。按终点站排序的大顶堆找出最远的乘客，按终点站统计的已搭载人数维护车上人
数。`O(N + K log K)`。

注意事项：

- 行程是半开区间：在某站下车的人把座位让给在该站上车的人（测试 05）；
- 没有人时答案是 0 和一个空列表（测试 02）；
- 多人可能想走完全相同的行程（测试 04、gen3）。

## 优化解法

`1424_sorting_greedy_optimized.cpp`. 保留按终点递增的贪心座位分配。用平坦有序数组保存各座位最后一次行程的终点。upper_bound 找到出发时可用且最近释放的座位；接纳行程时 memmove 删除该项，并将新终点追加在末尾，因为终点按顺序处理。保留树版本 1424_sorting_greedy.cpp 及其自身 Accepted 指标。M≤1000 时连续移动实测更快且更省空间，虽然每次接纳行程需 O(M)。最坏时间 O(N+M+KM)，空间 O(N+M+K)，另加固定 I/O 缓冲；树版本仍为 O(N+M+K log M)。

精确源代码 Accepted #11326980：0.015 s / 920 KB。2026-11-20 保存的 G++ 13.2 比较：时间排名 1/43，内存排名 3/43。

按终点站递增处理行程。每次分配一个在上车时已经空出的座位，优先选择最近才空出的座位。

用紧凑数组按上车站对行程分组。堆键同时保存终点站和乘客编号，座位不足时移除终点最远的行程。

**优化版本的 Timus 提交记录**

`1424_sorting_greedy_optimized.cpp` (G++ 13.2 x64) №11326980 · `1424_sorting_greedy.cpp` (G++ 13.2 x64) №11317526 · `1424_greedy_optimized.go` (Go 1.14 x64) №11317540 · `1424_greedy_optimized.java` (Java 1.8) №11317543 · `1424_greedy_optimized.py` (Python 3.12 x64) №11317528 · `1424_greedy_optimized.rs` (Rust 1.75 x64) №11317532.

**简单版本的 Timus 提交记录**

G++ 13.2 x64 №11322134 · Go 1.14 x64 №11322135 · Java 1.8 №11322136 · Python 3.12 x64 №11322137 · Rust 1.75 x64 №11322139.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1424_greedy.cpp](1424_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + K log K) | AC | 0.078 s | 4772 KB | 11322134 |
| [1424_greedy.go](1424_greedy.go) | Go 1.14 x64 | greedy | O(N + K log K) | AC | 0.109 s | 12396 KB | 11322135 |
| [1424_greedy.java](1424_greedy.java) | Java 1.8 | greedy | O(N + K log K) | AC | 0.218 s | 13936 KB | 11322136 |
| [1424_greedy.py](1424_greedy.py) | Python 3.12 x64 | greedy | O(N + K log K) | AC | 0.203 s | 30052 KB | 11322137 |
| [1424_greedy.rs](1424_greedy.rs) | Rust 1.75 x64 | greedy | O(N + K log K) | AC | 0.046 s | 10368 KB | 11322139 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|----|----|----|-----|------|----|----|---|
| [1424_sorting_greedy_optimized.cpp](1424_sorting_greedy_optimized.cpp) | G++ 13.2 x64 | sorting, greedy | O(N+M+KM) time; O(N+M+K) space | AC | 0.015 s | 920 KB | 11326980 |
| [1424_sorting_greedy.cpp](1424_sorting_greedy.cpp) \* | G++ 13.2 x64 | sorting, greedy | O(N + M + K log M) | AC | 0.078 s | 1032 KB | 11317526 |
| [1424_greedy_optimized.py](1424_greedy_optimized.py) | Python 3.12 x64 | greedy | O(N + K log K) | AC | 0.203 s | 3804 KB | 11317528 |
| [1424_greedy_optimized.rs](1424_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N + K log K) | AC | 0.046 s | 1752 KB | 11317532 |
| [1424_greedy_optimized.go](1424_greedy_optimized.go) | Go 1.14 x64 | greedy | O(N + K log K) | AC | 0.031 s | 3916 KB | 11317540 |
| [1424_greedy_optimized.java](1424_greedy_optimized.java) | Java 1.8 | greedy | O(N + K log K) | AC | 0.14 s | 4604 KB | 11317543 |

\* 带星号的解法尚未达到目标排名，仍可优化。
