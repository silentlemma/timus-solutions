# 1446. Волшебная шляпа

[Timus 1446](https://acm.timus.ru/problem.aspx?space=1&num=1446) · сложность 91 · implementation

Автор оригинальной задачи — Станислав Васильев; Десятый командный чемпионат Урала по спортивному программированию, 24–25 марта 2006 года.

[English](README.md) · **Русский** · [中文](README.zh.md) · [Español](README.es.md)

## Задача

N первокурсников (1 ≤ N ≤ 1000) распределены по факультетам; для
каждого в порядке церемонии одна строка содержит имя (латинские буквы,
пробелы и дефисы, не больше 200 символов), а следующая — факультет.
Нужно вывести списки Слизерина, Хаффлпаффа, Гриффиндора и Рейвенкло в
этом порядке: название факультета с двоеточием, затем его ученики по
одному в строке в порядке церемонии, с пустой строкой между списками. На
каждый факультет попадает хотя бы один ученик.

Ограничение времени: 1 секунда. Ограничение памяти: 64 МБ.

## Входные данные

N, затем 2N строк: имя и факультет каждого ученика.

## Выходные данные

Четыре списка.

## Примеры

### Пример 1

Ввод:

```
7
Ivan Ivanov
Gryffindor
Mac Go Nagolo
Hufflepuff
Zlobeus Zlei
Slytherin
Um Bridge
Slytherin
Tatiana Henrihovna Grotter
Ravenclaw
Garry Potnyj
Gryffindor
Herr Mionag-Ranger
Gryffindor
```

Вывод:

```
Slytherin:
Zlobeus Zlei
Um Bridge

Hufflepuff:
Mac Go Nagolo

Gryffindor:
Ivan Ivanov
Garry Potnyj
Herr Mionag-Ranger

Ravenclaw:
Tatiana Henrihovna Grotter
```

## Решение

Читаем вход построчно, потому что в именах есть пробелы, и добавляем
каждое имя в список нужного факультета; затем выводим списки в нужном
порядке. Из имени убирается только перевод строки, так что пробелы
внутри остаются как есть. `O(N)` строк.

Подводные камни:

- чтение по словам разрывает имена (тесты 01, 03, 04);
- ученика могут звать так же, как факультет (тест 03);
- порядок факультетов в выводе не алфавитный.

## Решения

| Решение | Язык | Подход | Асимптотика | Вердикт | Время | Память |
|---------|------|--------|-------------|---------|-------|--------|
| [1446_implementation.cpp](1446_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.031 s | 520 KB |
| [1446_implementation.go](1446_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1672 KB |
| [1446_implementation.java](1446_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 2324 KB |
| [1446_implementation.py](1446_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 1520 KB |
| [1446_implementation.rs](1446_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 980 KB |
