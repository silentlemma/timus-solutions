# 1253. 展开讣告模板

[Timus 1253](https://acm.timus.ru/problem.aspx?space=1&num=1253) · 难度 690 · strings

原题作者 Leonid Volkov，出自 2003 年 3 月 15 日乌拉尔国立大学公开团体赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

有 N 个模板（N ≤ 9），每个至多 1000 个字符，可能占多行。模板中的 `*M` 表示引用模板 M
（每个模板至多 10 个引用）。展开模板 1：把每个引用替换为对应模板的文本，反复进行，
直到没有引用为止。若结果有限且不超过 10⁶ 个字符，就输出它，否则输出 `#`。

时间限制：1 秒。内存限制：64 MB。

## 输入

第一行是 N；然后是各个模板，每个从新的一行开始，以 `#` 结束。

## 输出

展开后的文本，或 `#`。

## 样例

### 样例 1

输入：

```
7
She w*7s *7 *2 wom*7n.
*3#
wonderful#
Everyone loved her *5.
We will miss her *5.#
Some text *6#
very much#
Another text *4#
a#
```

输出：

```
She was a wonderful woman.
Everyone loved her very much.
We will miss her very much.
```

## 解法

展开模板 1 永不结束，当且仅当从它可以到达一个引用环；否则它的长度是确定的：
`size(i) = 普通字符数 + Σ size(被引用的模板)`。从模板 1 出发的深度优先搜索计算这些
长度，并标记正在展开的模板；再次遇到这样的模板就说明有环。长度在略超过 10⁶ 时截断，
因为八层、每层十个引用可以产生 10⁸ · 1000 个字符。如果没有环且 `size(1)` ≤ 10⁶，
就用同样的递归把文本写出来。时间为 `O(S + L + 10^N)`，Python 为 `O(N(S + L))`，
其中 S 是输入大小，L 是输出长度。

注意事项：

- 模板 1 到达不了的模板之间的环是无害的（测试 03）；
- 上限包含等号：恰好 10⁶ 个字符要输出，多一个就是 `#`（gen1 和 gen2）；
- 每个 `#` 后面紧跟的换行分隔各个模板，但模板内部的换行是其文本的一部分，模板也可能
  为空；
- 模板编号只有一位，所以 `*21` 是对模板 2 的引用，后面跟着数字 1（测试 08）。

## 各语言说明

- Python 把每个模板按 `*` 拆分一次并记住展开结果；其他语言逐字符处理，直接把文本写入
  一个缓冲区。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1253_strings.cpp](1253_strings.cpp) | G++ 13.2 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 2280 KB |
| [1253_strings.go](1253_strings.go) | Go 1.14 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 972 KB |
| [1253_strings.java](1253_strings.java) | Java 1.8 | strings | O(S + L + 10^N) | AC | 0.093 s | 6120 KB |
| [1253_strings.py](1253_strings.py) | Python 3.12 x64 | strings | O(N(S + L)) | AC | 0.078 s | 4556 KB |
| [1253_strings.rs](1253_strings.rs) | Rust 1.75 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 2080 KB |
