# 1213. El menor número de mamparas para llevar las cucarachas a la esclusa

[Timus 1213](https://acm.timus.ru/problem.aspx?space=1&num=1213) · dificultad 171 · graphs

Problema original de Evgeny Krokhalev, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un módulo de carga tiene hasta 30 compartimentos unidos por mamparas, y
todos están llenos de cucarachas. Llenar un compartimento de gas y abrir
una de sus mamparas hace que todas sus cucarachas pasen al compartimento
vecino. Todos los compartimentos están conectados con la esclusa. Hay que
hallar el menor número de aperturas de mamparas que reúnen todas las
cucarachas en la esclusa.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El nombre de la esclusa, luego una mampara por línea como dos nombres de
compartimento unidos por `-`, y luego una línea `#`. Los nombres tienen
hasta 20 letras y cifras, y las mayúsculas importan.

## Salida

El menor número de aperturas.

## Ejemplos

### Ejemplo 1

Entrada:

```
Gateway
Machinery-Gateway
Machinery-Control
Control-Central
Control-Engine
Central-Engine
Storage-Gateway
Storage-Waste
Central-Waste
#
```

Salida:

```
6
```

## Solución

Cada compartimento que no es la esclusa empieza con cucarachas y debe
acabar vacío, y un compartimento solo se vacía cuando se abre una de sus
propias mamparas, así que hace falta al menos una apertura por
compartimento. Con eso basta: se toma un árbol de mamparas que lleve a
la esclusa desde cada compartimento y se vacían los compartimentos desde
el más lejano hacia la esclusa, cada uno por su mampara de camino. La
respuesta es el número de nombres de compartimento distintos menos uno.
`O(P log P)` para `P` mamparas.

Detalles a tener en cuenta:

- `Engine` y `engine` son compartimentos distintos;
- puede que la esclusa no tenga ninguna mampara en la lista, y entonces
  la respuesta es 0;
- la disposición de las mamparas no importa, solo cuántos compartimentos
  hay.

Las respuestas se compararon con una solución escrita aparte en 100
módulos aleatorios.

## Notas por lenguaje

- Todos los lenguajes reúnen los nombres en un conjunto e imprimen su
  tamaño menos uno.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1213_graphs.cpp](1213_graphs.cpp) | G++ 13.2 x64 | graphs | O(P log P) | AC | 0.015 s | 392 KB |
| [1213_graphs.go](1213_graphs.go) | Go 1.14 x64 | graphs | O(P log P) | AC | 0.015 s | 1064 KB |
| [1213_graphs.java](1213_graphs.java) | Java 1.8 | graphs | O(P log P) | AC | 0.109 s | 1876 KB |
| [1213_graphs.py](1213_graphs.py) | Python 3.12 x64 | graphs | O(P log P) | AC | 0.078 s | 384 KB |
| [1213_graphs.rs](1213_graphs.rs) | Rust 1.75 x64 | graphs | O(P log P) | AC | 0.062 s | 416 KB |
