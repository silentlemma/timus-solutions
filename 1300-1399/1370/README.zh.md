# 1370. 魔术师

[Timus 1370](https://acm.timus.ru/problem.aspx?space=1&num=1370) · 难度 88 · implementation

原题作者 Stanislav Vasiliev，出自 2005 年 4 月 19–24 日在叶卡捷琳堡举行的第九届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

轮子边缘写着 N 个数字（11 ≤ N ≤ 1000），窗口显示 10 个连续的数字，起初是第 1 到第 10 个。每响一声，轮子转过一个
数字，所以一声之后窗口显示第 2 到第 11 个数字。已知响了 M ≤ 32 767 声，输出窗口中的 10 个数字。

时间限制：1 秒。内存限制：64 MB。

## 输入

N 和 M，然后是 N 个数字，每行一个。

## 输出

窗口中的 10 个数字，包括前导零。

## 样例

### 样例 1

输入：

```
12 7
1
2
3
4
5
6
7
8
9
0
7
7
```

输出：

```
8907712345
```

## 解法

响 M 声之后，窗口从第 M 个数字开始（从 0 计数），而轮子是一圈，所以答案就是 i = 0 … 9 时的第 (M + i) mod N 个
数字。读入之后 `O(1)`。

注意事项：

- M 可能比 N 大很多倍（测试 05）；
- 窗口可能跨过最后一个数字（样例）；
- 答案按数字输出，保留前导零（测试 03）。

## 各语言说明

- 五种解答都把数字当作文本保存，再把窗口中的十个拼接起来。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1370_implementation.cpp](1370_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 196 KB |
| [1370_implementation.go](1370_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 1108 KB |
| [1370_implementation.java](1370_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1892 KB |
| [1370_implementation.py](1370_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.062 s | 404 KB |
| [1370_implementation.rs](1370_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 244 KB |
