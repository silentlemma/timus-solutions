# 1612. 电车论坛

[Timus 1612](https://acm.timus.ru/problem.aspx?space=1&num=1612) · 难度 151 · strings

原题作者 Alexander Ipatov，由 Denis Musin 准备，出自 2008 年 3 月 29 日第十二届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

论坛上一条不超过 10000 个字符的消息由小写拉丁字母、空格、换行和标点 `. , - : ! ?` 组成。若其中单词 `tram`
出现得比 `trolleybus` 多，作者是电车司机；反之是无轨电车司机；否则是公交车司机。单词是由字母组成的连续片段。
这条消息是谁写的？

时间限制：0.5 秒。内存限制：64 MB。

## 输入

消息。

## 输出

`Tram driver`、`Trolleybus driver` 或 `Bus driver`。

## 样例

### 样例 1

输入:

```
of course, tram is the best transport
in the world!
```

输出:

```
Tram driver
```

### 样例 2

输入:

```
yes, yekaterinburg trams are the
best trams in the world, but
i like my trolleybus too.
```

输出:

```
Trolleybus driver
```

### 样例 3

输入:

```
read forum.tr.ru every day!
you can learn much about tram 
drivers and trolleybus drivers.
```

输出:

```
Bus driver
```

## 解法

在每个非字母字符处把消息切成单词，分别统计等于 `tram` 和 `trolleybus` 的单词个数并比较：`O(n)`。
答案已在生成的消息上与独立实现对比过。

注意事项：

- 只有完整的单词才算：`trams`、`tramway` 或 `forum.tr.ru` 中的 `tr` 都不是单词 `tram`（样例 2 和 3）；
- 标点也分隔单词，所以 `tram-tram` 中有两个 tram，`tram,trolleybus` 中各有一个（测试 06 和 07）；
- 两个数相等（包括都为零）时是公交车司机。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1612_strings.cpp](1612_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 156 KB |
| [1612_strings.go](1612_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1124 KB |
| [1612_strings.java](1612_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 840 KB |
| [1612_strings.py](1612_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 444 KB |
| [1612_strings.rs](1612_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 232 KB |
