# 1208. 没有共同队员的传奇队伍最多有几支

[Timus 1208](https://acm.timus.ru/problem.aspx?space=1&num=1208) · 难度 210 · bitmask, dp

原题作者 Leonid Volkov，出自 2002 年 3 月乌拉尔国立大学团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

从 `1 ≤ K ≤ 18` 支队伍中选择尽可能多支，使任意两支所选队伍没有共同成员。
每队恰有三个不同姓名，每个姓名至多 20 个小写拉丁字母；同一姓名可以出现在多队。
时间限制 0.5 秒，内存限制 64 MB。

## 输入

`K`，然后是每支队伍的三个名字，每个最多 20 个小写字母。

## 输出

能参赛的最多队伍数。

## 评测方式

精确比较答案词元。每个新源码有完整目标环境检查、独立数学比较及哈希绑定的自身Accepted；保留简单版本的各自测量。

## 样例

### 样例 1

输入：

```
7
gerostratos scorpio shamgshamg
zaitsev silverberg cousteau
zaitsev petersen shamgshamg
clipper petersen shamgshamg
clipper bakirelli vasiliadi
silverberg atn dolly
knuth dijkstra bellman
```

输出：

```
4
```

## 解法

两队成员集合相交就冲突。对每队 `i` 保存冲突掩码 `clash[i]`，包含自己。
对于剩余集合 `S`，取最低位队伍 `i`。任何合法选择要么不选它，
要么选它并删除所有与它冲突的队伍：

`best(S) = max(best(S 去掉 i), 1 + best(S 去掉 clash[i]))`。

两种情况覆盖所有可能，空集答案为零。新掩码都清掉 `i`，数值严格变小，
原生语言基线因而按掩码递增填表。Python 用 `lru_cache` 惰性求同一递推，
不一定访问所有掩码。姓名长度有界时，时间 `O(2^K + K²)`，表或记忆化
最多占 `O(2^K)` 空间。五份原 Accepted 基线逐字节保留。
姓名出现在不同列仍然冲突，相同队伍被列两次也不能同时选择。

## 优化解法

**C++, Go, Java, Rust.** 新算法搜索包含/排除树，不保存每个掩码的答案。状态为剩余掩码与已选队数，
剩余队伍均与已选队伍相容，另保存目前最好的可行答案。
`selected + popcount(mask)` 即使忽略剩余内部冲突也仍是上界，
若不超过已有答案，可以安全剪枝。

否则在剩余队伍中选冲突最多的一队，计数包含自己。若最大值不超过一，
剩余队伍间没有冲突，全部选择恰好达到上界。否则先包含该队并删除其冲突掩码，
再只排除该队，两分支覆盖全部可行延伸。先包含可能先改善已有答案，
最大度选择只是启发式，不是正确性的前提。每次至少删除一队，深度不超过 `K ≤ 18`。

最坏时间 `O(K 2^K + K²)`，因为每个节点选择下一队时扫描至多 `K` 位。
除输入姓名外，搜索空间为冲突掩码和递归栈的 `O(K)`，没有指数表。
掩码可放入 32 位。搜索算法已改变，因此命名 `backtracking_bitmask`，
不创建带 `_optimized` 的重复源码。四份发布版本均按内存改善准入。
Java 记录时间较高，为 0.125 秒对 0.109 秒，但内存减少 83.3%；
单个计时刻度不足以可靠证明 CPU 改变。

**Python/PyPy.** 保留对完整掩码记忆化的清晰独立集解。新折半算法把至多18支队分成各至多9支的两半。左半每个子集的最优值由跳过最低位队，或选它并删除冲突队得到。右半递归跳过/选取队伍，同时删除右冲突及不兼容左队；叶子查左表。每个兼容选择对应唯一右分支，加上最优允许左子集，故正确。姓名用精确相等比较，不依赖概率哈希。时间O(K²+2^ceil(K/2))，空间O(2^floor(K/2)+K)。

- `1208_backtracking_bitmask.cpp`: 0.015 s / 176 KB; 基础 `1208_bitmask.cpp`: 0.015 s / 976 KB; 相对变化: 时间 -0.0%, 内存 -82.0%.
- `1208_backtracking_bitmask.go`: 0.031 s / 1104 KB; 基础 `1208_bitmask.go`: 0.062 s / 3204 KB; 相对变化: 时间 -50.0%, 内存 -65.5%.
- `1208_backtracking_bitmask.java`: 0.125 s / 448 KB; 基础 `1208_bitmask.java`: 0.109 s / 2688 KB; 相对变化: 时间 +14.7%, 内存 -83.3%.
- `1208_backtracking_bitmask.rs`: 0.015 s / 224 KB; 基础 `1208_bitmask.rs`: 0.046 s / 684 KB; 相对变化: 时间 -67.4%, 内存 -67.3%.
- `1208_bitmask_dp.py`: 0.125 s / 296 KB; 基础 `1208_bitmask.py`: 0.078 s / 456 KB; 相对变化: 时间 +60.3%, 内存 -35.1%.

## 各语言说明

保存的排名快照为 2026 年 11 月 1–2 日。C++ 要求时间和内存均前 15% 或前十名；其他语言均要求两项第一。相等结果并列。空竞争样本只表示形式覆盖。

使用保存的当前编译器筛选，排除本作者及耗时低于0.015秒的旧记录；非C++还要求提交ID≥10770000。C++内存只比较前1000条符合条件的记录。本方低于0.015秒的耗时按0.015秒计算。ID界限是固定比较规则，不是精确的日历筛选。

- C++: 首选教学基础 `1208_bitmask.cpp`; 覆盖源码 `1208_backtracking_bitmask.cpp`; 时间/内存名次 1/27, 其他作者记录 109/109.

- Go: 首选教学基础 `1208_bitmask.go`; 覆盖源码 `1208_backtracking_bitmask.go`; 时间/内存名次 1/1, 其他作者记录 0/0.

- Java: 首选教学基础 `1208_bitmask.java`; 覆盖源码 `1208_backtracking_bitmask.java`; 时间/内存名次 2/1, 其他作者记录 4/4.

- Python/PyPy: 首选教学基础 `1208_bitmask.py`; 覆盖源码 `1208_bitmask_dp.py`; 时间/内存名次 4/2, 其他作者记录 21/21.

- Rust: 首选教学基础 `1208_bitmask.rs`; 覆盖源码 `1208_backtracking_bitmask.rs`; 时间/内存名次 1/1, 其他作者记录 0/0.

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1208_bitmask.cpp](1208_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K + K^2) | AC | 0.015 s | 976 KB | 11283611 |
| [1208_bitmask.go](1208_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K + K^2) | AC | 0.062 s | 3204 KB | 11283615 |
| [1208_bitmask.java](1208_bitmask.java) | Java 1.8 | bitmask | O(2^K + K^2) | AC | 0.109 s | 2688 KB | 11283617 |
| [1208_bitmask.py](1208_bitmask.py) | Python 3.12 x64 | bitmask | O(2^K + K^2) | AC | 0.078 s | 456 KB | 11283616 |
| [1208_bitmask.rs](1208_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K + K^2) | AC | 0.046 s | 684 KB | 11283620 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交 |
|---|---|---|---|---|---|---|---|
| [1208_backtracking_bitmask.cpp](1208_backtracking_bitmask.cpp) \* | G++ 13.2 x64 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.015 s | 176 KB | 11308198 |
| [1208_backtracking_bitmask.go](1208_backtracking_bitmask.go) | Go 1.14 x64 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.031 s | 1104 KB | 11308199 |
| [1208_backtracking_bitmask.java](1208_backtracking_bitmask.java) \* | Java 1.8 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.125 s | 448 KB | 11308200 |
| [1208_backtracking_bitmask.rs](1208_backtracking_bitmask.rs) | Rust 1.75 x64 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.015 s | 224 KB | 11308202 |
| [1208_bitmask_dp.py](1208_bitmask_dp.py) \* | PyPy 3.10 x64 | bitmask, dp | O(K^2 + 2^(K/2)) time, O(2^(K/2)+K) memory | AC | 0.125 s | 296 KB | 11309782 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
