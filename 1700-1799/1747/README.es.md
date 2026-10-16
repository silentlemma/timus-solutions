# 1747. Inspección del reino

[Timus 1747](https://acm.timus.ru/problem.aspx?space=1&num=1747) · dificultad 1366 · combinatorics

Problema original de Artyom Ripatti, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada dos de n ciudades están unidas por un camino. El rey parte de la
capital, debe visitar cada ciudad exactamente dos veces y volver a la
capital. Contar las rutas posibles módulo p.

## Entrada

n y p (3 ≤ n ≤ 10⁵, 1 ≤ p ≤ 10⁹ + 7).

## Salida

El número de rutas módulo p.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 123
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
4 123
```

Salida:

```
30
```

## Solución

La capital se visita al principio y al final, así que entre medias la
ruta es una palabra en la que cada una de las otras m = n − 1 ciudades
aparece dos veces y ninguna ciudad se sigue a sí misma, pues un camino
une dos ciudades distintas. Inclusión y exclusión sobre los pares
escritos juntos cuentan esas palabras como

a(m) = Σ (−1)^k C(m, k) (2m − k)! / 2^(m − k),

pero p no tiene por qué ser primo, y dividir módulo p no siempre es
posible. Los mismos números cumplen

a(m) = m(2m − 1)·a(m − 1) + m(m − 1)·a(m − 2), a(0) = 1, a(1) = 0,

que solo necesita multiplicaciones, así que la respuesta sale en `O(n)`
pasos módulo cualquier p.

Para n = 4 hay tres ciudades más y las palabras son 30, como `ABCABC` y
`ABACBC`.

Trampas:

- p puede ser 1, par o cualquier compuesto, lo que descarta los
  inversos modulares;
- m(2m − 1) llega a 2·10¹⁰, así que se reduce módulo p antes de la
  siguiente multiplicación para quedar en 64 bits.

La recurrencia da los mismos números que la suma de inclusión y
exclusión, ambas con enteros exactos, para todo m hasta 59 y para
m = 100, 250, 500, 1000 y 1500. Las respuestas también coinciden con
una implementación aceptada independiente, que descompone p en
potencias de primos, en 68 pruebas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1747_combinatorics.cpp](1747_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.015 s | 384 KB |
| [1747_combinatorics.go](1747_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.031 s | 1080 KB |
| [1747_combinatorics.java](1747_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.140 s | 1592 KB |
| [1747_combinatorics.py](1747_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.140 s | 376 KB |
| [1747_combinatorics.rs](1747_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 244 KB |
