# 1209. 连写的 1、10、100、1000 中的数字

[Timus 1209](https://acm.timus.ru/problem.aspx?space=1&num=1209) · 难度 34 · math

原题作者 Alexey Lakhtin，出自 2002 年 10 月 USU Open Collegiate Programming Contest（Junior Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

把 10 的各次幂依次写下：`110100100010000…`。对最多 65535 个位置
`1 ≤ K < 2³¹`，输出每个位置上的数字。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`，然后是 `N` 个位置。

## 输出

用空格分隔的 `N` 个数字。

## 样例

### 样例 1

输入：

```
4
3
14
7
6
```

输出：

```
0 0 1 0
```

## 解法

写下的第 `m` 个幂是 `10^(m−1)`，占 `m` 位，所以它从位置
`1 + (1 + 2 + … + (m − 1)) = 1 + m(m − 1)/2` 开始，它唯一的 1 就在那里。位置 `K`
上是 1 当且仅当对某个 `m` 有 `K − 1 = m(m − 1)/2`，也就是
`8(K − 1) + 1 = (2m − 1)²` 是完全平方数。每个位置 `O(1)`。

注意事项：

- `8(K − 1) + 1` 可达约 `1.7·10¹⁰`，超出 32 位；
- 浮点平方根在大平方数附近可能差一，所以必须用精确的整数检查来修正。

答案已在 1 到 65535 的所有位置、随机位置以及 1 附近的位置上与另一份独立解答比对。

## 各语言说明

- Python 用精确的 `math.isqrt`；其他语言用整数比较修正浮点平方根。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1209_math.cpp](1209_math.cpp) | G++ 13.2 x64 | math | O(1) per position | AC | 0.062 s | 388 KB |
| [1209_math.go](1209_math.go) | Go 1.14 x64 | math | O(1) per position | AC | 0.062 s | 2664 KB |
| [1209_math.java](1209_math.java) | Java 1.8 | math | O(1) per position | AC | 0.062 s | 1372 KB |
| [1209_math.py](1209_math.py) | Python 3.12 x64 | math | O(1) per position | AC | 0.125 s | 6556 KB |
| [1209_math.rs](1209_math.rs) | Rust 1.75 x64 | math | O(1) per position | AC | 0.015 s | 3160 KB |
