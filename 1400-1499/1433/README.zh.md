# 1433. 四面体

[Timus 1433](https://acm.timus.ru/problem.aspx?space=1&num=1433) · 难度 264 · bruteforce

原题作者 Pavel Egorov 与 Stanislav Vasiliev，出自 2006 年 2 月 25 日第七届乌拉尔国立大学个人公开赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

两个同样大小的正四面体，每个面都涂成 R、G、B 或 Y。两者的颜色按同样的顺序列出：
底面、左前面、右前面和后面。若其中一个四面体可以转动成与另一个完全一样，输出
"equal"，否则输出 "different"。

时间限制：1 秒。内存限制：64 MB。

## 输入

两行，每行四个字母。

## 输出

"equal" 或 "different"。

## 样例

### 样例 1

输入:

```
RGRB
GRRB
```

输出:

```
equal
```

## 解法

转动四面体会置换它的四个面，所有转动恰好给出 12 个偶置换：绕过顶点的轴转动使三个
面循环，绕过两条对棱中点的轴转半圈交换两对面，而奇置换（例如一次对换）则是镜像。
所以枚举四个面的全部 24 种排列，保留逆序数为偶数的，检查其中是否有一个把第一种涂
色变成第二种。`O(1)`。

注意事项：

- 镜像是不同的：四种颜色互不相同时，交换两个面不是转动（测试 03、11）；
- 有重复颜色时，同样颜色的任何排列都相等，因为交换两个同色面可以修正奇偶性
  （测试 05、07、08、12）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1433_bruteforce.cpp](1433_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 360 KB |
| [1433_bruteforce.go](1433_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1084 KB |
| [1433_bruteforce.java](1433_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1568 KB |
| [1433_bruteforce.py](1433_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 440 KB |
| [1433_bruteforce.rs](1433_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 224 KB |
