# 1794. 世界建筑杰作

[Timus 1794](https://acm.timus.ru/problem.aspx?space=1&num=1794) · 难度 197 · implementation

原题作者 Vladislav Isenbaev（由 Oleg Dolgorukov 准备），出自 2010 年乌拉尔地区团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

n 个学生围成一圈坐着，按顺时针编号为 1 到 n，并按顺时针依次发言。学生 i 希望第 aᵢ 个发言。选择由谁第一个发言，使尽可能多的学生恰好在自己希望的顺序发言。任何最优选择都可以。

## 输入

n（2 ≤ n ≤ 10⁵），然后是 a₁、…、aₙ（1 ≤ aᵢ ≤ n）。

## 输出

第一个发言的学生编号。

## 样例

### 样例 1

输入：

```
4
4 1 2 3
```

输出：

```
2
```

### 样例 2

输入：

```
3
1 1 1
```

输出：

```
3
```

## 解法

若学生 k 先发言，学生 i 在第 ((i − k) mod n) + 1 个发言。所以只有一个起点能满足学生 i：k = ((i − aᵢ) mod n) + 1。
统计所有学生的这些投票，输出得票最多的起点。`O(n)`。

第一个样例中四个学生都投给起点 2：例如学生 1 想第四个发言，而顺序 2、3、4、1 正好让他排在第四。

注意事项：

- i − aᵢ 可能为负，而在 C++、Go 和 Java 中此时余数也是负的；
- 几个起点可能票数相同，如第二个样例，三个中任何一个都可以。

检查器自己统计票数，接受任何得票最多的起点。在 300 个小班级上它与对所有起点的直接统计一致，在大班级上答案与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1794_implementation.cpp](1794_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.078 s | 588 KB |
| [1794_implementation.go](1794_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 2400 KB |
| [1794_implementation.java](1794_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 812 KB |
| [1794_implementation.py](1794_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 8340 KB |
| [1794_implementation.rs](1794_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 2136 KB |
