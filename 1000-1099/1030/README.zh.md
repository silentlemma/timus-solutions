# 1030. 船与冰山之间的大圆距离

[Timus 1030](https://acm.timus.ru/problem.aspx?space=1&num=1030) · 难度 898 · geometry, parsing

原题作者 Evgeny Shtykov，出自 1999 年第三届乌拉尔大学生团体程序设计锦标赛。

[English](README.md) · [Русский](README.ru.md) · **中文** · [Español](README.es.md)

## 任务

一条无线电消息给出了一艘船和一座冰山在直径 6875 英里的理想球面上的坐标。输出两者之间球面上最短路径的长度，
保留两位小数；若输出的距离小于 100.00 英里，再输出一行 `DANGER!`。

时间限制：0.5 秒。内存限制：64 MB。

## 输入

消息总是恰好由以下各行组成（数值会变化）：

```text
Message #<n>.
Received at <HH>:<MM>:<SS>.
Current ship's coordinates are
<X1>^<X2>'<X3>" <NL 或 SL>
and <Y1>^<Y2>'<Y3>" <EL 或 WL>.
An iceberg was noticed at
<X1>^<X2>'<X3>" <NL 或 SL>
and <Y1>^<Y2>'<Y3>" <EL 或 WL>.
===
```

`X1^X2'X3"` 表示北纬（`NL`）或南纬（`SL`）X1 度 X2 分 X3 秒，范围 0 到 90 度；`Y1^Y2'Y3"` 是经度，东经
（`EL`）或西经（`WL`），范围 0 到 180 度。

## 输出

```text
The distance to the iceberg: <s> miles.
```

其中 `<s>` 保留两位小数；若输出的 `<s>` 小于 100.00，接着输出一行 `DANGER!`。

## 评测方式

按记号逐一比较输出；数值最多可相差 0.01。

## 样例

### 样例 1

输入：

```
Message #100.
Received at 00:10:20.
Current ship's coordinates are
12^30'00" NL
and 40^10'00" WL.
An iceberg was noticed at
12^10'00" NL
and 41^00'00" WL.
===
```

输出：

```
The distance to the iceberg: 52.78 miles.
DANGER!
```

### 样例 2

输入：

```
Message #101.
Received at 01:11:21.
Current ship's coordinates are
55^45'20" NL
and 37^37'00" EL.
An iceberg was noticed at
59^56'30" NL
and 30^18'00" EL.
===
```

输出：

```
The distance to the iceberg: 342.61 miles.
```

## 题解

**解析。** 每个坐标是三个整数后跟 `NL`、`SL`、`EL` 或 `WL`。把字符 `^`、`'`、`"` 替换为空格，把文本拆成
记号；每遇到形如 `?L`（`?` 为 `N S E W` 之一）的记号，就取前面三个记号作为度、分、秒。数值为
`度 + 分 / 60 + 秒 / 3600`，南纬和西经取负。前两个数是船，后两个是冰山。

**距离。** 对弧度表示的纬度 `φ1, φ2` 与经度 `λ1, λ2`，两点间的圆心角 `θ` 由 **半正矢公式** 给出

`hav θ = sin²((φ2 - φ1) / 2) + cos φ1 · cos φ2 · sin²((λ2 - λ1) / 2)`，

于是 `θ = 2 · asin(sqrt(hav θ))`，距离为 `R · θ`，`R = 6875 / 2`。球面余弦定理
`cos θ = sin φ1 sin φ2 + cos φ1 cos φ2 cos(λ2 - λ1)` 给出相同的值，但对很近的两点会损失精度，因为此时
`cos θ` 极接近 1。

**危险行。** 它取决于输出的值：99.996 英里会输出为 `100.00`，不算危险。应把距离四舍五入到百分位后与
100.00 比较。

注意事项：

- 经度位于 180 度经线两侧（`179°59' E` 与 `179°59' W` 只差 2 分）；
- 在 `sqrt`/`asin` 之前把 `hav θ` 截断到 1：对对跖点舍入误差可能让它略大于 1；
- 阈值按四舍五入后的值判断，而不是精确值。

## 各语言说明

各语言使用同样的解析和公式；Python 用正则表达式，Java 用 `Locale.US` 输出。

## 题解代码

| 代码 | 语言 | 方法 | 复杂度 | 评测结果 | 时间 | 内存 |
|----|----|----|-----|------|----|----|
| [1030_geometry.cpp](1030_geometry.cpp) | G++ 13.2 x64 | geometry | O(length of the message) | AC | 0.015 s | 352 KB |
| [1030_geometry.go](1030_geometry.go) | Go 1.14 x64 | geometry | O(length of the message) | AC | 0.046 s | 1120 KB |
| [1030_geometry.java](1030_geometry.java) | Java 1.8 | geometry | O(length of the message) | AC | 0.093 s | 988 KB |
| [1030_geometry.py](1030_geometry.py) | Python 3.12 x64 | geometry | O(length of the message) | AC | 0.062 s | 516 KB |
| [1030_geometry.rs](1030_geometry.rs) | Rust 1.75 x64 | geometry | O(length of the message) | AC | 0.015 s | 288 KB |
