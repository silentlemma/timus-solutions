# 1003. Primera respuesta de paridad contradictoria

[Timus 1003](https://acm.timus.ru/problem.aspx?space=1&num=1003) · dificultad 385 · dsu, hashing

Problema original de la Olimpiada Centroeuropea de Informática 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay una secuencia desconocida de `L` bits (`L ≤ 10^9`). Llegan en orden
`q ≤ 5000` afirmaciones; la afirmación `i` dice que la cantidad de unos entre
los bits `l..r` (numerados desde 1, `l ≤ r`) es par o impar.

Encuentra el mayor `X` tal que alguna secuencia de bits cumple las primeras
`X` afirmaciones. Si todas pueden cumplirse a la vez, `X = q`.

La entrada contiene varias pruebas de este tipo.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Las pruebas van una tras otra. Una prueba es una línea con `L`, una línea con
`q` y `q` líneas `l r even` o `l r odd`. Una línea `-1` termina la entrada.

## Salida

Para cada prueba, una línea con `X`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
3
1 2 odd
3 4 even
1 4 even
-1
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
8
4
1 8 even
1 4 odd
5 8 odd
2 3 even
3
2
1 3 odd
1 3 even
-1
```

Salida:

```
4
1
```

## Solución

Sea `P(k)` la paridad de la cantidad de unos entre los primeros `k` bits, con
`P(0) = 0`. Una afirmación sobre `l..r` dice `P(l-1) xor P(r) = 0` (par) o `1`
(impar). Y al revés, cualquier valor de `P` con `P(0) = 0` proviene de
exactamente una secuencia de bits. Por eso las afirmaciones son compatibles
exactamente cuando el sistema de ecuaciones `P(a) xor P(b) = w` tiene
solución.

Se procesan las afirmaciones en orden con una estructura de conjuntos
disjuntos sobre las posiciones de prefijos que guarda, para cada nodo, la
paridad respecto a su padre. `find` devuelve la raíz y la paridad del nodo
respecto a ella. Para una ecuación nueva: si ambos extremos están en el mismo
conjunto, la ecuación debe coincidir con las paridades ya conocidas; si no, se
unen los conjuntos con la paridad correcta en la arista nueva. La primera
ecuación que no coincide da `X`.

Las posiciones llegan hasta `10^9`, pero aparecen como mucho `2q`: se asignan a
identificadores consecutivos con una tabla hash. Con compresión de caminos y
unión por rango el trabajo es `O(q · α(q))` por prueba; Python omite los rangos
y tarda `O(q log q)`.

Detalles a tener en cuenta:

- las ecuaciones relacionan los prefijos `l-1` y `r`, no `l` y `r`;
- después de la primera contradicción hay que seguir leyendo el resto de la
  prueba;
- una prueba puede no tener ninguna afirmación.

## Soluciones optimizadas

`1003_dsu_hashing_optimized.py`. Mantiene DSU exacto de paridad, IDs de coordenadas al vuelo y compresión iterativa por abuelo. Padre/paridad siguen codificados como 2*parent+parity, ahora en una lista nativa en vez de shorts, evitando conversiones por acceso; los rangos siguen en bytearray. No cambian orden, primera contradicción ni consumo posterior. Trabajo esperado O(Q α(Q)) más entrada; estado O(Q) y lectura por líneas.

Accepted exacto CPython 3.12 #11326679: 0.062 s / 1040 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 3/35, memoria 1/35. Desde 1024 KB se exigen ambos criterios estrictos; pasan ambos.

- `1003_dsu_hashing_optimized.py`: 0.062 s / 1040 KB; base didáctica conservada `1003_dsu_hashing.py` (Python 3.12 x64): 0.093 s / 4388 KB; cambio de tiempo -33.3%; cambio de memoria -76.3%.

Ambas codifican juntos padre y paridad. C++ usa entradas de 16 bits; el Python actual usa enteros normales en lista, no un arreglo de almacenamiento de 16 bits. La paridad ocupa el bit inferior. C++ primero ordena y elimina las posiciones repetidas, luego busca sus índices por búsqueda binaria. Python asigna índices según se necesitan con una tabla hash y reconecta cada nodo visitado con su abuelo usando la paridad combinada. Las ecuaciones se comprueban en orden de entrada.

Las bases Accepted conservadas [1003_dsu_hashing.cpp](1003_dsu_hashing.cpp), [1003_dsu_hashing.go](1003_dsu_hashing.go), [1003_dsu_hashing.java](1003_dsu_hashing.java), [1003_dsu_hashing.rs](1003_dsu_hashing.rs) pasan también diez primeros o 15% superior en las métricas exigidas de la comparación guardada. Se reutilizan sin duplicados; conserva las demás bases. El asterisco indica la meta propia del lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- **C++**: `std::unordered_map<int, int>` para los identificadores; un `find`
  recursivo está bien, los árboles son poco profundos con unión por rango.
- **Go**: `map[int]int` y un `find` recursivo con compresión de caminos.
- **Python**: un `find` iterativo que comprime el camino y recalcula las
  paridades de sus nodos.
- **Java**: arreglos de tamaño `2q` por prueba, `HashMap<Integer, Integer>`
  para los identificadores, `find` iterativo.
- **Rust**: `HashMap<i64, usize>` con `entry().or_insert_with()` para crear
  nodos; `find` iterativo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1003_dsu_hashing.cpp](1003_dsu_hashing.cpp) | G++ 13.2 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.015 s | 632 KB | 11277428 |
| [1003_dsu_hashing.go](1003_dsu_hashing.go) \* | Go 1.14 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.046 s | 3420 KB | 11277429 |
| [1003_dsu_hashing.java](1003_dsu_hashing.java) \* | Java 1.8 | dsu, hashing | O(q·α(q)) per test | AC | 0.109 s | 4788 KB | 11277431 |
| [1003_dsu_hashing.py](1003_dsu_hashing.py) | Python 3.12 x64 | dsu, hashing | O(q log q) per test | AC | 0.093 s | 4388 KB | 11277430 |
| [1003_dsu_hashing.rs](1003_dsu_hashing.rs) \* | Rust 1.75 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.001 s | 1268 KB | 11277432 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1003_dsu_sorting.cpp](1003_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(q log q) per test | AC | 0.015 s | 184 KB | 11310464 |
| [1003_dsu_hashing_optimized.py](1003_dsu_hashing_optimized.py) \* | Python 3.12 x64 | dsu, hashing | O(q·α(q)) expected per test | AC | 0.062 s | 1040 KB | 11326679 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
