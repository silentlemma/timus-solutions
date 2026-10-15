# 1654. 密信

[Timus 1654](https://acm.timus.ru/problem.aspx?space=1&num=1654) · 难度 60 · implementation

原题作者 Vladimir Yakovlev（创意来自 Alexander Klepinin），出自 NEERC 2008 东部分区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一段没有相邻相同字母的文本被加密：多次在任意位置插入一对相同的字母。删去所有插入的字母对，输出原文。

## 输入

一行，不超过 200000 个小写拉丁字母。

## 输出

还原后的文本（可能为空）。

## 样例

### 样例 1

输入：

```
wwstdaadierfflitzzz
```

输出：

```
stierlitz
```

## 解法

删去一对相邻相同字母，就像在每个字母都是自身逆元的群里约去 x · x = 1，这样的约化无论按什么顺序进行，
最后得到的文本都相同。原文没有相邻相同的字母，所以它正是这个约化形式。

用栈一遍即可求出：与栈顶相同的字母将其约去，其他字母入栈。`O(n)`。

易错点：

- 删除字母对可能让新的相同字母相邻（`abba` 会整体消失，测试 04），所以不用栈、只从左到右扫一遍是不够的；
- 三个相同字母剩下一个（测试 06）；
- 答案可能是空行（测试 02、04）。

在 60 个随机测试上，答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1654_implementation.cpp](1654_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 988 KB |
| [1654_implementation.go](1654_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 3072 KB |
| [1654_implementation.java](1654_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 3828 KB |
| [1654_implementation.py](1654_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 1424 KB |
| [1654_implementation.rs](1654_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 936 KB |
