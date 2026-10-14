# 1601. 反大写

[Timus 1601](https://acm.timus.ru/problem.aspx?space=1&num=1601) · 难度 92 · implementation

原题作者 Denis Musin，出自 2008 年 3 月 1 日第九届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Angela 在聊天室里全用大写字母写消息。要修正一条不超过 10000 个字符的消息：句子以 `.`、`!` 或 `?` 结尾，
每句的第一个字母保持大写，其余字母都变成小写。空格、换行以及 `,`、`-`、`:` 保持不变。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

消息。

## 输出

修正后的消息。

## 样例

### 样例 1

输入:

```
HI THERE!
HOW DID YOU KNOW I AM A BLONDE?
```

输出:

```
Hi there!
How did you know i am a blonde?
```

## 解法

把消息扫一遍，记住下一个字母是否开启新句子。开头以及每个 `.`、`!` 或 `?` 之后都是如此；此后的第一个字母保持大写，
其余字母一律变成小写。其他字符（包括换行）原样复制，所以按原始字节处理消息：`O(n)`。结果已在生成的消息上
与独立实现逐字节对照。

注意事项：

- 一个句子可能跨越多行，所以换行不开启新句子（测试 04）；
- 逗号、破折号和冒号不结束句子（测试 02）；
- 标点可能紧挨着字母而没有空格（测试 03），而像 `?!` 这样的连续标点只结束一个句子，而不是两个。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1601_implementation.cpp](1601_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 88 KB |
| [1601_implementation.go](1601_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 936 KB |
| [1601_implementation.java](1601_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 432 KB |
| [1601_implementation.py](1601_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 436 KB |
| [1601_implementation.rs](1601_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 236 KB |
