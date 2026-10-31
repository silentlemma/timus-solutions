# 1160. Conectar todos los concentradores con el cable más largo lo más corto posible

[Timus 1160](https://acm.timus.ru/problem.aspx?space=1&num=1160) · dificultad 140 · dsu

Problema original de Andrew Stankevich, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`2 ≤ N ≤ 1000` concentradores pueden unirse con `1 ≤ M ≤ 15000` cables
posibles de longitudes dadas. Elige cables que conecten cada
concentrador con todos los demás, directamente o a través de otros, de
modo que el cable más largo elegido sea lo más corto posible. Imprime
esa longitud, luego el número de cables y los cables.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`, y luego `M` líneas con dos concentradores, numerados de 1 a
`N`, y una longitud, un entero de 1 a 10⁶.

## Salida

El cable más largo, el número de cables `P` y luego `P` pares de
concentradores.

## Evaluación

Se acepta cualquier plan que conecte todos los concentradores con cables
posibles y cuyo cable más largo sea el menor posible. El comprobador halla
por su cuenta esa longitud mínima, con búsqueda binaria sobre las
longitudes y una prueba de conectividad, y verifica la longitud y el plan
impresos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 6
1 2 1
1 3 1
1 4 2
2 3 1
3 4 1
2 4 1
```

Salida:

```
1
3
1 2
1 3
3 4
```

## Solución

El algoritmo de Kruskal construye un árbol generador desde los cables más
cortos, saltando un cable cuyos extremos ya están conectados, lo que dice
una unión de conjuntos disjuntos. El árbol que construye es un árbol
generador mínimo, y un árbol generador mínimo también minimiza su arista
más larga: cuando Kruskal añade su última arista, la más larga `e`, los
cables más cortos que `e` dejan los concentradores en al menos dos grupos
separados, así que todo plan conectado necesita un cable al menos tan
largo como `e`. La respuesta es la longitud de la última arista tomada, y
los `N − 1` cables del árbol son un plan válido. `O(M log M)` (`O(M log² M)` en Go).

Detalles a tener en cuenta:

- el plan no tiene que ser un árbol, y se acepta cualquier plan con el
  menor cable más largo;
- hay que llegar a todos los concentradores, así que la respuesta la da la
  última arista que toma Kruskal, no la última considerada;
- las longitudes iguales no necesitan nada especial.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
60 redes aleatorias.

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB en lugar de `scanf` y guarda los cables en un arreglo fijo de
registros de 8 bytes: la longitud en un `int` y los dos concentradores
en `uint16_t`, que admite números hasta 1000. Los ordena en el sitio con
`std::sort` en lugar de `std::stable_sort`, que necesita una copia
temporal, detiene el algoritmo de Kruskal tras `N − 1` cables e imprime
con `printf` en lugar de construir la salida en una cadena:
{1160_dsu_optimized.cpp}.

La solución optimizada en Java analiza los números a mano desde un búfer
de 4 KB en lugar de `StreamTokenizer` y empaqueta cada cable en un solo
`long`: dos concentradores de 10 bits cada uno, suficientes para números
hasta 1000, y encima la longitud, hasta 10⁶. Ordenar el arreglo simple
de `long` ordena los cables por longitud sin un arreglo por cable ni
comparador, y el algoritmo de Kruskal se detiene tras `N − 1` cables:
{1160_dsu_optimized.java}.

La solución optimizada en Python lee la entrada en trozos de 8 KB y
convierte los tokens trozo a trozo en lugar de partir toda la entrada de
una vez. Empaqueta cada cable en un solo entero, la longitud encima de
dos números de concentrador de 10 bits (los números no pasan de 1000),
así que un `sort` simple ordena los cables por longitud sin tuplas ni
función clave, y el algoritmo de Kruskal se detiene tras `N − 1` cables:
{1160_dsu_optimized.py}.

La solución optimizada en Rust analiza los números a mano desde un búfer
de 4 KB en lugar de leer toda la entrada en un `String`. Cada cable es
una tupla de 8 bytes con una longitud `u32` y dos concentradores `u16`
en lugar de tres valores `usize`, la ordenación es `sort_unstable`, que
no necesita búfer adicional, el algoritmo de Kruskal se detiene tras
`N − 1` cables y la salida pasa por un `BufWriter`:
{1160_dsu_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1160_dsu_optimized.cpp`: reducción de tiempo +51.61%; reducción de
  memoria +52.29%; base: `1160_dsu.cpp`.

- `1160_dsu_optimized.java`: reducción de tiempo +54.39%; reducción de
  memoria +78.51%; base: `1160_dsu.java`.

- `1160_dsu_optimized.py`: reducción de tiempo -19.23%; reducción de
  memoria +72.78%; base: `1160_dsu.py`.

- `1160_dsu_optimized.rs`: reducción de tiempo -106.67%; reducción de
  memoria +69.20%; base: `1160_dsu.rs`.

## Notas por lenguaje

- Todos los lenguajes ordenan los cables y aplican la misma unión con
  reducción a la mitad de caminos.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1160_dsu.cpp](1160_dsu.cpp) | G++ 13.2 x64 | dsu | O(M log M) | AC | 0.031 s | 436 KB | 11281720 |
| [1160_dsu.go](1160_dsu.go) | Go 1.14 x64 | dsu | O(M log² M) | AC | 0.062 s | 1808 KB | 11304467 |
| [1160_dsu.java](1160_dsu.java) | Java 1.8 | dsu | O(M log M) | AC | 0.171 s | 3500 KB | 11281766 |
| [1160_dsu.py](1160_dsu.py) | Python 3.12 x64 | dsu | O(M log M) | AC | 0.078 s | 5864 KB | 11281753 |
| [1160_dsu.rs](1160_dsu.rs) | Rust 1.75 x64 | dsu | O(M log M) | AC | 0.015 s | 1104 KB | 11281779 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1160_dsu_optimized.cpp](1160_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O(M log M) | AC | 0.015 s | 208 KB | 11304463 |
| [1160_dsu_optimized.java](1160_dsu_optimized.java) | Java 1.8 | dsu | O(M log M) | AC | 0.078 s | 752 KB | 11304464 |
| [1160_dsu_optimized.py](1160_dsu_optimized.py) \* | Python 3.12 x64 | dsu | O(M log M) | AC | 0.093 s | 1596 KB | 11304465 |
| [1160_dsu_optimized.rs](1160_dsu_optimized.rs) \* | Rust 1.75 x64 | dsu | O(M log M) | AC | 0.031 s | 340 KB | 11304466 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
