# 1272. 不在叶卡捷琳堡的地铁

[Timus 1272](https://acm.timus.ru/problem.aspx?space=1&num=1272) · 难度 144 · dsu

原题作者 Magaz Asanov（由 Igor Goldberg 准备），出自 2003 年 10 月 25 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一座城镇建在 1 ≤ N ≤ 10 000 个岛上，岛间有 0 ≤ K ≤ 12 000 条隧道和
0 ≤ M ≤ 12 000 座桥，它们合起来连通所有岛屿。地铁要利用其中一部分连接所有
岛屿，并且使用的桥尽可能少。最少需要多少座桥？

时间限制：1 秒。内存限制：64 MB。

## 输入

N、K 和 M，然后是 K 条隧道和 M 座桥，每条用两个 1 到 N 之间的岛屿编号表示。

## 输出

最少的桥数。

## 评测方式

仓库测试精确比较输出记号，记号之间的空白分隔不影响结果。

## 样例

### 样例 1

输入：

```
7 4 4
1 2
2 3
4 5
6 7
1 3
2 4
5 6
6 7
```

输出：

```
2
```

## 解法

隧道不计代价，所以全部采用：它们把岛屿分成若干已连通的组。每座桥最多把两组合并成一组，
而整个网络是连通的，所以总能选出桥把各组逐个连起来。因此答案是隧道形成的组数减一，用
并查集处理隧道即可，忽略桥的端点。`O((N+K)log(N+1))`。

注意事项：

- 桥本身无关紧要，重要的只是它们能连接各组，而这一点题目已经保证；
- 隧道可能重复，也可能连接岛屿自身（测试 05）；
- 只有一个岛，或仅靠隧道就能连通全部时，答案为 0（测试 02、04）。

所有基础及快速本地版本无秩链接并用path halving。其对数界是允许任意链接的摊还界（[Tarjan–van Leeuwen，引理7–8](https://doi.org/10.1145/62.2160)），单次find可线性，不能据此声称反阿克曼。Iᶜ为实际消费字节含有界预读，总O((N+K)log(N+1)+Iᶜ)。基础C++/Go/Java只解析隧道，Python/Rust读完整文件；快速C++/Go/Rust读桥，Java/Python只需前缀。M按实际消费输入计。

基础C++/Go/Java N+1父节点及有界缓冲B，O(N+B)。Python全分词输入、Rust全String，O(N+I)。快速Go N+1 uint 16，Rust/Java原生父节点及有界缓冲，O(N+B)。快速C++无论N固定10001父槽，W=10000时O(W+B)。快速Python负根大小/父项和1024块，O(N+B)，n=1或k=0不分配DSU。流式版不保留桥列表。

## 优化解法

`1272_dsu_optimized.py`按大小合并并用path splitting。先保存旧父next_vertex，当前节点改指祖父，再走旧父；halving会走新父。根的负数保存大小。全网络连通故答案components−1，无需桥记录；合并剩一分量即退出，n=1或k=0直接N−1。1024块解析所需token，DSU摊还O(N+K·α(N))另输入，空间O(N+B)。只改文档，不改算法。

历史精确Python 3.12 Accepted #11327776：0.078 s / 784 KB。2026-11-20时间3/99、内存2/99；低于1024 KB只比时间，无独立第一名目标。更早#11304489另一历史对0.109 s / 1076 KB。

- `1272_dsu_optimized.py`: 0.078 s / 784 KB; 保留教学基础版 `1272_dsu.py`: 0.093 s / 3328 KB.

`1272_dsu_optimized.java`保持无秩链接/halving，仅用固定字节输入代替StreamTokenizer，隧道后不解析桥。DSU同样摊还对数界；O(N+K·N)只是单次find的更松界，不是不同算法。空间O(N+B)。Java历史对：基础0.140 s / 488 KB，快速输入0.109 s / 512 KB。

与 `1272_dsu.java` 相比：时间 0.140 s → 0.109 s；内存 488 KB → 512 KB。

优化的 C++ 解法从 4 KB 缓冲区中手工解析数字，而不是用 `scanf`，并把父节点存放在
有 10 001 个单元的固定全局数组中（`N ≤ 10 000`，足够用），而不是 `std::vector`。
它还会把桥一直读到末尾，而简单解法不读它们：[1272_dsu_optimized.cpp](1272_dsu_optimized.cpp)。

优化的 Go 解法从 `bufio.Reader` 中逐字节解析数字，而不是用 `fmt.Fscan`，并用
`uint16` 而不是 `int` 存放父节点，`uint16` 足以容纳不超过 10 000 的岛屿编号。它
还会把桥一直读到末尾，而简单解法不读它们：[1272_dsu_optimized.go](1272_dsu_optimized.go)。

优化的 Rust 解法从由标准输入反复填充的 4 KB 缓冲区中手工解析数字，而不是把整个输
入读进 `String`，因此内存中只剩父节点数组和缓冲区：[1272_dsu_optimized.rs](1272_dsu_optimized.rs)。

### 实测改进

以下收益对仅历史观测。准入按统一排名，无独立30%资源收益或第一名条件；有意义基础即使未过指标仍保留。

- `1272_dsu_optimized.cpp`: 时间降低 +51.61%; 内存降低 +49.12%; 基础版本: `1272_dsu.cpp`.

- `1272_dsu_optimized.go`: 时间降低 -106.67%; 内存降低 +35.85%; 基础版本: `1272_dsu.go`.

- `1272_dsu_optimized.rs`: 时间降低 +0.00%; 内存降低 +63.93%; 基础版本: `1272_dsu.rs`.

## 各语言说明

源码绑定缓存：快速C++/Java/Python普通时间通过，两份Rust普通时间通过，两份Go精确编译器稀疏参照通过（基础1428 KB两项，快速916 KB仅时间）。基础C++/Java/Python未过比较仍教学。[统一标准](../../RATING_CRITERIA.md)适用所有语言，低于1024 KB仅时间。历史Java时间6/90、内存2/90仅旧快照。

九个文件共同修正“每桥连接两个分量”：桥可在隧道分量内部，但全网络连通保证有足够跨分量桥。仅改解释行，可执行代码、基础版及其他有意义注释保留。

上述源码修订均已取得各自的 Accepted。解答表列出与最终源码对应的提交编号及同次运行的时间和内存；较早的观察对应此前的修订。所有有教学价值的简单实现均保留。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu.cpp](1272_dsu.cpp) | G++ 13.2 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.015 s | 216 KB | 11331137 |
| [1272_dsu.go](1272_dsu.go) | Go 1.14 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.031 s | 1396 KB | 11331005 |
| [1272_dsu.java](1272_dsu.java) | Java 1.8 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.109 s | 472 KB | 11331044 |
| [1272_dsu.py](1272_dsu.py) | Python 3.12 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.125 s | 3220 KB | 11331064 |
| [1272_dsu.rs](1272_dsu.rs) | Rust 1.75 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.015 s | 724 KB | 11331101 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu_optimized.cpp](1272_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.015 s | 128 KB | 11331138 |
| [1272_dsu_optimized.go](1272_dsu_optimized.go) | Go 1.14 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.031 s | 924 KB | 11331006 |
| [1272_dsu_optimized.py](1272_dsu_optimized.py) | Python 3.12 x64 | dsu | O(N+K·α(N)+Iᶜ) amortized | AC | 0.078 s | 888 KB | 11331065 |
| [1272_dsu_optimized.rs](1272_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.062 s | 268 KB | 11331102 |
| [1272_dsu_optimized.java](1272_dsu_optimized.java) | Java 1.8 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.109 s | 512 KB | 11325012 |
