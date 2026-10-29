# 1404. 轻松破解！

[Timus 1404](https://acm.timus.ru/problem.aspx?space=1&num=1404) · 难度 80 · implementation

原题作者 Vladimir Yakovlev，出自 2005 年 10 月 15 日第十二届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个不超过 100 个小写字母的单词这样加密：字母变为 0 到 25 的数，第一个数加 5，
之后每个数加上前一个数的新值，然后所有值对 26 取模再变回字母。给出密文，求原
来的单词。

时间限制：1 秒。内存限制：64 MB。

## 输入

加密后的单词。

## 输出

原来的单词。

## 样例

### 样例 1

输入:

```
xbduyr
```

输出:

```
secret
```

## 解法

第 k 个密文值等于第 k − 1 个密文值加上第 k 个字母，对 26 取模不会破坏这个关
系。所以每个字母就是它的编码减去前一个编码再对 26 取模，第一个编码之前视为 5。
`O(n)`。

注意事项：

- 差可能为负，需要调回 0 … 25（测试 03，z 加密成 e 再解回来）；
- 加密时的和在取模前会超过 25，但输入中的编码已经取过模，这就足够了。

测试由加密单词得到，按精确比较判定。

## 优化解法

优化解法（C++、Java）用 `getchar` 和 `System.in.read`（而不是 `iostream` 和
`Scanner`）一边读一边逐个解密字母，不把单词存成字符串：C++ 用 `putchar` 立即输出
每个字母，Java 把它们收集到 101 字节的数组中一次写出。模 26 的差取为
`(code − previous + 26) % 26`，它永远不会是负数。C++ 为 84 KB，而不是 360 KB；
Java 为 328 KB，而不是 1612 KB；两者时间都不变。

## 解答

### 简单版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1404_implementation.cpp](1404_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 360 KB | 11286038 |
| [1404_implementation.go](1404_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1068 KB | 11286039 |
| [1404_implementation.java](1404_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 1612 KB | 11286041 |
| [1404_implementation.py](1404_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 352 KB | 11286040 |
| [1404_implementation.rs](1404_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 208 KB | 11286042 |

### 优化版本

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 | 提交编号 |
|----|----|----|-----|------|----|----|------|
| [1404_implementation_optimized.cpp](1404_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 84 KB | 11303604 |
| [1404_implementation_optimized.java](1404_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 328 KB | 11303464 |
