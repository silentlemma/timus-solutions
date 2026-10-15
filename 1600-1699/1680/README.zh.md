# 1680. 第一个未出线名次

[Timus 1680](https://acm.timus.ru/problem.aspx?space=1&num=1680) · 难度 224 · strings

原题作者 Dmitry Ivankov，由 Alexander Ipatov 准备，出自 2009 年 2 月 28 日第十届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

半决赛向总决赛输送 q 支队伍，每所大学至多一支：凡是排在本校另一支队伍之后的队伍都会从排名表中划掉。
输出划掉之后位于第 q + 1 名的队伍。

## 输入

年份、n（n ≤ 201）和 q（3 ≤ q ≤ 12），然后按名次给出 n 支队伍。
队伍写作大学名、一个空格、'#' 和 1 到 8 的编号；只有一支队伍的大学可以不写编号。
名称由拉丁字母、空格、'.'、'-' 和 '&' 组成，长度不超过 36，两所大学的名称不会只在大小写上不同。答案一定存在。

## 输出

该队伍在排名表中的写法。

## 样例

### 样例 1

输入：

```
1999 10 6
St Petersburg SU #1
Belarusian SU #1
Moscow SU #4
Southern Ural SU
Moscow SU #1
Novosibirsk SU #1
St Petersburg SU #3
Belarusian SU #3
St Petersburg IFMO #1
Ural SU #3
```

输出：

```
Ural SU #3
```

## 解法

沿排名表往下走，维护已有队伍进入名单的大学集合。队伍所属的大学是最后一个 '#' 之前的文本去掉末尾空格，
没有 '#' 时就是整行。既然两所大学的名称不会只在大小写上不同，就用小写来比较。
所属大学已在集合中的队伍跳过；否则若集合里已有 q 所大学，这支队伍就是答案，若没有，则把它的大学加入集合。
名称长度为 L 时 `O(n · L)`。

注意事项：

- 同一所大学可能以不同的大小写出现（“Ural SU” 和 “URAL SU”，测试 02），所以比较时忽略大小写；
- 名称要整体比较：“Ural SU” 和 “Ural SU State” 是不同的大学（测试 03）；
- 按输入原样输出队伍，包括编号。

答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1680_strings.cpp](1680_strings.cpp) | G++ 13.2 x64 | strings | O(n · L) | AC | 0.015 s | 420 KB |
| [1680_strings.go](1680_strings.go) | Go 1.14 x64 | strings | O(n · L) | AC | 0.015 s | 1088 KB |
| [1680_strings.java](1680_strings.java) | Java 1.8 | strings | O(n · L) | AC | 0.078 s | 472 KB |
| [1680_strings.py](1680_strings.py) | Python 3.12 x64 | strings | O(n · L) | AC | 0.078 s | 456 KB |
| [1680_strings.rs](1680_strings.rs) | Rust 1.75 x64 | strings | O(n · L) | AC | 0.015 s | 432 KB |
