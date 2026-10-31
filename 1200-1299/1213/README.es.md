# 1213. El menor número de mamparas para llevar las cucarachas a la esclusa

[Timus 1213](https://acm.timus.ru/problem.aspx?space=1&num=1213) · dificultad 170 · graphs

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
hasta 20 letras latinas y cifras, y las mayúsculas importan.

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

## Soluciones optimizadas

La solución optimizada en C++ lee los tabiques con `scanf` en un búfer
de 42 bytes, suficiente para dos nombres de como mucho 20 caracteres y
el guion, y guarda los nombres distintos en una tabla estática de
30 nombres de 21 bytes, buscados con `strcmp`: hay como mucho
30 compartimentos, así que la búsqueda lineal es barata. Esto sustituye
a `iostream`, `std::string` y los nodos de `std::set`:
{1213_graphs_optimized.cpp}.

La solución optimizada en Java lee los tokens con `BufferedReader` y
`StringTokenizer` en lugar de `Scanner`, cuyas expresiones regulares son
caras de preparar. Busca el guion con `indexOf` y añade directamente los
dos nombres, sin el arreglo temporal ni la lista envoltorio que crean
`split` y `Arrays.asList`: {1213_graphs_optimized.java}.

La solución optimizada en Rust lee la entrada línea a línea en lugar de
leerla entera en una cadena, y guarda los nombres distintos en un vector
pequeño con búsqueda lineal en lugar de un conjunto hash: hay como mucho
30 compartimentos, así que se guardan como mucho 30 nombres, sea cual
sea el número de tabiques: {1213_graphs_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1213_graphs_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +74.49%; base: `1213_graphs.cpp`.

- `1213_graphs_optimized.java`: reducción de tiempo +28.44%; reducción
  de memoria +72.07%; base: `1213_graphs.java`.

- `1213_graphs_optimized.rs`: reducción de tiempo +50.00%; reducción de
  memoria +50.96%; base: `1213_graphs.rs`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1213_graphs.go](1213_graphs.go).

- Todos los lenguajes reúnen los nombres en un conjunto e imprimen su
  tamaño menos uno.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1213_graphs.cpp](1213_graphs.cpp) | G++ 13.2 x64 | graphs | O(P log P) | AC | 0.015 s | 392 KB | 11283651 |
| [1213_graphs.go](1213_graphs.go) | Go 1.14 x64 | graphs | O(P log P) | AC | 0.015 s | 1064 KB | 11283652 |
| [1213_graphs.java](1213_graphs.java) | Java 1.8 | graphs | O(P log P) | AC | 0.109 s | 1876 KB | 11283654 |
| [1213_graphs.py](1213_graphs.py) | Python 3.12 x64 | graphs | O(P log P) | AC | 0.078 s | 384 KB | 11283653 |
| [1213_graphs.rs](1213_graphs.rs) | Rust 1.75 x64 | graphs | O(P log P) | AC | 0.062 s | 416 KB | 11283655 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1213_graphs_optimized.cpp](1213_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(P log P) | AC | 0.015 s | 100 KB | 11307251 |
| [1213_graphs_optimized.java](1213_graphs_optimized.java) | Java 1.8 | graphs | O(P log P) | AC | 0.078 s | 524 KB | 11307254 |
| [1213_graphs_optimized.rs](1213_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(P log P) | AC | 0.031 s | 204 KB | 11307256 |
