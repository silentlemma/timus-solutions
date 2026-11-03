# 1052. El máximo de puntos en una recta

[Timus 1052](https://acm.timus.ru/problem.aspx?space=1&num=1052) · dificultad 239 · geometry, sorting

Problema original de Stanislav Vasiliev, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `N` puntos distintos (`3 ≤ N ≤ 200`) con coordenadas enteras de
−2000 a 2000, halla el mayor número de ellos que están en una misma recta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con `x` e `y`.

## Salida

El mayor número de puntos en una recta.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
7 122
8 139
9 156
10 173
11 190
-100 1
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
3
0 0
1 0
0 1
```

Salida:

```
2
```

## Solución

Prueba cada par de puntos distintos `i,j`, que define una recta.
Cuenta sus puntos `k` con la igualdad exacta
`(x[k]−x[i])·(y[j]−y[i]) = (y[k]−y[i])·(x[j]−x[i])` y toma el máximo.
Una recta óptima contiene al menos dos puntos de entrada y, por tanto,
algún par probado la define. A la inversa, cada punto contado pertenece
a la recta elegida. Así el máximo es exactamente la respuesta.

Esta fuente directa `geometry_bruteforce` es la base sencilla preferida
en los cinco lenguajes. Tiempo `O(N³)`, como máximo 3 980 000 comprobaciones
para `N=200`, y espacio `O(N)` para la entrada. Si una recta contiene ya
los `N` puntos, se puede terminar. Las diferencias de coordenadas tienen
valor absoluto máximo 4000; cada producto llega a 16 000 000 y cabe en
32 bits con signo. No necesita pendientes reales, divisiones ni gcd.

La misma igualdad trata rectas verticales, horizontales, sentidos opuestos
y pendientes casi iguales. Los puntos distintos evitan un vector nulo;
la respuesta es al menos dos. Las fuentes directas pasaron todos los tests
del juez y se contrastaron localmente con ecuaciones canónicas de rectas
calculadas por un método independiente.

## Soluciones optimizadas

El algoritmo conservado de direcciones fija un punto y reduce cada
`(dx,dy)` por `gcd(|dx|,|dy|)`. Se cambia el signo para tener `dx>0`, o
`dx=0,dy>0`: los vectores opuestos representan la misma recta. Contar
direcciones iguales da sus puntos junto al origen. Basta mirar puntos
posteriores: el primero de una recta óptima ve todos los demás.

Con tablas hash, el tiempo esperado es `O(N² log C)` y el espacio de trabajo
`O(N)`, con `C=4000` como cota de las diferencias. C++ usa `std::map`
ordenado, por lo que su cota es `O(N²(log N+log C))`. No se supone coste
constante para la peor búsqueda de una tabla hash.

La fuente Python de direcciones, sin cambios, se clasifica como
optimizada frente a la nueva base: su Accepted CPython es 0,078 s y 508 KB,
frente a 0,250 s y 2840 KB del PyPy sencillo. Ahorra un 68,8% de tiempo
y un 82,1% de memoria. La comparación incluye algoritmo e intérprete,
ambos identificados en la tabla. Las fuentes nativas anteriores se
conservan como otros algoritmos aceptados, pero no muestran una ventaja
del 30% frente a la nueva base del mismo lenguaje. Un tick no justifica
la admisión.

La nueva fuente Rust `geometry_sorting` normaliza exactamente las mismas
direcciones, ordena un arreglo fijo y cuenta tramos iguales. Sustituye la
tabla hash por tiempo determinista `O(N²(log N+log C))` y espacio `O(N)`.
El primer punto de una recta óptima ve todos los demás; si quedan como máximo
`best` puntos incluido el origen, ya no puede mejorarse la respuesta.
Dos arreglos de 200 pares y búferes de E/S acotados no usan el heap; la entrada
con ABI C evita el arranque y formato de Rust que no se utilizan.
Su Accepted propio es 0,015 s / 52 KB, frente a 0,031 s / 212 KB de la base
cúbica Rust: reduce memoria un 75,5%. La diferencia de tiempo es un solo tick
y no justifica la admisión. Además de los tests del repositorio, los 466
subconjuntos de al menos dos puntos de una cuadrícula con signo 3×3 se
contrastaron con un oráculo independiente basado en productos cruzados.

## Notas por lenguaje

El Python cúbico fue aceptado con PyPy 3.10; el de direcciones con
CPython 3.12. Las demás bases usan los compiladores habituales del juez
y entrada estándar. Las direcciones usan `std::map` en C++, tablas hash
en Go/Rust, `Counter` en Python y `HashMap` en Java, cuya clave
`dx·8192+dy` no colisiona para componentes distintos con `|dy|≤4000`.

## Soluciones

### Sencillas

Las primeras cinco filas son las bases sencillas preferidas. Las cuatro últimas conservan los algoritmos nativos anteriores para compararlos.

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1052_geometry_bruteforce.cpp](1052_geometry_bruteforce.cpp) | G++ 13.2 x64 | geometry, bruteforce | O(N³) | AC | 0.015 s | 108 KB | 11308047 |
| [1052_geometry_bruteforce.go](1052_geometry_bruteforce.go) | Go 1.14 x64 | geometry, bruteforce | O(N³) | AC | 0.031 s | 1076 KB | 11308048 |
| [1052_geometry_bruteforce.java](1052_geometry_bruteforce.java) | Java 1.8 | geometry, bruteforce | O(N³) | AC | 0.125 s | 452 KB | 11308050 |
| [1052_geometry_bruteforce.py](1052_geometry_bruteforce.py) | PyPy 3.10 x64 | geometry, bruteforce | O(N³) | AC | 0.250 s | 2840 KB | 11308046 |
| [1052_geometry_bruteforce.rs](1052_geometry_bruteforce.rs) | Rust 1.75 x64 | geometry, bruteforce | O(N³) | AC | 0.031 s | 212 KB | 11308054 |
| [1052_geometry.cpp](1052_geometry.cpp) | G++ 13.2 x64 | geometry | O(N²(log N+log C)) | AC | 0.001 s | 208 KB | 11278696 |
| [1052_geometry.go](1052_geometry.go) | Go 1.14 x64 | geometry | O(N² log C) expected | AC | 0.015 s | 3264 KB | 11278697 |
| [1052_geometry.java](1052_geometry.java) | Java 1.8 | geometry | O(N² log C) expected | AC | 0.156 s | 4180 KB | 11278700 |
| [1052_geometry.rs](1052_geometry.rs) | Rust 1.75 x64 | geometry | O(N² log C) expected | AC | 0.015 s | 412 KB | 11278703 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1052_geometry.py](1052_geometry.py) | Python 3.12 x64 | geometry | O(N² log C) expected | AC | 0.078 s | 508 KB | 11278698 |
| [1052_geometry_sorting.rs](1052_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(N²(log N+log C)) | AC | 0.015 s | 52 KB | 11309709 |
