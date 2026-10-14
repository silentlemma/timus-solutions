# 1517. 选择的自由

[Timus 1517](https://acm.timus.ru/problem.aspx?space=1&num=1517) · 难度 240 · suffix_structures

原题作者 Ilya Grebnov、Nikita Rybak 与 Dmitry Kovalioff，出自 Timus Top Coders: Third Challenge。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给出两篇各由 N 个大写拉丁字母组成的演讲（1 ≤ N ≤ 100000）。输出它们最长的公共片段：
在两篇中都作为连续部分出现的最长字符串。任何一个最长的都可以。

时间限制：2 秒。内存限制：64 MB。

## 输入

N，然后是两篇演讲，各占一行。

## 输出

最长公共片段；两篇没有共同字母时输出空行。

## 样例

### 样例 1

输入:

```
28
VOTEFORTHEGREATALBANIAFORYOU
CHOOSETHEGREATALBANIANFUTURE
```

输出:

```
THEGREATALBANIA
```

## 解法

为第一篇演讲建后缀自动机：它的状态是结束位置集合相同的子串类，每个类记录其中最长串
的长度，以及指向其更短后缀所在类的后缀链接。状态数不超过 2N，逐字母构建，`O(N)`。然
后让第二篇演讲在自动机上走，维护当前状态和已读部分中在第一篇里出现的最长后缀的长度
run。下一个字母没有转移时，沿后缀链接回退，并把 run 设为到达状态的长度，直到有该转
移或回到起点；然后走转移并加一。最大的 run 及其在第二篇中的结束位置给出答案。字母表
为 26 时 `O(N)`。

注意事项：

- 两篇可能没有共同字母，这时答案是空行（测试 03、gen5）；
- 答案可能是整篇演讲（gen4）；
- 比较所有位置对需要 10¹⁰ 步；
- 最长片段可能有很多，所以测试使用检查程序（所有测试）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1517_suffix_structures.cpp](1517_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.093 s | 29044 KB |
| [1517_suffix_structures.go](1517_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.046 s | 25012 KB |
| [1517_suffix_structures.java](1517_suffix_structures.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.203 s | 35156 KB |
| [1517_suffix_structures.py](1517_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(N) | AC | 0.500 s | 56240 KB |
| [1517_suffix_structures.rs](1517_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 28496 KB |
