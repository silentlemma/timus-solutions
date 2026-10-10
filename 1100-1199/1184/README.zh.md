# 1184. 把电缆切成 K 段等长电缆时的最大长度

[Timus 1184](https://acm.timus.ru/problem.aspx?space=1&num=1184) · 难度 244 · binary_search

原题作者 Vladimir Pinaev 和 Roman Elizarov，出自 2001–2002 年 ACM ICPC 东北欧区域赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 `N ≤ 10000` 根长 1 米到 100 千米的电缆，长度精确到厘米。求以整厘米计的最大
长度，使这些电缆能切出至少 `K ≤ 10000` 段该长度的电缆。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N` 和 `K`，然后是以米为单位、恰好两位小数的长度。

## 输出

以米为单位、两位小数的长度；若连 1 厘米都不行，输出 `0.00`。

## 样例

### 样例 1

输入：

```
4 11
8.02
7.43
4.57
5.39
```

输出：

```
2.00
```

## 解法

以厘米为单位计算：长度恰好有两位小数，去掉小数点就得到精确的整数。长为 `c`
的电缆能切出 `⌊c/L⌋` 段长为 `L` 的电缆，这个数随 `L` 增大只减不增。所以在 0 到
最长电缆之间二分查找满足 `Σ ⌊c/L⌋ ≥ K` 的最大 `L`；若连 `L = 1` 都不够，答案
保持为 0。`O(N log C)`。

注意事项：

- 把长度当作浮点数读入，可能把 `8.02` 变成 `801.99…` 厘米；按文本解析可以避免；
- `K` 可能超过以厘米计的总长度，这时要输出 `0.00` 而不是出错；
- 输出需要两位小数，所以 `2` 要打印成 `2.00`。

答案已在 300 组随机数据和所有测试上与另一份独立编写的解答比对。

## 各语言说明

- Python、Go、Java 和 Rust 去掉每个长度中的小数点；C++ 把整数部分和小数部分
  作为两个整数读入。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1184_binary_search.cpp](1184_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N log C) | AC | 0.031 s | 280 KB |
| [1184_binary_search.go](1184_binary_search.go) | Go 1.14 x64 | binary_search | O(N log C) | AC | 0.031 s | 1688 KB |
| [1184_binary_search.java](1184_binary_search.java) | Java 1.8 | binary_search | O(N log C) | AC | 0.125 s | 6284 KB |
| [1184_binary_search.py](1184_binary_search.py) | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 1580 KB |
| [1184_binary_search.rs](1184_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 420 KB |
