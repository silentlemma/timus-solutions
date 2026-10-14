# 1603. 博学者

[Timus 1603](https://acm.timus.ru/problem.aspx?space=1&num=1603) · 难度 255 · implementation

原题作者 Vladimir Yakovlev，出自 2008 年 3 月 1 日第九届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个 4 × 4 的表格中填着小写字母。单词可以沿着水平或竖直相邻的格子组成的路径写出，路径可以在任意处直角转弯，
但不能重复经过同一格。对最多 100 个长度为 1 到 16 的单词，判断能否在表中找到。

时间限制：1 秒。内存限制：64 MB。

## 输入

表格的四行，然后是 n 和各个单词。

## 输出

每个单词输出 `word: YES` 或 `word: NO`。

## 样例

### 样例 1

输入:

```
abra
adac
babr
arca
3
abracadabra
ababaab
ababaaba
```

输出:

```
abracadabra: YES
ababaab: YES
ababaaba: NO
```

## 解法

从每个写着首字母的格子开始深度优先搜索，每步走到一个未用过、写着下一个字母的相邻格子。已用过的格子构成 16 位掩码。
重复的字母会让搜索多次进入同一局面：同样的已用格子集合、同样的最后一格、同样的剩余单词。所以失败的
(掩码, 格子) 对会被记住，不再重复搜索；这样的对至多 16·2¹⁶ 个，实际能到达的少得多。另有一个快速检查，
先排除需要某个字母多于表中数量的单词。

结果已在生成的表格上与独立实现对照，包括单一重复字母配长单词的表格。

注意事项：

- 若不记住失败状态，十五个相同字母的表格加上一个放不下的 16 字母单词，会让搜索遍历所有不自交的路径（测试 04 和 07）；
- 这样的 NO 可能单由奇偶性导致：把表格按国际象棋盘染色，16 格的路径总是在另一种颜色上结束，
  所以首尾格子同色的单词不可能占满全部 16 格（测试 07）；
- 格子不能用两次，而且只能水平或竖直走（测试 03）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1603_implementation.cpp](1603_implementation.cpp) | G++ 13.2 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 452 KB |
| [1603_implementation.go](1603_implementation.go) | Go 1.14 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 5708 KB |
| [1603_implementation.java](1603_implementation.java) | Java 1.8 | implementation | O(n·16·2^16) | AC | 0.109 s | 5228 KB |
| [1603_implementation.py](1603_implementation.py) | Python 3.12 x64 | implementation | O(n·16·2^16) | AC | 0.359 s | 21264 KB |
| [1603_implementation.rs](1603_implementation.rs) | Rust 1.75 x64 | implementation | O(n·16·2^16) | AC | 0.062 s | 420 KB |
