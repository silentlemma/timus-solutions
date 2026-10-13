# 1353. La función milmillonaria de Vasya

[Timus 1353](https://acm.timus.ru/problem.aspx?space=1&num=1353) · dificultad 103 · dp

Problema original de Denis Musin, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado S, 1 ≤ S ≤ 81, hay que contar los enteros de 1 a 10⁹ cuya suma de
cifras es S.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número S.

## Salida

La cantidad.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
10
```

## Solución

Todo número menor que 10⁹ es una cadena de nueve cifras si se le añaden
ceros a la izquierda, y esos ceros no cambian la suma de cifras. Así que
se cuentan cadenas de cifras: ways[s] tras k cifras es la cantidad de
cadenas de k cifras con suma s, y cada cifra nueva d de 0 a 9 lleva
ways[s] a s + d. Tras nueve cifras, ways[S] cuenta los números de 0 a
999 999 999 con suma S. El cero tiene suma 0 y nunca se cuenta, y el
propio 10⁹, con suma de cifras 1, suma uno cuando S = 1.
`O(9 · 81 · 10)`.

Detalles a tener en cuenta:

- 10⁹ está en el rango: S = 1 da 10, no 9 (prueba 01);
- desde S = 10 una sola cifra ya no puede llevar toda la suma, y el
  conteo simple de barras y estrellas cuenta de más (prueba 07);
- los valores son simétricos, ways[s] = ways[81 − s], y el mayor es
  45 433 800 en S = 40 y 41, que cabe en 32 bits.

La misma tabla para 10⁶ en lugar de 10⁹ se comparó con contar las sumas
de cifras de todos los números hasta 10⁶.

## Notas por lenguaje

- Las cinco soluciones construyen la tabla cifra a cifra de la misma
  forma.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1353_dp.cpp](1353_dp.cpp) | G++ 13.2 x64 | dp | O(9·81·10) | AC | 0.015 s | 200 KB |
| [1353_dp.go](1353_dp.go) | Go 1.14 x64 | dp | O(9·81·10) | AC | 0.031 s | 1124 KB |
| [1353_dp.java](1353_dp.java) | Java 1.8 | dp | O(9·81·10) | AC | 0.109 s | 1584 KB |
| [1353_dp.py](1353_dp.py) | Python 3.12 x64 | dp | O(9·81·10) | AC | 0.093 s | 444 KB |
| [1353_dp.rs](1353_dp.rs) | Rust 1.75 x64 | dp | O(9·81·10) | AC | 0.015 s | 228 KB |
