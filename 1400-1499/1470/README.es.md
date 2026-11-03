# 1470. OVNI

[Timus 1470](https://acm.timus.ru/problem.aspx?space=1&num=1470) · dificultad 253 · fenwick

Problema original de Dmitry Zhukov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cubo de N × N × N sectores unitarios (1 ≤ N ≤ 128, coordenadas de 0
a N − 1) empieza vacío. Los registros llegan uno por línea. «1 x y z K»
cambia en K (−20000 ≤ K ≤ 20000) el número de objetos del sector
(x, y, z); ningún sector baja nunca de cero. «2 x1 y1 z1 x2 y2 z2»
pregunta cuántos objetos hay en la caja x1 ≤ x ≤ x2, y1 ≤ y ≤ y2,
z1 ≤ z ≤ z2. «3» termina la entrada. Hay como mucho 100002 registros.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego los registros, el último de ellos «3».

## Salida

La respuesta a cada pregunta en su propia línea.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2 1 1 1 1 1 1
1 0 0 0 1
1 0 1 0 3
2 0 0 0 0 0 0
2 0 0 0 0 1 0
1 0 1 0 -2
2 0 0 0 1 1 1
3
```

Salida:

```
0
1
4
2
```

## Solución

Un árbol de Fenwick funciona en cualquier número de dimensiones: la
celda (i, j, w) guarda la suma de un bloque de sectores cuyos índices
terminan en i, j y w y cuyas longitudes son sus bits más bajos. Un
cambio recorre i hacia arriba y, dentro, j y w hacia arriba; una suma
de prefijo sobre [1, x] × [1, y] × [1, z] recorre los tres hacia abajo.
Cada recorrido da como mucho 8 pasos por eje, así que un cambio o suma
de prefijo visita como mucho 8³ celdas. La suma sobre una caja sale de la
inclusión-exclusión en sus ocho esquinas, con las esquinas inferiores
desplazadas en uno. El árbol ocupa (N + 1)³ celdas de 64 bits, unos
17 MB. `O(log³ N)` por registro.

Detalles a tener en cuenta:

- las coordenadas empiezan en 0 y un árbol de Fenwick en 1, así que
  cada índice sube en uno (pruebas 03, 04);
- los objetos de todos los sectores juntos llegan a 2·10⁹ y las sumas
  parciales de la fórmula de las ocho esquinas salen del rango de 32
  bits, así que las sumas son de 64 bits (gen4);
- puede haber preguntas antes de cualquier cambio y un cambio puede
  valer 0 (pruebas 01, 02).

## Soluciones optimizadas

Se mantiene Fenwick tridimensional con sumas de nodos en 32 bits. Al ser no negativos los sectores, cada nodo queda acotado por la masa legal total, inferior al máximo de 32 bits con signo. Las sumas de prefijos y los términos intermedios de inclusión–exclusión usan aritmética suficientemente ancha. Disminuye la memoria sin cambiar rangos ni signos. Python también procesa cada operación sin retener todos los tokens y respuestas.

- `1470_fenwick_optimized.cpp`: 0.359 s / 8144 KB; base `1470_fenwick.cpp`: 0.375 s / 16552 KB; cambio respecto a la base: tiempo -4.3%, memoria -50.8%.
- `1470_fenwick_optimized.go`: 0.140 s / 10320 KB; base `1470_fenwick.go`: 0.156 s / 20044 KB; cambio respecto a la base: tiempo -10.3%, memoria -48.5%.
- `1470_fenwick_optimized.java`: 0.187 s / 12064 KB; base `1470_fenwick.java`: 0.281 s / 20908 KB; cambio respecto a la base: tiempo -33.5%, memoria -42.3%.
- `1470_fenwick_optimized.py`: 0.734 s / 16836 KB; base `1470_fenwick.py`: 0.890 s / 61120 KB; cambio respecto a la base: tiempo -17.5%, memoria -72.5%.
- `1470_fenwick_optimized.rs`: 0.046 s / 11476 KB; base `1470_fenwick.rs`: 0.125 s / 19804 KB; cambio respecto a la base: tiempo -63.2%, memoria -42.1%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1470_fenwick.cpp`; versión que cubre `1470_fenwick_optimized.cpp`; puestos tiempo/memoria 60/1, registros de otros autores 89/89.

- Go: base didáctica preferida `1470_fenwick.go`; versión que cubre `1470_fenwick.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1470_fenwick.java`; versión que cubre `1470_fenwick_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1470_fenwick.py`; versión que cubre `1470_fenwick_optimized.py`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Rust: base didáctica preferida `1470_fenwick.rs`; versión que cubre `1470_fenwick_optimized.rs`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1470_fenwick.cpp](1470_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(log^3 N) per record | AC | 0.375 s | 16552 KB | 11286549 |
| [1470_fenwick.go](1470_fenwick.go) | Go 1.14 x64 | fenwick | O(log^3 N) per record | AC | 0.156 s | 20044 KB | 11286550 |
| [1470_fenwick.java](1470_fenwick.java) | Java 1.8 | fenwick | O(log^3 N) per record | AC | 0.281 s | 20908 KB | 11286552 |
| [1470_fenwick.py](1470_fenwick.py) | PyPy 3.10 x64 | fenwick | O(log^3 N) per record | AC | 0.890 s | 61120 KB | 11286551 |
| [1470_fenwick.rs](1470_fenwick.rs) | Rust 1.75 x64 | fenwick | O(log^3 N) per record | AC | 0.125 s | 19804 KB | 11286553 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1470_fenwick_optimized.cpp](1470_fenwick_optimized.cpp) \* | G++ 13.2 x64 | fenwick | O(log^3 N) per operation | AC | 0.359 s | 8144 KB | 11308809 |
| [1470_fenwick_optimized.go](1470_fenwick_optimized.go) | Go 1.14 x64 | fenwick | O(log^3 N) per operation | AC | 0.140 s | 10320 KB | 11308810 |
| [1470_fenwick_optimized.java](1470_fenwick_optimized.java) | Java 1.8 | fenwick | O(log^3 N) per operation | AC | 0.187 s | 12064 KB | 11308811 |
| [1470_fenwick_optimized.py](1470_fenwick_optimized.py) | PyPy 3.10 x64 | fenwick | O(log^3 N) per operation | AC | 0.734 s | 16836 KB | 11308813 |
| [1470_fenwick_optimized.rs](1470_fenwick_optimized.rs) | Rust 1.75 x64 | fenwick | O(log^3 N) per operation | AC | 0.046 s | 11476 KB | 11308812 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
