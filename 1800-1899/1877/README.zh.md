# 1877. 自行车密码

[Timus 1877](https://acm.timus.ru/problem.aspx?space=1&num=1877) · 难度 19 · implementation

原题作者 Denis Mukhametianov，出自 2011 年乌拉尔地区中学生程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

Den 有两把四位密码的自行车锁，每晚轮流使用，小偷第一次来的那晚用的是第一把锁。小偷那晚试 0000，下一晚试 0001，依此类推。小偷最终能打开锁吗？

## 输入

第一把和第二把锁的密码，各四位数字。

## 输出

如果小偷某晚能打开锁输出 "yes"，否则输出 "no"。

## 样例

### 样例 1

输入：

```
0001
0000
```

输出：

```
no
```

### 样例 2

输入：

```
0002
0001
```

输出：

```
yes
```

## 解法

第 k 晚（从 0 开始）小偷试密码 k，而 k 为偶数时自行车锁在第一把锁上，k 为奇数时锁在第二把上。所以第一把锁的密码为偶数时会被打开，第二把锁的密码为奇数时会被打开，否则自行车安全。`O(1)`。

第一个样例中第一个密码是奇数、第二个是偶数，所以哪把锁都不会被试到自己的密码。

注意事项：

- 带前导零的密码必须按十进制读入；Go 的 `fmt.Scan` 会把 "0009" 当作八进制而出错，所以 Go 解法读入字符串；
- 只有每个密码的奇偶性重要，与哪个更小无关。

答案在所有测试上与一个独立的已通过实现一致。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1877_implementation.cpp](1877_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 120 KB |
| [1877_implementation.go](1877_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB |
| [1877_implementation.java](1877_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1572 KB |
| [1877_implementation.py](1877_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 404 KB |
| [1877_implementation.rs](1877_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 216 KB |
