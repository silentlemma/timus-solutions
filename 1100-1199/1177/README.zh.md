# 1177. 用 SQL like 模式匹配字符串

[Timus 1177](https://acm.timus.ru/problem.aspx?space=1&num=1177) · 难度 1249 · strings

原题作者 Pavel Atnashev，出自 2002 年 2 月 16 日在叶卡捷琳堡举行的第三届乌拉尔国立大学个人程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

回答至多 1000 个形如 `'字符串' like '模式'` 的问题。模式中，`%` 匹配任意长度
的任意字符，`_` 匹配任意一个字符，`[...]` 匹配由单个字符和范围 `c1-c2` 组成的
集合中的任意一个字符，`[^...]` 匹配不在这种集合中的任意一个字符；其他字符只
匹配自身。字符串和模式最长 100 个字符，字符编码在 32–255 之间，其中的引号写成
两个。

时间限制：1 秒。内存限制：64 MB。

## 输入

`N`，然后 `N` 行 `'字符串' like '模式'`。

## 输出

每行输出 `YES` 或 `NO`。

## 样例

### 样例 1

输入：

```
15
'abcde' like 'a'
'abcde' like 'a%'
'abcde' like '%a'
'abcde' like 'b'
'abcde' like 'b%'
'abcde' like '%b'
'25%' like '_5[%]'
'_52' like '[_]5%'
'ab' like 'a[a-cdf]'
'ad' like 'a[a-cdf]'
'ab' like 'a[-acdf]'
'a-' like 'a[-acdf]'
'[]' like '[[]]'
'''''' like '_'''
'U' like '[^a-zA-Z0-9]'
```

输出：

```
NO
YES
NO
NO
NO
NO
YES
YES
YES
YES
NO
YES
YES
YES
NO
```

## 解法

把每行按字节读入，并还原两部分中成对的引号。然后逐个元素扫描模式，维护长度
集合：长度 `i` 在集合中，当且仅当已扫描的模式部分恰好匹配字符串的前 `i` 个字节：

- 普通字节或 `_`：若下一个字节符合，就把每个 `i` 变成 `i + 1`；
- 集合：用它的成员判断做同样的事；
- `%`：保留从集合中最小长度开始的所有长度。

最后答案就是完整长度是否在集合中。每个问题 `O(n·m)`。

集合语法需要小心。`[` 之后可选的 `^` 表示取反；然后是直到第一个 `]` 为止的
各项。只有当存在第三个字符且它不是 `]` 时，`a-b` 才是范围，否则 `a` 和 `-` 是
两个单独的字符，所以 `[-acdf]` 和 `[a-]` 都包含减号，而 `[[]` 是只含 `[` 的
集合。没有闭合 `]` 的 `[` 什么也匹配不上。

注意事项：

- 编码大于 127 的字符是单个字节，必须按无符号字节比较和判断范围，而不能当作
  文本解码；
- 空模式只匹配空字符串，`%` 也能匹配空字符串；
- 端点颠倒的范围，例如 `[c-a]`，是空的。

答案已在 60,000 个包含引号、方括号、`^`、`-`、高位字节和未闭合集合的随机问题
上，与另一份独立编写的解答比对。

## 各语言说明

- Python 用大整数位掩码保存长度集合，字符串的每种字节各有一个掩码；其他语言
  每一步使用布尔数组。Java 以 Latin-1 读入，使每个字节都变成编码相同的字符。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1177_strings.cpp](1177_strings.cpp) | G++ 13.2 x64 | strings | O(n·m) per question | AC | 0.031 s | 372 KB |
| [1177_strings.go](1177_strings.go) | Go 1.14 x64 | strings | O(n·m) per question | AC | 0.015 s | 5424 KB |
| [1177_strings.java](1177_strings.java) | Java 1.8 | strings | O(n·m) per question | AC | 0.093 s | 5036 KB |
| [1177_strings.py](1177_strings.py) | Python 3.12 x64 | strings | O(n·m) per question | AC | 0.203 s | 1132 KB |
| [1177_strings.rs](1177_strings.rs) | Rust 1.75 x64 | strings | O(n·m) per question | AC | 0.015 s | 736 KB |
