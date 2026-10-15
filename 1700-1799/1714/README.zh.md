# 1714. 助记符与回文 2

[Timus 1714](https://acm.timus.ru/problem.aspx?space=1&num=1714) · 难度 3223 · constructive

原题作者 Igor Chevdar，出自 NEERC 2009 东部分区赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个词的复杂度是它最少能拆成的回文串个数。输出一个由 n 个字母 a、b 组成、复杂度最大的词。

## 输入

n（1 ≤ n ≤ 1000）。

## 输出

这样的一个词。任何一个都可以。

## 样例

### 样例 1

输入：

```
6
```

输出：

```
aababb
```

## 解法

在两个字母上回文很容易出现，所以复杂的词必须避开长回文。这里的词以 aabab 开头，重复块 bbaaba，
最后接一个按 n mod 6 选择的短尾巴：空、b、bb、bbaaababb、bbaa 或 bbaab。每个块使最少拆分多两个回文。
少数短长度需要专门的词：2 用 ab，8 用 aababbaa，11 用 aababbaabab；5 个字母以内取 aabab 的前缀即可。`O(n)`。

当 n ≥ 12 时这些词的复杂度为 ⌊n/3⌋ + 1，n ≡ 2 (mod 6) 时再多一。较小的长度给出 1、2、2、2、2、3、3、4、4、4、5。
对所有词的穷举搜索确认，对 20 以内的每个 n 这都是最大复杂度。对更大的 n 这里没有证明相应的上界：
这些词与一个独立的已通过实现的输出相同，在 1 到 1000 的每个 n 上都一致。

注意事项：

- 简单的前缀规则在 n = 2 时失效：aa 是一个回文，而 ab 需要两个；
- n = 8 时长尾巴还放不下，n = 11 时模式少一个回文，所以这两个长度使用搜索得到的词；
- 任何复杂度最大的词都可以，所以测试使用检查程序，用动态规划数回文。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1714_constructive.cpp](1714_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.031 s | 380 KB |
| [1714_constructive.go](1714_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1112 KB |
| [1714_constructive.java](1714_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.140 s | 1660 KB |
| [1714_constructive.py](1714_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 452 KB |
| [1714_constructive.rs](1714_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 224 KB |
