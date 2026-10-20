# 2151. Reconocer una mano de mahjong ganadora o casi ganadora

[Timus 2151](https://acm.timus.ru/problem.aspx?space=1&num=2151) · dificultad 904 · bruteforce, greedy

Problema original de Ivan Sychev, del Concurso Escolar de Programación de los Urales 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las fichas tienen un palo a, b o c y un número del 1 al 9. Una mano de 14
fichas gana cuando se divide en cuatro tríos y una pareja, donde un trío
son tres fichas iguales o tres números consecutivos de un palo y una
pareja son dos fichas iguales. Una mano está casi ganada cuando cambiar
exactamente una ficha la hace ganar. Clasificar una mano como Tsumo,
Tenpai o Noten. Los límites son 1 segundo y 256 MB.

## Entrada

14 fichas como 1a o 9c, a lo sumo cuatro de cada tipo.

## Salida

Tsumo, Tenpai o Noten.

## Ejemplos

### Ejemplo 1

Entrada:

```
1a 2a 3a 6a 7a 8a 5b 5b 5b 9c 8c 7c 1c 1c
```

Salida:

```
Tsumo
```

### Ejemplo 2

Entrada:

```
1a 2a 3a 6a 7a 8a 5b 5b 5b 9c 8c 7c 1c 1b
```

Salida:

```
Tenpai
```

## Solución

Se cuentan las fichas de cada uno de los 27 tipos. Para saber si una
mano gana, primero se observa que los tríos no salen de un palo, así que
exactamente un palo tiene un número de fichas ≡ 2 módulo 3 y contiene la
pareja, y los demás son ≡ 0. Se prueba como pareja cada tipo de ese palo
con al menos dos fichas. El resto debe dividirse en tríos, lo que decide
una pasada voraz: subiendo desde el número menor, una cantidad c deja
c mod 3 fichas que no pueden ir en tríos iguales, porque tres escaleras
iguales equivalen a tres tríos iguales, así que exactamente c mod 3
escaleras deben empezar allí.

Una mano es Tenpai si no gana pero gana tras quitar una ficha de algún
tipo y añadir una de otro tipo; un cambio puede crear una quinta ficha
de un tipo. Son a lo sumo 27 · 26 comprobaciones de una prueba voraz de
27 elementos.

En el segundo ejemplo la mano tiene 1c y 1b donde hace falta una
pareja, así que cambiar una por la otra la completa.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2151_bruteforce_greedy.cpp](2151_bruteforce_greedy.cpp) | G++ 13.2 x64 | bruteforce, greedy | O(27^3) | AC | 0.015 s | 400 KB |
| [2151_bruteforce_greedy.go](2151_bruteforce_greedy.go) | Go 1.14 x64 | bruteforce, greedy | O(27^3) | AC | 0.031 s | 1100 KB |
| [2151_bruteforce_greedy.java](2151_bruteforce_greedy.java) | Java 1.8 | bruteforce, greedy | O(27^3) | AC | 0.109 s | 492 KB |
| [2151_bruteforce_greedy.py](2151_bruteforce_greedy.py) | Python 3.12 x64 | bruteforce, greedy | O(27^3) | AC | 0.078 s | 652 KB |
| [2151_bruteforce_greedy.rs](2151_bruteforce_greedy.rs) | Rust 1.75 x64 | bruteforce, greedy | O(27^3) | AC | 0.015 s | 216 KB |
