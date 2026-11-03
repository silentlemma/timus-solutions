# 1157. Las menos baldosas que forman N rectángulos, cuando K baldosas menos formaban M

[Timus 1157](https://acm.timus.ru/problem.aspx?space=1&num=1157) · dificultad 200 · number_theory

Problema original del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un niño coloca todas sus baldosas cuadradas en forma de rectángulo. Dados
`M`, `N` y `K` (`M, N ≤ 50`, `K ≤ 9999`), halla el menor número de
baldosas `L` tal que con `L` baldosas se formen exactamente `N`
rectángulos distintos y con `L − K` baldosas exactamente `M`. Imprime `0`
si no hay tal `L` hasta 10000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`M`, `N` y `K`.

## Salida

El menor `L`, o `0`.

## Evaluación

Se factorizaron independientemente todos los números de baldosas
`1..10000`, calculando divisores mediante exponentes primos para obtener
la tabla de formas de referencia; su máximo es 32. El candidato Python
real se comprobó con 125 consultas, incluido el ejemplo, cantidades sin
solución y `K = 9999`, buscando la primera coincidencia en esa tabla
independiente. Los cinco candidatos reales pasaron además 13 entradas
del repositorio cada uno en Docker. No es una prueba exhaustiva de todas
las ternas de entrada. Después los cinco obtuvieron su propio Accepted.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3 1
```

Salida:

```
16
```

## Solución

Cada rectángulo de `x` baldosas corresponde a una pareja no ordenada
de divisores `a × b = x`, `a ≤ b`; girarlo no crea otra forma. Sea `d[x]`
el número de divisores. Emparejando cada divisor con su cociente obtenemos
`shapes[x] = (d[x] + 1) // 2`: en un cuadrado el divisor central se empareja
consigo mismo.

La criba sencilla incrementa `d[x]` en cada múltiplo de cada divisor
`1..B`, con `B = 10000`, contando cada divisor una vez. Recorremos `L`
en orden desde `K + 1` hasta `B` y comprobamos ambos números de formas.
La primera coincidencia es mínima; si no existe, imprimimos `0`.
Empezar en `K + 1` garantiza `L − K ≥ 1`. Esto demuestra el recuento y
la selección de la respuesta. Tiempo `O(B log B)`, espacio auxiliar `O(B)`.
Se conservan sin cambios las cinco fuentes Accepted originales. Python
materializa otra lista de formas; las bases nativas calculan la cantidad
de formas a partir de la tabla de divisores cuando la necesitan.

## Soluciones optimizadas

Contamos directamente parejas no ordenadas de divisores. Para cada
lado menor `a = 1..floor(sqrt(B))`, incrementamos `a², a² + a, …, B`.
Son exactamente los productos `a × b` con `b ≥ a`. Cada rectángulo tiene
un único lado menor, de modo que se visita una vez; el cuadrado también
se cuenta una vez. La misma búsqueda creciente obtiene la misma respuesta.

Basta un byte por contador: para cualquier `x ≤ B` hay como máximo
`floor(sqrt(x)) ≤ 100` lados menores posibles. Ni siquiera el `byte`
con signo de Java puede desbordarse. La tabla ocupa `10001` bytes, sin
contar cabecera, E/S ni entorno de ejecución. Tiempo `O(B log B)` y
espacio `O(B)`, con menos incrementos y almacenamiento compacto. Java
también sustituye `Scanner` por `StreamTokenizer`; Rust analiza tres
números sin recopilar un vector numérico. Son implementaciones distintas
del mismo enfoque de criba de parejas, de ahí el sufijo `_optimized`.

Frente a la base del mismo lenguaje, la memoria de C++ baja de 216 a
120 KB (44,4%), Python de 712 a 428 KB (39,9%), Java de 1620 a 420 KB
(74,1%). C++ y Python mantienen el tiempo registrado; Java también mejora
0,125 → 0,078 s (37,6%). Rust se admite por tiempo: 0,046 → 0,015 s
(67,4%); la memoria solo baja un 25,3%, 300 → 224 KB. Cada versión
publicada tiene su propio Accepted ligado a sus bytes exactos.

El candidato Go también fue Accepted, pero la memoria solo mejora un
8,2%, 1172 → 1076 KB; 0,031 → 0,015 s supone un solo tic del temporizador.
Ese tic no demuestra una aceleración fiable: no se añade como fuente
optimizada y se conserva la base Go original.

## Notas por lenguaje

La instantánea es del 2 de noviembre de 2026. C++ optimizado ocupa
los puestos 1 en tiempo y 2 en memoria frente a 73 registros filtrados
de otros autores y cumple el objetivo. Python tiene puestos 2 y 2 frente
a 16 registros; Java, 1 y 2 frente a cinco. Con el perfil más estricto
establecido para lenguajes distintos de C++, que exige primer puesto
en ambas métricas, conservan asteriscos pese a las mejoras admitidas.
Las muestras filtradas Go y Rust están vacías: su cobertura formal no
demuestra superioridad competitiva. El objetivo de clasificación y el
criterio de admisión del 30% se registran por separado.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1157_number_theory.cpp](1157_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(B log B) | AC | 0.015 s | 216 KB | 11281313 |
| [1157_number_theory.go](1157_number_theory.go) | Go 1.14 x64 | number_theory | O(B log B) | AC | 0.031 s | 1172 KB | 11281331 |
| [1157_number_theory.java](1157_number_theory.java) | Java 1.8 | number_theory | O(B log B) | AC | 0.125 s | 1620 KB | 11281380 |
| [1157_number_theory.py](1157_number_theory.py) | Python 3.12 x64 | number_theory | O(B log B) | AC | 0.078 s | 712 KB | 11281359 |
| [1157_number_theory.rs](1157_number_theory.rs) | Rust 1.75 x64 | number_theory | O(B log B) | AC | 0.046 s | 300 KB | 11281448 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1157_number_theory_optimized.cpp](1157_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(B log B) | AC | 0.015 s | 120 KB | 11308304 |
| [1157_number_theory_optimized.java](1157_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(B log B) | AC | 0.078 s | 420 KB | 11308317 |
| [1157_number_theory_optimized.py](1157_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(B log B) | AC | 0.078 s | 428 KB | 11308301 |
| [1157_number_theory_optimized.rs](1157_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(B log B) | AC | 0.015 s | 224 KB | 11308320 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
