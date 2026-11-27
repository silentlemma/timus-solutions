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
7
```

Salida:

```
12
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

El resultado tiene O(N) dígitos/bits. Vectores decimales crecientes, enteros largos y salida requieren O(N) espacio vivo de valor/salida más trabajo aritmético de biblioteca; C++ optimizado reserva realmente array fijo de 1000 dígitos. Multiplicación pequeña repetida admite cota conservadora O(N²) de trabajo por dígitos. La potencia de biblioteca usa multiplicaciones mayores; la cota común no dice que la potencia integrada repita N multiplicaciones.

Detalles a tener en cuenta:

- `N = 1` da 1, y `N = 4` da 4;
- un resto de 1 no debe quedarse como factor 1;
- la respuesta va mucho más allá de 64 bits.

Las respuestas se comprobaron con una fuerza bruta sobre todos los
repartos para cada `N` hasta 59, y se compararon con una solución escrita
aparte en todas las pruebas.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1222_math_optimized.java`. Conserva la partición óptima en treses, sustituyendo resto uno por factor cuatro, con N<4 separado. Calcula el mismo producto en bloques base10^9 con multiplicadores generados hasta 3^18, sin BigInteger ni respuestas precalculadas. Cada intermedio long es menor que 10^9*3^18<2^63; al imprimir rellena bloques inferiores a nueve dígitos. Cota conservadora O(N²) trabajo aritmético y O(N) espacio; conserva la versión matemática simple.

Accepted exacto Java 1.8 #11327402: 0.093 s / 348 KB. Comparación guardada 2026-11-20: tiempo 12/136, memoria 2/136. Cumple solo por tiempo bajo 1024 KB, sin meta separada de primer puesto ni estrella. El optimizado anterior #11304486 de 0.125 s / 484 KB es otro par histórico, no el comprobante actual. Se conserva el algoritmo Java sencillo; la corrección solo del comentario se indica abajo.

- `1222_math_optimized.java`: 0.093 s / 348 KB; base didáctica conservada `1222_math.java`: 0.093 s / 1708 KB.

`1222_math_optimized.rs`. Conserva descomposición óptima en treses y un cuatro si sobra uno. Empaqueta nueve cifras decimales por u32 en vez de una y emite grupos rellenados sin construir String decimal. Multiplicar por tres cabe en u32: 3*(10^9-1)+2<2^32. Las multiplicaciones pequeñas siguen O(n²) trabajo de limbs y O(n) cifras almacenadas; mejora representación, no asintótica. Conserva versión sencilla de un dígito por limb.

Frente a `1222_math.rs`: tiempo 0.031 s → 0.015 s; memoria 208 KB → 64 KB.

La solución optimizada en C++ multiplica un arreglo global fijo de 1000
dígitos decimales en lugar de un `std::vector` que crece con el
producto, así que el programa no necesita memoria dinámica; con
`N ≤ 3000` el producto tiene como mucho 478 dígitos:
{1222_math_optimized.cpp}.

### Mejora medida

Son diferencias históricas de valores Accepted emparejados, no admisión universal por mejora del 30%. Se conservan las bases. Reducción negativa significa aumento; tiempos originales bajo un tick no garantizan aceleración portátil.

- `1222_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +45.83%; base: `1222_math.cpp`.

`1222_math_optimized.py` mantiene la fórmula exacta de máximo producto con treses, sustituyendo resto uno por cuatro. Usa pow en vez de ** y vacía stdout antes de os._exit(0). El resultado de O(N) bits tiene cota escolar conservadora O(N²) de aritmética/conversión decimal y O(N) espacio de valor/salida más trabajo de runtime. PyPy 0.109 s / 248 KB y CPython base 0.078 s / 396 KB son pares de intérpretes/ejecuciones distintos: no aíslan ganancia causal de exit o pow. Se conserva el algoritmo sencillo y se indica abajo su comentario corregido.

Frente a `1222_math.py`: tiempo 0.078 s → 0.109 s; memoria 396 KB → 248 KB.

## Notas por lenguaje

La caché exacta sigue los [criterios compartidos](../../RATING_CRITERIA.md). Cumplen ambos C++, Go, CPython base, Java optimizado y ambos Rust. Java sencillo falla memoria exigida; PyPy falla tiempo y mantiene marca. Bajo 1024 KB solo cuenta tiempo; Go con 1184 KB exige ambas y referencia exacta. Rust usa grupo del mismo lenguaje: 0.031 s / 208 KB y 0.015 s / 64 KB cumplen numéricamente, no por tabla vacía o excepción de ahorro. Puestos PyPy antiguos 19/61 tiempo y 3/61 memoria son históricos, no meta actual de primer puesto.

Esta revisión solo corrige el comentario de prueba en `1222_math.cpp`, `1222_math_optimized.cpp`, `1222_math.go`, `1222_math.java`, `1222_math.py` y `1222_math.rs`: dividir una parte mayor que 4 mejora estrictamente; 4=2+2 empata. Texto ejecutable y demás comentarios no cambian. Los comprobantes de tablas y admisión anterior son de bytes históricos exactos.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math.cpp](1222_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 176 KB | 11331135 |
| [1222_math.go](1222_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1216 KB | 11331004 |
| [1222_math.java](1222_math.java) | Java 1.8 | math | O(N²) | AC | 0.109 s | 1688 KB | 11331043 |
| [1222_math.py](1222_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.093 s | 420 KB | 11331062 |
| [1222_math.rs](1222_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.015 s | 204 KB | 11331100 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math_optimized.cpp](1222_math_optimized.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 112 KB | 11331136 |
| [1222_math_optimized.java](1222_math_optimized.java) | Java 1.8 | math | O(N²) time; O(N) space | AC | 0.093 s | 348 KB | 11327402 |
| [1222_math_optimized.py](1222_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N²) | AC | 0.109 s | 248 KB | 11324929 |
| [1222_math_optimized.rs](1222_math_optimized.rs) | Rust 1.75 x64 | math | O(n²) limb work; O(n) digits | AC | 0.015 s | 64 KB | 11325523 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
