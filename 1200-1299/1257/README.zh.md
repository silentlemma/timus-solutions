# 1257. 断字

[Timus 1257](https://acm.timus.ru/problem.aspx?space=1&num=1257) · 难度 1722 · implementation

原题作者 Den Raskovalov，出自 2003 年 10 月 11 日斯维尔德洛夫斯克州中学生公开团体程序设计竞赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

按断字规则把文本排到宽 40 个字符的页面上。单词是连续的拉丁字母；其他字符都是分隔符。
规则 `s1-s2`（最多 100 条，|s1| + |s2| ≤ 40）表示：以 s1s2 结尾（不区分大小写）的单词
可以在 s2 前断开，前半部分留在当前行并在后面加 `-`，s2 从下一行开始。输出的每一行
（包括 `-`）都不能超过 40 个字符。单词放不下时，选能放下且移到下一行的字母最少的规则；
没有能放下的规则时，整个单词移到下一行。空格、标点和文本中原有的换行都要保留。

时间限制：1 秒。内存限制：64 MB。

## 输入

N，接着 N 条规则，每行一条，然后是文本：最多 450 行，每行最多 250 个字符，单词最长
40 个字母。

## 输出

排好的文本。

## 样例

### 样例 1

输入：

```
12
un-usual
for-ced
re-al
sum-mer
N-ED
home-work
sec-ret
ho-lidays
Wi-zard
th-Er
L-so
Holi-days
Harry Potter was a highly unusual boy in many ways. 
For one thing, he hated the summer holidays more than any 
other time of year. For another, he really 
 wanted to do his homework but was forced to do it in 
secret, in the dead of night. And he also happened 
to be a wizard.
```

输出：

```
Harry Potter was a highly unusual boy in
 many ways. 
For one thing, he hated the summer holi-
days more than any 
other time of year. For another, he 
really 
 wanted to do his homework but was for-
ced to do it in 
secret, in the dead of night. And he al-
so happened 
to be a wizard.
```

## 解法

遍历文本，记录当前列：

- 换行符照抄，并把列归零；
- 其他分隔符照抄，但如果当前行已有 40 个字符，先输出换行；
- 放得下的单词照抄；
- 否则，在 s1s2 位于单词末尾（按小写比较）且前半部分加 `-` 仍放得下的规则中，取 s2
  最短的那条：输出前半部分、`-`、换行和 s2；若没有这样的规则，输出换行和整个单词。

单词最多 40 个字母，所以在新行上总能放下。对 L 个字符的文本，复杂度
`O(N · 40 + L · (1 + N · 40))`。

注意事项：

- 分隔符也会换到新行：满行之后的空格作为下一行的开头（样例中的 ` many ways.`），点号也
  一样（测试 02）；
- 输入中紧跟在满行之后的换行就是此处唯一的断行，不能再多输出一个（测试 03、10）；
- 文本末尾可能没有换行（测试 04）；
- 规则必须与单词的结尾匹配，而不是与其字母第一次出现的位置匹配（测试 05）；
- 规则不区分大小写（测试 06），最短的移行部分只在前半部分放得下的规则中比较
  （测试 07、12）；
- 只移一个字母的规则永远用不上：此时前半部分加 `-` 和整个单词一样长，而整个单词本来
  就放得下。

在 450 组随机文本上与一个独立实现比较过。

## 各语言说明

- 所有语言都按字节读入，去掉 `\r`，然后遍历一次文本。
- Java 按 ISO-8859-1 解码和输出，使每个字节仍是一个字符。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1257_implementation.cpp](1257_implementation.cpp) | G++ 13.2 x64 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.046 s | 768 KB |
| [1257_implementation.go](1257_implementation.go) | Go 1.14 x64 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.031 s | 1876 KB |
| [1257_implementation.java](1257_implementation.java) | Java 1.8 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.156 s | 5152 KB |
| [1257_implementation.py](1257_implementation.py) | Python 3.12 x64 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.140 s | 1740 KB |
| [1257_implementation.rs](1257_implementation.rs) | Rust 1.75 x64 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.015 s | 600 KB |
