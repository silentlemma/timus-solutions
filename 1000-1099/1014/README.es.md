# 1014. El menor número con un producto de dígitos dado

[Timus 1014](https://acm.timus.ru/problem.aspx?space=1&num=1014) · dificultad 94 · greedy

Problema original del Ural State University Internal Contest '99 #2.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado `N` (`0 ≤ N ≤ 10^9`), encuentra el menor entero positivo `Q` cuyos
dígitos decimales multiplicados den exactamente `N`, o indica que no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El entero `N`.

## Salida

`Q`, o `-1` si no existe tal número.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
36
```

Salida:

```
49
```

### Ejemplo 2

Entrada:

```
0
```

Salida:

```
10
```

## Solución

Primero, dos casos especiales:

- `N = 0`: un número tiene producto de dígitos 0 exactamente cuando contiene
  un cero, y el menor de esos números positivos es `10`;
- `N = 1`: la respuesta es `1` (no un número vacío).

En otro caso ningún dígito es 0 o 1 (un 1 solo alarga el número), así que
`Q` está formado por dígitos 2–9. Un número más corto es menor, y entre los
de igual longitud el menor es el que tiene los dígitos en orden creciente.
Así que hay que escribir `N` como producto del menor número de dígitos.

**Voraz:** se divide `N` entre 9 mientras se pueda, luego entre 8, 7, ..., 2,
y se van guardando los dígitos. Si queda algo distinto de 1, `N` tiene un
factor primo mayor que 7 y la respuesta es `-1`. Se imprimen los dígitos
guardados en orden creciente.

Por qué primero los dígitos grandes: las potencias de 3 se empaquetan mejor
en nueves (dos treses en un dígito), las de 2 en ochos, y un 3 y un 2
sobrantes forman un 6 en vez de dos dígitos; dividir entre 9, 8, ..., 2 en
ese orden produce justo ese empaquetado. `O(log N)` pasos de división.

Detalles a tener en cuenta:

- `N = 0` y `N = 1`;
- la respuesta puede tener 12 dígitos (`10^9 = 2^9 · 5^9` da
  `555555555888`): no la guardes en un entero de 32 bits; imprime los
  dígitos como cadena.
- contar solo las divisiones omite el coste de insertar dígitos al principio:
  el [test 05](tests/05.in) ya construye una respuesta de 12 dígitos.

## Soluciones optimizadas

`1014_greedy_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327014 mide 0.078 s / 724 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 6/482, memoria 448/482. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11325471, 0.125 s / 240 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

`1014_greedy_optimized.py`. Conserva la factorización voraz de 9 a 2 y la inversión de dígitos. Cero da 10, uno da 1 y un factor restante da -1. Entrada por bytes y ejecución directa sustituyen input() y la función envolvente. Tiempo y almacenamiento de dígitos siguen O(log(N+2)); no se afirma mejora asintótica. La fila Accepted indica el runtime real y sus medidas emparejadas. Vacía salida antes de os._exit(0), que omite cierre del intérprete; la mejora medida de memoria depende del runtime y no implica aceleración asintótica.

Frente a `1014_greedy.py`: tiempo 0.093 s → 0.125 s; memoria 444 KB → 240 KB.

`1014_greedy_optimized.go`. Mantiene factorización por dígitos descendentes y casos cero=>10, uno=>1. En vez de anteponer cadenas formateadas, añade bytes a32celdas fijas y emite al revés. Cada factor>=2 y N<=10^9 garantizan capacidad. Elimina copias cuadráticas en factores y formato repetido; búferes256/64sustituyen fmt/cadenas. Tiempo O(log(N+2)), espacio auxiliar O(1) en el rango. Admisión por clasificación, sin afirmar mejora medida del30%.

Frente a `1014_greedy.go`: tiempo 0.031 s → 0.031 s; memoria 1096 KB → 780 KB.

La solución optimizada en Java analiza el número byte a byte desde
`System.in` en lugar de usar `Scanner`, y añade las cifras al final e
invierte la cadena una sola vez en lugar de insertar cada cifra al
principio: 380 KB en lugar de 1604 KB, con el mismo tiempo.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1014_greedy_optimized.go`: puesto de tiempo 4/12 y de memoria 1/12 en esta muestra comparable.

Comparación PyPy anterior: `1014_greedy_optimized.py`: puesto de tiempo 442/482 y de memoria 2/482 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1014_greedy.cpp](1014_greedy.cpp) | G++ 13.2 x64 | greedy | O((log N)^2) | AC | 0.015 s | 192 KB | 11278098 |
| [1014_greedy.go](1014_greedy.go) | Go 1.14 x64 | greedy | O((log N)^2) | AC | 0.031 s | 1096 KB | 11278101 |
| [1014_greedy.java](1014_greedy.java) | Java 1.8 | greedy | O((log N)^2) | AC | 0.125 s | 1604 KB | 11278109 |
| [1014_greedy.py](1014_greedy.py) | Python 3.12 x64 | greedy | O(log N) | AC | 0.093 s | 444 KB | 11278104 |
| [1014_greedy.rs](1014_greedy.rs) | Rust 1.75 x64 | greedy | O(log N) | AC | 0.046 s | 232 KB | 11278114 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1014_greedy_optimized.java](1014_greedy_optimized.java) | Java 1.8 | greedy | O(log N) | AC | 0.109 s | 380 KB | 11303700 |
| [1014_greedy_optimized.go](1014_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(log(N+2)) | AC | 0.031 s | 780 KB | 11328371 |
| [1014_greedy_optimized.py](1014_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(log(N+2)) | AC | 0.078 s | 724 KB | 11327014 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
