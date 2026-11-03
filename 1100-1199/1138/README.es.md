# 1138. La serie más larga de trabajos con aumentos de un número entero de por ciento

[Timus 1138](https://acm.timus.ru/problem.aspx?space=1&num=1138) · dificultad 204 · dp

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El primer sueldo de un programador fue exactamente `s`, cada sueldo
siguiente es un entero positivo mayor que el anterior en un número entero
de por ciento, y el último es como mucho `n`, con `1 ≤ n, s ≤ 10000`. Halla
el mayor número posible de trabajos, contando el primero.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y `s`.

## Salida

El mayor número de trabajos.

## Evaluación

Comparar un token entero. Las adiciones nativas conservadas tienen 380 ejecuciones extra cada una: 320 enumeraciones exactas pequeñas y 60 regresiones de frontera. El Python didáctico revisado tiene 7730 ejecuciones contra un oráculo DAG literal, 7260 comparaciones de sucesores, 12 pruebas del repositorio y 169 comprobaciones extra de PyPy, incluido n máximo. Son comprobaciones distintas, no totales de todos los lenguajes nativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2
```

Salida:

```
5
```

## Solución

Sea `jobs[a]` la mayor cantidad de trabajos desde `s` hasta el salario `a`.
Una subida a `b>a` es válida si `100(b−a)` es divisible por `a`. Las cuatro
versiones didácticas nativas prueban cada salario entero mayor y actualizan
`jobs[b]=max(jobs[b],jobs[a]+1)`. Solo se inicializa `jobs[s]=1`. Los salarios
crecen estrictamente: el orden ascendente es topológico y la inducción
demuestra la DP del camino máximo. Tiempo `O(n²)`, espacio `O(n)`.

El Python didáctico aceptado enumera porcentajes enteros positivos:
para cada `a` alcanzable prueba `p≤floor(100(n−a)/a)` y pasa a `a+a*p/100`
solo si `a*p % 100 == 0`. Cada sucesor válido corresponde a un único
porcentaje, así que conserva la prueba sin necesitar el argumento del mcd.
Son `O(P n log n)` comprobaciones, `P=100`, y `O(n)` espacio; no es el barrido
cuadrático de parejas. Está aceptado con PyPy 3.10. La versión Python
anterior de parejas excedió el tiempo y no se publica.

Si `s>n`, devolver cero; en caso contrario contar el primer trabajo. Las
subidas son positivas y se omiten estados inalcanzables. Los productos
no superan un millón y hay como máximo 10000 trabajos: bastan 32 bits.

## Soluciones optimizadas

Con `P=100` y `g=mcd(a,P)`, los números `a/g` y `P/g` son coprimos.
Por ello `a | P(b−a)` equivale a `(a/g) | (b−a)`: los sucesores son
exactamente `a+a/g,a+2a/g,…`. Se generan solo esos salarios, sin probar
todos los salarios o porcentajes. La prueba topológica permanece válida.
Hay como máximo `Pn/a` actualizaciones por salario; tiempo
`O(P n log n+n log P)`, incluido el mcd, y espacio `O(n)`. El Java adicional
precalcula `mcd(r,100)` para los 100 residuos y usa StreamTokenizer.

Se conservan los cinco programas previos con mcd. Su algoritmo difiere de
las enumeraciones didácticas y mantiene el nombre `dp`; el Java adicional
`_optimized` conserva ese mismo algoritmo. Las comparaciones usan la base
preferida real de cada lenguaje. Python incluye el cambio PyPy/CPython;
ahorrar memoria no implica cumplir ambas metas de clasificación.

- `1138_dp.cpp`: 0.015 s / 224 KB; base `1138_bruteforce_dp.cpp`: 0.125 s / 208 KB; cambio respecto a la base: tiempo -88.0%, memoria +7.7%.
- `1138_dp.go`: 0.031 s / 1144 KB; base `1138_bruteforce_dp.go`: 0.546 s / 1140 KB; cambio respecto a la base: tiempo -94.3%, memoria +0.4%.
- `1138_dp.java`: 0.125 s / 1680 KB; base `1138_bruteforce_dp.java`: 0.296 s / 460 KB; cambio respecto a la base: tiempo -57.8%, memoria +265.2%.
- `1138_dp.py`: 0.093 s / 508 KB; base `1138_bruteforce_dp.py`: 0.140 s / 1988 KB; cambio respecto a la base: tiempo -33.6%, memoria -74.4%.
- `1138_dp.rs`: 0.015 s / 256 KB; base `1138_bruteforce_dp.rs`: 0.234 s / 236 KB; cambio respecto a la base: tiempo -93.6%, memoria +8.5%.
- `1138_dp_optimized.java`: 0.093 s / 448 KB; base `1138_bruteforce_dp.java`: 0.296 s / 460 KB; cambio respecto a la base: tiempo -68.6%, memoria -2.6%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1138_bruteforce_dp.cpp`; fuente que cubre `1138_dp.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 64/64.

- Go: base didáctica preferida `1138_bruteforce_dp.go`; fuente que cubre `1138_dp.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1138_bruteforce_dp.java`; fuente que cubre `1138_dp_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1138_bruteforce_dp.py`; fuente que cubre `1138_dp.py`; puestos tiempo/memoria 2/3, registros de otros autores 10/10.

- Rust: base didáctica preferida `1138_bruteforce_dp.rs`; fuente que cubre `1138_dp.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1138_bruteforce_dp.cpp](1138_bruteforce_dp.cpp) | G++ 13.2 x64 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.125 s | 208 KB | 11308262 |
| [1138_bruteforce_dp.go](1138_bruteforce_dp.go) | Go 1.14 x64 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.546 s | 1140 KB | 11308263 |
| [1138_bruteforce_dp.java](1138_bruteforce_dp.java) | Java 1.8 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.296 s | 460 KB | 11308265 |
| [1138_bruteforce_dp.py](1138_bruteforce_dp.py) | PyPy 3.10 x64 | bruteforce, dp | O(P n log n) time; O(n) space, P=100 | AC | 0.140 s | 1988 KB | 11309354 |
| [1138_bruteforce_dp.rs](1138_bruteforce_dp.rs) | Rust 1.75 x64 | bruteforce, dp | O(n^2) time; O(n) space | AC | 0.234 s | 236 KB | 11308269 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1138_dp.cpp](1138_dp.cpp) | G++ 13.2 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.015 s | 224 KB | 11279425 |
| [1138_dp.go](1138_dp.go) | Go 1.14 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.031 s | 1144 KB | 11279426 |
| [1138_dp.java](1138_dp.java) \* | Java 1.8 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.125 s | 1680 KB | 11279429 |
| [1138_dp.py](1138_dp.py) \* | Python 3.12 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.093 s | 508 KB | 11279428 |
| [1138_dp.rs](1138_dp.rs) | Rust 1.75 x64 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.015 s | 256 KB | 11279431 |
| [1138_dp_optimized.java](1138_dp_optimized.java) | Java 1.8 | dp | O(P n log n + n log P) time; O(n+P) space, P=100 | AC | 0.093 s | 448 KB | 11308275 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
