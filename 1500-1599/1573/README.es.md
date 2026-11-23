# 1573. Alquimia

[Timus 1573](https://acm.timus.ru/problem.aspx?space=1&num=1573) · dificultad 108 · math

Problema original de Alexander Ipatov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sandro tiene tres bolsas de reactivos distintos: B azules, R rojos y Y
amarillos (de 1 a 100 cada una). Una poción necesita un reactivo de cada
color de su receta, todos de colores distintos. Hay que contar los
conjuntos de reactivos con los que se hace la poción.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

B, R e Y, y luego un K positivo y los K colores distintos de la receta
(Blue, Red o Yellow).

## Salida

El número de maneras.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3 5
3
Red
Yellow
Blue
```

Salida:

```
30
```

## Solución

Cada color de la receta toma un reactivo de su propia bolsa, y las
elecciones son independientes, así que la respuesta es el producto de
los tamaños de las bolsas que nombra la receta. Es como mucho
100³ = 10⁶. `O(K)`.

Detalles a tener en cuenta:

- la entrada da las bolsas en el orden azul, rojo, amarillo, mientras
  que la receta del ejemplo empieza por el rojo;
- solo cuentan los colores de la receta (pruebas 02, 03).

## Soluciones optimizadas

`1573_math_optimized.java`. Conserva el producto de elecciones independientes de las bolsas de colores distintos requeridos. Iniciales B/R/Y identifican Blue/Red/Yellow; omite el resto sin crear cadenas de receta. Entrada de 1024 bytes y salida numérica directa reducen costes. Como máximo tres factores de hasta 100 caben en int: O(K) trabajo para K colores y espacio auxiliar fijo. Conserva la demostración combinatoria y fuente simple.

Accepted exacto Java 1.8 #11327456: 0.093 s / 344 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 12/82, memoria 2/82. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11304267 era 0.109 s / 328 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1573_math_optimized.java`: 0.093 s / 344 KB; base didáctica conservada `1573_math.java`: 0.125 s / 1628 KB.

La solución optimizada en C++ lee con `scanf` en lugar de `iostream` y
elige la bolsa por la primera letra del color, ya que Blue, Red y Yellow
empiezan por letras distintas, en lugar de buscar el nombre en un
`std::map` de cadenas. Cada color se lee en un búfer de 7 bytes,
suficiente para el nombre más largo, Yellow, y el producto se guarda en
`int`, que basta porque no pasa de 10⁶: {1573_math_optimized.cpp}.

La solución optimizada en Rust guarda los tamaños de las tres bolsas en
tres variables y elige uno con un `match` sobre el nombre del color en
lugar de construir un `HashMap`: {1573_math_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1573_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +69.23%; base: `1573_math.cpp`.

- `1573_math_optimized.rs`: reducción de tiempo -206.67%; reducción de
  memoria +45.10%; base: `1573_math.rs`.

`1573_math_optimized.py`. Conserva el producto de cantidades disponibles de los colores distintos de la receta. Asocia directamente los nombres ASCII en bytes Blue, Red, Yellow con cantidades enteras, sin entrada decodificada ni claves de texto. Hace O(K) multiplicaciones y guarda O(K) tokens, con K<=3 y producto hasta 10^6. Cambia representación y sobrecarga, no la regla combinatoria. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1573_math.py`: tiempo 0.078 s → 0.109 s; memoria 452 KB → 232 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1573_math_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328571 (Go 1.14 x64): **0.015 s / 948 KB**. Comparación archivada: `1573_math.go` (Go 1.14 x64) — 0.015 s / 1084 KB (#11287815).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1573_math_optimized.py`: puesto de tiempo 34/51 y de memoria 1/51 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math.cpp](1573_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 416 KB | 11287812 |
| [1573_math.go](1573_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 1084 KB | 11287815 |
| [1573_math.java](1573_math.java) | Java 1.8 | math | O(K) | AC | 0.125 s | 1628 KB | 11287819 |
| [1573_math.py](1573_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.078 s | 452 KB | 11287817 |
| [1573_math.rs](1573_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.015 s | 408 KB | 11287824 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math_optimized.cpp](1573_math_optimized.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 128 KB | 11304264 |
| [1573_math_optimized.java](1573_math_optimized.java) | Java 1.8 | math | O(K) time; O(1) auxiliary space | AC | 0.093 s | 344 KB | 11327456 |
| [1573_math_optimized.rs](1573_math_optimized.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 224 KB | 11304268 |
| [1573_math_optimized.py](1573_math_optimized.py) \* | PyPy 3.10 x64 | math | O(K) | AC | 0.109 s | 232 KB | 11324919 |
| [1573_math_optimized.go](1573_math_optimized.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 948 KB | 11328571 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
