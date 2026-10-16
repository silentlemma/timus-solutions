# 1738. Seguridad informática

[Timus 1738](https://acm.timus.ru/problem.aspx?space=1&num=1738) · dificultad 1001 · implementation

Problema original de Daniil Ayzenshteyn, del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los empleados están numerados de 1 a n, y cada uno tiene un PIN
distinto de cuatro cifras hexadecimales. Dos números son parecidos si
uno se convierte en el otro insertando, borrando o cambiando una cifra
decimal, sin ceros a la izquierda. Para cada par de empleados con
números parecidos contar las posiciones en que difieren sus PIN, e
informar cuántos pares difieren en 1, 2, 3 y 4 posiciones.

## Entrada

n (2 ≤ n ≤ 65 536) y luego los PIN de los empleados 1 a n.

## Salida

Cuatro números: cuántos pares parecidos tienen PIN que difieren en 1,
2, 3 y 4 posiciones.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
dead
beef
f00d
```

Salida:

```
0 0 2 1
```

## Solución

Cada par se cuenta desde su número menor i. El número mayor j es
entonces i con una cifra aumentada en su lugar, o i con una cifra
insertada; un borrado daría un número menor, y ese par se cuenta desde
el otro lado.

- Una cifra aumentada da j = i + (d − old)·10^q. Posiciones o cifras
  distintas dan números distintos, así que nada se repite, y las cifras
  se aumentan en orden hasta que j pasa de n.
- Una inserción alarga j en una cifra, así que solo hace falta cuando i
  es más corto que n. Insertar la misma cifra junto a una igual da dos
  veces el mismo número, así que estos candidatos pasan por un
  conjunto, y se descartan los que empiezan por cero.

Los PIN se leen como números, y las posiciones en que dos PIN difieren
son las cifras hexadecimales no nulas de su XOR, de una tabla de
65 536 entradas. Cada número tiene unos 25 candidatos. `O(n·L)` para L
cifras decimales.

En el ejemplo 1, 2 y 3 son parecidos entre sí cambiando una cifra;
`dead` y `beef` difieren en 3 posiciones, `dead` y `f00d` en 3, `beef`
y `f00d` en 4.

Trampas:

- 1 y 11 son parecidos de dos maneras (el segundo 1 se inserta a
  cualquier lado), pero son un solo par;
- 10 se parece a 1 borrando el cero, pero 01 no es un número, así que
  borrar el 1 de 10 no da nada;
- los conteos llegan a unos 1,2 millones, bien dentro de 32 bits.

Los conteos coinciden con una comprobación de todos los pares en
conjuntos aleatorios de hasta 200 empleados y con una implementación
aceptada independiente en las pruebas grandes. La solución en Python
corre en PyPy; con CPython necesita aquí unos 0,5 s para 65 536
empleados, demasiado cerca del límite.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1738_implementation.cpp](1738_implementation.cpp) | G++ 13.2 x64 | implementation | O(n·L) | AC | 0.171 s | 728 KB |
| [1738_implementation.go](1738_implementation.go) | Go 1.14 x64 | implementation | O(n·L) | AC | 0.187 s | 7008 KB |
| [1738_implementation.java](1738_implementation.java) | Java 1.8 | implementation | O(n·L) | AC | 0.265 s | 5820 KB |
| [1738_implementation.py](1738_implementation.py) | PyPy 3.10 x64 | implementation | O(n·L) | AC | 0.328 s | 9528 KB |
| [1738_implementation.rs](1738_implementation.rs) | Rust 1.75 x64 | implementation | O(n·L) | AC | 0.125 s | 1996 KB |
