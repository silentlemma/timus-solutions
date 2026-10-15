# 1694. 杀手词

[Timus 1694](https://acm.timus.ru/problem.aspx?space=1&num=1694) · 难度 2856 · backtracking

原题作者 Alex Samsonov，出自 2009 年 2 月彼得罗扎沃茨克冬季集训的 Ural SU Contest。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

杀手词只使用前 m 个拉丁字母，是一个 k 次重复（同一个词连写 k 遍），且它的任何真子串都不是 k 次重复。
统计长度不超过 n 的杀手词个数。

## 输入

m, k, n（1 ≤ m ≤ 18；2 ≤ k ≤ 5；1 ≤ n ≤ 22）。

## 输出

杀手词的个数。

## 样例

### 样例 1

输入：

```
3 2 4
```

输出：

```
9
```

## 解法

杀手词就是 wᵏ，其中 w 的长度 L ≤ n / k，至多 11。wᵏ 是否合格与 w 用了哪些字母无关，只与它们的排列模式有关。
所以按首次出现的顺序给字母编号来枚举 w（先是 0，然后是 0 或 1，依此类推）。含 d 种不同字母的模式代表 m(m − 1)⋯(m − d + 1) 个词。

w 的任何子串都是 wᵏ 的子串，所以已经以 k 次重复结尾的 w 的前缀连同其所有延伸都可以舍弃。
对每个留下的 w 检查 wᵏ 本身。由于 w 中没有 k 次重复且 wᵏ 有周期 L，只需检查从第一份 w 开始并越过它的窗口。
即使 w 的幂不合格也要继续延伸，因为更长的 w 可能合格：(010)² 含有 00，而 (0102)² 合格。

按长度和字母种数统计的模式数与 m 的下降阶乘相乘后求和。k = 2、n = 22 时搜索约访问 10⁵ 个模式，k 更大时少得多。
最大答案 3.5 · 10¹³ 可以放进 64 位整数。

注意事项：

- 整个词不是真子串，所以 wᵏ 本身是允许的；
- 不能在 w 的幂不合格时停止（三字母的测试 06 需要这一点）；
- n < k 时根本没有词（测试 07）。

Python 解答以 PyPy 提交：本地 CPython 在 k = 2、n = 22 时约需 0.6 秒，离 1 秒的时限太近。

答案与小 m、n 下对所有词的计数一致，也与一个独立的已通过实现在 120 组参数上一致。

复杂度：`O(B(n/k)·n^3)`，其中 B(L) 是长度为 L 的字母模式数（贝尔数），每个模式用 O(n³) 检查。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1694_backtracking.cpp](1694_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(B(n/k)·n^3) | AC | 0.062 s | 192 KB |
| [1694_backtracking.go](1694_backtracking.go) | Go 1.14 x64 | backtracking | O(B(n/k)·n^3) | AC | 0.156 s | 1120 KB |
| [1694_backtracking.java](1694_backtracking.java) | Java 1.8 | backtracking | O(B(n/k)·n^3) | AC | 0.171 s | 1596 KB |
| [1694_backtracking.py](1694_backtracking.py) | PyPy 3.10 x64 | backtracking | O(B(n/k)·n^3) | AC | 0.546 s | 7688 KB |
| [1694_backtracking.rs](1694_backtracking.rs) | Rust 1.75 x64 | backtracking | O(B(n/k)·n^3) | AC | 0.078 s | 232 KB |
