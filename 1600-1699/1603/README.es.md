# 1603. Erudito

[Timus 1603](https://acm.timus.ru/problem.aspx?space=1&num=1603) · dificultad 255 · implementation

Problema original de Vladimir Yakovlev, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula de 4 × 4 contiene letras minúsculas. Una palabra puede
escribirse en ella a lo largo de un camino de casillas vecinas en
horizontal o vertical, que puede girar en ángulo recto en cualquier
punto pero no pasa dos veces por la misma casilla. Para cada una de hasta
100 palabras de 1 a 16 letras hay que decir si se puede encontrar.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Cuatro filas de la cuadrícula, luego n y las palabras.

## Salida

`word: YES` o `word: NO` para cada palabra.

## Ejemplos

### Ejemplo 1

Entrada:

```
abra
adac
babr
arca
3
abracadabra
ababaab
ababaaba
```

Salida:

```
abracadabra: YES
ababaab: YES
ababaaba: NO
```

## Solución

Se busca en profundidad desde cada casilla con la primera letra,
pasando a una casilla vecina no usada con la letra siguiente. Las
casillas usadas forman una máscara de 16 bits. Las letras repetidas
pueden hacer que la búsqueda vuelva muchas veces a la misma situación:
el mismo conjunto de casillas usadas, la misma última casilla y el mismo
resto de palabra. Así que un par (máscara, casilla) fallido se recuerda
y no se vuelve a explorar; hay como mucho 16·2¹⁶ pares así, y en la
práctica muchos menos alcanzables. Una comprobación rápida descarta
antes la palabra que necesita más de alguna letra de las que hay.

Los resultados se compararon con una implementación independiente en
cuadrículas generadas, incluidas cuadrículas de una sola letra repetida
con palabras largas.

Detalles a tener en cuenta:

- contar las letras permite descartar una palabra antes de buscar:
  quince casillas `a` no bastan para dieciséis letras `a`, y la única
  casilla `b` no puede usarse en ambos extremos de una palabra (prueba 04);
- las letras repetidas pueden llevar a explorar estados repetidos, por
  lo que se recuerdan los pares (máscara, casilla) fallidos; la prueba 07
  tiene catorce casillas `a` y una de cada letra `b` y `c`, y su palabra
  más larga supera la comprobación de cantidades de letras;
- ese NO puede deberse solo a la paridad: si se colorea la cuadrícula
  como un tablero de ajedrez, un camino de 16 casillas siempre termina en
  el otro color, así que una palabra que empieza y acaba en casillas del
  mismo color no puede ocupar las 16 (prueba 07);
- una casilla no puede usarse dos veces, y los pasos son solo
  horizontales o verticales (prueba 03).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1603_implementation.cpp](1603_implementation.cpp) | G++ 13.2 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 452 KB |
| [1603_implementation.go](1603_implementation.go) | Go 1.14 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 5708 KB |
| [1603_implementation.java](1603_implementation.java) | Java 1.8 | implementation | O(n·16·2^16) | AC | 0.109 s | 5228 KB |
| [1603_implementation.py](1603_implementation.py) | Python 3.12 x64 | implementation | O(n·16·2^16) | AC | 0.359 s | 21264 KB |
| [1603_implementation.rs](1603_implementation.rs) | Rust 1.75 x64 | implementation | O(n·16·2^16) | AC | 0.062 s | 420 KB |
