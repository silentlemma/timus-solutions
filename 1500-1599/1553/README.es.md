# 1553. Cuevas y túneles

[Timus 1553](https://acm.timus.ru/problem.aspx?space=1&num=1553) · dificultad 282 · trees

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 100000 cuevas forman un árbol. Cada cueva tiene un nivel de
radiación, 0 al principio. Hay que responder Q ≤ 100000 consultas:
«I U V» sube el nivel de la cueva U en V ≤ 10000, y «G U V» pregunta el
nivel más alto en el camino de U a V.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

N, los N − 1 túneles, Q y las consultas.

## Salida

La respuesta a cada consulta G, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 2
2 3
2 4
6
I 1 1
G 1 1
G 3 4
I 2 3
G 1 1
G 3 4
```

Salida:

```
1
0
1
3
```

## Solución

Descomposición en caminos pesados: se enraíza el árbol en la cueva 1 y
cada cueva continúa su cadena por el hijo con el subárbol más grande.
Cualquier camino de una cueva hacia la raíz cruza como mucho log₂ N
cadenas, porque cada arista ligera al menos divide a la mitad el tamaño
del subárbol. Las cadenas se colocan una tras otra, de modo que cada una
ocupa posiciones consecutivas, y se mantiene un árbol de segmentos de
máximos sobre las posiciones.

Un aumento cambia una hoja y los máximos sobre ella. Una consulta de
camino sube desde el extremo cuya cabeza de cadena es más profunda,
tomando el máximo en ese tramo de la cadena, hasta que los dos extremos
comparten cadena, y termina con el tramo entre ellos. El árbol se
construye sin recursión, a partir de un orden de búsqueda en anchura,
porque un camino de 100000 cuevas desbordaría una búsqueda recursiva.
`O((N + Q) log² N)`.

Detalles a tener en cuenta:

- una consulta de una cueva a sí misma es el nivel de esa cueva
  (pruebas 01, 04);
- se permiten aumentos de 0 (prueba 04);
- un nivel puede llegar a 10⁹ (10⁵ aumentos de 10⁴), cerca del límite
  de 32 bits, así que las soluciones guardan los niveles en 64 bits;
- un camino de 100000 cuevas es una sola cadena larga (gen2).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1553_trees.cpp](1553_trees.cpp) | G++ 13.2 x64 | trees | O((N + Q) log^2 N) | AC | 0.390 s | 9584 KB |
| [1553_trees.go](1553_trees.go) | Go 1.14 x64 | trees | O((N + Q) log^2 N) | AC | 0.203 s | 19108 KB |
| [1553_trees.java](1553_trees.java) | Java 1.8 | trees | O((N + Q) log^2 N) | AC | 0.203 s | 10684 KB |
| [1553_trees.py](1553_trees.py) | Python 3.12 x64 | trees | O((N + Q) log^2 N) | AC | 2.140 s | 60768 KB |
| [1553_trees.rs](1553_trees.rs) | Rust 1.75 x64 | trees | O((N + Q) log^2 N) | AC | 0.140 s | 19664 KB |
