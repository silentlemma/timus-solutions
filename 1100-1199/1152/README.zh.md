# 1152. 大厅周围阳台上怪物造成的最小伤害

[Timus 1152](https://acm.timus.ru/problem.aspx?space=1&num=1152) · 难度 155 · bitmask

原题作者 Evgeny Bryzgalov，出自 2001 年 4 月在彼尔姆举行的乌拉尔团体程序设计锦标赛英语轮。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

`N` 个阳台（`3 ≤ N ≤ 20`）围成一圈，每个阳台上有 1 到 100 个怪物。一次射击会
摧毁三个相邻的阳台（第 `N` 个与第 1 个相邻）。每次射击后，每个还活着的怪物
造成一点伤害。射击持续到怪物全部消灭为止。求最小的总伤害。

时间限制：2 秒。内存限制：64 MB。

## 输入

`N`，然后是各阳台上的怪物数。

## 输出

最小的总伤害。

## 样例

### 样例 1

输入：

```
7
3 4 2 2 1 4 1
```

输出：

```
9
```

## 解法

状态是仍被占据的阳台集合，即 `N` 位的掩码。从一个状态出发，射击阳台 `i` 会
清掉 `i − 1`、`i` 和 `i + 1`，剩下集合 `rest`；代价是 `rest` 中的怪物数，之后
再从 `rest` 开始最优地进行。所以令 `damage(∅) = 0`，

`damage(mask) = 对所有能打中东西的射击取 min(alive(rest) + damage(rest))`。

只有从满圈可达的状态才有意义：它们被清掉的部分是若干段三个相邻阳台的并，
`N = 20` 时只有 15126 个。带记忆的递归只访问这些状态，每个尝试 `N` 次射击。
递归转移至多 `N − 2` 次（同时存在的调用至多 `N − 1` 个）：第一次射击清掉
三个阳台，之后每次有效射击至少清掉一个。打不中任何被占阳台的射击直接跳过，
它们永远没用。设可达状态数为 `S`，计算 `alive(rest)` 需要 `O(N)`，因此递归
耗时为 `O(S·N²)`。

注意事项：

- 圈是闭合的，所以射击第 1 个阳台也会清掉第 `N` 个；
- 最后一次射击后伤害为零，因为什么都不剩了；
- 射击顺序很重要，因为大的群体应当尽早消灭；
- 重叠的射击可能只清掉一个新阳台。在测试 07 中，以 1、2、3 为中心的射击形成
  三次转移的分支，尽管最优答案为 2；`⌈N / 3⌉` 不是递归深度的上界。

答案已在 120 个最多 13 个阳台的随机输入上，以及所有 20 个阳台的测试上，与
对全部 `2^N` 个子集自底向上计算的表比对。

## 优化解法

优化的 C++ 解法为每个状态缓存剩余伤害与该状态下存活怪物数之和，这样存活数每个状
态只算一次，而不是每次转移都算一次，总时间为 `O(S·N)`；答案是整圈的缓存值减去全
部怪物数。缓存是只存可达状态的 `unordered_map`，而不是覆盖全部 `2^N` 个掩码的数
组：{1152_bitmask_optimized.cpp}。

优化的 Go 解法为每个状态缓存剩余伤害与该状态下存活怪物数之和，这样存活数每个状态
只算一次，而不是每次转移都算一次，总时间为 `O(S·N)`；答案是整圈的缓存值减去全部
怪物数。缓存是只存可达状态的 `map`，而不是覆盖全部 `2^N` 个掩码的切片：
{1152_bitmask_optimized.go}。

优化的 Java 解法为每个状态缓存剩余伤害与该状态下存活怪物数之和，这样存活数每个状
态只算一次，而不是每次转移都算一次，总时间为 `O(S·N)`；答案是整圈的缓存值减去全
部怪物数。缓存不是覆盖全部 `2^N` 个掩码的数组，而是建在两个 `int` 数组上、填满一
半就翻倍的开放寻址哈希表，因此只存可达状态，键也无需装箱；输入用
`StreamTokenizer` 而不是 `Scanner` 读取：{1152_bitmask_optimized.java}。

优化的 Python 解法用普通字典代替 `lru_cache` 保存可达状态，并为每个状态缓存剩余
伤害与该状态下存活怪物数之和，这样存活数每个状态只算一次，而不是每次转移都算一
次，总时间为 `O(S·N)`；答案是整圈的缓存值减去全部怪物数：
{1152_bitmask_optimized.py}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1152_bitmask_optimized.cpp`: 时间降低 +0.00%; 内存降低 +87.18%; 基础版本: `1152_bitmask.cpp`.

- `1152_bitmask_optimized.go`: 时间降低 +51.61%; 内存降低 +75.09%; 基础版本: `1152_bitmask.go`.

- `1152_bitmask_optimized.java`: 时间降低 +25.60%; 内存降低 +81.78%; 基础版本: `1152_bitmask.java`.

- `1152_bitmask_optimized.py`: 时间降低 +67.52%; 内存降低 +6.28%; 基础版本: `1152_bitmask.py`.

## 各语言说明

- 所有语言都对同一个递归做记忆化；Python 用以掩码为键的缓存，其余语言用
  `2^N` 个元素的数组。
- Python 使用 `O(S + N)` 空间。其余语言会初始化全部 `2^N` 个元素，因此总时间
  为 `O(2^N + S·N²)`，空间为 `O(2^N + N)`。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1152_bitmask.cpp](1152_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^N + S·N²) | AC | 0.015 s | 3868 KB | 11280481 |
| [1152_bitmask.go](1152_bitmask.go) | Go 1.14 x64 | bitmask | O(2^N + S·N²) | AC | 0.031 s | 10052 KB | 11280557 |
| [1152_bitmask.java](1152_bitmask.java) | Java 1.8 | bitmask | O(2^N + S·N²) | AC | 0.125 s | 5356 KB | 11280628 |
| [1152_bitmask.py](1152_bitmask.py) | Python 3.12 x64 | bitmask | O(S·N²) | AC | 0.625 s | 2420 KB | 11280596 |
| [1152_bitmask.rs](1152_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^N + S·N²) | AC | 0.001 s | 1592 KB | 11280672 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1152_bitmask_optimized.cpp](1152_bitmask_optimized.cpp) | G++ 13.2 x64 | bitmask | O(2^N + S·N) | AC | 0.015 s | 496 KB | 11305857 |
| [1152_bitmask_optimized.go](1152_bitmask_optimized.go) | Go 1.14 x64 | bitmask | O(S·N) | AC | 0.015 s | 2504 KB | 11305860 |
| [1152_bitmask_optimized.java](1152_bitmask_optimized.java) | Java 1.8 | bitmask | O(2^N + S·N) | AC | 0.093 s | 976 KB | 11305862 |
| [1152_bitmask_optimized.py](1152_bitmask_optimized.py) | Python 3.12 x64 | bitmask | O(S·N) | AC | 0.203 s | 2268 KB | 11305865 |
