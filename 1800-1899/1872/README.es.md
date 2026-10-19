# 1872. Oficina espaciosa

[Timus 1872](https://acm.timus.ru/problem.aspx?space=1&num=1872) · dificultad 799 · matching

Problema original de Alexander Klepinin, del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n equipos de proyecto y n salas de áreas dadas. El equipo i acepta
una sala de área entre lᵢ y rᵢ. Hay que dar a cada equipo su propia
sala. Si hay exactamente una forma, se escribe; si hay varias, o
ninguna, se indica.

## Entrada

n (2 ≤ n ≤ 1000), luego las n áreas de las salas y luego n líneas
lᵢ rᵢ (lᵢ ≤ rᵢ). Todas las áreas están entre 1 y 10 000.

## Salida

"Perfect!" y la sala de cada equipo si el reparto es único,
"Ask Shiftman for help." si hay varios repartos y "Let's search for
another office." si no hay ninguno.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
40 50 60
30 70
20 40
60 60
```

Salida:

```
Perfect!
2 1 3
```

### Ejemplo 2

Entrada:

```
3
40 50 70
30 70
20 50
60 60
```

Salida:

```
Let's search for another office.
```

## Solución

Se ordenan las salas por área. Para hallar un reparto, las salas se dan
de la menor a la mayor: cada sala va al equipo en espera (con lᵢ como
mucho su área) de menor rᵢ. Si no espera ningún equipo, o el rᵢ de ese
equipo ya es menor que la sala, no hay reparto. Cualquier reparto puede
convertirse en este mediante intercambios que lo mantienen válido, así
que el voraz nunca falla cuando existe un reparto.

En orden la sala q tiene un equipo que acepta un bloque contiguo de
salas first(q) … last(q) que contiene q. Existe otro reparto
exactamente cuando varios equipos pueden pasarse salas en ciclo, cada
uno mudándose a la sala del siguiente. El ciclo más corto siempre tiene
longitud 2. Sea M su mayor sala, P la sala del equipo que se muda a M y
S la sala a la que se muda el equipo de M; P y S son menores que M. Si
P ≥ S, el bloque de M cubre P, así que los equipos de P y M pueden
intercambiarse. Si P < S, el bloque de P cubre S, así que el equipo de
P podría mudarse directamente a S, lo que da un ciclo más corto. Por
tanto el reparto es único exactamente cuando no hay p < q con
last(p) ≥ q y first(q) ≤ p. Las salas de igual área siempre dan tal
pareja. El voraz cuesta `O(n log n)` y la comprobación `O(n²)`.

En el primer ejemplo las salas 40, 50 y 60 van a los equipos 2, 1 y 3.
El equipo 1 acepta las tres salas, pero los equipos 2 y 3 solo la suya,
así que nadie puede intercambiar.

Trampas:

- dos salas de la misma área siempre se pueden intercambiar, así que un
  reparto que use ambas nunca es único;
- un intercambio no tiene por qué ser entre salas vecinas: los equipos
  de la sala más pequeña y de la más grande pueden intercambiarse por
  encima de una sala intermedia ocupada por un equipo que solo quiere
  esa;
- comprobar la existencia con el voraz no basta; la unicidad es un paso
  aparte.

Los veredictos coinciden con una búsqueda sobre todos los repartos en
30 000 oficinas aleatorias de hasta 6 salas, y con una implementación
aceptada independiente en 180 oficinas aleatorias de hasta 1000 salas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1872_matching.cpp](1872_matching.cpp) | G++ 13.2 x64 | matching | O(n^2) | AC | 0.015 s | 244 KB |
| [1872_matching.go](1872_matching.go) | Go 1.14 x64 | matching | O(n^2) | AC | 0.031 s | 1260 KB |
| [1872_matching.java](1872_matching.java) | Java 1.8 | matching | O(n^2) | AC | 0.156 s | 2884 KB |
| [1872_matching.py](1872_matching.py) | Python 3.12 x64 | matching | O(n^2) | AC | 0.125 s | 2932 KB |
| [1872_matching.rs](1872_matching.rs) | Rust 1.75 x64 | matching | O(n^2) | AC | 0.046 s | 292 KB |
