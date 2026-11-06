# 1406. El número siguiente

[Timus 1406](https://acm.timus.ru/problem.aspx?space=1&num=1406) · dificultad 344 · greedy

Problema original de Alexander Ipatov, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da un número N de K cifras, K ≤ 2000, quizá con ceros a la
izquierda. Hay que imprimir el menor número de K cifras mayor que N con
la misma suma de cifras, también con ceros a la izquierda, o -1 si no
existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N con todas sus K cifras.

## Salida

El número siguiente, o -1.

## Ejemplos

### Ejemplo 1

Entrada:

```
113
```

Salida:

```
122
```

### Ejemplo 2

Entrada:

```
0050
```

Salida:

```
0104
```

## Solución

Un número mayor con la misma suma coincide con N hasta cierta posición,
tiene ahí una cifra mayor, y las cifras siguientes devuelven lo que esa
cifra tomó. El número siguiente cambia la posición más tardía posible y
sube su cifra exactamente en uno, así que se busca la cifra más a la
derecha menor que 9 con suma positiva tras ella. Se sube en uno y se
rehace la cola con esa suma menos uno en su forma más pequeña: primero
ceros y la suma empujada al final, nueves desde la derecha. Si ninguna
cifra sirve, la respuesta es -1. `O(K)`.

Detalles a tener en cuenta:

- los ceros a la izquierda forman parte del número y deben conservarse
  (ejemplo 2 y prueba 09);
- 0, 9 y números como 1000 no tienen siguiente (pruebas 05 a 07, y
  prueba generada 3, el mayor número de su suma);
- el número tiene hasta 2000 cifras, mucho más que los tipos enteros de
  ancho fijo; `int` de Python admite precisión arbitraria, pero hay que
  conservar la longitud para mantener los ceros iniciales (prueba 09).

Las respuestas se compararon con contar número a número en 2 000
números aleatorios de hasta cinco cifras.

## Soluciones optimizadas

C++ y Go recorren de derecha a izquierda manteniendo la suma de cifras del sufijo. Incrementan la primera cifra menor que nueve con suma positiva a su derecha y distribuyen el resto desde el extremo derecho para minimizar el sufijo. Ambas versiones modifican las cifras de entrada en el mismo búfer, con espacio adicional constante. Go lee y guarda las cifras en matrices fijas de bytes, sin tokens de Scanner. Accede directamente a los descriptores estándar, reintenta llamadas interrumpidas y completa escrituras parciales.

Las implementaciones base aceptadas [1406_greedy.java](1406_greedy.java), [1406_greedy.py](1406_greedy.py), [1406_greedy.rs](1406_greedy.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1406_greedy.cpp](1406_greedy.cpp) | G++ 13.2 x64 | greedy | O(K) | AC | 0.015 s | 376 KB | 11286049 |
| [1406_greedy.go](1406_greedy.go) | Go 1.14 x64 | greedy | O(K) | AC | 0.031 s | 1088 KB | 11286050 |
| [1406_greedy.java](1406_greedy.java) \* | Java 1.8 | greedy | O(K) | AC | 0.125 s | 1576 KB | 11286052 |
| [1406_greedy.py](1406_greedy.py) \* | Python 3.12 x64 | greedy | O(K) | AC | 0.093 s | 552 KB | 11286051 |
| [1406_greedy.rs](1406_greedy.rs) \* | Rust 1.75 x64 | greedy | O(K) | AC | 0.062 s | 200 KB | 11286053 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1406_greedy_optimized.cpp](1406_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(K) | AC | 0.015 s | 96 KB | 11310623 |
| [1406_greedy_optimized.go](1406_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(K) | AC | 0.015 s | 328 KB | 11311213 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
