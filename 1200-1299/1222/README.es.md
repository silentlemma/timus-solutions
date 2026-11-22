# 1222. El mayor producto de números con una suma dada

[Timus 1222](https://acm.timus.ru/problem.aspx?space=1&num=1222) · dificultad 144 · math

Problema original del folclore, propuesto por Leonid Volkov, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grupo de águilas con `1 ≤ N ≤ 3000` cabezas en total tiene un CI
igual al producto de las cabezas de sus águilas. Hay que hallar el mayor
CI posible; es decir, el mayor producto de enteros positivos que suman
`N`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

El mayor producto.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
```

Salida:

```
6
```

## Solución

Una parte de 4 o más se puede partir en 2 y el resto sin bajar el
producto, y una de 5 o más lo sube así (`2(k − 2) > k` para `k > 4`),
mientras que una parte de 1 solo desperdicia una cabeza. Así que un
reparto óptimo usa solo doses, treses y cuatros, y un 4 es lo mismo que
2 + 2. Tres doses son peores que dos treses (`8 < 9`), así que hay como
mucho dos doses. Queda: todo treses cuando 3 divide a `N`, un 2 más cuando
el resto es 2, y dos doses (o un 4) en lugar de un 3 cuando el resto es 1.
Para `N` hasta 3 lo mejor es el águila sola. El producto tiene hasta 478
cifras. `O(N²)` operaciones con cifras para la multiplicación repetida por
3.

Detalles a tener en cuenta:

- `N = 1` da 1, y `N = 4` da 4;
- un resto de 1 no debe quedarse como factor 1;
- la respuesta va mucho más allá de 64 bits.

Las respuestas se comprobaron con una fuerza bruta sobre todos los
repartos para cada `N` hasta 59, y se compararon con una solución escrita
aparte en todas las pruebas.

## Soluciones optimizadas

`1222_math_optimized.java`. Conserva la partición óptima en treses, sustituyendo resto uno por factor cuatro, con N<4 separado. Calcula el mismo producto en bloques base10^9 con multiplicadores generados hasta 3^18, sin BigInteger ni respuestas precalculadas. Cada intermedio long es menor que 10^9*3^18<2^63; al imprimir rellena bloques inferiores a nueve dígitos. Cota conservadora O(N²) trabajo aritmético y O(N) espacio; conserva la versión matemática simple.

Accepted exacto Java 1.8 #11327402: 0.093 s / 348 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 12/136, memoria 2/136. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11304486 era 0.125 s / 484 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1222_math_optimized.java`: 0.093 s / 348 KB; base didáctica conservada `1222_math.java`: 0.093 s / 1708 KB.

`1222_math_optimized.rs`. Conserva descomposición óptima en treses y un cuatro si sobra uno. Empaqueta nueve cifras decimales por u32 en vez de una y emite grupos rellenados sin construir String decimal. Multiplicar por tres cabe en u32: 3*(10^9-1)+2<2^32. Las multiplicaciones pequeñas siguen O(n²) trabajo de limbs y O(n) cifras almacenadas; mejora representación, no asintótica. Conserva versión sencilla de un dígito por limb.

Frente a `1222_math.rs`: tiempo 0.031 s → 0.015 s; memoria 208 KB → 64 KB.

La solución optimizada en C++ multiplica un arreglo global fijo de 1000
dígitos decimales en lugar de un `std::vector` que crece con el
producto, así que el programa no necesita memoria dinámica; con
`N ≤ 3000` el producto tiene como mucho 478 dígitos:
{1222_math_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1222_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +45.83%; base: `1222_math.cpp`.

`1222_math_optimized.py`. Mantiene la partición de producto máximo en treses, resuelve N<4 directamente y cambia un resto uno por un cuatro. El resultado exacto no cambia; pow y ** son potencias enteras equivalentes. Para un resultado de O(N) bits, la cota conservadora de aritmética escolar y salida decimal es O(N²) de tiempo y O(N) bits. La ganancia medida procede de la implementación del programa independiente. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1222_math.py`: tiempo 0.078 s → 0.109 s; memoria 396 KB → 248 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1222_math_optimized.py`: puesto de tiempo 19/61 y de memoria 3/61 en esta muestra comparable.

`1222_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math.cpp](1222_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 192 KB | 11283695 |
| [1222_math.go](1222_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1184 KB | 11283696 |
| [1222_math.java](1222_math.java) | Java 1.8 | math | O(N²) | AC | 0.093 s | 1708 KB | 11283698 |
| [1222_math.py](1222_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.078 s | 396 KB | 11283697 |
| [1222_math.rs](1222_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.031 s | 208 KB | 11283699 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math_optimized.cpp](1222_math_optimized.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.001 s | 104 KB | 11304484 |
| [1222_math_optimized.java](1222_math_optimized.java) \* | Java 1.8 | math | O(N²) time; O(N) space | AC | 0.093 s | 348 KB | 11327402 |
| [1222_math_optimized.py](1222_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N²) | AC | 0.109 s | 248 KB | 11324929 |
| [1222_math_optimized.rs](1222_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n²) limb work; O(n) digits | AC | 0.015 s | 64 KB | 11325523 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
