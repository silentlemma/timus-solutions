# 1617. 车轮擦伤

[Timus 1617](https://acm.timus.ru/problem.aspx?space=1&num=1617) · 难度 65 · implementation

原题作者 Vladimir Yakovlev，出自 2008 年 3 月 29 日第十二届乌拉尔竞技编程锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

车库里有 n 个轮对（1 ≤ n ≤ 150），每个的直径是 600 到 700 毫米之间的整数。
一节电车车厢需要四个直径相同的轮对。最多能装备多少节车厢？

时间限制：0.5 秒。内存限制：64 MB。

## 输入

n，然后是 n 个直径。

## 输出

车厢数。

## 样例

### 样例 1

输入：

```
9
689
690
690
689
689
690
689
688
688
```

输出：

```
1
```

## 解法

统计每种直径的轮对数。有 c 对的直径能装备 ⌊c / 4⌋ 节车厢，不同直径互不影响，
所以答案是对所有直径求和。`O(n)`。

易错点：

- 不同直径剩下的轮对不能拼在一起（测试 01）；
- 同一尺寸的八对能装备两节车厢，而不是一节（测试 03）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1617_implementation.cpp](1617_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB |
| [1617_implementation.go](1617_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1092 KB |
| [1617_implementation.java](1617_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1680 KB |
| [1617_implementation.py](1617_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 368 KB |
| [1617_implementation.rs](1617_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 244 KB |
