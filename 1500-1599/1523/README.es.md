# 1523. K-inversiones

[Timus 1523](https://acm.timus.ru/problem.aspx?space=1&num=1523) · dificultad 296 · fenwick

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una permutación a1, …, an de 1 … n (1 ≤ n ≤ 20000), hay que contar
sus k-inversiones (2 ≤ k ≤ 10): sucesiones de índices
i1 < i2 < … < ik con ai1 > ai2 > … > aik. Se escribe la cuenta módulo
10⁹.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y k, y luego la permutación.

## Salida

El número de k-inversiones módulo 10⁹.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
3 1 2
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
5 3
5 4 3 2 1
```

Salida:

```
10
```

## Solución

Sea ends[i] el número de cadenas decrecientes de longitud L que acaban
en la posición i; para L = 1 vale 1 en todas partes. Una cadena de
longitud L + 1 que acaba en i es una cadena de longitud L que acaba en
una posición anterior p con ap > ai, seguida de i. Así, cada nivel es
una pasada de izquierda a derecha con un árbol de Fenwick sobre los
valores: se consulta la suma de los valores mayores que ai y luego se
suma ends[i] en ai. Contando los valores desde arriba, «mayor» se
convierte en un prefijo. k − 1 pasadas dan `O(n·k·log n)`.

Detalles a tener en cuenta:

- k puede superar la longitud de la cadena decreciente más larga, o
  incluso n, y entonces la respuesta es 0 (pruebas 04, 05, gen3);
- las cuentas crecen como C(20000, 10), así que hay que reducirlas
  módulo 10⁹ al sumarlas (gen2, gen5).

## Soluciones optimizadas

La DP por capas de inversiones usa un arreglo in situ. En cada posición se guarda el valor de la capa anterior, se consulta un Fenwick que solo contiene posiciones anteriores de esa capa, se sobrescribe la celda y se inserta el valor viejo guardado. Insertar el nuevo mezclaría capas y sería incorrecto. El árbol se limpia y reutiliza. Las cotas permiten celdas compactas y una resta condicional sustituye al módulo al sumar dos residuos.

- `1523_fenwick_optimized.cpp`: 0.015 s / 192 KB; base `1523_fenwick.cpp`: 0.031 s / 596 KB; cambio respecto a la base: tiempo -51.6%, memoria -67.8%.
- `1523_fenwick_optimized.java`: 0.140 s / 624 KB; base `1523_fenwick.java`: 0.125 s / 3512 KB; cambio respecto a la base: tiempo +12.0%, memoria -82.2%.
- `1523_fenwick_optimized.py`: 0.859 s / 2000 KB; base `1523_fenwick.py`: 0.562 s / 5172 KB; cambio respecto a la base: tiempo +52.8%, memoria -61.3%.
- `1523_fenwick_optimized.rs`: 0.031 s / 472 KB; base `1523_fenwick.rs`: 0.031 s / 1292 KB; cambio respecto a la base: tiempo -0.0%, memoria -63.5%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1523_fenwick.cpp`; versión que cubre `1523_fenwick_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 95/95.

- Go: base didáctica preferida `1523_fenwick.go`; versión que cubre `1523_fenwick.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1523_fenwick.java`; versión que cubre `1523_fenwick_optimized.java`; puestos tiempo/memoria 4/1, registros de otros autores 5/5.

- Python/PyPy: base didáctica preferida `1523_fenwick.py`; versión que cubre `1523_fenwick_optimized.py`; puestos tiempo/memoria 7/1, registros de otros autores 7/7.

- Rust: base didáctica preferida `1523_fenwick.rs`; versión que cubre `1523_fenwick_optimized.rs`; puestos tiempo/memoria 2/1, registros de otros autores 2/2.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1523_fenwick.cpp](1523_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 596 KB | 11287382 |
| [1523_fenwick.go](1523_fenwick.go) | Go 1.14 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 4576 KB | 11287383 |
| [1523_fenwick.java](1523_fenwick.java) | Java 1.8 | fenwick | O(n * k * log n) | AC | 0.125 s | 3512 KB | 11287388 |
| [1523_fenwick.py](1523_fenwick.py) | Python 3.12 x64 | fenwick | O(n * k * log n) | AC | 0.562 s | 5172 KB | 11287386 |
| [1523_fenwick.rs](1523_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 1292 KB | 11287389 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1523_fenwick_optimized.cpp](1523_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(NK log N) | AC | 0.015 s | 192 KB | 11309407 |
| [1523_fenwick_optimized.java](1523_fenwick_optimized.java) \* | Java 1.8 | fenwick | O(NK log N) | AC | 0.140 s | 624 KB | 11309408 |
| [1523_fenwick_optimized.py](1523_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(NK log N) | AC | 0.859 s | 2000 KB | 11309406 |
| [1523_fenwick_optimized.rs](1523_fenwick_optimized.rs) \* | Rust 1.75 x64 | fenwick | O(NK log N) | AC | 0.031 s | 472 KB | 11309409 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
