# 1452. Pascal contra C++

[Timus 1452](https://acm.timus.ru/problem.aspx?space=1&num=1452) · dificultad 607 · hashing

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una sucesión tiene N elementos (2 ≤ N ≤ 2000), enteros de 0 a 10⁹. Hay
que elegir tantos elementos como se pueda, con valores distintos, que
formen términos consecutivos de una progresión aritmética creciente; su
orden en la sucesión no importa. Se imprime la cantidad y los números de
los elementos elegidos en cualquier orden.

Límite de tiempo: 0.25 segundos. Límite de memoria: 16 MB.

## Entrada

N y luego los N elementos.

## Salida

La cantidad y luego los números de los elementos. Se acepta cualquier
progresión más larga.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
7 3 2 3 5 9
```

Salida:

```
4
4 5 1 6
```

## Solución

Solo importa el conjunto de valores, así que cada valor se guarda una
vez en una tabla hash junto con el número de un elemento que lo tiene, y
los valores distintos se ordenan. Toda progresión de al menos dos
términos queda fijada por sus dos primeros términos x < y, con paso
d = y − x. Se recorre solo desde su verdadero comienzo, es decir,
cuando x − d no está: luego se sigue por y + d, y + 2d, ... mientras
estén en la tabla.

Cada par de términos vecinos de una progresión maximal cae en un solo
recorrido, y cada par (x, y) cuesta una consulta para comprobar el
comienzo, así que la búsqueda completa hace O(m²) consultas para m
valores distintos, sin tabla de pares: la memoria se queda en O(N),
dentro del límite de 16 MB. Con un solo valor distinto la
respuesta es un elemento. `O(N + m²)` en tiempo esperado.

Detalles a tener en cuenta:

- los valores repetidos cuentan una vez (pruebas 02, 04, 07, gen4);
- una progresión que pasa por todos los valores exige un recorrido
  de longitud completa (gen3);
- una tabla de todos los pares, como en la programación dinámica
  habitual en O(N²), necesita más memoria de la permitida con algunas
  representaciones.

## Notas por lenguaje

- Python corre en CPython y poda los pares. Primero descarta algunos valores
  extremos que no pertenecen a ninguna progresión de tres términos, y un par
  x < y solo se recorre cuando una progresión desde x con paso y − x aún
  podría superar a la mejor hallada: su término en esa longitud debe ser
  como mucho el mayor valor y estar en la tabla. La versión anterior,
  que recorría todos los pares, excedía el límite de 0,25 s en la prueba
  9 del juez con CPython y en la prueba 28 con PyPy.

## Soluciones optimizadas

La versión optimizada en C++ guarda cada valor distinto y su primera posición en una tabla fija de direccionamiento abierto. Comprueba una diferencia solo si puede existir el término necesario para superar el mejor resultado y si la progresión carece de un término anterior en la entrada. Reconstruye la respuesta a partir del primer término y la diferencia. Las métricas corresponden al envío 11317031.

Rust guarda los valores y sus índices originales en arreglos separados, con enteros de 16 bits para los índices. El envío 11318214 tardó 0,031 s y usó 292 KB. La versión sencilla tardó 0,093 s y usó 620 KB.

Java usa una tabla hash de tamaño fijo con direccionamiento abierto y descarta las diferencias que no pueden alargar la mejor progresión. El envío 11318310 tardó 0,187 s y usó 492 KB frente a 0,187 s y 924 KB de la versión sencilla.

Go usa una tabla hash de tamaño fijo con direccionamiento abierto y descarta las diferencias que no pueden alargar la mejor progresión. El envío 11321984 tardó 0,062 s y usó 864 KB frente a 0,125 s y 1376 KB de la versión sencilla.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322326 · Go 1.14 x64 №11322327 · Java 1.8 №11322328 · Python 3.12 x64 №11322330 · Rust 1.75 x64 №11322331.

La versión optimizada en Python usa conjuntos de bits enteros cuando los valores ocupan un intervalo denso. Con valores dispersos comprueba en una tabla hash que existe el término final necesario antes de extender la progresión. El envío 11322818 tardó 0.109 s y usó 1884 KB, frente a 0.140 s y 1608 KB de la versión sencilla. Ocupa el primer puesto en ambas métricas en la clasificación pública de Python/PyPy.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1452_hashing.cpp](1452_hashing.cpp) | G++ 13.2 x64 | hashing | O(N + m^2) | AC | 0.093 s | 248 KB | 11322326 |
| [1452_hashing.go](1452_hashing.go) | Go 1.14 x64 | hashing | O(N + m^2) | AC | 0.125 s | 1376 KB | 11322327 |
| [1452_hashing.java](1452_hashing.java) | Java 1.8 | hashing | O(N + m^2) | AC | 0.187 s | 924 KB | 11322328 |
| [1452_hashing.py](1452_hashing.py) | Python 3.12 x64 | hashing | O(N + m^2) | AC | 0.14 s | 1608 KB | 11322330 |
| [1452_hashing.rs](1452_hashing.rs) | Rust 1.75 x64 | hashing | O(N + m^2) | AC | 0.093 s | 620 KB | 11322331 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1452_hashing_optimized.cpp](1452_hashing_optimized.cpp) \* | G++ 13.2 x64 | hashing | O(N + m^2) | AC | 0.046 s | 156 KB | 11317031 |
| [1452_hashing_optimized.rs](1452_hashing_optimized.rs) \* | Rust 1.75 x64 | hashing | O(N + m^2) | AC | 0.031 s | 292 KB | 11318214 |
| [1452_hashing_optimized.go](1452_hashing_optimized.go) \* | Go 1.14 x64 | hashing | O(N + m^2) | AC | 0.062 s | 864 KB | 11321984 |
| [1452_hashing_optimized.java](1452_hashing_optimized.java) \* | Java 1.8 | hashing | O(N + m^2) | AC | 0.187 s | 492 KB | 11318310 |
| [1452_bitmask_hashing.py](1452_bitmask_hashing.py) | Python 3.12 x64 | bitmask, hashing | O(N + m^2) | AC | 0.109 s | 1884 KB | 11322818 |

\* Aceptada. Aún queda por alcanzar el objetivo de clasificación de C++. El objetivo de clasificación de Rust sigue pendiente. El objetivo de clasificación de Go sigue pendiente. El objetivo de clasificación de Java sigue pendiente.
