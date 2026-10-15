# 1700. 觉醒

[Timus 1700](https://acm.timus.ru/problem.aspx?space=1&num=1700) · 难度 482 · implementation

原题作者 Pavel Atnashev，出自 2009 年 4 月 4 日第十三届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

每个物体有一组联想词。对若干组物体中的每一组，按字母顺序输出所有物体共有的联想词；若没有，输出 “No solution.”。

## 输入

n（2 ≤ n ≤ 1000）行 “名称: 联想词 联想词 …”，然后是 m（1 ≤ m ≤ 1000）行，每行是至少两个物体名组成的一组。
单词由小写拉丁字母组成，每行不超过 250 个字符。

## 输出

每组一行。

## 样例

### 样例 1

输入：

```
6
whale: big black water animal
penguin: black white ice beak
piano: keyboard black white wire
jackboot: leather heel black
train: rail wheel black
rose: red green thorn
3
whale penguin piano jackboot train
penguin piano
jackboot rose
```

输出：

```
black
black white
No solution.
```

## 解法

以名称为键，把每个物体的联想词存成集合。对一组物体，求各成员集合的交集，排序后输出；若为空则输出 “No solution.”。
每行都很短；每组需要 `O(L²)` 次集合查询。对长为 L 的行，复杂度为 `O((n + m · L) · L log(n + L))`。

注意事项：

- 同一物体的联想词可能重复出现，但只输出一次（测试 02）；
- 一组中同一物体可能出现两次（测试 03）；
- 物体可能完全没有联想词，此时该行在冒号后就结束了。

答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1700_implementation.cpp](1700_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.359 s | 7788 KB |
| [1700_implementation.go](1700_implementation.go) | Go 1.14 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.765 s | 8908 KB |
| [1700_implementation.java](1700_implementation.java) | Java 1.8 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.437 s | 12376 KB |
| [1700_implementation.py](1700_implementation.py) | Python 3.12 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.390 s | 13524 KB |
| [1700_implementation.rs](1700_implementation.rs) | Rust 1.75 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.593 s | 3584 KB |
