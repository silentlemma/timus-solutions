# 1439. 与那个人的对决

[Timus 1439](https://acm.timus.ru/problem.aspx?space=1&num=1439) · 难度 428 · binary_search

原题作者 Alexander Klepinin 和 Stanislav Vasiliev，出自 2006 年 3 月 24–25 日第十届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

魔法部的房间编号为 1, 2, …, N（1 ≤ N ≤ 10⁹），编号始终连续：一个房间被摧毁时，
所有编号更大的房间编号都减一。按顺序给出 M ≤ 10⁵ 个事件，每个是 "D x"（当前编号
为 x 的房间被摧毁）或 "L x"（哈利看着当前编号为 x 的门）。最多摧毁 10⁴ 个房间。
对每个 "L" 事件，输出该房间最初的编号。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 M，然后是 M 个事件。

## 输出

最初的编号，每行一个。

## 样例

### 样例 1

输入:

```
20 7
L 5
D 5
L 4
L 5
D 5
L 4
L 5
```

输出:

```
5
4
6
4
7
```

## 解法

把被摧毁房间的原编号存入有序数组 g。当前编号为 x 的房间，原编号为 x + k，其中 k
是在它下面被摧毁的房间数。沿数组往上走，房间 g[j] 在它下面当且仅当
g[j] ≤ x + j，即 g[j] − j ≤ x；由于 g 中的编号互不相同，g[j] − j 不减，所以在它
下面的房间构成一个前缀，其长度 k 用二分查找求出。

对 "L" 输出 x + k。对 "D"，新的原编号 x + k 恰好放在数组的位置 k：之前的都更小，
之后的都更大，所以插入后数组仍然有序。设摧毁了 D 个房间，复杂度
`O(M log D + D²)`，每次插入最多移动 10⁴ 个数。

注意事项：

- 反复摧毁同一个门牌号，每次都会藏起一个新房间（测试 03、07、gen3）；
- 编号可达十亿，无法为每个房间开数组（测试 05、gen1）。

## 优化解法

C++ 修订版保留有序销毁编号向量上的二分查找，以及插入时的元素移动。各 16 KB 的固定输入、输出缓冲区替代格式化调用。复杂度仍为 O(M log D + D²) 时间、O(D) 存储，并未改用顺序统计树。

精确源代码的 Accepted（G++ 13.2 x64, #11326643: 0.031 s / 188 KB）；教学基础版 `1439_binary_search.cpp`: 0.156 s / 424 KB。此前优化版的测量为 0.156 s / 216 KB。在保存的 2026 年 11 月 20 日比较中，时间名次为 1/80，内存名次为 1/80；内存低于 1 MiB 时规则仅评估时间排名。

这些实现保留已删除房间的有序数组及前缀二分查找；插入仍需移动元素，因此时间仍为 O(M log D + D²)。改进在于紧凑存储和流式输入输出。C++ 使用 32 位原始编号 （N ≤ 10⁹ 足够）并预留最多 10000 次删除的容量。Go、Rust 使用有界输入输出缓冲；Rust 也使用 32 位编号及 C runtime 入口。Python 处理后即释放输入行，并保存输出字节，而非保留所有输入标记和输出整数。Python 空间为 O(D + 输出字节数)，其他新版本为 O(D) 加固定缓冲区。原有直接实现均保留。

通过评测的 Python 3.12 x64 版本耗时 0.437 秒，基础版为 0.421 秒，内存为 2 376 KB，基础版为 21004 KB。

通过评测的 Rust 1.75 x64 版本耗时 0.046 秒，基础版为 0.031 秒，内存为 96 KB，基础版为 4664 KB。

已通过评测的基础实现 [1439_binary_search.java](1439_binary_search.java) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1439_binary_search.cpp](1439_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(M log D + D^2) | AC | 0.156 s | 424 KB | 11286248 |
| [1439_binary_search.go](1439_binary_search.go) | Go 1.14 x64 | binary_search | O(M log D + D^2) | AC | 0.171 s | 5708 KB | 11286251 |
| [1439_binary_search.java](1439_binary_search.java) \* | Java 1.8 | binary_search | O(M log D + D^2) | AC | 0.171 s | 10132 KB | 11286253 |
| [1439_binary_search.py](1439_binary_search.py) | Python 3.12 x64 | binary_search | O(M log D + D^2) | AC | 0.421 s | 21004 KB | 11286252 |
| [1439_binary_search.rs](1439_binary_search.rs) | Rust 1.75 x64 | binary_search | O(M log D + D^2) | AC | 0.031 s | 4664 KB | 11286256 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1439_binary_search_optimized.cpp](1439_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O(M log D + D²) | AC | 0.031 s | 188 KB | 11326643 |
| [1439_binary_search_optimized.go](1439_binary_search_optimized.go) \* | Go 1.14 x64 | binary_search | O(M log D + D²) | AC | 0.031 s | 404 KB | 11314850 |
| [1439_binary_search_optimized.py](1439_binary_search_optimized.py) \* | Python 3.12 x64 | binary_search | O(M log D + D²) | AC | 0.437 s | 2376 KB | 11314854 |
| [1439_binary_search_optimized.rs](1439_binary_search_optimized.rs) \* | Rust 1.75 x64 | binary_search | O(M log D + D²) | AC | 0.046 s | 96 KB | 11314853 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
