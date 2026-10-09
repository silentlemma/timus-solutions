# 1089. 用词典修正一个字母的拼写错误

[Timus 1089](https://acm.timus.ru/problem.aspx?space=1&num=1089) · 难度 840 · strings

原题作者 Anton Botov，出自 2001 年 3 月 4 日斯维尔德洛夫斯克州第三届中学生团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个最多 100 个小写单词（每个最多 8 个字母）的词典以一行 `#` 结束；其后是最多 1000 个单词的文本。单词是由
字母 `a`–`z` 组成的极长连续串。文本中每个不在词典里、但与某个词典单词恰好相差一个字母（长度相同，只有一个位置
不同）的单词，都要替换成那个词典单词；词典保证至多只有一种改法。输出修正后的文本，其他内容保持原样，然后输出
修正的次数。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

词典（每行一个单词）、一行 `#`，然后是文本。

## 输出

修正后的文本，然后单独一行输出修正次数。

## 评测方式

输出必须与期望文本相同；只忽略末尾的空白字符。

## 样例

### 样例 1

输入：

```
country
occupies
surface
covers
russia
largest
europe
part
about
world
#
the rushia is the larjest cauntry in the vorld.
it ockupies abaut one-seventh of the earth's surfase.
it kovers the eastern park of yurope and the northern park of asia.
```

输出：

```
the russia is the largest country in the world.
it occupies about one-seventh of the earth's surface.
it covers the eastern part of europe and the northern part of asia.
11
```

## 题解

逐个字符扫描文本。不是字母的字符原样复制；连续的字母构成一个单词。在词典中的单词保持不变。否则把它与所有
同样长度的词典单词比较，如果有一个恰好在一个位置上不同，就写下那个词典单词并记一次修正。`O(T · W · L)`，
其中 `T` 为文本单词数，`W` 为词典单词数，长度 `L ≤ 8`。

注意事项：

- 只有写错的字母可以修正，少写或多写一个字母不算，所以 `aple` 和 `appple` 保持不变；
- 已经在词典中的单词是正确的，即使另一个词典单词与它只差一个字母；
- 数字、撇号和连字符会把单词分开：`one-seventh` 是两个单词；
- 空格、标点和空行必须原样保留。

答案与在字母串上做正则替换（并检查每次修正的唯一性）的结果做了核对。

## 各语言说明

- Python 用 `re.sub` 和一个维护计数的函数。
- C++ 和 Java 逐行读取文本；Go、Python 和 Rust 一次读入全部文本再按换行拆分，并去掉回车符。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1089_strings.cpp](1089_strings.cpp) | G++ 13.2 x64 | strings | O(T · W · L) | AC | 0.015 s | 416 KB |
| [1089_strings.go](1089_strings.go) | Go 1.14 x64 | strings | O(T · W · L) | AC | 0.015 s | 1244 KB |
| [1089_strings.java](1089_strings.java) | Java 1.8 | strings | O(T · W · L) | AC | 0.125 s | 700 KB |
| [1089_strings.py](1089_strings.py) | Python 3.12 x64 | strings | O(T · W · L) | AC | 0.109 s | 496 KB |
| [1089_strings.rs](1089_strings.rs) | Rust 1.75 x64 | strings | O(T · W · L) | AC | 0.031 s | 464 KB |
