# 1278. “… Connecting people”

[Timus 1278](https://acm.timus.ru/problem.aspx?space=1&num=1278) · 难度 988 · constructive

原题作者 Sergey Volchenkov、Vladimir Pinaev 和 Michael Kopachev，出自 2003 年 10 月 15–16 日在雷宾斯克举行的 ACM ICPC 2003–2004 俄罗斯中部赛区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一个声音处理器只有两条指令，每个内存单元放一条。`CALL X` 把下一个单元的地址压入容量为
100 的栈，并跳到单元 X。`BELL&RET` 响一声，然后返回到栈顶的地址；若栈为空则停止。执行从
单元 0 开始。写一个最多 100 条指令、唯一的 `BELL&RET` 放在最后的程序，使它恰好响 K 次
（1 ≤ K ≤ 10⁹）。

时间限制：1 秒。内存限制：64 MB。

## 输入

K。

## 输出

程序，每行一条指令，从单元 0 开始。

## 评测方式

可行的程序很多，所以评测程序接受任意一个：它检查每一行的格式以及每次调用是否指向后面，
然后从最后一个单元向上计算从每个单元开始的响声数，检查栈深度和总数。

## 样例

### 样例 1

输入：

```
4
```

输出：

```
CALL 1
CALL 2
BELL&RET
```

### 样例 2

输入：

```
1
```

输出：

```
BELL&RET
```

## 解法

设 bells(i) 为处理器从单元 i 开始执行、直到这次执行返回为止所发出的响声数。最后一个单元
的 bells = 1。单元 i 中的 `CALL X` 先从 X 执行，再从 i + 1 执行，所以
bells(i) = bells(X) + bells(i + 1)。X 只需两种取法：

- `CALL i+1` 使其翻倍：bells(i) = 2 · bells(i + 1)；
- 调用最后一个单元使其加一：bells(i) = bells(i + 1) + 1。

从最后一个单元向上，从 1 开始，依次处理 K 在最高位 1 之后的二进制位：每一位都翻倍，遇到
1 再加一。K 小于 2³⁰ 时最多需要 29 次翻倍和 29 次加一，连同响铃共 59 个单元。所有调用都
指向后面，所以栈中每个单元最多一个地址。`O(log K)`。

注意事项：

- K = 1 时程序只有一条 `BELL&RET`（测试 02）；
- 调用同一个或更早的单元会无限地调用自己并使栈溢出，所以调用都不能指向前面；
- 程序从单元 0 开始读取，所以自下而上构造的单元要倒序输出。

另外把 299 以内的所有 K 在一个逐条执行的处理器模型上运行过，所有测试的答案也都通过了评测
程序。

## 各语言说明

- 所有语言都以同样的方式遍历 K 的二进制位。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1278_constructive.cpp](1278_constructive.cpp) | G++ 13.2 x64 | constructive | O(log K) | AC | 0.015 s | 192 KB |
| [1278_constructive.go](1278_constructive.go) | Go 1.14 x64 | constructive | O(log K) | AC | 0.031 s | 1096 KB |
| [1278_constructive.java](1278_constructive.java) | Java 1.8 | constructive | O(log K) | AC | 0.109 s | 1656 KB |
| [1278_constructive.py](1278_constructive.py) | Python 3.12 x64 | constructive | O(log K) | AC | 0.093 s | 448 KB |
| [1278_constructive.rs](1278_constructive.rs) | Rust 1.75 x64 | constructive | O(log K) | AC | 0.015 s | 244 KB |
