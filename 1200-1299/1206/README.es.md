# 1206. Pares de números cuyas sumas de cifras se suman

[Timus 1206](https://acm.timus.ru/problem.aspx?space=1&num=1206) · dificultad 124 · combinatorics

Problema original de Leonid Volkov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sea `S(N)` la suma de las cifras de `N`. Para `2 ≤ K ≤ 50`, hay que
contar los pares ordenados de números de `K` cifras `A` y `B`, sin ceros
a la izquierda, con `S(A + B) = S(A) + S(B)`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K`.

## Salida

El número de pares.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
5989500
```

## Solución

Cada acarreo en la suma convierte un 10 en una posición en un 1 en la
siguiente, y baja la suma de cifras en 9. Así que la igualdad se cumple
exactamente cuando no hay acarreos, es decir, cuando las cifras de cada
posición suman como mucho 9. Entonces las posiciones son independientes.
En la posición más alta ambas cifras van de 1 a 9, lo que da
`8 + 7 + … + 1 = 36` pares; en cada una de las otras `K − 1` posiciones
las cifras van de 0 a 9, lo que da `10 + 9 + … + 1 = 55` pares. La
respuesta es `36 · 55^(K−1)`, un número de hasta 87 cifras. `O(K²)` con
la multiplicación escolar.

El resultado necesita O(K) dígitos decimales o bits salvo un factor constante. C++/Rust sencillos conservan vectores crecientes de dígitos; Rust añade String de salida O(K). Go/Java/Python guardan enteros largos y salida decimal: O(K) de valores/salida vivos, más trabajo aritmético y búferes. O(K²) escolar es un modelo conservador de cálculo/conversión, no implica K multiplicaciones repetidas de la potencia integrada. Java optimizado asigna exactamente 2K posiciones y O(K) bytes de respuesta; C++ optimizado reserva 100 posiciones fijas en pila para K ≤ 50. 36·55^(K−1) < 100^K da a lo sumo 2K dígitos, con igualdad para K=2 y K=3.

Detalles a tener en cuenta:

- la respuesta supera los 64 bits ya con `K = 12`;
- las cifras más altas no pueden ser 0, así que su número de pares es
  distinto.

La fórmula se comprobó por fuerza bruta sobre todos los pares para
`K = 2` y `K = 3`, y cada `K` se comparó con una solución escrita aparte.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1206_combinatorics_optimized.java`. Conserva la fórmula sin acarreo 36*55^(K-1). Para K<=50 guarda como máximo 100 dígitos decimales y multiplica por 55 K-1 veces durante la ejecución; emite bytes directamente. Cambia la representación aritmética, no la demostración combinatoria, sin respuestas precalculadas. Cota conservadora O(K²) operaciones sobre dígitos y O(K) espacio, evitando inicialización BigInteger; conserva la fórmula simple con BigInteger.

Accepted histórico de fuente exacta Java 1.8 #11327341: 0.109 s / 308 KB; comparación guardada del 2026-11-20: tiempo 14/141, memoria 1/141. Cumple el criterio temporal compartido bajo 1024 KB, sin primer puesto o marca independientes. El anterior #11304422 es el par histórico separado 0.125 s / 448 KB. Esta revisión solo cambia el comentario de menos de 2K a como máximo 2K; el resto del texto ejecutable es idéntico.

- `1206_combinatorics_optimized.java`: 0.109 s / 308 KB; base didáctica conservada `1206_combinatorics.java`: 0.14 s / 1748 KB.

El Accepted seleccionado de fuente exacta CPython 3.12 #11327017 de `1206_combinatorics_optimized.py` es 0.078 s / 612 KB; puestos guardados del 2026-11-20: tiempo 2/76, memoria 60/76. Bajo 1024 KB cumple solo por tiempo. Frente a la base actual #11283600 de 0.109 s / 416 KB, baja tiempo 28.44% y sube memoria 47.12%: ninguna métrica mejora 30%. PyPy 3.10 histórico #11324911 es el par distinto 0.140 s / 252 KB; la comparación posterior de ahorro de memoria se refiere a él, no a la fila CPython seleccionada.

La solución optimizada en C++ multiplica igualmente las cifras decimales
por 55, pero en un arreglo fijo de 100 elementos en la pila en lugar de
un `std::vector` que crece: como `K ≤ 50`, la respuesta `36 · 55^(K−1)`
es menor que `100^K` y tiene como mucho 100 cifras (en realidad, como
mucho 87). Sin `<vector>` el programa no lleva código de contenedores:
{1206_combinatorics_optimized.cpp}.

### Mejora medida

Son diferencias históricas entre registros Accepted emparejados, no una regla universal de admisión por mejora del 30%. Las bases se conservan; reducción negativa indica aumento. La admisión actual sigue la política compartida de ranking.

- `1206_combinatorics_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +46.81%; base: `1206_combinatorics.cpp`.

`1206_combinatorics_optimized.py`. Conserva la fórmula exacta 36*55^(K-1) y los enteros arbitrarios de Python. Tanto ** en la base como pow aquí ya calculan potencias enteras; no se atribuye un algoritmo nuevo de conteo. Una cota conservadora con aritmética escolar y conversión decimal es O(K²) de tiempo y O(K) bits de respuesta. Lee el único token y evita la función envolvente y la finalización normal. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. El Accepted histórico PyPy muestra ahorro de memoria; el CPython actual seleccionado cambia mayor memoria por menor tiempo registrado. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1206_combinatorics.py`: tiempo 0.109 s → 0.14 s; memoria 416 KB → 252 KB.

## Notas por lenguaje

Rigen los [criterios compartidos](../../RATING_CRITERIA.md) y la caché ligada a fuentes. Cumplen ambos C++, Go, Rust y Java/Python optimizados vinculados a sus registros. Java/Python sencillos fallan y quedan didácticos sin estrella. El comentario Java revisado todavía requiere nuevo Accepted, como se explica arriba. Bajo 1024 KB solo cuenta tiempo; Go con 1200 KB necesita ambas frente a dos rivales exactos. Rust usa referencia de su único rival. No hay primer puesto, admisión por mejora del 30% ni sustitución de cobertura actual por puestos PyPy antiguos.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics.cpp](1206_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 188 KB | 11283595 |
| [1206_combinatorics.go](1206_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.031 s | 1200 KB | 11283596 |
| [1206_combinatorics.java](1206_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.14 s | 1748 KB | 11283601 |
| [1206_combinatorics.py](1206_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 416 KB | 11283600 |
| [1206_combinatorics.rs](1206_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 212 KB | 11283602 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1206_combinatorics_optimized.cpp](1206_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 100 KB | 11304421 |
| [1206_combinatorics_optimized.java](1206_combinatorics_optimized.java) | Java 1.8 | combinatorics | O(K²) time; O(K) space | AC | 0.078 s | 356 KB | 11331216 |
| [1206_combinatorics_optimized.py](1206_combinatorics_optimized.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.078 s | 612 KB | 11327017 |
