# 2068. 拆分次数的奇偶性

[Timus 2068](https://acm.timus.ru/problem.aspx?space=1&num=2068) · 难度 108 · games

原题作者 Alexey Danilyuk，出自 2015 年乌拉尔地区程序设计团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 n 堆坚果，每堆的个数都是奇数。两人轮流操作；一次操作把某一堆分成三个非空的堆，且每堆的个数仍为奇数。无法操作的人输。Daenerys 先手，Stannis 后手。求双方都采取最优策略时的胜者。时间限制 1 秒，内存限制 64 MB。

## 输入

奇数 n（1 ≤ n ≤ 777），然后是 n 个奇数堆大小，范围 1 到 54321。

## 输出

若 Daenerys 获胜输出 `Daenerys`，否则输出 `Stannis`。

## 评测方式

仓库测试比较完整输出文本，仅忽略末尾空白。应保留有意义的空格、换行、大小写及标点。

## 样例

### 样例 1

输入：

```
1
3
```

输出：

```
Daenerys
```

### 样例 2

输入：

```
3
1 1 1
```

输出：

```
Stannis
```

### 样例 3

输入：

```
5
777 313 465 99 1
```

输出：

```
Daenerys
```

## 解法

这里策略无关紧要。一次操作把一堆换成三堆，所以堆数恰好增加 2，而坚果总数不变。游戏恰好在每堆只剩一个坚果时结束：3 个及以上（奇数个）坚果的堆总能分成 1 + 1 + (a − 2)。此时堆数等于坚果数，因此总操作次数恒为 (S − n) / 2，即各堆 (aᵢ − 1) / 2 之和。

Daenerys 走第奇数步，所以她获胜当且仅当这个数是奇数。第三个样例中各堆给出 388 + 156 + 232 + 49 + 0 = 825 步，是奇数。时间 O(n)。

## 优化解法

`2068_games_optimized.py` 逐字节复用，不增加源文件，也不引入新算法。精确源代码的 CPython 3.12 Accepted #11327048 为 0.078 s / 696 KB。2026-11-20 保存的当前 Python 语言族编译器组中，时间排名 5/50、内存排名 37/50。本次内存低于 1024 KB，因此严格前十名或前 15% 标准只看时间；星号仍表示单独的语言排名目标。同一未改动文件另有早先的 PyPy 3.10 Accepted #11325080：0.109 s / 236 KB。这些是不同运行各自成对的指标：选择 CPython 的时间与排名，PyPy 的内存更低。本节早先的省内存说明指此 PyPy 测量，不是 CPython 表格行。全部教学源代码保持不变。

`2068_games_optimized.java`. 保留 ((堆−1)/2) 奇偶 XOR。直接用已有标准输入，无额外字节数组；固定胜者字节经 System.out.write 后 flush。免 String 编码，仅普通标准流，无 FileDescriptor 访问。O(N) 时间、常数额外空间。

与 `2068_games.java` 相比：时间 0.109 s → 0.093 s；内存 480 KB → 340 KB。

`2068_games_optimized.py`. 保留总步数固定的不变量：一次分裂增加两堆，原有 a 颗的一堆在全变单颗前贡献 (a-1)//2 步。只需总和奇偶。每读一个整数便 XOR 其贡献奇偶，不保存所有文本记号或完整步数和。65536 字节解析器仅保留解析块和未完成记号，博弈状态一位。堆大小有界时，时间 O(N)，存储与 N 无关地有界。 独立评测程序在 os._exit(0) 前显式刷新 stdout，跳过常规解释器清理。其自身 Accepted 记录证明内存收益。单独改变退出方式不改进渐近复杂度，运行环境收益也不保证跨平台成立。简单版本保持不变。

与 `2068_games.py` 相比：时间 0.093 s → 0.109 s；内存 388 KB → 236 KB。

## 各语言说明

新增代码按 2026 年 11 月 18 日的快照，与其他作者在当前评测编译器上的结果比较，不设提交编号或日期门槛。相同指标并列，低于 0.015 s 的时间按 0.015 s 比较。下面的名次仅针对新增版本，原有代码仍保留各自历史 Accepted 提交的指标。

早先的 PyPy 比较：`2068_games_optimized.py`：在该可比样本中，时间名次 33/50，内存名次 1/50。

星号表示未达排名目标：C++ 要求时间和内存都位于前十或前 15%，其他语言族要求两项都为第一。代码仍可按独立的排名或改进准则纳入，包括时间或内存至少减少 30%。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2068_games.cpp](2068_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.015 s | 124 KB | 11294416 |
| [2068_games.go](2068_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.031 s | 1108 KB | 11294420 |
| [2068_games.java](2068_games.java) | Java 1.8 | games | O(n) | AC | 0.109 s | 480 KB | 11304044 |
| [2068_games.py](2068_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.093 s | 388 KB | 11304045 |
| [2068_games.rs](2068_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.015 s | 256 KB | 11304046 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2068_games_optimized.py](2068_games_optimized.py) | Python 3.12 x64 | games | O(N) | AC | 0.078 s | 696 KB | 11327048 |
| [2068_games_optimized.java](2068_games_optimized.java) | Java 1.8 | games | O(N) time; O(1) space | AC | 0.093 s | 340 KB | 11325849 |
