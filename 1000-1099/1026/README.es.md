# 1026. El k-ésimo menor elemento de una base de datos

[Timus 1026](https://acm.timus.ru/problem.aspx?space=1&num=1026) · dificultad 156 · sorting, prefix_sums

Problema original de Leonid Volkov, de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una base de datos guarda `N` enteros (`N ≤ 100 000`, cada uno de 1 a 5000,
en cualquier orden y con repeticiones). Responde `K` consultas
(`1 ≤ K ≤ 100`): para un `i` dado (`1 ≤ i ≤ N`), imprime el `i`-ésimo menor
elemento, contando las repeticiones.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` números, uno por línea; después una línea `###`; luego
`K` y las `K` consultas, una por línea.

## Salida

`K` líneas: las respuestas a las consultas en orden.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
42
7
5000
7
1
300
###
5
1
2
3
6
4
```

Salida:

```
1
7
7
5000
42
```

### Ejemplo 2

Entrada:

```
1
3000
###
1
1
```

Salida:

```
3000
```

## Solución

**Ordenación.** Se ordena la base una vez; la respuesta a la consulta `i`
es el elemento en la posición `i` (contando desde 1). `O(N log N + K)`.

**Conteo.** Los valores son pequeños, así que se cuenta cuántas veces
aparece cada valor `v ≤ 5000` y se toman sumas prefijas: `atMost[v]` es el
número de elementos no mayores que `v`. El `i`-ésimo menor elemento es el
menor `v` con `atMost[v] ≥ i`, que se encuentra con búsqueda binaria sobre
el arreglo no decreciente. `O(N + V + K log V)` con `V = 5000`.

Detalles a tener en cuenta:

- los valores repetidos ocupan varias posiciones: con 7 dos veces, las
  posiciones 2 y 3 contienen 7;
- la línea separadora `###` hay que saltarla, no leerla como número;
- lee la entrada rápido: son `10^5` líneas.

## Soluciones optimizadas

La solución optimizada en C++ cuenta los valores como la solución
sencilla por conteo, pero guarda los contadores en un arreglo global de
5001 `int`, analiza los números a mano desde un búfer de 4 KB que se
rellena con `fread` (la línea `###` se salta junto con los demás
caracteres que no son dígitos) e imprime con `printf` en lugar de
`iostream`: {1026_prefix_sums_optimized.cpp}.

La solución optimizada en Go cuenta en lugar de ordenar: guarda solo
cuántas veces aparece cada valor de 1 a 5000, calcula sumas prefijas y
responde cada consulta con una búsqueda binaria mediante
`sort.SearchInts`, así que la base no se guarda ni se ordena. Además
analiza los dígitos a mano desde el lector de `bufio` en lugar de
`fmt.Fscan`: {1026_prefix_sums.go}.

La solución optimizada en Java también cuenta en lugar de ordenar: las
frecuencias de los valores hasta 5000, sus sumas prefijas y una búsqueda
binaria por consulta. Lee la entrada en bloques de 4 KB y analiza los
dígitos a mano, saltándose la línea `###`, en lugar de crear un `String`
por cada línea: {1026_prefix_sums.java}.

La solución optimizada en Python también cuenta en lugar de ordenar. Lee
la base línea a línea, ya que cada valor está en su propia línea, anota
cada valor en una lista de 5001 frecuencias, calcula sumas prefijas y
responde cada consulta con `bisect_left`; no guarda ni la lista de todos
los tokens ni la lista ordenada de `N` números: {1026_prefix_sums.py}.

La solución optimizada en Rust cuenta los valores en un arreglo fijo de
5001 `u32` mientras lee la entrada línea a línea en un mismo `String`
reutilizado, y luego responde cada consulta con una búsqueda binaria
sobre las sumas prefijas en lugar de ordenar; no guarda ni la entrada
entera ni la base: {1026_prefix_sums.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1026_prefix_sums_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +76.36%; base: `1026_prefix_sums.cpp`.

- `1026_prefix_sums.go`: reducción de tiempo +67.39%; reducción de
  memoria +53.87%; base: `1026_sorting.go`.

- `1026_prefix_sums.java`: reducción de tiempo +0.00%; reducción de
  memoria +92.25%; base: `1026_sorting.java`.

- `1026_prefix_sums.py`: reducción de tiempo +14.68%; reducción de
  memoria +95.17%; base: `1026_sorting.py`.

- `1026_prefix_sums.rs`: reducción de tiempo -48.39%; reducción de
  memoria +89.10%; base: `1026_sorting.rs`.

## Notas por lenguaje

- **C++**: la ordenación y también el conteo con búsqueda binaria.
- **Go**, **Python**, **Java**, **Rust**: ordenación; Python lee todos los
  tokens de una vez.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1026_prefix_sums.cpp](1026_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.015 s | 440 KB | 11278309 |
| [1026_sorting.cpp](1026_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + K) | AC | 0.015 s | 816 KB | 11278308 |
| [1026_sorting.go](1026_sorting.go) | Go 1.14 x64 | sorting | O(N log N + K) | AC | 0.046 s | 2324 KB | 11278311 |
| [1026_sorting.java](1026_sorting.java) | Java 1.8 | sorting | O(N log N + K) | AC | 0.109 s | 5112 KB | 11278313 |
| [1026_sorting.py](1026_sorting.py) | Python 3.12 x64 | sorting | O(N log N + K) | AC | 0.109 s | 11668 KB | 11278312 |
| [1026_sorting.rs](1026_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + K) | AC | 0.031 s | 2128 KB | 11278314 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1026_prefix_sums_optimized.cpp](1026_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.001 s | 104 KB | 11305903 |
| [1026_prefix_sums.go](1026_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.015 s | 1072 KB | 11305908 |
| [1026_prefix_sums.java](1026_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.109 s | 396 KB | 11305911 |
| [1026_prefix_sums.py](1026_prefix_sums.py) \* | Python 3.12 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.093 s | 564 KB | 11305912 |
| [1026_prefix_sums.rs](1026_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.046 s | 232 KB | 11305916 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
