# 1110. N 次幂余数为 Y 的所有剩余

[Timus 1110](https://acm.timus.ru/problem.aspx?space=1&num=1110) · 难度 53 · bruteforce

原题出自保加利亚全国信息学奥林匹克竞赛第一天。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 `N`、`M` 和 `Y`（`0 < N < 999`，`1 < M < 999`，`0 < Y < 999`），求 `[0, M − 1]` 中所有满足 `X^N mod M = Y`
的整数 `X`。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

一行 `N M Y`。

## 输出

按递增顺序输出所有这样的 `X`，用空格分隔；如果没有，输出 `-1`。

## 评测方式

输出按记号逐个比较；多余的空白字符无关紧要。

## 样例

### 样例 1

输入：

```
2 6 4
```

输出：

```
2 4
```

## 解法

候选不到一千个，所以逐个尝试 `X`，用快速幂计算 `X^N mod M`，每次乘法后都对 `M` 取余。`O(M log N)`。

注意事项：

- `Y` 可能等于或大于 `M`；余数不可能如此，这时答案是 `-1`；
- `X^N` 本身大得惊人：每一步都要取余，乘积保持在 `M²` 以下，32 位整数放得下；
- 当 `N = 1` 时，只要 `Y < M`，答案就只有 `Y`。

答案经过验证：与朴素的重复乘法比对，对每个 `X` 做 `N` 次乘法。

## 优化解法

`1110_bruteforce_optimized.java`. Java 保留重复平方的穷举模根搜索，但将 x 与 M-x 配对：N 为偶数时两者幂相同，奇数时互为模 M 的相反数。因此一次幂计算检查两个余数；零单独处理，Y>=M 时无根。布尔数组标记根，再用有界字节缓冲区按升序输出，或输出 -1。M<999，每个根至多三位十进制数字，4*M 字节答案缓冲区足够。时间 O(M log N)，辅助空间 O(M)。保留直接整数解析，无答案表或另一数论求根算法。

精确源代码 Java 1.8 Accepted #11327344：0.078 s / 304 KB。2026-11-20 保存的编译器组比较：时间 1/228、内存 1/228。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。两项均第一，也满足单独语言目标，无需星号。此前记录的优化运行 #11303558 为 0.109 s / 412 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1110_bruteforce_optimized.java`: 0.078 s / 304 KB; 保留教学基础版 `1110_bruteforce.java`: 0.109 s / 1568 KB.

`1110_bruteforce_optimized.py`. 保留逐个模幂测试的完整根枚举。按升序收集根并一次连接输出，替代逐根 print；无根仍为 -1。刷新后直接退出。所有模测试及教学版不变，不引入概率判根。

精确源代码 CPython 3.12 Accepted #11327010：0.062 s / 656 KB。2026-11-20 保存的当前语言族编译器组比较：时间排名 4/147，内存排名 118/147。低于 1024 KB，严格收录只看时间。

- `1110_bruteforce_optimized.py`: 0.062 s / 656 KB; 保留的教学基础版 `1110_bruteforce.py` (Python 3.12 x64): 0.078 s / 352 KB; 时间变化 -20.5%; 内存变化 +86.4%.

优化的 C++ 解法每找到一个根就立即输出，而不是先把根收集到 vector 里：
128 KB，而不是 196 KB，时间不变。

## 语言说明

- Python 使用内置的三参数 `pow`；其他语言自带一个小的幂函数。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1110_bruteforce.cpp](1110_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 196 KB | 11279202 |
| [1110_bruteforce.go](1110_bruteforce.go) | Go 1.14 x64 | bruteforce | O(M log N) | AC | 0.015 s | 1104 KB | 11279203 |
| [1110_bruteforce.java](1110_bruteforce.java) | Java 1.8 | bruteforce | O(M log N) | AC | 0.109 s | 1568 KB | 11279205 |
| [1110_bruteforce.py](1110_bruteforce.py) | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.078 s | 352 KB | 11279204 |
| [1110_bruteforce.rs](1110_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(M log N) | AC | 0.015 s | 212 KB | 11279206 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1110_bruteforce_optimized.cpp](1110_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 128 KB | 11303557 |
| [1110_bruteforce_optimized.java](1110_bruteforce_optimized.java) | Java 1.8 | bruteforce | O(M log N) time; O(M) auxiliary space | AC | 0.078 s | 304 KB | 11327344 |
| [1110_bruteforce_optimized.py](1110_bruteforce_optimized.py) \* | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.062 s | 656 KB | 11327010 |

\* 带星号的解法尚未达到目标排名，仍可优化。
