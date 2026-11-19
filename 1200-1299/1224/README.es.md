# 1224. Los giros de un robot que barre un rectángulo en espiral

[Timus 1224](https://acm.timus.ru/problem.aspx?space=1&num=1224) · dificultad 65 · math

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un robot empieza en la casilla superior izquierda de un campo de `N`
filas y `M` columnas, ambas hasta `2³¹ − 1`, mirando a la derecha, y
recorre todas las casillas siguiendo una espiral en sentido horario que
se cierra hacia el centro. Hay que contar sus giros.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`.

## Salida

El número de giros.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5
```

Salida:

```
4
```

## Solución

El camino alterna tramos horizontales y verticales, empezando por uno
horizontal, y gira una vez entre dos tramos. Cada tramo horizontal gasta
una fila y cada tramo vertical una columna, porque la espiral pela el
campo desde fuera.

Si `N ≤ M`, primero se agotan las filas, tras `N` tramos horizontales y
`N − 1` verticales: `2N − 1` tramos y `2(N − 1)` giros. Si no, primero se
agotan las columnas, tras `M` tramos de cada tipo: `2M` tramos y
`2M − 1` giros. `O(1)`.

Detalles a tener en cuenta:

- una sola fila no necesita ningún giro, pero una sola columna con `N > 1` necesita
  uno, porque el robot empieza mirando a la derecha;
- la respuesta llega a unos `4.3·10⁹`, más de 32 bits con signo.

La fórmula se comprobó simulando el robot en todos los campos hasta
14 × 14, y se comparó con una solución escrita aparte en todas las
pruebas.

## Soluciones optimizadas

La solución optimizada en Java lee la entrada en bloques de 1 KB y
analiza los dos números a mano en lugar de usar `Scanner`: 348 KB en
lugar de 1564 KB, con el mismo tiempo.

`1224_math_optimized.py`. Conserva la fórmula de giros: 2*(N-1) si N<=M, y 2*M-1 en otro caso. Incluye una fila o columna sin simulación. La respuesta puede superar 32 bits con signo, así que Rust usa i64 y Python enteros exactos. Aritmética acotada y espacio O(1). Lee las dos dimensiones de tokens de bytes crudos; no introduce otro algoritmo de espiral. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1224_math.py`: tiempo 0.078 s → 0.125 s; memoria 372 KB → 196 KB.

`1224_math_optimized.rs`. Conserva la fórmula de giros: 2*(N-1) si N<=M, y 2*M-1 en otro caso. Incluye una fila o columna sin simulación. La respuesta puede superar 32 bits con signo, así que Rust usa i64 y Python enteros exactos. Aritmética acotada y espacio O(1). Guarda solo las dos dimensiones y la respuesta en vez del String de entrada y el vector. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1224_math.rs`: tiempo 0.031 s → 0.015 s; memoria 208 KB → 56 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1224_math_optimized.py`: puesto de tiempo 283/296 y de memoria 4/296 en esta muestra comparable.

`1224_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1224_math.cpp](1224_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11283705 |
| [1224_math.go](1224_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1076 KB | 11283706 |
| [1224_math.java](1224_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB | 11283708 |
| [1224_math.py](1224_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 372 KB | 11283707 |
| [1224_math.rs](1224_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 208 KB | 11283709 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1224_math_optimized.java](1224_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 348 KB | 11303726 |
| [1224_math_optimized.py](1224_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 196 KB | 11324840 |
| [1224_math_optimized.rs](1224_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 56 KB | 11324853 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
