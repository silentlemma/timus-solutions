# 1573. 炼金术

[Timus 1573](https://acm.timus.ru/problem.aspx?space=1&num=1573) · 难度 108 · math

原题作者 Alexander Ipatov，出自 2007 年 10 月第十四届斯维尔德洛夫斯克州中学生团体程序设计公开赛（USU Junior Contest）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Sandro 有三袋各不相同的试剂：B 个蓝色、R 个红色、Y 个黄色（各 1 … 100 个）。一种药水需要配方中每种颜色的试剂
各一个，颜色互不相同。求能配出药水的试剂组合数。

时间限制：1 秒。内存限制：64 MB。

## 输入

B、R 和 Y，然后是 K 以及配方中的 K 种颜色（Blue、Red 或 Yellow）。

## 输出

方法数。

## 样例

### 样例 1

输入:

```
2 3 5
3
Red
Yellow
Blue
```

输出:

```
30
```

## 解法

配方中的每种颜色从自己的袋子里取一个试剂，各次选择互相独立，所以答案是配方中提到的各袋大小的乘积，至多为
100³ = 10⁶。`O(K)`。

注意事项：

- 输入中袋子的顺序是蓝、红、黄，而样例的配方先列出红色；
- 只计配方中出现的颜色（测试 02、03）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1573_math.cpp](1573_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 416 KB |
| [1573_math.go](1573_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 1084 KB |
| [1573_math.java](1573_math.java) | Java 1.8 | math | O(K) | AC | 0.125 s | 1628 KB |
| [1573_math.py](1573_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.078 s | 452 KB |
| [1573_math.rs](1573_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.015 s | 408 KB |
