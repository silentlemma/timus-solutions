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

## 语言说明

- Python 使用内置的三参数 `pow`；其他语言自带一个小的幂函数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1110_bruteforce.cpp](1110_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 196 KB |
| [1110_bruteforce.go](1110_bruteforce.go) | Go 1.14 x64 | bruteforce | O(M log N) | AC | 0.015 s | 1104 KB |
| [1110_bruteforce.java](1110_bruteforce.java) | Java 1.8 | bruteforce | O(M log N) | AC | 0.109 s | 1568 KB |
| [1110_bruteforce.py](1110_bruteforce.py) | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.078 s | 352 KB |
| [1110_bruteforce.rs](1110_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(M log N) | AC | 0.015 s | 212 KB |
