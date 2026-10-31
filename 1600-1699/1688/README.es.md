# 1688. Team.GOV!

[Timus 1688](https://acm.timus.ru/problem.aspx?space=1&num=1688) · dificultad 134 · implementation

Problema original de Alexander Ipatov, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres miembros de un equipo piden lo mismo y uno de ellos paga siempre
la cuenta. Otro miembro puede irse en cuanto lo pagado por su parte, un
tercio de cada cuenta, supere n. Dadas las cuentas en orden, decir
después de qué visita ocurre.

## Entrada

n y m (1 ≤ n ≤ 2 · 10⁹; 0 ≤ m ≤ 3000), y luego m cuentas, enteros de 1
a 2 · 10⁶.

## Salida

«Free after x times.» para la primera visita x así, o «Team.GOV!» si
nunca ocurre.

## Ejemplos

### Ejemplo 1

Entrada:

```
1666 5
2000
1024
900
1156
1200
```

Salida:

```
Free after 4 times.
```

### Ejemplo 2

Entrada:

```
3000 5
2000
1024
900
1156
1200
```

Salida:

```
Team.GOV!
```

## Solución

Se lleva la suma acumulada de las cuentas. La parte total / 3 supera n
exactamente cuando total > 3n, lo que evita fracciones; se para en la
primera visita en que se cumple. `O(m)`.

Trampas:

- 3n llega a 6 · 10⁹ y la suma también: hacen falta enteros de 64 bits
  (test 06);
- una parte igual a n no basta, la comparación es estricta (tests 04
  y 06).

Las respuestas coinciden con una implementación aceptada independiente.

## Soluciones optimizadas

La solución optimizada en Java analiza los números byte a byte desde un
búfer de 4 KB que rellena desde `System.in`, en lugar de copiar primero
toda la entrada a un `StringBuilder` y después a otra cadena más para el
tokenizador. Lee las m cuentas aunque ya conozca la respuesta, y guarda
el total y 3n en `long`, porque ambos pueden llegar a 6 · 10⁹:
{1688_implementation_optimized.java}.

La solución optimizada en Python toma los tokens línea a línea de un
generador sobre `sys.stdin.buffer` en lugar de leer toda la entrada y
convertirla en una lista de hasta 3002 enteros; el total acumulado se
lleva como en la solución simple: {1688_implementation_optimized.py}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1688_implementation_optimized.java`: reducción de tiempo -60.26%;
  reducción de memoria +62.20%; base: `1688_implementation.java`.

- `1688_implementation_optimized.py`: reducción de tiempo +0.00%;
  reducción de memoria +44.67%; base: `1688_implementation.py`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1688_implementation.cpp](1688_implementation.cpp).
- [1688_implementation.go](1688_implementation.go).
- [1688_implementation.rs](1688_implementation.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1688_implementation.cpp](1688_implementation.cpp) | G++ 13.2 x64 | implementation | O(m) | AC | 0.015 s | 128 KB | 11304065 |
| [1688_implementation.go](1688_implementation.go) | Go 1.14 x64 | implementation | O(m) | AC | 0.015 s | 1124 KB | 11288883 |
| [1688_implementation.java](1688_implementation.java) | Java 1.8 | implementation | O(m) | AC | 0.078 s | 1016 KB | 11288886 |
| [1688_implementation.py](1688_implementation.py) | Python 3.12 x64 | implementation | O(m) | AC | 0.078 s | 788 KB | 11288885 |
| [1688_implementation.rs](1688_implementation.rs) | Rust 1.75 x64 | implementation | O(m) | AC | 0.015 s | 232 KB | 11304066 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1688_implementation_optimized.java](1688_implementation_optimized.java) | Java 1.8 | implementation | O(m) | AC | 0.125 s | 384 KB | 11304439 |
| [1688_implementation_optimized.py](1688_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(m) | AC | 0.078 s | 436 KB | 11304440 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
