# 1631. Rey borracho 2

[Timus 1631](https://acm.timus.ru/problem.aspx?space=1&num=1631) · dificultad 489 · math

Problema original de Igor Chevdar, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un rey recorre un tablero m × n de lados impares: empieza y termina en
una esquina, visita cada casilla salvo la primera exactamente una vez,
no cruza su propio camino y, por estar borracho, nunca hace dos
movimientos seguidos en la misma dirección. Hay que hallar la longitud
del recorrido más corto, medida entre centros de casillas (un movimiento
recto vale 1 y uno diagonal √2).

## Entrada

Una línea con m y n (6 < m, n < 500, ambos impares).

## Salida

La longitud del recorrido más corto con precisión 10⁻⁹.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 7
```

Salida:

```
55.213203435596425732025330863145
```

## Solución

El recorrido es un camino cerrado por las m · n casillas, así que tiene
exactamente m · n movimientos. Si D de ellos son diagonales, la longitud
es m · n + D · (√2 − 1), y se trata de hacer D lo menor posible.

Las diagonales no se pueden evitar. Dos movimientos rectos seguidos
tienen que girar, así que en cada casilla hay a lo sumo un movimiento
horizontal y uno vertical. En una fila los movimientos horizontales
emparejan casillas vecinas y, con un número impar de casillas, al menos
una queda sin pareja; lo mismo vale para cada columna. Cada casilla
sobrante necesita un movimiento diagonal, así que ya D ≥ (m + n) / 2.
Esta cota sencilla no es ajustada: las demás condiciones elevan el
mínimo posible hasta D = m + n + 1 (no se demuestra aquí). El dibujo del
enunciado de un recorrido de 7 × 7 usa 15 diagonales, y
49 + 15 · (√2 − 1) = 55,2132… es la respuesta esperada. El programa
imprime esta fórmula con 12 decimales; el valor mayor, unos 2,5 · 10⁵,
mantiene en double un error absoluto cercano a 10⁻¹¹. `O(1)`.

Detalles a tener en cuenta:

- el recorrido es cerrado, así que hay m · n movimientos, no m · n − 1;
- Java formatea con la configuración regional por defecto y puede
  imprimir una coma decimal; `Locale.US` conserva el punto.

Las respuestas coinciden con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1631_math.cpp](1631_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 140 KB |
| [1631_math.go](1631_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1084 KB |
| [1631_math.java](1631_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1800 KB |
| [1631_math.py](1631_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 412 KB |
| [1631_math.rs](1631_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 260 KB |
