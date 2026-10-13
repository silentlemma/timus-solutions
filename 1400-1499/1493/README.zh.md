# 1493. 离幸运只差一步

[Timus 1493](https://acm.timus.ru/problem.aspx?space=1&num=1493) · 难度 47 · implementation

原题作者 Vladimir Yakovlev，出自 2006 年 10 月 14 日第十三届斯维尔德洛夫斯克州中学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

车票号码是六位数，前导零也算在内；若前三位与后三位的数字和相等，车票就是幸运的。
给定车票的两个和恰好相差一。若前一张或后一张车票是幸运的，输出 "Yes"，否则输出
"No"。

时间限制：1 秒。内存限制：64 MB。

## 输入

车票的六位数字。

## 输出

"Yes" 或 "No"。

## 样例

### 样例 1

输入:

```
715068
```

输出:

```
Yes
```

### 样例 2

输入:

```
445219
```

输出:

```
No
```

### 样例 3

输入:

```
012200
```

输出:

```
Yes
```

## 解法

直接检查两个相邻的号码：取号码减一和加一，各写成六位数，比较两半的数字和。给定
车票的两个和不相等，所以它既不是 000000 也不是 999999，两个邻居都是真实存在的车
票。进位可能一次改变好几位数字，所以要重新计算邻居，而不是只改一位。`O(1)`。

注意事项：

- 号码可能以零开头，这些零也是数字（测试 03）；把前导 0 当作八进制前缀的读法会
  出错；
- 跨过中间的进位或借位会同时改变两半，例如从 100000 到 099999（测试 06、08、
  09）；
- 邻居 000000 和 999999 也是幸运车票（测试 04、05）。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1493_implementation.cpp](1493_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 124 KB |
| [1493_implementation.go](1493_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB |
| [1493_implementation.java](1493_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1596 KB |
| [1493_implementation.py](1493_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.062 s | 376 KB |
| [1493_implementation.rs](1493_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.062 s | 224 KB |
