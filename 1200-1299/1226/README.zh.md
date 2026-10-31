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

从头扫描文本：每遇到一段字母，就找到它的结尾并翻转。数字、标点、空格和换行都不
动，因此文本保持原有的排版。`L` 为字符数时 `O(L)`。

注意事项：

- 行尾可能有空格，必须保留，所以不能把文本拆成单词再拼回去；
- 单词在任何非字母处结束，包括数字和下划线：`abc123` 变成 `cba123`；
- 最后一行可能没有换行符，不能补上。

输出已在所有测试上与期望文本逐字符比对，其中包括 1000 行随机可打印字符。

## 优化解法

优化的 C++ 解法用 `getchar` 读取文本，只在 255 字节的缓冲区中保存当前单词——这已
足够，因为单词不会跨行，而一行最多 255 个字符；一旦遇到非字母结束单词，就把它倒
序输出，而不是把整个文本收集到 `std::string` 中：{1226_strings_optimized.cpp}。

优化的 Java 解法按 64 KB 分块把全部输入读成字节，在这个字节数组中就地翻转每段字
母，而不是通过 reader 和 writer 解码字符并为每个单词创建字符串：
{1226_strings_optimized.java}。

优化的 Python 解法每次在一个 `bytearray` 中处理一行，用切片翻转每段字母，而不是
导入正则表达式模块并在整个文本上替换；单词不会跨行，所以这样做是安全的。这样省内
存，但对每个字符的循环在 Python 中执行，要多花时间：
{1226_strings_optimized.py}。

### 实测改进

每个优化版本均已获 Accepted，且相对同语言的基础版本，时间或内存至少降低 30%。基础源代码均保留。负的降低比例表示开销增加。星号只表示尚未达到排名目标。

- `1226_strings_optimized.cpp`: 时间降低 +0.00%; 内存降低 +46.15%; 基础版本: `1226_strings.cpp`.

- `1226_strings_optimized.java`: 时间降低 +0.00%; 内存降低 +35.00%; 基础版本: `1226_strings.java`.

- `1226_strings_optimized.py`: 时间降低 +0.00%; 内存降低 +33.10%; 基础版本: `1226_strings.py`.

## 各语言说明

在 2026-10-31 的排名快照中，下列基础实现已达到时间和内存目标。保留现有基础解法文件；这些语言无需额外实现即可满足排名目标。

- [1226_strings.rs](1226_strings.rs).

- Python 对原始字节上正则表达式的每个匹配做翻转；C++、Go 和 Rust 读入全部输入，
  就地翻转每段字母；Java 以 Latin-1 编码逐字符读取文本（这种编码原样保留每个
  字节），遇到非字母结束一个单词时把它翻转后输出。

## 解答

### 简单版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1226_strings.cpp](1226_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 156 KB | 11283715 |
| [1226_strings.go](1226_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 916 KB | 11283716 |
| [1226_strings.java](1226_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 720 KB | 11304343 |
| [1226_strings.py](1226_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 568 KB | 11283717 |
| [1226_strings.rs](1226_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 224 KB | 11283719 |

### 优化版本

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1226_strings_optimized.cpp](1226_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 84 KB | 11304344 |
| [1226_strings_optimized.java](1226_strings_optimized.java) \* | Java 1.8 | strings | O(L) | AC | 0.093 s | 468 KB | 11304346 |
| [1226_strings_optimized.py](1226_strings_optimized.py) \* | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 380 KB | 11304345 |

\* 已接受；尚未达到排名目标，此版本仍可继续优化。
