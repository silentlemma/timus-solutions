# 1738. 计算机安全

[Timus 1738](https://acm.timus.ru/problem.aspx?space=1&num=1738) · 难度 995 · implementation

原题作者 Daniil Ayzenshteyn，出自第十四届乌拉尔国立大学公开团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

员工编号为 1 到 n，每人有一个互不相同的四位十六进制 PIN 码。如果一个编号可以通过插入、删除或替换一位十进制数字（不能有前导零）
变成另一个，则两个编号相似。对每一对编号相似的员工，统计他们 PIN 码不同的位数，并报告有多少对在 1、2、3、4 位上不同。

## 输入

n（2 ≤ n ≤ 65 536），然后是员工 1 到 n 的 PIN 码。

## 输出

四个数：PIN 码在 1、2、3、4 位上不同的相似对各有多少。

## 样例

### 样例 1

输入：

```
3
dead
beef
f00d
```

输出：

```
0 0 2 1
```

## 解法

每一对都从较小的编号 i 来计。较大的编号 j 要么是 i 的某一位数字原地增大，要么是在 i 中插入一位数字；删除会得到更小的编号，那样的对从另一侧计入。

- 增大一位数字得到 j = i + (d − old)·10^q。不同的位置或数字给出不同的编号，所以没有重复，数字按顺序增大直到 j 超过 n。
- 插入使 j 多一位，所以只在 i 比 n 短时才需要。在相同数字旁插入同一数字会多次得到同一编号，所以这些候选经过集合去重，带前导零的丢弃。

PIN 码按数读入，两个 PIN 码不同的位置就是它们异或值中非零的十六进制位，用 65 536 项的表查得。每个编号有 `O(L)` 个候选，构造每个插入字符串需 `O(L)`。
总计 `O(n·L²)`，L 为十进制位数。

样例中 1、2、3 两两通过替换一位相似；`dead` 与 `beef` 有 3 位不同，`dead` 与 `f00d` 有 3 位，`beef` 与 `f00d` 有 4 位。

注意事项：

- 1 和 11 以两种方式相似（第二个 1 插在任一侧），但只算一对；
- 10 删除 0 后与 1 相似，但 01 不是编号，所以删除 10 中的 1 什么也得不到；
- 计数约达 120 万，32 位足够。

在最多 200 名员工的随机数据上，计数与检查所有对的结果一致；在大测试上与一个独立的已通过实现一致。
Python 解答在 PyPy 下运行；用 CPython 在这里处理 65 536 名员工约需 0.5 秒，离时限太近。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1738_implementation.cpp](1738_implementation.cpp) | G++ 13.2 x64 | implementation | O(n·L²) | AC | 0.171 s | 728 KB |
| [1738_implementation.go](1738_implementation.go) | Go 1.14 x64 | implementation | O(n·L²) | AC | 0.187 s | 7008 KB |
| [1738_implementation.java](1738_implementation.java) | Java 1.8 | implementation | O(n·L²) | AC | 0.265 s | 5820 KB |
| [1738_implementation.py](1738_implementation.py) | PyPy 3.10 x64 | implementation | O(n·L²) | AC | 0.328 s | 9528 KB |
| [1738_implementation.rs](1738_implementation.rs) | Rust 1.75 x64 | implementation | O(n·L²) | AC | 0.125 s | 1996 KB |
