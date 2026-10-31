# 1604. 在傻瓜国

[Timus 1604](https://acm.timus.ru/problem.aspx?space=1&num=1604) · 难度 139 · greedy

原题作者 Alexander Ipatov（创意来自 Alexander Toropov），出自 2008 年 3 月 1 日第九届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 k 种限速牌，第 i 种有 nᵢ 块，总数不超过 10000。要把它们全部沿公路摆放，使司机尽可能多地改变车速：
第一块牌以及每块与前一块不同的牌处都会改变车速。任何最优顺序都可接受。

时间限制：1 秒。内存限制：64 MB。

## 输入

k，然后是 n₁, …, nₖ，其中 1 ≤ k ≤ 10000，每个 nᵢ 都是正整数，总和不超过 10000。

## 输出

按公路顺序给出各块牌的种类。

## 样例

### 样例 1

输入:

```
2
2 2
```

输出:

```
1 2 1 2
```

## 解法

尽可能多地改变车速，就是让相邻相同的牌尽可能少。设最大数量为 m，总数为 n。其余 n − m 块牌最多把最常见种类的
m 块牌分成 n − m + 1 组，所以相邻相同的对数至少为 max(0, 2m − n − 1)。

贪心顺序能达到这个下界：总是放剩余最多的种类，除非它就是前一块牌，那时放剩余第二多的种类。用堆可以在
`O(log k)` 内取出这两者，整个顺序需要 `O(n log k)`。

测试使用检查器，统计相邻相同的对数并与下界比较。下界本身已在小规模的牌集合上与枚举所有顺序的结果对照。

注意事项：

- 当且仅当 2m > n + 1 时，相邻相同无法避免，贪心会把它们集中放在末尾（测试 05）；
  在 2m = n + 1 时仍可避免相邻相同（测试 02 和 04）；
- 每次都取最常见的种类而不看前一块牌，会造成重复；而不看数量轮流取各种类，可能过早用完其他种类（测试 07）。

## 优化解法

优化的 C++ 解法把种类和它的剩余数量压进一个 `int`：数量·2¹⁴ + 种类。两者都不超
过 10000，小于 2¹⁴ = 16384，所以两个字段不会重叠，比较压缩后的数就是先比数量、再
比种类，与比较二元组相同。堆是一个容纳 10000 个这种数的固定数组，用
`std::push_heap` 和 `std::pop_heap` 维护，而不是由二元组组成的
`priority_queue`；种类选出后立即用 `printf` 输出，而不是先拼进字符串：
{1604_greedy_optimized.cpp}。

优化的 Go 解法在预留了 k 个位置的切片上自己实现堆，而不是用 `container/heap`，后
者会把每块压入和弹出的牌转换成 `interface{}` 值并为它分配内存。数字从
`bufio.Reader` 中逐字节解析，而不是用 `fmt.Fscan`：{1604_greedy_optimized.go}。

优化的 Java 解法传给 `PriorityQueue` 的是普通的 `Comparator` 类，而不是 lambda；
lambda 第一次使用时会加载运行时的额外机制。放置一个种类时，它的数组本来就已从堆
中取出，所以解法直接在这个数组里减少计数再放回去，而不是每块牌新建一个数组。种类
通过 `BufferedWriter` 输出，而不是 `StringBuilder`：
{1604_greedy_optimized.java}。

优化的 Python 解法把堆元素 (−数量, 种类) 压成一个整数 −数量·(k + 1) + 种类，而不
是元组：种类在 1 到 k 之间，小于基数 k + 1，所以这些整数的比较结果与元组完全相
同，`divmod` 可以还原两个字段。它按字节读入，在主循环之前释放词元列表，并以每
256 个为一批输出种类，而不是把整个顺序留在内存中：{1604_greedy_optimized.py}。

优化的 Rust 解法每放置一个种类就通过 `BufWriter` 写出，而不是把多达 10000 个字符
串收集到 `Vec` 中再拼接成另一个字符串：{1604_greedy_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1604_greedy_optimized.cpp`: 时间降低 +0.00%; 内存降低 +49.32%; 基础版本: `1604_greedy.cpp`.

- `1604_greedy_optimized.go`: 时间降低 +51.61%; 内存降低 +49.27%; 基础版本: `1604_greedy.go`.

- `1604_greedy_optimized.java`: 时间降低 +19.87%; 内存降低 +64.35%; 基础版本: `1604_greedy.java`.

- `1604_greedy_optimized.py`: 时间降低 +0.00%; 内存降低 +42.12%; 基础版本: `1604_greedy.py`.

- `1604_greedy_optimized.rs`: 时间降低 -313.33%; 内存降低 +56.70%; 基础版本: `1604_greedy.rs`.

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1604_greedy.cpp](1604_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log k) | AC | 0.015 s | 292 KB | 11288133 |
| [1604_greedy.go](1604_greedy.go) | Go 1.14 x64 | greedy | O(n log k) | AC | 0.031 s | 2184 KB | 11288136 |
| [1604_greedy.java](1604_greedy.java) | Java 1.8 | greedy | O(n log k) | AC | 0.156 s | 3456 KB | 11288142 |
| [1604_greedy.py](1604_greedy.py) | Python 3.12 x64 | greedy | O(n log k) | AC | 0.093 s | 1776 KB | 11288140 |
| [1604_greedy.rs](1604_greedy.rs) | Rust 1.75 x64 | greedy | O(n log k) | AC | 0.015 s | 1044 KB | 11288144 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1604_greedy_optimized.cpp](1604_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n log k) | AC | 0.015 s | 148 KB | 11304457 |
| [1604_greedy_optimized.go](1604_greedy_optimized.go) | Go 1.14 x64 | greedy | O(n log k) | AC | 0.015 s | 1108 KB | 11304458 |
| [1604_greedy_optimized.java](1604_greedy_optimized.java) \* | Java 1.8 | greedy | O(n log k) | AC | 0.125 s | 1232 KB | 11304459 |
| [1604_greedy_optimized.py](1604_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(n log k) | AC | 0.093 s | 1028 KB | 11304460 |
| [1604_greedy_optimized.rs](1604_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(n log k) | AC | 0.062 s | 452 KB | 11304461 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
