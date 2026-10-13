# 1409. 两个强盗

[Timus 1409](https://acm.timus.ru/problem.aspx?space=1&num=1409) · 难度 15 · math

原题作者 Den Raskovalov，出自 2005 年 10 月 15 日第十二届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一排最多放着 10 个罐子。Harry 从左边开始逐个射击，Larry 从右边开始，最后一个
罐子被两人同时击中。已知各自击中的罐子数，求 Harry 没有击中的罐子数和 Larry
没有击中的罐子数。

时间限制：1 秒。内存限制：64 MB。

## 输入

Harry 和 Larry 击中的罐子数。

## 输出

Harry 和 Larry 没有击中的罐子数。

## 样例

### 样例 1

输入:

```
4 7
```

输出:

```
6 3
```

## 解法

共同的那个罐子在两个数里都算了一次，所以共有 H + L − 1 个罐子。Harry 没有击中
Larry 的其余 L − 1 个，Larry 没有击中 H − 1 个，答案是 L − 1 和 H − 1。
`O(1)`。

注意事项：

- Harry 的答案来自 Larry 的数，反之亦然，顺序容易弄反（测试 03）；
- 只有一个罐子时答案为 0 0（测试 02）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1409_math.cpp](1409_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 400 KB |
| [1409_math.go](1409_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1080 KB |
| [1409_math.java](1409_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1560 KB |
| [1409_math.py](1409_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.046 s | 360 KB |
| [1409_math.rs](1409_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 212 KB |
