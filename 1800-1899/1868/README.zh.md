# 1868. 预测竞赛

[Timus 1868](https://acm.timus.ru/problem.aspx?space=1&num=1868) · 难度 158 · implementation

原题作者 Denis Dublennykh，出自 2011 年乌拉尔联邦大学开放团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

世界总决赛上前四名获得金牌，接下来四名获得银牌，再接下来四名获得铜牌。几位老将做了形如"X 队获得 Y 种奖牌"的预测，Vadik 给猜对次数最多的每位老将付五美元。已知按名次排列的十二支获奖队伍和全部预测，Vadik 要付多少钱？

## 输入

从第一名到第十二名的十二个队名，然后是 n（1 ≤ n ≤ 100）和 n 份预测。每份预测先给
出猜测数 kᵢ，接着 kᵢ 行 "队名 : 奖牌"，奖牌为 "gold"、"silver" 或 "bronze"。任何
预测都不会给一支队两枚奖牌，也不会把同一种奖牌给四支以上的队。队名由 1 到 30 个
拉丁字母、下划线、点和逗号组成。每个队名、每个数和每条猜测各占一行。

## 输出

Vadik 支付的美元数。

## 样例

### 样例 1

输入：

```
Zhejiang_U
U_of_Michigan_at_Ann_Arbor
Tsinghua_U
St._Petersburg_SU
Nizhny_Novgorod_SU
Saratov_SU
Friedrich_Alexander_U
Donetsk_National_U
Jagiellonian_U_in_Krakow
Moscow_SU
Ural_SU
U_of_Waterloo
3
6
Moscow_SU : gold
St._Petersburg_SU_of_ITMO : gold
Warsaw_U : gold
Tsinghua_U : gold
Nizhny_Novgorod_SU : silver
Saratov_SU : silver
6
Warsaw_U : gold
Saratov_SU : gold
Tsinghua_U : gold
Donetsk_National_U : silver
St._Petersburg_SU_of_ITMO : silver
Ural_SU : bronze
6
Zhejiang_U : gold
Tsinghua_U : gold
Shanghai_Jiao_Tong_U : gold
Fudan_U : gold
Moscow_SU : silver
Nizhny_Novgorod_SU : silver
```

输出：

```
15
```

## 解法

队名中没有空格，所以输入就是一串单词：十二个队名，然后每条猜测是队名、冒号和奖牌。用一个从十二个队名到奖牌的字典（第 1–4 名金牌，5–8 名银牌，9–12 名铜牌）判断猜测是否正确；字典里没有的队什么也没得。统计每位老将猜对的次数，给次数最多的每位老将付五美元。`O(n·k)` 次字典查询。

样例中每位老将都猜对三次，所以三人都获胜，Vadik 付 15 美元。

注意事项：

- 奖牌由名次决定：队名按顺序给出，前四名是金牌，依此类推；
- 预测中可能出现根本没有获奖的队；
- 队名区分大小写，并且可能只由点和逗号组成；
- 如果谁都没猜对，所有老将以零次并列第一，每人都要付钱。

在 150 次随机竞赛上，金额与一个独立的已通过实现一致。

## 优化解法

优化的 C++ 解法把十二个队名存放在每个 31 字节的固定 `char` 数组中（因为队名至多
30 个字符），用 `scanf` 把每条猜测读进 31 字节和 7 字节的缓冲区（奖牌名至多 6 个
字母），并用 `strcmp` 与十二个队名逐一比较，而不是用 `string` 组成的 `map`。它边
读边维护最多的猜对数和达到它的老兵人数，而不是保存所有计数的 `vector`，并用
`stdio` 代替 `iostream`：{1868_implementation_optimized.cpp}。

优化的 Python 解法利用每个队名、每个数和每条猜测各占一行这一点逐行读入，而不是把
整个输入切分成单词列表；它边读边维护最多的猜对数和达到它的老兵人数，而不是保存所
有计数的列表：{1868_implementation_optimized.py}。

优化的 Rust 解法利用每个队名、每个数和每条猜测各占一行这一点，把输入逐行读进同一
个反复使用的 `String`，而不是一次读入整个输入；它把每条猜测直接与保存的十二个队
名比较，而不是用 `HashMap`，并边读边维护最多的猜对数和达到它的老兵人数，而不是保
存所有计数的向量：{1868_implementation_optimized.rs}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1868_implementation_optimized.cpp`: 时间降低 +0.00%; 内存降低 +75.45%; 基础版本: `1868_implementation.cpp`.

- `1868_implementation_optimized.py`: 时间降低 -19.23%; 内存降低 +42.20%; 基础版本: `1868_implementation.py`.

- `1868_implementation_optimized.rs`: 时间降低 +0.00%; 内存降低 +60.45%; 基础版本: `1868_implementation.rs`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1868_implementation.go](1868_implementation.go).

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1868_implementation.cpp](1868_implementation.cpp) | G++ 13.2 x64 | implementation | O(n k) | AC | 0.015 s | 440 KB | 11304080 |
| [1868_implementation.go](1868_implementation.go) | Go 1.14 x64 | implementation | O(n k) | AC | 0.015 s | 1220 KB | 11290927 |
| [1868_implementation.java](1868_implementation.java) | Java 1.8 | implementation | O(n k) | AC | 0.093 s | 1196 KB | 11290930 |
| [1868_implementation.py](1868_implementation.py) | Python 3.12 x64 | implementation | O(n k) | AC | 0.078 s | 692 KB | 11290928 |
| [1868_implementation.rs](1868_implementation.rs) | Rust 1.75 x64 | implementation | O(n k) | AC | 0.015 s | 536 KB | 11290931 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1868_implementation_optimized.cpp](1868_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n k) | AC | 0.015 s | 108 KB | 11305924 |
| [1868_implementation_optimized.py](1868_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(n k) | AC | 0.093 s | 400 KB | 11305927 |
| [1868_implementation_optimized.rs](1868_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n k) | AC | 0.015 s | 212 KB | 11305928 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
