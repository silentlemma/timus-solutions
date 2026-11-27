# 1110. N 次幂余数为 Y 的所有剩余

[Timus 1110](https://acm.timus.ru/problem.aspx?space=1&num=1110) · 难度 53 · bruteforce

原题出自保加利亚全国信息学奥林匹克竞赛第一天。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定 `N`、`M` 和 `Y`（`0 < N < 999`，`1 < M < 999`，`0 < Y < 999`），求 `[0, M − 1]` 中所有满足 `X^N mod M = Y`
的整数 `X`。

输入的 N、M、Y 都是整数。

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

快速幂保持 result*b^e 与原始 X^N 模 M 同余。奇数指数时乘入
result，再将 b 平方、e 减半，保持该不变量；e=0 得到精确余数。
0..M-1 的每个 X 恰检查一次，因此保留全部且仅有的根，并已升序。
结果为空时输出 -1。N=1 时每个候选仅需常数工作。

幂函数只用 O(1) 算术字。简单 C++ 存 O(M) 个整数根；Go/Rust
存根字符串和连接后的答案，Java 存答案构建器。简单 Python 存
整数根及格式化输出。若输出为 P 字节，这些答案占 O(M+P)；
这里每个根最多三位，故为 O(M)。Python/Rust 和优化 Go 的完整
输入另加 I 字节。优化 C++ 直接输出，只用 O(1) 状态；Java 存
O(M) 标记/输出字节；优化 Python/Go 仍存根字符串及连接答案。
固定库输入输出缓冲另计。

注意事项：

- `Y` 可能等于或大于 `M`；余数不可能如此，这时答案是 `-1`；
- `X^N` 本身大得惊人：每一步都要取余，乘积保持在 `M²` 以下，32 位整数放得下；
- 当 `N = 1` 时，只要 `Y < M`，答案就只有 `Y`。

答案经过验证：与朴素的重复乘法比对，对每个 `X` 做 `N` 次乘法。

## 优化解法

`1110_bruteforce_optimized.java`. Java 保留重复平方的穷举模根搜索，但将 x 与 M-x 配对：N 为偶数时两者幂相同，奇数时互为模 M 的相反数。因此一次幂计算检查两个余数；零单独处理，Y>=M 时无根。布尔数组标记根，再用有界字节缓冲区按升序输出，或输出 -1。M<999，每个根至多三位十进制数字，4*M 字节答案缓冲区足够。时间 O(M log N)，辅助空间 O(M)。保留直接整数解析，无答案表或另一数论求根算法。

精确源代码 Java 1.8 Accepted #11327344：0.078 s / 304 KB。2026-11-20 保存的编译器组比较：时间 1/228、内存 1/228。低于 1024 KB 时严格收录只看时间：前十或前 15%，相同指标共享名次，百分比名额向上取整。适用的时间准则已通过，没有单独语言目标，该行不加星号。此前记录的优化运行 #11303558 为 0.109 s / 412 KB，是独立历史指标对，并非本源代码的当前测量。保留教学版不变。

- `1110_bruteforce_optimized.java`: 0.078 s / 304 KB; 保留教学基础版 `1110_bruteforce.java`: 0.109 s / 1568 KB.

`1110_bruteforce_optimized.py`。两个 Python 版本都已使用三参数
pow 和一次连接输出。优化版直接保存根字符串，而非整数列表再
在打印时转换；使用 stdin.buffer，写出时不加末尾换行，显式
刷新后调用 os._exit(0)。根测试及升序不变，空列表仍输出 -1。
变化在输出和运行时结束处理，不是穷举模幂算法。

精确源代码 CPython 3.12 Accepted #11327010：0.062 s / 656 KB。2026-11-20 保存的当前语言族编译器组比较：时间排名 4/147，内存排名 118/147。低于 1024 KB，严格收录只看时间。

- `1110_bruteforce_optimized.py`: 0.062 s / 656 KB; 保留的教学基础版 `1110_bruteforce.py` (Python 3.12 x64): 0.078 s / 352 KB; 时间变化 -20.5%; 内存变化 +86.4%.

优化的 C++ 解法每找到一个根就立即输出，而不是先把根收集到 vector 里：
128 KB，而不是 196 KB，时间不变。

### 新的已通过版本

以下版本使用统一的[排名标准](../../RATING_CRITERIA.md)，并具有精确源码的 Accepted 证据。此前的性能讨论记录历史提交及快照，不构成另一套现行准入规则。有意义的简单版本及此前不同的实现均保留。

`1110_bruteforce_optimized.go`. 保留原有算法和边界处理，用数字及词元转换和可复用输出缓冲区替代 fmt。整个输入保存在字节缓冲区中，以存储输入的空间换取较少的通用输入输出开销。

Accepted #11328498 (Go 1.14 x64): **0.031 s / 944 KB**. 历史对照: `1110_bruteforce.go` (Go 1.14 x64) — 0.015 s / 1104 KB (#11279203).

当前 1110_bruteforce_optimized.go 仅命名原有 64 位数值转换和
64 字节初始输出容量。Accepted #11328498（0.算法、简单版本及实质注释均保留。

## 语言说明

- Python 使用内置的三参数 `pow`；其他语言自带一个小的幂函数。

上述源码修订均已取得各自的 Accepted。解答表列出与最终源码对应的提交编号及同次运行的时间和内存；较早的观察对应此前的修订。所有有教学价值的简单实现均保留。

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
| [1110_bruteforce_optimized.py](1110_bruteforce_optimized.py) | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.062 s | 656 KB | 11327010 |
| [1110_bruteforce_optimized.go](1110_bruteforce_optimized.go) | Go 1.14 x64 | bruteforce | O(M log N) | AC | 0.031 s | 1020 KB | 11330989 |
