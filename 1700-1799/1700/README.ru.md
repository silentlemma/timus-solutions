# 1700. Пробуждение

[Timus 1700](https://acm.timus.ru/problem.aspx?space=1&num=1700) · сложность 482 · implementation

Автор оригинальной задачи — Павел Атнашев; XIII чемпионат Урала по спортивному программированию, 4 апреля 2009 года.

[English](README.md) · **Русский** · [中文](README.zh.md) · [Español](README.es.md)

## Задача

У каждого объекта есть набор ассоциаций. Для каждой из нескольких
групп объектов вывести общие для всех них ассоциации по алфавиту или
«No solution.», если таких нет.

## Входные данные

n (2 ≤ n ≤ 1000) строк «имя: ассоциация ассоциация …», затем m
(1 ≤ m ≤ 1000) строк — группы хотя бы из двух имён объектов. Слова из
строчных латинских букв, строки не длиннее 250 символов.

## Выходные данные

По строке на группу.

## Примеры

### Пример 1

Ввод:

```
6
whale: big black water animal
penguin: black white ice beak
piano: keyboard black white wire
jackboot: leather heel black
train: rail wheel black
rose: red green thorn
3
whale penguin piano jackboot train
penguin piano
jackboot rose
```

Вывод:

```
black
black white
No solution.
```

## Решение

Храним ассоциации каждого объекта как множество по его имени. Для
группы пересекаем множества её членов и выводим результат по порядку
или «No solution.», если он пуст. Все строки короткие; на группу нужно
`O(L²)` проверок в множествах.
`O((n + m · L) · L log(n + L))` для строк длины L.

Подводные камни:

- ассоциация может быть указана у объекта дважды, но выводится один
  раз (тест 02);
- в группе один объект может быть назван дважды (тест 03);
- у объекта может не быть ассоциаций вовсе, тогда строка кончается
  сразу после двоеточия.

Ответы совпадают с независимой принятой реализацией.

## Решения

| Решение | Язык | Подход | Асимптотика | Вердикт | Время | Память |
|---------|------|--------|-------------|---------|-------|--------|
| [1700_implementation.cpp](1700_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.359 s | 7788 KB |
| [1700_implementation.go](1700_implementation.go) | Go 1.14 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.765 s | 8908 KB |
| [1700_implementation.java](1700_implementation.java) | Java 1.8 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.437 s | 12376 KB |
| [1700_implementation.py](1700_implementation.py) | Python 3.12 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.390 s | 13524 KB |
| [1700_implementation.rs](1700_implementation.rs) | Rust 1.75 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.593 s | 3584 KB |
