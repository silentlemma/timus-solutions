# 1590. Contar subcadenas distintas

[Timus 1590](https://acm.timus.ru/problem.aspx?space=1&num=1590) · dificultad 186 · strings

Problema original de Alexey Zhevak, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una cadena no vacía de `N ≤ 5000` letras latinas minúsculas, cuenta sus subcadenas contiguas distintas y no vacías. Tiempo: 2 segundos. Memoria: 64 MB.

## Entrada

La cadena.

## Salida

El número de subcadenas distintas.

## Evaluación

Se compara el entero de salida como token separado por espacios en blanco.

## Ejemplos

### Ejemplo 1

Entrada:

```
aaba
```

Salida:

```
8
```

## Solución

El algoritmo sencillo recomendado ordena todos los sufijos. El que empieza
en `i` tiene `N−i` prefijos no vacíos. Los ya vistos son exactamente los
prefijos compartidos con el sufijo anterior: todos los sufijos con cierto
prefijo ocupan un intervalo continuo en orden lexicográfico. La respuesta
es `N(N+1)/2` menos la suma de LCP entre sufijos adyacentes. El primero
aporta todos sus prefijos. Cada subcadena distinta se cuenta una sola vez.

Las cinco fuentes `sorting_strings` usan este algoritmo directo. Cada
comparación puede leer `O(N)` caracteres, por lo que el tiempo peor es
`O(N² log N)`. Las vistas C++, slices Go y slices prestados Rust necesitan
`O(N)` espacio auxiliar. Java 8 y Python bytes copian las subcadenas y
necesitan `O(N²)` espacio. Python busca el LCP por búsqueda binaria sobre
igualdad de prefijos, con comparaciones de bytes en C; conserva la cota
temporal. Las cinco implementaciones fueron aceptadas.

También se conservan los cinco autómatas de sufijos originales. Cada
estado agrupa subcadenas con las mismas posiciones finales y contribuye
`len(v)−len(link(v))` longitudes distintas. La suma sobre estados no raíz
da la respuesta en `O(N)` tiempo y espacio para el alfabeto fijo de 26.
Los clones copian transiciones y heredan el enlace de sufijo anterior.

## Soluciones optimizadas

El algoritmo didáctico preferido ordena sufijos y resta sus prefijos comunes adyacentes del número de ocurrencias de subcadenas. El C++ compacto ordena posiciones iniciales sin copiar cada sufijo, reduciendo memoria pero conservando el coste de comparaciones largas en el peor caso. Los autómatas de sufijos compactos guardan transiciones en listas de aristas planas; cada clon copia su lista antes de redirigir. Son algoritmos distintos, con nombres y comparaciones separados. Menor memoria puede implicar más tiempo, o al contrario.

- `1590_strings.java`: 0.093 s / 2412 KB; base `1590_sorting_strings.java`: 0.187 s / 28464 KB; cambio respecto a la base: tiempo -50.3%, memoria -91.5%.
- `1590_strings.py`: 0.109 s / 3132 KB; base `1590_sorting_strings.py`: 0.109 s / 14664 KB; cambio respecto a la base: tiempo -0.0%, memoria -78.6%.
- `1590_strings.rs`: 0.015 s / 2272 KB; base `1590_sorting_strings.rs`: 0.046 s / 300 KB; cambio respecto a la base: tiempo -67.4%, memoria +657.3%.
- `1590_strings_optimized.java`: 0.109 s / 748 KB; base `1590_sorting_strings.java`: 0.187 s / 28464 KB; cambio respecto a la base: tiempo -41.7%, memoria -97.4%.
- `1590_strings_optimized.py`: 0.109 s / 1084 KB; base `1590_sorting_strings.py`: 0.109 s / 14664 KB; cambio respecto a la base: tiempo -0.0%, memoria -92.6%.
- `1590_strings_optimized.rs`: 0.015 s / 504 KB; base `1590_sorting_strings.rs`: 0.046 s / 300 KB; cambio respecto a la base: tiempo -67.4%, memoria +68.0%.
- `1590_sorting_strings_optimized.cpp`: 0.031 s / 152 KB; base `1590_sorting_strings.cpp`: 0.015 s / 508 KB; cambio respecto a la base: tiempo +106.7%, memoria -70.1%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1590_sorting_strings.cpp`; versión que cubre `1590_sorting_strings_optimized.cpp`; puestos tiempo/memoria 43/1, registros de otros autores 119/119.

- Go: base didáctica preferida `1590_sorting_strings.go`; versión que cubre `1590_sorting_strings.go`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Java: base didáctica preferida `1590_sorting_strings.java`; versión que cubre `1590_strings.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1590_sorting_strings.py`; versión que cubre `1590_strings.py`; puestos tiempo/memoria 19/15, registros de otros autores 60/60.

- Rust: base didáctica preferida `1590_sorting_strings.rs`; versión que cubre `1590_sorting_strings.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1590_sorting_strings.cpp](1590_sorting_strings.cpp) | G++ 13.2 x64 | sorting, strings | O(N² log N) time, O(N) space for suffix views | AC | 0.015 s | 508 KB | 11308193 |
| [1590_sorting_strings.go](1590_sorting_strings.go) | Go 1.14 x64 | sorting, strings | O(N² log N) time, O(N) space for suffix views | AC | 0.031 s | 1192 KB | 11308194 |
| [1590_sorting_strings.java](1590_sorting_strings.java) | Java 1.8 | sorting, strings | O(N² log N) time, O(N²) space for copied Java 8 suffix strings | AC | 0.187 s | 28464 KB | 11308195 |
| [1590_sorting_strings.py](1590_sorting_strings.py) | Python 3.12 x64 | sorting, strings | O(N² log N) time, O(N²) space for copied suffixes; prefix equality tested by binary search | AC | 0.109 s | 14664 KB | 11308191 |
| [1590_sorting_strings.rs](1590_sorting_strings.rs) | Rust 1.75 x64 | sorting, strings | O(N² log N) time, O(N) space for suffix slices | AC | 0.046 s | 300 KB | 11308196 |
| [1590_strings.cpp](1590_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1428 KB | 11287986 |
| [1590_strings.go](1590_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2328 KB | 11287991 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1590_strings.java](1590_strings.java) | Java 1.8 | strings | O(N) | AC | 0.093 s | 2412 KB | 11287997 |
| [1590_strings.py](1590_strings.py) \* | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 3132 KB | 11287994 |
| [1590_strings.rs](1590_strings.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.015 s | 2272 KB | 11287999 |
| [1590_strings_optimized.java](1590_strings_optimized.java) | Java 1.8 | strings | O(N) | AC | 0.109 s | 748 KB | 11308188 |
| [1590_strings_optimized.py](1590_strings_optimized.py) \* | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 1084 KB | 11308180 |
| [1590_strings_optimized.rs](1590_strings_optimized.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.015 s | 504 KB | 11308189 |
| [1590_sorting_strings_optimized.cpp](1590_sorting_strings_optimized.cpp) \* | G++ 13.2 x64 | sorting, strings | O(N^2 log N) | AC | 0.031 s | 152 KB | 11309286 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
