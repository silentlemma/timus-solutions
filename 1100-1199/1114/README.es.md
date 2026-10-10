# 1114. Colocar hasta A y B bolas idénticas de dos colores en N cajas

[Timus 1114](https://acm.timus.ru/problem.aspx?space=1&num=1114) · dificultad 194 · combinatorics

Problema original de la primera competición de selección del equipo búlgaro para la IOI.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` cajas en fila (`1 ≤ N ≤ 20`), `A` bolas rojas idénticas y `B`
bolas azules idénticas (`0 ≤ A, B ≤ 15`). En cada caja puede ir cualquier
número de bolas de cualquier color, las cajas pueden quedar vacías y las
bolas pueden quedar sin usar. Cuenta las distintas colocaciones.

Límite de tiempo: 0,6 segundos. Límite de memoria: 64 MB.

## Entrada

`N A B` en una línea.

## Salida

El número de colocaciones.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1 1
```

Salida:

```
9
```

## Solución

Los dos colores son independientes, así que la respuesta es el producto
de las cuentas de cada color. Poner como mucho `A` bolas idénticas en `N`
cajas equivale a poner exactamente `A` en `N + 1` cajas, donde la caja de
más guarda las no usadas; por el método de barras y estrellas son
`C(A + N, N)`. La respuesta es `C(A + N, N) · C(B + N, N)`.
C++, Go, Java y Rust construyen una tabla de Pascal de tamaño fijo en cada
ejecución, con tiempo y espacio `O(TOP²)`, donde `TOP = 40`, y después
realizan dos consultas y una multiplicación. Python llama dos veces a
`math.comb`, sin construir una tabla; su tiempo y espacio adicional son
`O(1)` bajo los límites dados `A + N, B + N ≤ 35`. Como `TOP` es fijo,
las otras implementaciones también usan tiempo y espacio `O(1)` respecto a la entrada.

Detalles a tener en cuenta:

- el caso mayor `N = 20, A = B = 15` ([prueba 03](tests/03.in)) da `C(35, 20)² ≈ 1,05 · 10^19`, que
  supera el máximo con signo de 64 bits `9,22 · 10^18` pero cabe en un
  entero de 64 bits sin signo;
- se permiten bolas sin usar: contar solo las colocaciones de todas las
  `A` bolas daría `C(A + N − 1, N − 1)`.

Las respuestas se comprobaron con una programación dinámica por cajas que
cuenta los llenados con cada número de bolas y los suma hasta `A` y `B`.

## Notas por lenguaje

- C++, Go y Rust multiplican en enteros de 64 bits sin signo; Java no
  tiene tipos sin signo, así que multiplica valores `long`, cuyos 64 bits
  son correctos módulo `2^64`, y los imprime con `Long.toUnsignedString`;
  los enteros de Python no se desbordan.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1114_combinatorics.cpp](1114_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(TOP²) | AC | 0.015 s | 140 KB |
| [1114_combinatorics.go](1114_combinatorics.go) | Go 1.14 x64 | combinatorics | O(TOP²) | AC | 0.015 s | 1060 KB |
| [1114_combinatorics.java](1114_combinatorics.java) | Java 1.8 | combinatorics | O(TOP²) | AC | 0.109 s | 1648 KB |
| [1114_combinatorics.py](1114_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) | AC | 0.078 s | 372 KB |
| [1114_combinatorics.rs](1114_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(TOP²) | AC | 0.015 s | 232 KB |
