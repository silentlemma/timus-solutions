# 1422. Luciérnagas

[Timus 1422](https://acm.timus.ru/problem.aspx?space=1&num=1422) · dificultad 851 · geometry

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N moscas (1 ≤ N ≤ 2000) cuelgan quietas en puntos enteros con
coordenadas de hasta 10⁷ en valor absoluto. Una bola de fuego puntual
vuela por cualquier recta y convierte en luciérnaga cada mosca que
encuentra. Hay que hallar el mayor número de moscas que alcanza una
sola bola, es decir, el mayor número de puntos en una recta.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas X Y Z.

## Salida

El mayor número de moscas en una recta.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
-1 1 -1
0 1 2
0 0 -1
-2 -1 2
2 -1 -2
-1 0 2
```

Salida:

```
3
```

## Solución

Se toma cada mosca por turno como la primera de una recta y se miran
las direcciones hacia las moscas posteriores. Dos moscas están en la
misma recta que la primera justo cuando sus vectores diferencia son
múltiplos uno del otro, así que cada vector se divide entre el máximo
común divisor de sus componentes y se fija el signo para que la primera
componente no nula sea positiva. Vectores reducidos iguales son la
misma recta; contarlos (con una tabla hash o ordenando) da la mejor
recta por esa mosca. Las moscas en el mismo punto que la primera están
en todas las rectas que pasan por ella y se suman a la mejor cuenta.
Tiempo esperado `O(N² log C)` con hash; `O(N²(log C + log N))`
ordenando, con C = 2·10⁷, incluido el mcd.

Detalles a tener en cuenta:

- varias moscas pueden compartir un punto (pruebas 03, 05, gen4);
- una sola mosca también cuenta como 1 (prueba 02);
- las diferencias llegan a 2·10⁷, que aún cabe en 32 bits, y las claves
  enteras evitan redondear direcciones (pruebas 06, gen2).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1422_geometry.cpp](1422_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2 (log C + log N)) | AC | 0.328 s | 224 KB |
| [1422_geometry.go](1422_geometry.go) | Go 1.14 x64 | geometry | O(N^2 log C) | AC | 0.468 s | 6524 KB |
| [1422_geometry.java](1422_geometry.java) | Java 1.8 | geometry | O(N^2 log C) | AC | 0.343 s | 744 KB |
| [1422_geometry.py](1422_geometry.py) | Python 3.12 x64 | geometry | O(N^2 log C) | AC | 1.828 s | 1868 KB |
| [1422_geometry.rs](1422_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2 (log C + log N)) | AC | 0.312 s | 312 KB |
