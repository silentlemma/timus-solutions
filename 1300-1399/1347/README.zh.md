# 1347. 博客

[Timus 1347](https://acm.timus.ru/problem.aspx?space=1&num=1347) · 难度 1362 · parsing

原题作者 Den Raskovalov，出自 2005 年 3 月中学生锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

N ≤ 100 位博主各写一个博客，并用 `<friend>名字</friend>` 标记自己读的人。按输入顺序，对每位博主输出三个按
字母顺序排好的列表：这位博主提到的人、提到这位博主的博主，以及同时出现在两个列表中的人。博主不会是自己的朋友。
名字区分大小写，由拉丁字母和 `_` 组成。

时间限制：0.4 秒。内存限制：64 MB。

## 输入

N，然后对每个博客，先是作者名字占一行，再是以 `<blog>` 开头、以 `</blog>` 结尾的博客内容。博客最多 1000 行，
每行最多 255 个字符，输入的最后一行可能没有换行符。

## 输出

对每位博主输出名字和三行，分别以 `1: `、`2: `、`3: ` 开头，名字之间用逗号加空格分隔；博主之间空一行。

## 样例

### 样例 1

输入：

```
3
xoposhiy
<blog>
Tomorrow I found <friend>_denplusplus_</friend> to
 be <b>smartest</b> blogger in the net.
Also I received interesting link from
 <friend>strange_human</friend>
</blog>
_denplusplus_
<blog>
Some shit about my work.
</blog>
strange_human
<blog>
<friend>xoposhiy</friend>
<friend>_denplusplus_</friend>
</blog>
```

输出：

```
xoposhiy
1: _denplusplus_, strange_human
2: strange_human
3: strange_human

_denplusplus_
1: 
2: strange_human, xoposhiy
3: 

strange_human
1: _denplusplus_, xoposhiy
2: xoposhiy
3: xoposhiy
```

## 解法

从名字那一行读到第一个包含 `</blog>` 的行，就是一个博客，这一行也可能就是 `<blog>` 所在的行。每个 `<friend>`
到下一个 `</friend>` 给出一个名字：两者之间的内容，去掉其他标签并修剪空格。这些名字去掉博主本人后就是列表 1。
某位博主的列表 2 是列表 1 中含有其名字的其他博主的集合，列表 3 是两者的交集。所有列表都按字符编码排序，所以
`_` 排在大写字母之后、小写字母之前。这里 L 为输入长度，S 为名字的最大长度，K 为不同名字的数量（至少为 2）；
哈希集合的复杂度按期望时间计算。

注意事项：

- 提到自己不算（测试 02）；
- 朋友标签中名字周围可能有空格或其他标签（测试 03）；
- 整个博客可能只占一行（测试 04）；
- 没有博客的人可以是朋友，但不会提到任何人（测试 05）；
- `Bob` 和 `bob` 是不同的人，被多次提到的朋友只列一次（测试 06）；
- 空列表输出为带空格的 `1: `。

## 各语言说明

- 五种解答都一次读入全部输入，并把标签当作普通文本查找。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1347_parsing.cpp](1347_parsing.cpp) | G++ 13.2 x64 | parsing | O((L + N K S) log K) | AC | 0.015 s | 4996 KB |
| [1347_parsing.go](1347_parsing.go) | Go 1.14 x64 | parsing | O((L + N K S) log K) | AC | 0.031 s | 9156 KB |
| [1347_parsing.java](1347_parsing.java) | Java 1.8 | parsing | O((L + N K S) log K) | AC | 0.140 s | 16724 KB |
| [1347_parsing.py](1347_parsing.py) | Python 3.12 x64 | parsing | O((L + N K S) log K) | AC | 0.140 s | 5328 KB |
| [1347_parsing.rs](1347_parsing.rs) | Rust 1.75 x64 | parsing | O((L + N K S) log K) | AC | 0.015 s | 4076 KB |
