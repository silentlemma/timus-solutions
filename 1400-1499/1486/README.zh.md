# 1486. 相同的正方形

[Timus 1486](https://acm.timus.ru/problem.aspx?space=1&num=1486) · 难度 621 · hashing

原题作者 Vladimir Yakovlev，出自 2006 年 10 月 7 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

在由小写字母组成的 N × M 矩阵（1 ≤ N, M ≤ 500）中，找出最大的 K，使得存在两个不
同的 K × K 正方形（可以重叠，但不能重合）完全相同，输出 K 和它们的左上角；若没有
两个相同的格子，输出 0。

时间限制：2 秒。内存限制：128 MB。

## 输入

N 和 M，然后是 N 行，每行 M 个字母。

## 输出

K，然后是两个左上角的行号和列号；或者只输出 0。任意一对都可以。

## 样例

### 样例 1

输入:

```
5 10
ljkfghdfas
isdfjksiye
pgljkijlgp
eyisdafdsi
lnpglkfkjl
```

输出:

```
3
1 1
3 3
```

## 解法

两个不同的相同 K × K 正方形，它们左上方的 (K − 1) × (K − 1) 部分也是两个不同的相
同正方形。所以"存在大小为 K 的一对"关于 K 单调，二分查找大约九次检查即可找到最
大的 K。

一次检查用 `O(NM)` 算出所有 K × K 正方形的哈希：在每一行上做滚动哈希，得到每个长
为 K 的窗口的哈希；再用另一个底数沿每一列对这些行哈希做第二次滚动哈希。相同的正
方形哈希相同。重复的哈希再逐字母比较两个正方形来确认，所以冲突只会多花时间，不
会导致错误答案。`O(NM log min(N, M))`。

注意事项：

- 两个正方形可以重叠，比如棋盘图案中最佳正方形只相差一步（测试 07）；
- 若没有重复的字母，答案只有一个 0（测试 02、03、05）；
- 全是同一字母的方阵只能取 K = N − 1，因为两个 N × N 正方形会重合；非方阵则可取
  min(N, M)（gen4、测试 06）。

## 语言说明

- Python 在 PyPy 下运行：最大的测试 CPython 约需 1.2 秒，PyPy 约 0.35 秒。它对
  2⁶¹ − 1 取模；其他语言把模 10⁹ + 7 和模 998244353 的两个哈希拼成一个 64 位键。
- 在 PyPy 下仍在评测的第 10 个测试上超过 2 秒的限制；因此保留并标为 TLE：它通过了这里的全部测试，但不保证在评测的每个测试上都足够快。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1486_hashing.cpp](1486_hashing.cpp) | G++ 13.2 x64 | hashing | O(NM log min(N, M)) | AC | 0.234 s | 7924 KB |
| [1486_hashing.go](1486_hashing.go) | Go 1.14 x64 | hashing | O(NM log min(N, M)) | AC | 0.718 s | 25556 KB |
| [1486_hashing.java](1486_hashing.java) | Java 1.8 | hashing | O(NM log min(N, M)) | AC | 0.671 s | 17900 KB |
| [1486_hashing.py](1486_hashing.py) | PyPy 3.10 x64 | hashing | O(NM log min(N, M)) | TLE (test 10) | 2.031 s | 37456 KB |
| [1486_hashing.rs](1486_hashing.rs) | Rust 1.75 x64 | hashing | O(NM log min(N, M)) | AC | 0.125 s | 7980 KB |
