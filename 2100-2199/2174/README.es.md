# 2174. Emparejar billetes para que cada par sume un primo

[Timus 2174](https://acm.timus.ru/problem.aspx?space=1&num=2174) · dificultad 885 · matching

Problema original de Ignat Nigmatullin, del Concurso de Programación por Equipos de los Urales 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Repartir N billetes, con N par, en pares de modo que los dos valores de
cada par sumen un primo, o indicar que es imposible. Se acepta cualquier
emparejamiento válido. Los límites son 1 segundo y 256 MB.

## Entrada

N, 2 ≤ N ≤ 500, y luego los valores, 1 ≤ cᵢ ≤ 10⁶.

## Salida

NO, o YES y N / 2 pares.

## Evaluación

Un comprobador verifica el veredicto y que los pares usen exactamente
los billetes dados con sumas primas.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
6 2 4 5 2 3 1 5
```

Salida:

```
YES
5 2
3 2
5 6
1 4
```

### Ejemplo 2

Entrada:

```
2
1 3
```

Salida:

```
NO
```

## Solución

El único primo par es 2 = 1 + 1, así que todo otro par debe unir un
billete impar con uno par. Sea O el número de billetes impares, unos
incluidos, y E el de billetes pares. Los pares de dos unos quitan
billetes impares de dos en dos, así que hacen falta exactamente
(O − E) / 2; si eso es negativo o necesita más unos de los que hay, la
respuesta es NO. Todos los unos son iguales, así que no importa cuáles
se emparejan entre sí.

Los billetes impares y pares restantes, en igual número, forman un grafo
bipartito con una arista cuando la suma es prima, lo que da una criba
hasta 2 · 10⁶. Un emparejamiento perfecto en él, hallado con los caminos
de aumento de Kuhn en O(N³), es la respuesta; si no existe, la respuesta
es NO.

En el segundo ejemplo 1 + 3 = 4 no es primo, y dos billetes impares no
pueden emparejarse de otro modo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2174_matching.cpp](2174_matching.cpp) | G++ 13.2 x64 | matching | O(N^3 + C log log C) | AC | 0.015 s | 1752 KB |
| [2174_matching.go](2174_matching.go) | Go 1.14 x64 | matching | O(N^3 + C log log C) | AC | 0.031 s | 3248 KB |
| [2174_matching.java](2174_matching.java) | Java 1.8 | matching | O(N^3 + C log log C) | AC | 0.109 s | 2904 KB |
| [2174_matching.py](2174_matching.py) | Python 3.12 x64 | matching | O(N^3 + C log log C) | AC | 0.109 s | 4620 KB |
| [2174_matching.rs](2174_matching.rs) | Rust 1.75 x64 | matching | O(N^3 + C log log C) | AC | 0.046 s | 2116 KB |
