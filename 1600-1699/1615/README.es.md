# 1615. Solitario del tranvía

[Timus 1615](https://acm.timus.ru/problem.aspx?space=1&num=1615) · dificultad 2101 · math

Problema original de Vladimir Yakovlev, del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una baraja barajada tiene 2n cartas: dos palos, con n valores cada uno
(2 ≤ n ≤ 10 000). Las cartas se colocan una a una en fila de izquierda a
derecha. Tras cada carta la fila se criba: mientras dos cartas con
exactamente una carta entre ellas compartan palo o valor, se quita la
carta izquierda del par más a la izquierda y las cartas de su derecha
cierran el hueco. El solitario sale si al final quedan exactamente dos
cartas. Imprime la probabilidad de ello como fracción irreducible.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

n.

## Salida

La probabilidad como `p/q`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
2/3
```

## Solución

La respuesta es (n² + 3n − 2) / (2n(2n − 1)), reducida por el máximo
común divisor de sus dos partes. `O(log n)`.

Algunos hechos detrás de ella. Una carta solo se quita como carta
izquierda de un par, así que las dos últimas cartas de la baraja siempre
quedan: nunca hay una carta dos lugares a su derecha. El solitario sale
exactamente cuando todo lo que está delante de ellas se barre. La
fórmula misma se encontró jugando todas las manos de barajas pequeñas:
n = 2, 3, 4, 5 dan 2/3, 8/15, 13/28 y 19/45, exactamente sus valores, y
manos aleatorias para n = 10, 30 y 100 concuerdan con ella. La
probabilidad de fallar se factoriza como (n − 1)(3n − 2) / (2n(2n − 1)).

Detalles a tener en cuenta:

- la fracción debe reducirse: con n = 6 es 52/132 = 13/33 (prueba 05);
- 2n(2n − 1) llega a unos 4·10⁸, así que el producto cabe en 32 bits,
  pero las soluciones usan enteros de 64 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1615_math.cpp](1615_math.cpp) | G++ 13.2 x64 | math | O(log n) | AC | 0.015 s | 128 KB |
| [1615_math.go](1615_math.go) | Go 1.14 x64 | math | O(log n) | AC | 0.031 s | 1060 KB |
| [1615_math.java](1615_math.java) | Java 1.8 | math | O(log n) | AC | 0.109 s | 1560 KB |
| [1615_math.py](1615_math.py) | Python 3.12 x64 | math | O(log n) | AC | 0.093 s | 328 KB |
| [1615_math.rs](1615_math.rs) | Rust 1.75 x64 | math | O(log n) | AC | 0.015 s | 232 KB |
