# 1354. 回文，又是回文

[Timus 1354](https://acm.timus.ru/problem.aspx?space=1&num=1354) · 难度 139 · strings

原题作者 Denis Nazarov，出自 2005 年 3 月中学生锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定一个最多 10 000 个拉丁字母的单词 S1，求最短的非空单词 S2，使 S1S2 是回文，并输出 S1S2。

时间限制：1 秒。内存限制：64 MB。

## 输入

一行，单词 S1。

## 输出

单词 S1S2。

## 样例

### 样例 1

输入：

```
No
```

输出：

```
NoN
```

### 样例 2

输入：

```
OnLine
```

输出：

```
OnLineniLnO
```

### 样例 3

输入：

```
AbabaAab
```

输出：

```
AbabaAababA
```

## 解法

若 S1S2 是回文且 S2 不长于 S1，则 S2 是 S1 某个前缀的反转，而 S1 去掉这个前缀后剩下的部分本身必须是回文。所以
最短的 S2 来自 S1 中从位置 1 或之后开始的最长回文后缀：S2 必须非空，因此即使 S1 本身是回文也不能直接使用。

设 T 为 S1 去掉首字母后的部分，T 的后缀 X 是回文，当且仅当 X 同时是 reverse(T) 的前缀。对
reverse(T) + `#` + T 计算前缀函数，最后一个值就是最长这种后缀的长度 L，答案是 S1 后接 S1 前 |S1| − L 个字母
的反转。`O(|S1|)`。

注意事项：

- 回文也仍需添加一个字母：`abcba` 得到 `abcbabcba`（测试 05）；
- 单个字母会被重复一次，因为空的尾部也算回文（测试 04）；
- 大写和小写是不同的字母（测试 03 和 07）；
- 直接检查每个后缀，在同一字母的长串上可能需要 10⁸ 步（生成测试 4）。

在 300 个最多 12 个字母的随机单词上，与直接枚举前缀长度的结果比较过；生成的测试也检查了答案是回文且不存在更短的
补充。

## 各语言说明

- 五种解答都对字节或字符使用同样的前缀函数。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1354_strings.cpp](1354_strings.cpp) | G++ 13.2 x64 | strings | O(len(S1)) | AC | 0.015 s | 396 KB |
| [1354_strings.go](1354_strings.go) | Go 1.14 x64 | strings | O(len(S1)) | AC | 0.031 s | 1540 KB |
| [1354_strings.java](1354_strings.java) | Java 1.8 | strings | O(len(S1)) | AC | 0.171 s | 960 KB |
| [1354_strings.py](1354_strings.py) | Python 3.12 x64 | strings | O(len(S1)) | AC | 0.109 s | 1216 KB |
| [1354_strings.rs](1354_strings.rs) | Rust 1.75 x64 | strings | O(len(S1)) | AC | 0.031 s | 336 KB |
