# 1507. Decisión difícil

[Timus 1507](https://acm.timus.ru/problem.aspx?space=1&num=1507) · dificultad 447 · math

Problema original de Evgeny Krokhalev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una matriz A de n × n (2 ≤ n ≤ 50) de enteros de 0 a 100, hay que
decidir si la matriz
B = A^(n(n−1)) + A^(n(n−1)+1) + … + A^(n(n+1)) tiene algún elemento
nulo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y luego las n filas de A.

## Salida

«No» si B tiene un elemento nulo; si no, «Yes».

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 7
15 30
```

Salida:

```
Yes
```

### Ejemplo 2

Entrada:

```
3
100 35 40
0 22 0
10 11 0
```

Salida:

```
No
```

## Solución

Los elementos son enormes, pero solo importa si son nulos, y con
elementos no negativos una suma solo es nula si lo son todos sus
términos, y un producto solo si lo es algún factor. Así que A se ve como un grafo dirigido con una arista
i → j donde el elemento no es nulo: (A^k)[i][j] no es nulo justo cuando
algún camino de longitud k lleva de i a j, y B no tiene ceros justo
cuando cada j se alcanza desde cada i por un camino de longitud entre
n(n−1) y n(n+1).

Cada fila de una matriz booleana se guarda como máscara de bits, y un
producto combina con OR las filas del segundo factor elegidas por los
bits del primero. Se calcula A^(n(n−1)) por cuadrados sucesivos y luego
las 2n + 1 potencias consecutivas, una multiplicación cada vez,
uniéndolas con OR. Unos 125 productos de `O(n²)` operaciones sobre
palabras.

De hecho la respuesta es «Yes» justo cuando el grafo es fuertemente
conexo: una comprobación de todos los grafos con n ≤ 4 y de grafos
aleatorios hasta n = 12 no encontró excepciones. La ventana de 2n + 1
longitudes consecutivas cubre todos los restos de una estructura
cíclica, así que incluso un solo ciclo, cuyas potencias nunca son
positivas, la cumple.

Detalles a tener en cuenta:

- la fórmula solo aparece como imagen en el enunciado: las potencias
  van de n(n−1) a n(n+1);
- los valores reales desbordan los enteros de 64 bits, así que solo se
  calcula si son nulos o no (prueba 06);
- un solo ciclo no tiene ninguna potencia positiva, pero B no tiene
  ceros (pruebas 03, 07);
- un enlace en un solo sentido entre dos partes, o un vértice sin
  aristas de salida o de entrada, dan ceros (pruebas 04, 08, gen3).

## Soluciones optimizadas

La versión con grafos comprueba la conectividad fuerte recorriendo desde el vértice 0 el grafo y su transpuesto. Esto basta para la fórmula matricial: para cualesquiera u y v, tomamos un camino simple de longitud p ≤ n−1 y un ciclo dirigido por u de longitud c ≤ n. Sea L = n(n−1). Repetir el ciclo antes del camino da longitud p + k·c. Elegimos el menor k no negativo que alcance L; la longitud es menor que L + c y pertenece a [n(n−1), n(n+1)]. A la inversa, una entrada positiva para cada par implica alcanzabilidad y conectividad fuerte. Leer la matriz cuesta O(n²). Como n ≤ 50, cada fila cabe en una máscara de bits y el grafo ocupa O(n) palabras de máquina.

## Notas por lenguaje

Se conservan las bases con potencias matriciales en los cinco lenguajes. Las versiones con grafos guardan cada fila en una máscara. Python lee todos los tokens, por lo que su búfer de entrada ocupa O(n²), aunque el grafo ocupa O(n). Go usa manejadores estándar; Rust usa E/S del C runtime con búferes acotados y una entrada C para reducir el arranque. Los fuentes exactos de Go y Rust también se compilaron para Windows antes de enviarlos.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1507_math.cpp](1507_math.cpp) | G++ 13.2 x64 | math | O(n^3) | AC | 0.015 s | 188 KB | 11287289 |
| [1507_math.go](1507_math.go) | Go 1.14 x64 | math | O(n^3) | AC | 0.031 s | 1184 KB | 11287290 |
| [1507_math.java](1507_math.java) | Java 1.8 | math | O(n^3) | AC | 0.171 s | 524 KB | 11287292 |
| [1507_math.py](1507_math.py) | Python 3.12 x64 | math | O(n^3) | AC | 0.140 s | 740 KB | 11287291 |
| [1507_math.rs](1507_math.rs) | Rust 1.75 x64 | math | O(n^3) | AC | 0.046 s | 256 KB | 11287293 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1507_graphs.cpp](1507_graphs.cpp) | G++ 13.2 x64 | graphs | O(n²) | AC | 0.015 s | 108 KB | 11314642 |
| [1507_graphs.go](1507_graphs.go) \* | Go 1.14 x64 | graphs | O(n²) | AC | 0.015 s | 288 KB | 11314641 |
| [1507_graphs.java](1507_graphs.java) | Java 1.8 | graphs | O(n²) | AC | 0.093 s | 392 KB | 11314637 |
| [1507_graphs.py](1507_graphs.py) \* | Python 3.12 x64 | graphs | O(n²) | AC | 0.093 s | 584 KB | 11314647 |
| [1507_graphs.rs](1507_graphs.rs) \* | Rust 1.75 x64 | graphs | O(n²) | AC | 0.046 s | 48 KB | 11314650 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
