# 2068. La paridad del número de divisiones

[Timus 2068](https://acm.timus.ru/problem.aspx?space=1&num=2068) · dificultad 108 · games

Problema original de Alexey Danilyuk, del Concurso Regional por Equipos de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n montones de nueces, cada uno con un número impar de nueces. Dos
jugadores alternan turnos; una jugada divide un montón en tres montones
no vacíos, cada uno de nuevo con un número impar de nueces. Quien no
puede jugar pierde. Daenerys juega primero y luego Stannis. Hallar el
ganador con juego óptimo. Los límites son 1 segundo y 64 MB.

## Entrada

Un n impar, 1 ≤ n ≤ 777, y después n tamaños impares de montones entre
1 y 54321.

## Salida

`Daenerys` si ella gana, y `Stannis` en otro caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
3
```

Salida:

```
Daenerys
```

### Ejemplo 2

Entrada:

```
3
1 1 1
```

Salida:

```
Stannis
```

### Ejemplo 3

Entrada:

```
5
777 313 465 99 1
```

Salida:

```
Daenerys
```

## Solución

Aquí la estrategia no importa. Una jugada cambia un montón por tres, así
que el número de montones crece exactamente en dos, y el total de nueces
no cambia. El juego termina exactamente cuando cada montón tiene una
nuez: un montón de 3 o más nueces (impar) siempre se puede dividir como
1 + 1 + (a − 2). En ese momento hay tantos montones como nueces, de modo
que el número de jugadas es siempre (S − n) / 2, la suma de
(aᵢ − 1) / 2 sobre los montones.

Daenerys hace las jugadas impares, así que gana exactamente cuando ese
número es impar. En el tercer ejemplo los montones dan
388 + 156 + 232 + 49 + 0 = 825 jugadas, un número impar. El trabajo es
O(n).

## Notas por lenguaje

La suma es como máximo 777 · 27160 y cabe en un entero de 32 bits; en C++
y Java se guarda de todos modos en 64 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2068_games.cpp](2068_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.015 s | 124 KB |
| [2068_games.go](2068_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.031 s | 1108 KB |
| [2068_games.java](2068_games.java) | Java 1.8 | games | O(n) | AC | 0.093 s | 440 KB |
| [2068_games.py](2068_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.093 s | 368 KB |
| [2068_games.rs](2068_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.031 s | 248 KB |
