# 1175. Dónde empieza a repetirse una recurrencia de dos términos y su periodo

[Timus 1175](https://acm.timus.ru/problem.aspx?space=1&num=1175) · dificultad 946 · math

Problema original de Alexander Klepinin, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una sucesión empieza con `X1`, `X2`, y cada término siguiente es
`F(Xn−1, Xn)`: se toma `H = A1·X·Y + A2·X + A3·Y + A4` y, si `H > B1`, se
resta `C` hasta que `H ≤ B2`. Todo `H` queda en `0..100000`. Hay que
hallar los menores `p` y `q` tales que `Xp+n = Xp+q+n` para todo `n ≥ 0`.

Límite de tiempo: 1 segundo. Límite de memoria: 2 MB.

## Entrada

`A1 A2 A3 A4 B1 B2 C`, y luego `X1 X2`.

## Salida

`p` y `q`.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0 2 3 20 5 7
0 1
```

Salida:

```
2 3
```

## Solución

El término siguiente depende de los dos últimos, así que el par
`(Xn, Xn+1)` evoluciona por sí solo, y los términos se repiten desde `p`
con periodo `q` exactamente cuando lo hacen los pares. Los pares recorren
un conjunto finito, así que caen en un ciclo: `p` es el índice del primer
par del ciclo y `q` su longitud.

Con 2 MB de memoria no se pueden guardar los pares, así que el ciclo se
busca con el método de Brent. Un puntero lento espera en un paso que es
potencia de dos mientras uno rápido avanza; cuando el rápido lo alcanza,
la distancia recorrida desde el último salto es la longitud `q`. Después
dos punteros salen del principio, uno `q` pasos por delante, y avanzan
juntos; se encuentran por primera vez al comienzo del ciclo, lo que da
`p`. `O(p + q)` pasos y memoria `O(1)`.

El bucle de restas se sustituye por una división: cuando `H > B1` y
`H > B2`, se resta `C` por `⌈(H − B2) / C⌉`.

Detalles a tener en cuenta:

- `p` se cuenta desde 1, el índice del primer término del par;
- el ciclo puede ser largo, por ejemplo los números de Fibonacci módulo
  31250 tienen periodo 187 500, así que guardar los pares rompería el
  límite de memoria;
- si `B1 < H ≤ B2`, no se resta nada.

Las respuestas se compararon con una búsqueda directa que guarda los
pares en un diccionario en 300 conjuntos aleatorios de parámetros, y con
una solución escrita aparte en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes hacen la misma búsqueda de Brent sobre pares de
  enteros de 64 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1175_math.cpp](1175_math.cpp) | G++ 13.2 x64 | math | O(p + q) | AC | 0.015 s | 128 KB |
| [1175_math.go](1175_math.go) | Go 1.14 x64 | math | O(p + q) | AC | 0.046 s | 1072 KB |
| [1175_math.java](1175_math.java) | Java 1.8 | math | O(p + q) | AC | 0.156 s | 1632 KB |
| [1175_math.py](1175_math.py) | Python 3.12 x64 | math | O(p + q) | AC | 0.171 s | 460 KB |
| [1175_math.rs](1175_math.rs) | Rust 1.75 x64 | math | O(p + q) | AC | 0.015 s | 224 KB |
