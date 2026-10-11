# 1226. 把每个单词倒着写

[Timus 1226](https://acm.timus.ru/problem.aspx?space=1&num=1226) · 难度 114 · strings

原题出自 2002 年 10 月在雷宾斯克举行的 ACM ICPC 2002–2003 俄罗斯中部赛区四分之一决赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

题面让读者从样例中猜出变换方式：一段最多 1000 行、每行最多 255 个可打印字符的
文本，要把每个单词的字母倒序后原样输出。单词是由大写或小写拉丁字母组成的最长连续
段；其他所有字符保持原位。

时间限制：1 秒。内存限制：64 MB。

## 输入

文本。

## 输出

每个单词都倒序后的文本。

## 样例

### 样例 1

输入：

```
This is an example of a simple test. If you did not 
understand the ciphering algorithm yet, then write the 
letters of each word in the reverse order. By the way, 
"reversing" the text twice restores the original text.
```

输出：

```
sihT si na elpmaxe fo a elpmis tset. fI uoy did ton 
dnatsrednu eht gnirehpic mhtirogla tey, neht etirw eht 
srettel fo hcae drow ni eht esrever redro. yB eht yaw, 
"gnisrever" eht txet eciwt serotser eht lanigiro txet.
```

## 解法

一次读入全部输入并从头扫描：每遇到一段字母，就找到它的结尾并原地翻转。数字、
标点、空格和换行都不动，因此文本保持原有的排版。`L` 为字符数时 `O(L)`。

注意事项：

- 行尾可能有空格，必须保留，所以不能把文本拆成单词再拼回去；
- 单词在任何非字母处结束，包括数字和下划线：`abc123` 变成 `cba123`；
- 最后一行可能没有换行符，不能补上。

输出已在所有测试上与期望文本逐字符比对，其中包括 1000 行随机可打印字符。

## 各语言说明

- Python 对原始字节上正则表达式的每个匹配做翻转；其他语言手工扫描字节。

## 解答

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1226_strings.cpp](1226_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 156 KB |
| [1226_strings.go](1226_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 916 KB |
| [1226_strings.java](1226_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 444 KB |
| [1226_strings.py](1226_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 568 KB |
| [1226_strings.rs](1226_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 224 KB |
