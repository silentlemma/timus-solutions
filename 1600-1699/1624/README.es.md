# 1624. ¡Sal de aquí!

[Timus 1624](https://acm.timus.ru/problem.aspx?space=1&num=1624) · dificultad 5072 · implementation

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una prisión es una cuadrícula de W × H celdas (2 ≤ W · H ≤ 150) con
paredes o puertas entre celdas vecinas y paredes en todo el borde. Dos
exploradores ciegos empiezan en celdas desconocidas (quizá la misma) y
por turnos intentan moverse al norte, sur, este u oeste, informando la
dirección y si lo lograron; los informes impares son del primero. Dados
K informes (K ≤ 10⁵), imprime el primer informe tras el cual ambas
posiciones son seguras, o que no hay datos suficientes, o el primer
informe que contradice a los anteriores (esto tiene prioridad).

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

W, H y K, luego K informes como `E+` o `N-`.

## Salida

Uno de los tres mensajes con el número de informe.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1 4
E+
W-
N-
S-
```

Salida:

```
The scouts are safe at step number 2
```

### Ejemplo 2

Entrada:

```
2 1 4
N-
W-
N-
S-
```

Salida:

```
There is not enough data
```

### Ejemplo 3

Entrada:

```
2 1 4
N-
W-
N-
S+
```

Salida:

```
A mistake has been made at step number 4
```

## Solución

Cada explorador guarda su posición relativa a su propio inicio
desconocido, el rango de posiciones visitadas y lo que vio en cada arista
relativa a su inicio: puerta o pared. Las incógnitas son los dos
inicios. El inicio del primero debe mantener su rango visitado dentro de
la prisión, lo que da un intervalo para cada coordenada; igual para el
segundo.

Los exploradores solo se topan con las mismas paredes a través del
desplazamiento entre sus inicios. Si el primero vio una puerta en la
arista relativa e y el segundo una pared en la arista relativa f del
mismo tipo, el desplazamiento e − f es imposible. Estos desplazamientos
se marcan en una tabla de (2H − 1) · (2W − 1) entradas. El número de
pares de inicios que quedan es una suma sobre los desplazamientos no
marcados, cada uno con un rectángulo de inicios del primero; el conteo
se detiene en 2. Un conteo de 1 significa que están localizados, 0 un
error, igual que un explorador que informa puerta y pared en la misma
arista.

El conteo solo puede cambiar cuando un explorador ve una arista nueva o
amplía su rango, lo que ocurre a lo sumo unos cientos de veces, así que
solo se recalcula entonces. `O(K + E · W · H)` para E de estos eventos.

Detalles a tener en cuenta:

- un error debe informarse aunque los exploradores ya estén localizados;
- caminar más lejos que el ancho de la prisión es un error (prueba 05);
- los exploradores pueden estar en la misma celda sin notarlo.

Las respuestas coinciden con una implementación aceptada independiente
en 132 prisiones aleatorias, con informes verdaderos y falseados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1624_implementation.cpp](1624_implementation.cpp) | G++ 13.2 x64 | implementation | O(K + E · W · H) | AC | 0.046 s | 412 KB |
| [1624_implementation.go](1624_implementation.go) | Go 1.14 x64 | implementation | O(K + E · W · H) | AC | 0.046 s | 3004 KB |
| [1624_implementation.java](1624_implementation.java) | Java 1.8 | implementation | O(K + E · W · H) | AC | 0.109 s | 4636 KB |
| [1624_implementation.py](1624_implementation.py) | Python 3.12 x64 | implementation | O(K + E · W · H) | AC | 0.156 s | 8036 KB |
| [1624_implementation.rs](1624_implementation.rs) | Rust 1.75 x64 | implementation | O(K + E · W · H) | AC | 0.031 s | 1436 KB |
