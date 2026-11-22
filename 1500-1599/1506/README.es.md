# 1506. Columnas de números

[Timus 1506](https://acm.timus.ru/problem.aspx?space=1&num=1506) · dificultad 134 · implementation

Problema original de Stanislav Vasiliev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que imprimir N números de 0 a 999 (1 ≤ N ≤ 100) en K columnas
(1 ≤ K ≤ N) con el menor número de filas. Todas las columnas tienen la
misma altura salvo la última, que puede ser más corta. Los números
llenan la primera columna de arriba abajo, luego la segunda, y así
sucesivamente. Cada número va alineado a la derecha en un campo de
4 caracteres, y ninguna línea tiene espacios finales.
Se garantiza que existe una tabla con exactamente K columnas no vacías.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y K, y luego los N números.

## Salida

La tabla.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación. En particular, conserva la alineación de la tabla y el relleno inicial de cada campo.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 3
1 2 30 40 50 600 700
```

Salida:

```
   1  40 700
   2  50
  30 600
```

## Solución

El menor número de filas es H = ⌈N / K⌉. Toda altura válida h cumple
h ≥ H y (K − 1)·h < N. La garantía de existencia implica entonces
(K − 1)·H < N, así que con altura H la última columna no queda vacía.
La columna c tiene los números
de índices c·H a c·H + H − 1, así que la fila r está formada por los
números c·H + r que existen, para c = 0, 1, …; se acaban en la primera
columna agotada, que solo puede ser la última. Cada uno se imprime en
un campo de 4 y ahí termina la fila. `O(N)`.

Detalles a tener en cuenta:

- los números bajan por las columnas, no van a lo largo de las filas
  (prueba 01);
- cada número ocupa 4 caracteres, también el primero, así que cada
  línea empieza con espacios (prueba 01);
- cuando la última columna es más corta, las filas de abajo terminan un
  número antes, sin espacios finales (prueba 06);
- la garantía de existencia es esencial: la última columna debe tener
  al menos un número (prueba 06); no todo par con 1 ≤ K ≤ N es viable;
- K = N da una sola fila y K = 1 una sola columna (pruebas 03, 04).

## Soluciones optimizadas

`1506_implementation_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327027 mide 0.046 s / 720 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 1/291, memoria 285/291. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11325476, 0.125 s / 248 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

`1506_implementation_optimized.py`. Mantiene height=ceil(n/k) y distribución por columnas. Analiza números una vez y recorre row,row+height,..., emitiendo una fila de campos de ancho cuatro alineados a la derecha. Elimina todas las filas formateadas acumuladas y la lista cortada de textos numéricos. Conserva la lista de enteros: O(n) tiempo y espacio. El relleno inicial y los saltos son significativos. La fila Accepted indica el runtime real y sus medidas emparejadas. Vacía salida antes de os._exit(0), que omite cierre del intérprete; la mejora medida de memoria depende del runtime y no implica aceleración asintótica.

Frente a `1506_implementation.py`: tiempo 0.093 s → 0.125 s; memoria 460 KB → 248 KB.

La solución optimizada en C++ guarda los números en un arreglo fijo de
100 `int` en la pila en lugar de un `std::vector`, ya que N ≤ 100, así
que el programa no reserva nada en el montón:
{1506_implementation_optimized.cpp}.

La solución optimizada en Java rellena cada celda por su cuenta:
convierte el número con `Integer.toString` y pone espacios delante hasta
4 caracteres, en lugar de llamar a `String.format`, que crea un
formateador nuevo y analiza el patrón en cada celda. Un número de hasta
999 tiene como mucho tres cifras, así que cada celda lleva al menos un
espacio delante: {1506_implementation_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1506_implementation_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +48.98%; base: `1506_implementation.cpp`.

- `1506_implementation_optimized.java`: reducción de tiempo +14.68%;
  reducción de memoria +56.56%; base: `1506_implementation.java`.

`1506_implementation_optimized.rs`. Guarda hasta 100 valores en un arreglo u16 fijo, los indexa por columna y fila y emite directamente el relleno necesario. No conserva cadenas por valor, filas concatenadas ni toda la salida. El trabajo es O(N); el almacenamiento queda limitado al arreglo fijo y al estado de impresión numérica. Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `1506_implementation.rs`: tiempo 0.015 s → 0.031 s; memoria 252 KB → 52 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Comparación PyPy anterior: `1506_implementation_optimized.py`: puesto de tiempo 279/291 y de memoria 2/291 en esta muestra comparable.

`1506_implementation_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation.cpp](1506_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11287283 |
| [1506_implementation.go](1506_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB | 11287284 |
| [1506_implementation.java](1506_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 976 KB | 11287286 |
| [1506_implementation.py](1506_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.093 s | 460 KB | 11287285 |
| [1506_implementation.rs](1506_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 252 KB | 11287287 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation_optimized.cpp](1506_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 100 KB | 11304437 |
| [1506_implementation_optimized.java](1506_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 424 KB | 11304438 |
| [1506_implementation_optimized.rs](1506_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 52 KB | 11325099 |
| [1506_implementation_optimized.py](1506_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(n) time; O(n) space | AC | 0.046 s | 720 KB | 11327027 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
