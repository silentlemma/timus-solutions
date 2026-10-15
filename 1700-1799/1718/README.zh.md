# 1718. 重测

[Timus 1718](https://acm.timus.ru/problem.aspx?space=1&num=1718) · 难度 309 · implementation

原题作者 Alexander Ipatov，由 Alex Samsonov 整理，出自 NEERC 2009 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

某题原有七个测试。之后在它们后面添加了十个新测试，又删除了测试 6，然后重测所有以前的提交。
结果有变化的提交列表非空的每位作者会收到一封信。根据旧的评测结果，求可能收到信的作者数的最小值和最大值。

## 输入

n（1 ≤ n ≤ 1000），然后 n 行，每行是作者名和旧结果：AC、CE，或 ML X、TL X、WA X（1 ≤ X ≤ 7）。
带测试号 X 的结果表示通过了测试 1 … X − 1，未通过测试 X。只有 X 不同的结果也视为不同。

## 输出

收到信的作者数的最小值和最大值。

## 样例

### 样例 1

输入：

```
5
[SPbSU_ITMO]_WiNGeR TL 6
Milanin_(TNU) WA 6
Vladimir_Yakovlev_(USU) AC
Sandro_(USU) WA 1
Sandro_(USU) ML 3
```

输出：

```
0 3
```

## 解法

修改之后测试 1 … 5 不变，旧测试 7 变成测试 6，新测试编号为 7 … 16。每个旧结果要么一定改变，要么可能改变，要么一定不变：

- CE 以及在测试 1 … 5 上失败的结果不变，因为前面的测试相同；
- 在测试 7 上失败的结果一定改变：该测试现在是第 6 个，所以结果至少会从 7 变为 6；
- AC 可能改变，因为新测试可能失败；在测试 6 上失败的结果也可能改变：该测试已删除，评测继续到旧测试 7。
  如果在旧测试 7 上以同样方式失败，结果保持不变，因为该测试现在正是第 6 个。

因此最少的信数是在测试 7 上失败过的作者数；最多再加上有 AC 或在测试 6 上失败过的作者。作者名用集合统计：C++ 为 `O(n log n)`，其余语言期望为 `O(n)`。

注意事项：

- 一位作者只算一次，无论他有多少个提交改变；
- 在旧测试 6 上失败的结果可能保持完全相同，所以它不一定导致来信；
- 作者名中可能有方括号和圆括号，但没有空格，所以按单词读取即可。

在 600 个随机测试上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1718_implementation.cpp](1718_implementation.cpp) | G++ 13.2 x64 | implementation | O(n log n) | AC | 0.015 s | 596 KB |
| [1718_implementation.go](1718_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1344 KB |
| [1718_implementation.java](1718_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.078 s | 1140 KB |
| [1718_implementation.py](1718_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 724 KB |
| [1718_implementation.rs](1718_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 532 KB |
