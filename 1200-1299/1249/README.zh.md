# 1249. 所有暗区都是矩形吗？

[Timus 1249](https://acm.timus.ru/problem.aspx?space=1&num=1249) · 难度 220 · implementation

原题作者 Nikita Shamgunov 和 Leonid Volkov，出自 2003 年 3 月 15 日乌拉尔国立大学公开团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

给定一幅由 0 和 1 组成的 N × M 图像（N, M ≤ 3000）。判断每个由 1 组成的连通区域
（格子以边相连）是否都是边与坐标轴平行的矩形。

时间限制：2.5 秒。内存限制：4 MB。

## 输入

N 和 M，然后是 N 行，每行 M 个用空格分隔的数字。

## 输出

`Yes` 或 `No`。

## 样例

### 样例 1

输入：

```
2 2
0 1
1 1
```

输出：

```
No
```

### 样例 2

输入：

```
3 3
0 0 1
1 1 0
1 1 0
```

输出：

```
Yes
```

## 解法

一个区域不是矩形，当且仅当它在某处有一个内角，而内角就是恰好有三个暗格的 2 × 2
窗口。反过来，如果没有任何窗口有三个暗格，每个区域都是矩形：沿着区域的边界走，
永远不会向内拐。所以整个检查就是：没有任何 2 × 2 窗口恰好含三个 1。

真正的限制是内存：图像最多有 900 万个格子，输入文本约 18 MB，而限制只有 4 MB。
一个窗口只需要两行，所以程序只保存上一行和当前行，以流的方式读入，并在第一个坏
窗口处停止。时间 `O(N·M)`，内存 `O(M)`。

注意事项：

- 一次读入全部输入或保存整幅图像都会超出 4 MB；
- 只在一个角相接的两个区域没问题：那个窗口里有两个暗格（第二个样例）。

该规则在 400 幅随机的小图像上与逐个找出区域并检查它是否填满其包围盒的结果比较过。

## 各语言说明

- Python 每次读一行，把它转成当作位集的整数，用位运算找坏窗口：四个位中 1 的个数
  为奇数且至少有两个。
- Java 和 Rust 通过一个小缓冲区逐字节读取输入。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1249_implementation.cpp](1249_implementation.cpp) | G++ 13.2 x64 | implementation | O(N·M) | AC | 0.531 s | 208 KB |
| [1249_implementation.go](1249_implementation.go) | Go 1.14 x64 | implementation | O(N·M) | AC | 0.093 s | 1096 KB |
| [1249_implementation.java](1249_implementation.java) | Java 1.8 | implementation | O(N·M) | AC | 0.156 s | 452 KB |
| [1249_implementation.py](1249_implementation.py) | Python 3.12 x64 | implementation | O(N·M) | AC | 0.218 s | 1532 KB |
| [1249_implementation.rs](1249_implementation.rs) | Rust 1.75 x64 | implementation | O(N·M) | AC | 0.031 s | 224 KB |
