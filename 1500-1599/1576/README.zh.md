# 1576. 电话资费

[Timus 1576](https://acm.timus.ru/problem.aspx?space=1&num=1576) · 难度 147 · implementation

原题为民间流传的题目，出自 2007 年 10 月第十四届斯维尔德洛夫斯克州中学生团体程序设计公开赛（USU Junior Contest）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

三种资费：基本资费，月租 N1，每分钟 C1；组合资费，月租 N2 含 T 分钟，超出 T 的每分钟 C2；不限量资费，月租
N3。不超过 6 秒的通话免费，更长的通话按整分钟向上取整。给定至多 1000 次通话（格式 mm:ss），输出每种资费下的
月账单。

时间限制：1 秒。内存限制：64 MB。

## 输入

N1 和 C1，然后是 N2、T 和 C2，然后是 N3，再是 K 和 K 次通话时长。

## 输出

按样例格式输出三行。

## 样例

### 样例 1

输入:

```
135 1
220 10 1
300
5
00:05
00:10
09:59
07:00
01:01
```

输出:

```
Basic:     155
Combined:  230
Unlimited: 300
```

### 样例 2

输入:

```
10 2
100 1 1
1000
1
03:00
```

输出:

```
Basic:     16
Combined:  102
Unlimited: 1000
```

## 解法

把计费分钟数加起来：s 秒的通话在 s ≤ 6 时不计，否则计 ⌈s / 60⌉ 分钟。总共 M 分钟时，三种账单分别为
N1 + C1·M、N2 + C2·max(0, M − T) 和 N3，都小于 7·10⁷。`O(K)`。

注意事项：

- 恰好 6 秒的通话免费，7 秒的通话算一整分钟，恰好一分钟的通话算一分钟（测试 03）；
- 组合资费在分钟数不超过 T 时不额外收费，所以超出部分不会是负数；
- 标签按相同宽度对齐：`Basic:` 后五个空格，`Combined:` 后两个，`Unlimited:` 后一个。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1576_implementation.cpp](1576_implementation.cpp) | G++ 13.2 x64 | implementation | O(K) | AC | 0.015 s | 132 KB |
| [1576_implementation.go](1576_implementation.go) | Go 1.14 x64 | implementation | O(K) | AC | 0.015 s | 1168 KB |
| [1576_implementation.java](1576_implementation.java) | Java 1.8 | implementation | O(K) | AC | 0.109 s | 2244 KB |
| [1576_implementation.py](1576_implementation.py) | Python 3.12 x64 | implementation | O(K) | AC | 0.078 s | 508 KB |
| [1576_implementation.rs](1576_implementation.rs) | Rust 1.75 x64 | implementation | O(K) | AC | 0.015 s | 232 KB |
