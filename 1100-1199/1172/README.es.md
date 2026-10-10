# 1172. Contar viajes circulares por tres islas solo en barco

[Timus 1172](https://acm.timus.ru/problem.aspx?space=1&num=1172) · dificultad 549 · combinatorics

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres islas tienen `N ≤ 30` ciudades cada una. Hay barcos entre cualquier
par de ciudades de islas distintas y no se puede viajar dentro de una
isla. Empezando en una ciudad dada, hay que contar los viajes circulares
que visitan cada otra ciudad exactamente una vez y vuelven; un viaje y el
mismo leído al revés cuentan como uno.

Límite de tiempo: 1 segundo. Límite de memoria: 16 MB.

## Entrada

`N`.

## Salida

El número de viajes, que tiene decenas de dígitos para `N` grande.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
16
```

## Solución

Se separa un viaje en su patrón de islas y la elección de ciudades. El
patrón es una secuencia cíclica de `3N` etiquetas de isla, que empieza en
la isla del turista, con `N` de cada etiqueta y sin dos vecinas iguales,
incluidas la última y la primera. Para un patrón fijo, las otras `N − 1`
ciudades de la isla de origen llenan sus huecos de `(N − 1)!` maneras y
cada una de las otras islas de `N!` maneras. Leer un viaje al revés da
otra secuencia desde el mismo inicio (el viaje tiene al menos tres
ciudades), así que el total se divide entre dos.

Los patrones se cuentan con `ways[a][b][c][i]`: secuencias que empiezan en
la isla 0, usan `a`, `b` y `c` huecos de las tres islas y terminan en la
isla `i`. Cada valor es la suma de dos valores con un hueco menos de la
isla `i` que terminan en otra isla. La respuesta cuenta las secuencias
completas que no terminan en la isla 0. Solo se guardan dos planos de `a`
fijo, así que hay pocos números grandes a la vez. `O(N³)`
sumas de números grandes.

Detalles a tener en cuenta:

- el ciclo también prohíbe que la última ciudad esté en la isla de
  origen;
- la ciudad inicial está fija, así que la isla de origen aporta
  `(N − 1)!`, no `N!`;
- la tabla completa para `N = 30` tendría unos 90 000 números grandes,
  y dos planos solo necesitan unos 6 000.

Las respuestas se compararon con una fuerza bruta sobre todos los órdenes
para `N ≤ 3` y con una solución escrita aparte para todo `N` hasta 30.

## Notas por lenguaje

- Python, Go y Java usan sus enteros grandes; C++ y Rust guardan los
  números como arreglos de dígitos en base 10⁹ con suma, multiplicación
  por un número pequeño y división entre dos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1172_combinatorics.cpp](1172_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 376 KB |
| [1172_combinatorics.go](1172_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 6024 KB |
| [1172_combinatorics.java](1172_combinatorics.java) | Java 1.8 | combinatorics | O(N³) big additions | AC | 0.125 s | 4580 KB |
| [1172_combinatorics.py](1172_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N³) big additions | AC | 0.093 s | 884 KB |
| [1172_combinatorics.rs](1172_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N³) big additions | AC | 0.031 s | 568 KB |
