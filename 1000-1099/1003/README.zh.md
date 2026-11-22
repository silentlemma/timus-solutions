# 1003. 第一个矛盾的奇偶性回答

[Timus 1003](https://acm.timus.ru/problem.aspx?space=1&num=1003) · 难度 385 · dsu, hashing

原题出自 1999 年中欧信息学奥林匹克竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有一个未知的长度为 `L` 的比特序列（`L ≤ 10^9`）。依次给出 `q ≤ 5000` 条陈述；第 `i` 条陈述
说明第 `l..r` 位（从 1 开始编号，`l ≤ r`）中 1 的个数是偶数还是奇数。

求最大的 `X`，使得存在某个比特序列满足前 `X` 条陈述。如果所有陈述可以同时成立，则
`X = q`。

输入包含多组这样的测试。

时间限制：2 秒。内存限制：64 MB。

## 输入

各组测试依次给出。每组测试为：一行 `L`，一行 `q`，以及 `q` 行形如 `l r even` 或 `l r odd`
的陈述。以一行 `-1` 结束输入。

## 输出

每组测试输出一行，即 `X`。

## 评测方式

按记号逐一比较输出，多余的空白字符不影响结果。

## 样例

### 样例 1

输入：

```
6
3
1 2 odd
3 4 even
1 4 even
-1
```

输出：

```
2
```

### 样例 2

输入：

```
8
4
1 8 even
1 4 odd
5 8 odd
2 3 even
3
2
1 3 odd
1 3 even
-1
```

输出：

```
4
1
```

## 题解

设 `P(k)` 为前 `k` 位中 1 的个数的奇偶性，`P(0) = 0`。关于区间 `l..r` 的陈述等价于
`P(l-1) xor P(r) = 0`（偶数）或 `1`（奇数）。反过来，任意满足 `P(0) = 0` 的 `P` 值恰好对应
一个比特序列。因此这些陈述相容，当且仅当方程组 `P(a) xor P(b) = w` 有解。

按顺序处理陈述，在前缀位置上维护并查集，并为每个结点额外记录它相对于父结点的奇偶性。
`find` 返回根以及该结点相对于根的奇偶性。对于新方程：如果两端在同一集合中，方程必须与已知的
奇偶性一致；否则用新边上正确的奇偶性合并两个集合。第一个不一致的方程给出 `X`。

位置最大到 `10^9`，但出现的位置最多 `2q` 个：用哈希表把它们映射为连续编号。使用路径压缩和按秩
合并，每组测试的复杂度为 `O(q · α(q))`；Python 未按秩合并，为 `O(q log q)`。

注意事项：

- 方程连接的是前缀 `l-1` 和 `r`，而不是 `l` 和 `r`；
- 出现第一个矛盾之后，仍需读完该组测试的剩余输入；
- 一组测试可能没有任何陈述。

## 优化解法

`1003_dsu_hashing_optimized.py`. 保留精确前缀奇偶 DSU、按需坐标编号和迭代奇偶路径折半。父节点与边奇偶仍编码为 2*parent+parity，但 Python 改用原生列表替代短整数数组，避免逐次取值转换；秩仍为 bytearray。输入顺序、首个矛盾和剩余语句消费均不变。DSU/哈希期望 O(Q α(Q)) 加输入，状态 O(Q)，逐行读取。

精确源代码 CPython 3.12 Accepted #11326679：0.062 s / 1040 KB。2026-11-20 保存的当前语言族编译器组比较：时间排名 3/35，内存排名 1/35。至少 1024 KB：两个严格指标均须通过，两项已通过。

- `1003_dsu_hashing_optimized.py`: 0.062 s / 1040 KB; 保留的教学基础版 `1003_dsu_hashing.py` (Python 3.12 x64): 0.093 s / 4388 KB; 时间变化 -33.3%; 内存变化 -76.3%.

两种版本都联合编码父节点与边奇偶性；C++ 使用 16 位条目，当前 Python 则用普通整数列表而非 16 位存储数组；最低位保存奇偶性。C++ 先排序并去重所有前缀位置，再二分查找编号。Python 通过哈希表按需分配编号，遍历时把访问到的节点连到祖父，并合并两条边的奇偶性。方程按输入顺序检查。

保留的 Accepted 基础版 [1003_dsu_hashing.cpp](1003_dsu_hashing.cpp), [1003_dsu_hashing.go](1003_dsu_hashing.go), [1003_dsu_hashing.java](1003_dsu_hashing.java), [1003_dsu_hashing.rs](1003_dsu_hashing.rs) 在保存比较中也通过所需指标的严格前十或前 15% 标准，直接复用而不复制源文件。保留其余教学版；星号表示单独的语言排名目标。

## 各语言说明

以下说明针对基础实现。

- **C++**：用 `std::unordered_map<int, int>` 编号；递归 `find` 没有问题，按秩合并保证树很浅。
- **Go**：`map[int]int` 配合带路径压缩的递归 `find`。
- **Python**：迭代实现 `find`，压缩路径并重新计算路径上结点的奇偶性。
- **Java**：每组测试使用大小为 `2q` 的数组，用 `HashMap<Integer, Integer>` 编号，迭代 `find`。
- **Rust**：`HashMap<i64, usize>` 配合 `entry().or_insert_with()` 创建结点；迭代 `find`。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1003_dsu_hashing.cpp](1003_dsu_hashing.cpp) | G++ 13.2 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.015 s | 632 KB | 11277428 |
| [1003_dsu_hashing.go](1003_dsu_hashing.go) \* | Go 1.14 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.046 s | 3420 KB | 11277429 |
| [1003_dsu_hashing.java](1003_dsu_hashing.java) \* | Java 1.8 | dsu, hashing | O(q·α(q)) per test | AC | 0.109 s | 4788 KB | 11277431 |
| [1003_dsu_hashing.py](1003_dsu_hashing.py) | Python 3.12 x64 | dsu, hashing | O(q log q) per test | AC | 0.093 s | 4388 KB | 11277430 |
| [1003_dsu_hashing.rs](1003_dsu_hashing.rs) \* | Rust 1.75 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.001 s | 1268 KB | 11277432 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1003_dsu_sorting.cpp](1003_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(q log q) per test | AC | 0.015 s | 184 KB | 11310464 |
| [1003_dsu_hashing_optimized.py](1003_dsu_hashing_optimized.py) \* | Python 3.12 x64 | dsu, hashing | O(q·α(q)) expected per test | AC | 0.062 s | 1040 KB | 11326679 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
