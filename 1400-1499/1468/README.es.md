# 1468. Fracción

[Timus 1468](https://acm.timus.ru/problem.aspx?space=1&num=1468) · dificultad 836 · math

Problema original de Dmitry Zhukov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para hasta 100 pruebas a, b, k (1 ≤ a, b ≤ 10000, 2 ≤ k ≤ 36) hay que
escribir a / b en base k con las cifras 0–9 y A–Z: la parte entera y,
si el número no es entero, un punto y las cifras fraccionarias, con el
periodo entre paréntesis. No debe haber ceros innecesarios. La entrada
termina con «0 0».

Límite de tiempo: 0.4 segundos. Límite de memoria: 64 MB.

## Entrada

Líneas a b k y luego «0 0».

## Salida

Una línea por prueba.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 5 2
1 2 8
8780 1 29
2794 6083 23
157 7 19
1 12 10
0 0
```

Salida:

```
10
0.4
ACM
0.(ACM)
13.(82DAG5)
0.08(3)
```

## Solución

La parte entera a div b se escribe en base k como siempre. La parte
fraccionaria es una división larga: el resto se multiplica por k, el
cociente entre b es la cifra siguiente y lo que sobra es el nuevo resto.
Hay b restos posibles, así que o alguno llega a 0 (la fracción termina)
o alguno vuelve a salir. Anotando la posición en que apareció cada resto
por primera vez se obtiene el periodo exacto: las cifras desde esa
posición se repiten para siempre, y como un resto decide todo lo que
sigue, es el periodo más corto y empieza lo antes posible. `O(b)` por
prueba.

Detalles a tener en cuenta:

- los resultados enteros no llevan punto (pruebas 01, 02);
- el periodo puede empezar tras algunas cifras no periódicas, como en
  0.08(3) (prueba 01);
- los periodos pueden tener casi 10000 cifras (prueba 03, gen2).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1468_math.cpp](1468_math.cpp) | G++ 13.2 x64 | math | O(b) per test | AC | 0.031 s | 380 KB |
| [1468_math.go](1468_math.go) | Go 1.14 x64 | math | O(b) per test | AC | 0.031 s | 6576 KB |
| [1468_math.java](1468_math.java) | Java 1.8 | math | O(b) per test | AC | 0.125 s | 10144 KB |
| [1468_math.py](1468_math.py) | Python 3.12 x64 | math | O(b) per test | AC | 0.343 s | 5672 KB |
| [1468_math.rs](1468_math.rs) | Rust 1.75 x64 | math | O(b) per test | AC | 0.015 s | 1820 KB |
