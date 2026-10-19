# 2112. Проверка лога перестрелки и угадывание команд

[Timus 2112](https://acm.timus.ru/problem.aspx?space=1&num=2112) · сложность 818 · dsu, greedy, simulation

Автор оригинальной задачи — Иван Сычёв; Вузовско-академическая олимпиада по информатике 2019.

[English](README.md) · **Русский** · [中文](README.zh.md) · [Español](README.es.md)

## Задача

n игроков играют в скрытых командах по четыре. У каждого игрока есть
состояние 3 (здоров), 2 (ранен), 1 (при смерти) или 0 (мёртв), вначале
3. В логе бывают события трёх видов: попадание в тело или голову
понижает состояние цели на 1 или 2 (не ниже 0), аптечка возвращает
использующего в 3, а оживление переводит союзника из 1 в 2. Действовать
может только игрок в состоянии 3 или 2, а оживлять можно только
союзника при смерти. Выведите «FAKE», если никакое разбиение на команды
по четыре не делает лог корректным, иначе «CORRECT» и любое подходящее
разбиение. Ограничения: 1 секунда и 256 МБ.

## Входные данные

n, 4 ≤ n ≤ 1000, делится на 4, n различных имён, затем m,
0 ≤ m ≤ 10⁴, и события «X HIT Y IN BODY», «X HIT Y IN HEAD»,
«X USES MEDKIT» и «X REVIVE Y».

## Выходные данные

«FAKE» или «CORRECT» и n / 4 строк по четыре имени.

## Проверка

Проверяющая программа принимает любое подходящее разбиение.

## Примеры

### Пример 1

Ввод:

```
8
Shroud
Forsen
Wycc
Ragyra
BeastQT
Lirik
Asmadey
Ninja
12
Wycc HIT Shroud IN BODY
Shroud HIT Wycc IN HEAD
Ragyra REVIVE Wycc
Wycc USES MEDKIT
Lirik HIT BeastQT IN BODY
Asmadey HIT BeastQT IN BODY
Asmadey REVIVE BeastQT
Ragyra HIT Forsen IN HEAD
Shroud REVIVE Forsen
BeastQT HIT Shroud IN HEAD
Wycc HIT Forsen IN HEAD
Ninja HIT BeastQT IN HEAD
```

Вывод:

```
CORRECT
Wycc Ragyra BeastQT Asmadey
Lirik Ninja Shroud Forsen
```

### Пример 2

Ввод:

```
8
Shroud
Forsen
Wycc
Ragyra
BeastQT
Lirik
Asmadey
Ninja
8
Shroud HIT Wycc IN HEAD
Shroud HIT Ragyra IN HEAD
Shroud HIT BeastQT IN HEAD
Shroud HIT Asmadey IN HEAD
Lirik REVIVE Wycc
Lirik REVIVE Ragyra
Lirik REVIVE BeastQT
Lirik REVIVE Asmadey
```

Вывод:

```
FAKE
```

### Пример 3

Ввод:

```
4
Shroud
Forsen
Wycc
Ragyra
3
Shroud HIT Wycc IN HEAD
Wycc HIT Shroud IN HEAD
Wycc HIT Shroud IN BODY
```

Вывод:

```
FAKE
```

## Решение

Состояния не зависят от команд, поэтому лог просто моделируется.
Событие, у которого действующий игрок в состоянии 1 или 0, поддельно,
как и оживление цели не в состоянии 1. Попадания в кого угодно
допустимы, даже в себя.

Единственная связь с командами — оживление ставит двух игроков в одну
команду. Они объединяются в системе непересекающихся множеств. Каждая
получившаяся группа должна поместиться в одну команду, так что группа
больше четырёх — подделка. Затем группы упаковываются в команды по
четыре:

- группы из четырёх — уже команды;
- каждой группе из трёх нужен одиночка, и если одиночек меньше, чем
  троек, лог поддельный;
- группы из двух объединяются попарно;
- оставшаяся непарная двойка берёт двух одиночек, которые есть, потому
  что n делится на четыре;
- остальные одиночки образуют команды по четыре.

Моделирование и упаковка занимают O(n + m) при хешировании имён.

В третьем примере Wycc получает выстрел в голову, оказывается при
смерти и всё равно стреляет, так что лог поддельный.

## Решения

| Решение | Язык | Подход | Асимптотика | Вердикт | Время | Память |
|---------|------|--------|-------------|---------|-------|--------|
| [2112_dsu_greedy_simulation.cpp](2112_dsu_greedy_simulation.cpp) | G++ 13.2 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.031 s | 644 KB |
| [2112_dsu_greedy_simulation.go](2112_dsu_greedy_simulation.go) | Go 1.14 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.046 s | 2824 KB |
| [2112_dsu_greedy_simulation.java](2112_dsu_greedy_simulation.java) | Java 1.8 | dsu, greedy, simulation | O(n + m) | AC | 0.156 s | 4712 KB |
| [2112_dsu_greedy_simulation.py](2112_dsu_greedy_simulation.py) | Python 3.12 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.109 s | 1140 KB |
| [2112_dsu_greedy_simulation.rs](2112_dsu_greedy_simulation.rs) | Rust 1.75 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.046 s | 1280 KB |
