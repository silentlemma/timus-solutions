# 1414. 天文数据库

[Timus 1414](https://acm.timus.ru/problem.aspx?space=1&num=1414) · 难度 431 · sorting, binary_search

原题作者 Pavel Egorov，出自 2005 年 10 月 29 日乌拉尔国立大学锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

星名数据库开始时只有一个名字 "sun"。之后是最多 10 000 个操作，每行一个："+name"
添加一个名字（之后可能再次添加），"?prefix" 查询以该前缀开头的名字。参数由 1 到
20 个小写拉丁字母或数字组成。对每个查询，先输出前缀，再按字典序输出匹配的名字，
不重复，每个缩进两个空格，最多输出前 20 个。

时间限制：2 秒。内存限制：64 MB。

## 输入

各个操作。

## 输出

各查询的答案。

## 样例

### 样例 1

输入:

```
?e
+earth
+egg
?e
+eagle
+earth
?ea
```

输出:

```
e
e
  earth
  egg
ea
  eagle
  earth
```

## 解法

用有序集合保存名字。具有给定前缀的名字在字典序中构成连续的一段，从前缀本身应插
入的位置开始，所以每个查询用二分查找找到该位置，然后向后走，直到名字不再以前缀
开头或已输出 20 个。C++、Java 和 Rust 使用树形集合；Go 和 Python 维护一个有序数
组并插入其中，每次添加最多移动 10 000 个引用。使用树形集合时为 `O(Q log Q)`。

注意事项：

- "sun" 从一开始就在数据库中（测试 02）；
- 重复添加的名字在答案中不能重复（测试 03）；
- 只输出前 20 个名字（测试 04）；
- 名字中可以有数字，数字排在字母之前（测试 07）；
- 样例中用点表示两个缩进空格。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1414_sorting.cpp](1414_sorting.cpp) | G++ 13.2 x64 | sorting | O(Q log Q) | AC | 0.031 s | 5748 KB |
| [1414_sorting.go](1414_sorting.go) | Go 1.14 x64 | sorting | O(Q log Q) | AC | 0.031 s | 1868 KB |
| [1414_sorting.java](1414_sorting.java) | Java 1.8 | sorting | O(Q log Q) | AC | 0.156 s | 24264 KB |
| [1414_sorting.py](1414_sorting.py) | Python 3.12 x64 | sorting | O(Q log Q) | AC | 0.156 s | 19372 KB |
| [1414_sorting.rs](1414_sorting.rs) | Rust 1.75 x64 | sorting | O(Q log Q) | AC | 0.031 s | 6144 KB |
