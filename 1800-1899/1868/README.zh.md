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
North_A
North_B
North_C
North_D
East_A
East_B
East_C
East_D
West_A
West_B
West_C
West_D
3
3
North_A : gold
East_A : silver
West_A : bronze
4
North_B : gold
East_C : silver
West_D : bronze
Other : gold
3
North_C : silver
East_B : gold
Other : bronze
```

输出：

```
10
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

`1868_implementation_optimized.java`. 保留获奖者到奖牌的精确映射，仅保留预测最高分及并列人数。1024 字节 ASCII token 解析替代逐行 StringTokenizer，仍按完整姓名及奖牌相等判定。新提交为 0.078 s / 956 KB，比旧优化版 0.109 s / 900 KB 快，但稍增内存。保留的简单 Java 版为 0.093 s / 1196 KB；不声称相对旧优化版节省内存。

精确源代码 Java 1.8 Accepted #11326969：0.078 s / 956 KB。2026-11-20 保存的当前 Java 比较：时间排名 2/57，内存排名 9/57。内存低于 1024 KB，严格收录只看时间。

- `1868_implementation_optimized.java`: 0.078 s / 956 KB; 保留的教学基础版 `1868_implementation.java`: 0.093 s / 1196 KB; 时间变化 -16.1%; 内存变化 -20.1%.

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

每个保留的优化版本均已获 Accepted。收录依据为时间和内存均列前十或前 15%，两项均列前 30% 且至少一项排名优于同语言基础版，或相对同语言基础版时间或内存至少降低 30%。负的降低比例表示开销增加。星号对应单独的语言排名目标。

- `1868_implementation_optimized.cpp`: 时间降低 +0.00%; 内存降低 +75.45%; 基础版本: `1868_implementation.cpp`.

- `1868_implementation_optimized.py`: 时间降低 -19.23%; 内存降低 +42.20%; 基础版本: `1868_implementation.py`.

- `1868_implementation_optimized.rs`: 时间降低 +0.00%; 内存降低 +60.45%; 基础版本: `1868_implementation.rs`.

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1868_implementation_parsing_optimized.py`. 以字节读取奖牌名，单次遍历求最高分及获胜者人数，避免重复文本转换和扫描。 独立程序先刷新两个输出流，再调用 os._exit(0)，在完整答案写出后跳过解释器清理。这只改变进程结束方式，不改变数学算法；简单版本仍保留。

Accepted #11329012 (Python 3.12 x64): **0.062 s / 912 KB**. 历史对照: `1868_implementation.py` (Python 3.12 x64) — 0.078 s / 692 KB (#11290928).

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
| [1868_implementation_optimized.java](1868_implementation_optimized.java) | Java 1.8 | implementation | O(n k) | AC | 0.078 s | 956 KB | 11326969 |
| [1868_implementation_parsing_optimized.py](1868_implementation_parsing_optimized.py) | Python 3.12 x64 | implementation, parsing | O(n k) | AC | 0.062 s | 912 KB | 11329012 |

\* Accepted；尚未达到 [RATING_CRITERIA.md](../../RATING_CRITERIA.md) 中的排名目标，可继续优化。
