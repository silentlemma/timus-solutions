# 1585. Пингвины

[Timus 1585](https://acm.timus.ru/problem.aspx?space=1&num=1585) · сложность 38 · implementation

Автор оригинальной задачи — Владимир Яковлев; ACM ICPC 2007–2008, NEERC, Восточный подрегион, Екатеринбург, 27 октября 2007 года.

[English](README.md) · **Русский** · [中文](README.zh.md) · [Español](README.es.md)

## Задача

В блокноте записаны N ≤ 1000 пингвинов, каждый как «Emperor Penguin»,
«Little Penguin» или «Macaroni Penguin». Нужно вывести вид, который
встречается чаще всех; он единственный.

Ограничение времени: 1 секунда. Ограничение памяти: 64 МБ.

## Входные данные

N, затем по одному виду в строке.

## Выходные данные

Самый частый вид.

## Примеры

### Пример 1

Ввод:

```
7
Emperor Penguin
Macaroni Penguin
Little Penguin
Emperor Penguin
Macaroni Penguin
Macaroni Penguin
Little Penguin
```

Вывод:

```
Macaroni Penguin
```

## Решение

Посчитаем записи по первому слову и выведем вид с наибольшим числом, а
после него «Penguin». `O(N)`.

Подводные камни:

- в каждой записи есть пробел, так что её читают либо целой строкой,
  либо двумя словами;
- какого-то вида может не быть вовсе (тест 03).

## Решения

| Решение | Язык | Подход | Асимптотика | Вердикт | Время | Память |
|---------|------|--------|-------------|---------|-------|--------|
| [1585_implementation.cpp](1585_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 388 KB |
| [1585_implementation.go](1585_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1132 KB |
| [1585_implementation.java](1585_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.171 s | 4576 KB |
| [1585_implementation.py](1585_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 512 KB |
| [1585_implementation.rs](1585_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 440 KB |
