# 1644. Un montón de nueces

[Timus 1644](https://acm.timus.ru/problem.aspx?space=1&num=1644) · dificultad 100 · implementation

Problema original de Alexey Samsonov, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En cada uno de n experimentos el loro comió entre 3 y 9 nueces y anotó
si seguía con hambre o quedó satisfecho. La saciedad es monótona: más
nueces nunca dejan más hambre. Se sabe que diez nueces siempre bastan y
dos nunca. Hay que hallar el menor número de nueces que seguro basta, o
decir que las anotaciones se contradicen.

## Entrada

n (0 ≤ n ≤ 100) y luego n líneas: un número de nueces y `hungry` o
`satisfied`.

## Salida

El menor número de nueces que seguro basta, o `Inconsistent`.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
4 hungry
7 satisfied
5 hungry
8 satisfied
```

Salida:

```
7
```

### Ejemplo 2

Entrada:

```
2
6 hungry
5 satisfied
```

Salida:

```
Inconsistent
```

## Solución

Se toma la mayor cantidad con hambre, empezando en 2, y la menor
cantidad satisfecha, empezando en 10. Las anotaciones encajan con un
umbral monótono exactamente cuando la segunda es mayor; entonces la
respuesta es la menor cantidad satisfecha, pues nada menor se ha visto
saciar. Si no, `Inconsistent`. `O(n)`.

Detalles a tener en cuenta:

- sin anotaciones la respuesta es 10 (prueba 03), y con solo anotaciones
  de hambre sigue siendo 10 (prueba 04);
- la misma cantidad anotada de las dos maneras es una contradicción
  (prueba 06).

Las respuestas coinciden con una implementación aceptada independiente
en 180 conjuntos aleatorios de anotaciones.

## Soluciones optimizadas

`1644_implementation_optimized.py`. Mantiene máximo hungry y mínimo full, inicialmente 2 y 10. Recorre exactamente n parejas número/veredicto en bytes sin dos cortes alternos de listas. Emite full solo si supera estrictamente hungry. El algoritmo tiene dos extremos, pero retiene entrada dividida: O(n) tiempo, O(I) espacio total para tamaño de entrada I. La fila Accepted indica el runtime real y sus medidas emparejadas. Vacía salida antes de os._exit(0), que omite cierre del intérprete; la mejora medida de memoria depende del runtime y no implica aceleración asintótica.

Frente a `1644_implementation.py`: tiempo 0.109 s → 0.156 s; memoria 444 KB → 212 KB.

La solución optimizada en Java analiza los números a mano desde un
búfer pequeño en lugar de usar `Scanner` y distingue las dos palabras
por su primera letra, `h` o `s`, saltándose el resto: 400 KB en lugar de
1708 KB, con el mismo tiempo.

La solución optimizada en C++ lee con `scanf` en un pequeño arreglo de
`char` en lugar de `iostream` y `std::string`, y distingue las dos
palabras por la primera letra: 128 KB en lugar de 388 KB, con el mismo
tiempo.

`1644_implementation_optimized.rs`. Actualiza solo la mayor observación de hambre y la menor de saciedad. Las dos respuestas del enunciado difieren en su primer byte; usa ese byte y omite el resto del token sin asignar una cadena. El intervalo es coherente exactamente cuando el límite superior supera al inferior. O(N) tiempo y O(1) estado auxiliar. Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `1644_implementation.rs`: tiempo 0.015 s → 0.031 s; memoria 220 KB → 64 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1644_implementation_optimized.py`: puesto de tiempo 53/53 y de memoria 1/53 en esta muestra comparable.

`1644_implementation_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1644_implementation.cpp](1644_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 388 KB | 11303499 |
| [1644_implementation.go](1644_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1084 KB | 11288487 |
| [1644_implementation.java](1644_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1708 KB | 11288489 |
| [1644_implementation.py](1644_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 444 KB | 11288488 |
| [1644_implementation.rs](1644_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 220 KB | 11288490 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1644_implementation_optimized.cpp](1644_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303768 |
| [1644_implementation_optimized.java](1644_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 400 KB | 11303630 |
| [1644_implementation_optimized.rs](1644_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 64 KB | 11324867 |
| [1644_implementation_optimized.py](1644_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) time; O(I) space | AC | 0.156 s | 212 KB | 11325477 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
