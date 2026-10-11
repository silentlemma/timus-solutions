# 1243. 七个小矮人平分后剩下的东西

[Timus 1243](https://acm.timus.ru/problem.aspx?space=1&num=1243) · 难度 49 · math

原题作者 Stanislav Vasilyev，出自 2003 年 3 月 1 日乌拉尔国立大学个人赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

七个小矮人平分 N 件相同的东西（1 ≤ N ≤ 10⁵⁰），分不匀的部分归白雪公主。白雪公主能得到
多少件？

时间限制：1 秒。内存限制：64 MB。

## 输入

N。

## 输出

N mod 7。

## 样例

### 样例 1

输入：

```
123456123456
```

输出：

```
1
```

## 解法

答案是 N 除以 7 的余数，但 N 最多有 51 位，远超 64 位整数。把 N 当作字符串读入，
只保存其前缀的余数，就能逐位得到它：`rest = (rest · 10 + 数字) mod 7`。`O(len N)`。

注意事项：

- 仅 20 位数就已经超出 64 位整数（测试 gen4）。

## 各语言说明

- Python 的整数能精确表示 N，所以直接用 `int(N) % 7`；其他语言逐位折叠。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1243_math.cpp](1243_math.cpp) | G++ 13.2 x64 | math | O(len N) | AC | 0.015 s | 380 KB |
| [1243_math.go](1243_math.go) | Go 1.14 x64 | math | O(len N) | AC | 0.046 s | 1060 KB |
| [1243_math.java](1243_math.java) | Java 1.8 | math | O(len N) | AC | 0.078 s | 400 KB |
| [1243_math.py](1243_math.py) | Python 3.12 x64 | math | O(len N) | AC | 0.046 s | 328 KB |
| [1243_math.rs](1243_math.rs) | Rust 1.75 x64 | math | O(len N) | AC | 0.046 s | 216 KB |
