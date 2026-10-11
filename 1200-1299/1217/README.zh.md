# 1217. 既按莫斯科又按圣彼得堡规则算幸运的车票

[Timus 1217](https://acm.timus.ru/problem.aspx?space=1&num=1217) · 难度 408 · combinatorics

原题作者 Leonid Volkov，出自第七届乌拉尔国立大学大学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

车票号码有 `N` 位，`N` 为偶数且不超过 20，允许前导零。按莫斯科的说法，前后两半
数字和相等的车票是幸运的；按圣彼得堡的说法，奇数位上的数字和等于偶数位上的数字
和的车票是幸运的。统计两种意义上都幸运的车票数。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`。

## 输出

这类车票的数量。

## 样例

### 样例 1

输入：

```
4
```

输出：

```
100
```

## 解法

按所在半边和奇偶把位置分成四组：`A`、`B` 是前半的奇数位和偶数位，`C`、`D` 是后半
的，并让每个字母也表示该组的数字和。两个条件写作 `A + B = C + D` 和
`A + C = B + D`。两式相加得 `A = D`，相减得 `B = C`；反过来，由这两个等式也能
推出两个条件。各组互相独立，所以答案是

（数字和相等的 `A`、`D` 填法对数）×（数字和相等的 `B`、`C` 填法对数）。

用 `k` 位数字凑出和 `s` 的方法数可以由一张逐位构建的小表得到，每个因子就是对 `s`
求两个这样的数之积的和。`O(N²)`，常数很小。

注意事项：

- 各组大小取决于 `N/2` 是否为奇数；逐个位置地数可以避免出错；
- `N = 20` 时答案约为 `1.9·10¹⁷`，超出 32 位，但在 64 位以内。

公式已用枚举全部六位车票验证，并且 2 到 20 的每个偶数 `N` 都与另一份独立解答比对
过。

## 各语言说明

- 所有语言都用同样的方式构建数字和表，并使用 64 位整数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1217_combinatorics.cpp](1217_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N²) | AC | 0.001 s | 192 KB |
| [1217_combinatorics.go](1217_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N²) | AC | 0.031 s | 1072 KB |
| [1217_combinatorics.java](1217_combinatorics.java) | Java 1.8 | combinatorics | O(N²) | AC | 0.109 s | 1592 KB |
| [1217_combinatorics.py](1217_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N²) | AC | 0.078 s | 436 KB |
| [1217_combinatorics.rs](1217_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N²) | AC | 0.031 s | 224 KB |
