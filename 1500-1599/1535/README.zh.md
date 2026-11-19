# 1535. 霍比特人，或去而复返

[Timus 1535](https://acm.timus.ru/problem.aspx?space=1&num=1535) · 难度 497 · constructive

原题作者 Alexander Ipatov，出自 2007 年 3 月 3 日第八届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

比尔博从城市 1 出发，2 … N 号城市各访问一次，再回到城市 1（2 ≤ N ≤ 50000）。从城市 Q
进入城市 P 要付 P·Q 枚金币。输出一个总花费最小的访问顺序和一个总花费最大的访问顺序。

时间限制：1 秒。内存限制：64 MB。

## 输入

N。

## 输出

两行，每行 N 个数并以 1 开头：最便宜的顺序和最贵的顺序。任何最优顺序都可以。

## 评测方式

仓库使用语义检查器，接受满足以下条件的任意输出。 仓库检查器要求两行非空输出，各为从1开始的 1..N 排列。每条路线闭合回首城，累加相邻编号乘积，再与对应最小或最大参考费用比较；并列最优排列均有效。

## 样例

### 样例 1

输入:

```
4
```

输出:

```
1 4 2 3
1 3 4 2
```

## 解法

环的代价是相邻标号乘积之和，包含回到城市1的末边。令 D(i,j)=N²−ij，
矩阵非负且对称。对 i<j<k<l，

(Dᵢⱼ+Dₖₗ)−(Dᵢₖ+Dⱼₗ)=(k−j)(i−l)<0，

(Dᵢₖ+Dⱼₗ)−(Dᵢₗ+Dⱼₖ)=(j−i)(k−l)<0。

这满足 Supnick 不等式。最小 D 环先按升序排列奇数，再按降序排列偶数。
最大 D 环由两条交替的分支组成。每个 D 环的代价为 N³ 减去原乘积和，
所以这两个环分别使原乘积和最大和最小。[极值环定理](https://doi.org/10.1016/S0166-218X(99)00148-1)

最大乘积和按 1、3、5、… 升序排列，再将偶数降序排列到 2。构造最小值时
从 N 出发，令 q=⌊(N−1)/2⌋。当 k=1…q 时，一条分支 aₖ 在 k 为奇数时取
k+1，在 k 为偶数时取 N−k。另一条分支 bₖ 在 k 为奇数时取 k，在 k 为偶数时
取 N−k+1。依次连接 N、a₁、…、a_q，若 N 为偶数则插入唯一剩余值
2⌊N/4⌋+1，最后连接 b_q、…、b₁。旋转环使其从 1 开始。反向读取即得最大
D 环 1、N−1、3、N−3、…、N−2、2、N，从而使原乘积和最小。N 为 2 或 3 时，
无向环的边集唯一。

简单版显式存两臂并旋转环，O(N)时间与额外空间；不同的快速版本
直接生成同样的索引并使用有界输出缓冲。

两行均以 1 开始。计算代价时包含闭合边，每个城市只输出一次。

## 优化解法

`1535_constructive_optimized.py`. 保留最小交替两侧巡回与最大奇数升/偶数降巡回。由循环索引及奇偶直接生成城市，包括偶数 n 时单独的中间城，不存访问标志、两侧表、中间表或完整巡回。两行 n 城通过 4096 字节缓冲输出，保留空格和首城 1。构造 O(n) 算术步骤，十进制输出 O(n log n) 工作，缓冲/整数空间 O(B+log n)。语义检查器验证两巡回最优性，不要求唯一排列。

与 `1535_constructive.py` 相比：时间 0.109 s → 0.187 s；内存 8752 KB → 3 184 KB。

`1535_constructive_optimized.java`. 保留两个已证明的极值环游构造，但直接生成城市，不再构造 used[]、装箱列表、环、子列表副本或完整输出字符串。最小路线交替输出两端配对，必要时加唯一中间城市；最大路线先奇数升序，再偶数降序。同一循环覆盖 N=2。每行均从一开始且每城一次。输出有界整数耗时 O(N)，固定输入输出缓冲之外额外空间 O(1)；原列表教学构造单独保留。

与 `1535_constructive.java` 相比：时间 0.140 s → 0.109 s；内存 11176 KB → 504 KB。

C++、Go、Rust 直接按索引输出旧的双臂环，不存访问标记、两臂、环、旋转排列或字符串。令 q=⌊(N−1)/2⌋，先输出 1,N，再输出 k=1…q 的 aₖ：奇 k 为 k+1，偶 k 为 N−k。偶数 N>2 时唯一剩余中值是 2⌊N/4⌋+1。再按 k=q…2 输出 bₖ：奇 k 为 k，偶 k 为 N−k+1；b₁=1 已在首位。N=2 只输出 1,2。它与原双臂构造相同，只是不存两臂。最大代价排列仍是奇数递增、偶数递减。8192 字节块给出 O(N) 时间、O(1) 额外空间。保留简单版；Java/Python 复用达标基础版。独立子集 DP 验证 N≤14 的两个全局极值；一般最优性来自简单解法中的 Supnick 归约。

通过评测的 Rust 1.75 x64 版本耗时 0.046 秒，基础版为 0.031 秒，内存为 232 KB，基础版为 4376 KB。

已通过评测的基础实现 [1535_constructive.java](1535_constructive.java), [1535_constructive.py](1535_constructive.py) 也满足快速版本的要求：在保存的比较快照中，时间和内存均符合前 15% 或前十名的排名收录规则。直接复用这些源文件，不创建相同副本。星号标记尚未达到该语言目标排名的版本。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

`1535_constructive_optimized.java`：在该可比样本中，时间名次 2/18，内存名次 1/18。

`1535_constructive_optimized.py`：在该可比样本中，时间名次 16/33，内存名次 2/33。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1535_constructive.cpp](1535_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1700 KB | 11287470 |
| [1535_constructive.go](1535_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 7060 KB | 11287471 |
| [1535_constructive.java](1535_constructive.java) \* | Java 1.8 | constructive | O(N) | AC | 0.140 s | 11176 KB | 11287473 |
| [1535_constructive.py](1535_constructive.py) \* | Python 3.12 x64 | constructive | O(N) | AC | 0.109 s | 8752 KB | 11287472 |
| [1535_constructive.rs](1535_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 4376 KB | 11287474 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1535_constructive_optimized.cpp](1535_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 100 KB | 11315377 |
| [1535_constructive_optimized.go](1535_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 936 KB | 11315379 |
| [1535_constructive_optimized.rs](1535_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 232 KB | 11315380 |
| [1535_constructive_optimized.java](1535_constructive_optimized.java) \* | Java 1.8 | constructive | O(N) | AC | 0.109 s | 504 KB | 11325038 |
| [1535_constructive_optimized.py](1535_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(n log n) output work; O(B+log n) space | AC | 0.187 s | 3184 KB | 11325487 |

\* Accepted；尚未达到排名目标，该版本仍有优化空间。
