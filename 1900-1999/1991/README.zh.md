# 1991. 统计剩余供给与未消除目标

[Timus 1991](https://acm.timus.ru/problem.aspx?space=1&num=1991) · 难度 48 · implementation

原题作者 Denis Dublennykh（由 Egor Shchelkonogov 整理）。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 `n` 个独立组，每组恰有 `k` 个目标。第 `i` 组得到 `a_i` 单位供给，每单位只能使用一次，消除本组一个目标，且总能成功。组间不能交换供给。各组尽可能消除目标后，求未使用供给总数和剩余目标总数。

限制：`1≤n,k≤10000`，`0≤a_i≤100000`。时间限制 1 秒，内存限制 64 MB。

## 输入

第一行是 `n k`，第二行是 `n` 个供给数量。

## 输出

两个整数：先输出未使用供给总数，再输出剩余目标总数。

## 评测方式

按记号逐个比较输出。

## 样例

输入：

```
4 5
2 7 5 0
```

输出：

```
2 8
```

各组的 `(剩余供给,剩余目标)` 分别为 `(0,3)`、`(2,0)`、`(0,0)`、`(0,5)`，总和为 `(2,8)`。

## 解法

每组使用量不能超过供给数 `a_i`，也不能超过目标数 `k`。逐一配对恰好能形成 `b_i=min(a_i,k)` 对，此后一侧为空。因此本组剩余供给为 `a_i−b_i=max(a_i−k,0)`，剩余目标为 `k−b_i=max(k−a_i,0)`。

维护两个初始为零的累计值。如果 `a_i>k`，将 `a_i−k` 加入剩余供给，否则将 `k−a_i` 加入剩余目标。处理前 `j` 组后，两累计值恰为这些组的真实剩余总数：单组公式正确，且组间没有交换。该不变量证明处理全部 `n` 组后的答案正确。

不能先合并供给：某组供给过剩时，另一组仍可能有剩余目标。`a_i=k` 时两项均为零，`a_i=0` 时剩余全部 `k` 个目标。校验恒等式为 `剩余供给−剩余目标=Σa_i−nk`，但只靠它不能确定两个输出。

## 各语言说明

时间 `O(n)`，两个累计值占 `O(1)` 额外状态。C++、Go、Java 使用缓冲流依次读取。Python 保留 `O(n)` 个解析后的值，Rust 保留 `I` 个输入字节，所以实际输入存储分别是 `O(n)`、`O(I)`。Python 切片还创建一个 `O(n)` 临时数组，不改变时间复杂度。

未使用供给最大为 `10000·(100000−1)=999990000`，剩余目标最大为 `10000²=100000000`。两者都适合有符号 32 位，编译语言仍采用更宽的累计类型。Rust 在比较后才执行减法，避免无符号下溢。Java 的分词器能精确读取这些范围内的整数。无需排序、重新分配或浮点输出。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1991_implementation.cpp](1991_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 448 KB |
| [1991_implementation.go](1991_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1236 KB |
| [1991_implementation.java](1991_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 496 KB |
| [1991_implementation.py](1991_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 1380 KB |
| [1991_implementation.rs](1991_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 480 KB |
