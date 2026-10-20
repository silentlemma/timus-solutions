# 2176. 三进制写法藏在二进制写法中的数的不同数之和

[Timus 2176](https://acm.timus.ru/problem.aspx?space=1&num=2176) · 难度 1169 · dp, meet_in_middle

原题作者 Konstantin Rychkov，出自 2023 年乌拉尔中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

如果一个数的三进制写法是其二进制写法的子串，就称它是漂亮的，例如 12 = 110₃ = 1100₂。对 N 个数 xᵢ 中的每一个，判断它是否能写成若干个不同漂亮数之和。时间限制 1 秒，内存限制 256 MB。

## 输入

N（1 ≤ N ≤ 1000），然后是 x₁ … x_N（1 ≤ xᵢ ≤ 10⁹）。

## 输出

对每个数输出 YES 或 NO。

## 样例

### 样例 1

输入：

```
6
1 2 3 8 9 10
```

输出：

```
YES
NO
NO
NO
YES
YES
```

### 样例 2

输入：

```
4
854789369 694089367 789789379 795089367
```

输出：

```
NO
YES
NO
YES
```

## 解法

二进制串只有数字 0 和 1，所以漂亮数的三进制写法中没有数字 2。不超过 10⁹ 的这类数最多有 19 位三进制数字，因此少于 2¹⁹ 个；通过在三进制前缀后添加 0 或 1 生成它们，同时把同样的数字当作二进制模式，在二进制写法中查找。其中只有 40 个是漂亮的，最大的是 133991292。

问题于是变成 40 个固定数的子集和，把它们分成两部分。

- 最小的 31 个数之和为 48106098，所以用这么大的位集标记所有不同小数之和；每个数把位集平移后与原位集按位或。
- 剩下的 9 个数只有 2⁹ 个子集和，列出并排序。

对查询 x，尝试大部分中满足 x − 48106098 ≤ h ≤ x 的和 h，只要某个 x − h 在位集中被标记，答案就是 YES。

第一个样例中 9 = 100₃ = 1001₂ 和 10 = 101₃ = 1010₂ 是漂亮数，而 2 和 3 不是，也无法由 1 凑出。

构造位集需要对 4800 万位做 31 遍，每个查询至多尝试 512 个和。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [2176_dp_meet_in_middle.cpp](2176_dp_meet_in_middle.cpp) | G++ 13.2 x64 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.046 s | 5616 KB |
| [2176_dp_meet_in_middle.go](2176_dp_meet_in_middle.go) | Go 1.14 x64 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.046 s | 7528 KB |
| [2176_dp_meet_in_middle.java](2176_dp_meet_in_middle.java) | Java 1.8 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.125 s | 6340 KB |
| [2176_dp_meet_in_middle.py](2176_dp_meet_in_middle.py) | Python 3.12 x64 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.562 s | 18964 KB |
| [2176_dp_meet_in_middle.rs](2176_dp_meet_in_middle.rs) | Rust 1.75 x64 | dp, meet_in_middle | O(S / w + N · 2^9) | AC | 0.046 s | 5772 KB |
