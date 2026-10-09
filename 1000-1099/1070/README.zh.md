# 1070. 由往返航班求两个机场的时差

[Timus 1070](https://acm.timus.ru/problem.aspx?space=1&num=1070) · 难度 662 · bruteforce

原题作者 Magaz Asanov 与 Stanislav Vasiliev，出自 2001 年 2 月 Ural State University Personal Contest Online（Students Session）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个航班从一个机场飞往另一个机场，另一个航班飞回来。每个航班的起飞和到达时间都按事件发生地机场的当地时间给出。
两个机场的时钟相差整数个小时，不超过 5；每次飞行不超过 6 小时，两次飞行的时长相差不超过 10 分钟。求两个时钟的差。

时间限制：1 秒。内存限制：64 MB。

## 输入

两行，每行一个航班，给出 `HH.MM` 形式的起飞和到达时间。

## 输出

以小时为单位的差，一个非负整数。

## 评测方式

按记号逐个比较输出；多余的空白不影响结果。

## 样例

### 样例 1

输入：

```
23.42 00.39
08.10 17.11
```

输出：

```
4
```

## 题解

设第二个机场比第一个快 `k` 小时。则第一次飞行的实际时长是时钟读数之差减去 `k` 小时，第二次飞行的实际时长是
时钟读数之差加上 `k` 小时，两者都对一天取模，因为按时钟看，航班可能在起飞“之前”就降落。枚举 −5 到 5 的每个
`k`，保留两个时长都不超过 6 小时且相差不超过 10 分钟的那个。输出 `|k|`。`O(1)`。

只有一个 `k` 满足条件：`k` 每变化一小时，两个时长之差就变化两小时；而时长不超过 6 小时，跨越一天的取模也不会
产生第二个匹配。

注意事项：

- 航班可能跨过午夜，加上时差后，按时钟看甚至可能比起飞更早降落，所以时长要对 24 小时取模；
- `HH.MM` 不是十进制小数：小时和分钟要分开读取，不能当作实数读。

答案用另一种方法做了核对：枚举第一次飞行在六小时以内的每个实际时长，由它推出时差并检查返程航班，结果时差是
唯一的。

## 各语言说明

- C++ 用 `scanf("%d.%d")` 读取每个时间；其他语言在点处拆分记号。
- Python、Java（`Math.floorMod`）和 Rust（`rem_euclid`）的取模结果从不为负；C++ 和 Go 在第二次 `%` 前加上一天。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1070_bruteforce.cpp](1070_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.001 s | 128 KB |
| [1070_bruteforce.go](1070_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.015 s | 1080 KB |
| [1070_bruteforce.java](1070_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1552 KB |
| [1070_bruteforce.py](1070_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 368 KB |
| [1070_bruteforce.rs](1070_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.015 s | 208 KB |
