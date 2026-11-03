# 1108. Fracciones unitarias que dejan el menor resto positivo

[Timus 1108](https://acm.timus.ru/problem.aspx?space=1&num=1108) · dificultad 252 · math

Problema original de Pavlin Peev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elige enteros positivos `a_1 ≤ a_2 ≤ … ≤ a_N` (`1 ≤ N ≤ 18`) de modo que
`1 − (1/a_1 + … + 1/a_N)` sea positivo y lo más pequeño posible.
Imprímelos en ese orden, uno por línea.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

`a_1`, …, `a_N`, cada uno en su propia línea.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `1108_math_optimized.java` (Java 1.8): 11 pruebas del repositorio; 18 comparaciones adicionales de fuente exacta.

- `1108_math_optimized.py` (Python 3.12 x64): 11 pruebas del repositorio; 18 comparaciones adicionales de fuente exacta.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
2
3
```

## Solución

Cada fracción se toma de forma voraz: la mayor fracción unitaria que aún
deja algo. Así sale la sucesión de Sylvester `a_1 = 2`,
`a_{k+1} = a_k (a_k − 1) + 1`, y por inducción el resto tras `k` términos
es exactamente `1 / (a_{k+1} − 1)`, de modo que la siguiente mayor
fracción admisible es `1/a_{k+1}`. Que la elección voraz sea además la
mejor para todo `N` es un resultado clásico sobre fracciones egipcias
(Curtiss, 1922).

Los términos se elevan al cuadrado en cada paso: `a_18` tiene unas 26 700
cifras y la salida entera unos 53 000 caracteres, así que hacen falta
enteros grandes. Una multiplicación por término, `O(D²)` con el método
escolar para `D` cifras, basta de sobra.

Detalles a tener en cuenta:

- los enteros de 64 bits se desbordan ya en `a_8`;
- Python se niega por defecto a convertir a texto enteros de más de 4300
  cifras, y `a_16` ya los supera;
- los denominadores deben imprimirse completos, sin notación científica
  ni redondeo.

Las respuestas se comprobaron con una búsqueda sobre todos los
denominadores no decrecientes con fracciones exactas para `N ≤ 4`, y para
todo `N` verificando con fracciones exactas que el resto es
`1 / (a_1 ⋯ a_N)`, el valor que da el argumento voraz.

## Soluciones optimizadas

Se conservan las cinco recurrencias Sylvester claras. Las rápidas calculan a[1]=2,a[k+1]=a[k]^2-a[k]+1 y no construyen un término tras la última salida. Java guarda dígitos int en base 10000, eleva simétricamente por multiplicación escolar en acumuladores long, resta el valor anterior y suma uno con acarreos exactos. Para N <= 18, a[18]<2^131072<10^40960. Por eso, 11000 bloques bastan y cada coeficiente cabe en long. Emite bloques de cuatro dígitos sin cadena gigante. Python mantiene enteros nativos, pero divide recursivamente la salida en conversiones de hasta 1000 dígitos, bajo el límite normal. Una cota racional de log10(2) y comparación exacta con potencia de diez dan el ancho. Cada dígito sale una vez. Cota conservadora O(D²) de tiempo y O(D) dígitos. Se verificaron los 18 prefijos. Un tick de tiempo Python no justifica admisión: su memoria baja más del 30%.

- `1108_math_optimized.java`: 0.125 s / 516 KB; base `1108_math.java`: 0.187 s / 6508 KB; cambio respecto a la base: tiempo -33.2%, memoria -92.1%.
- `1108_math_optimized.py`: 0.015 s / 788 KB; base `1108_math.py`: 0.031 s / 1144 KB; cambio respecto a la base: tiempo -51.6%, memoria -31.1%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1108_math.cpp`; fuente que cubre `1108_math.cpp`; puestos tiempo/memoria 1/4, registros de otros autores 23/23.

- Go: base didáctica preferida `1108_math.go`; fuente que cubre `1108_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1108_math.java`; fuente que cubre `1108_math_optimized.java`; puestos tiempo/memoria 2/1, registros de otros autores 13/13.

- Python/PyPy: base didáctica preferida `1108_math.py`; fuente que cubre `1108_math_optimized.py`; puestos tiempo/memoria 1/3, registros de otros autores 21/21.

- Rust: base didáctica preferida `1108_math.rs`; fuente que cubre `1108_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1108_math.cpp](1108_math.cpp) | G++ 13.2 x64 | math | O(D²) per term | AC | 0.015 s | 232 KB | 11279192 |
| [1108_math.go](1108_math.go) | Go 1.14 x64 | math | O(D²) per term | AC | 0.015 s | 1920 KB | 11279193 |
| [1108_math.java](1108_math.java) | Java 1.8 | math | O(D²) per term | AC | 0.187 s | 6508 KB | 11279195 |
| [1108_math.py](1108_math.py) | Python 3.12 x64 | math | O(D²) per term | AC | 0.031 s | 1144 KB | 11279194 |
| [1108_math.rs](1108_math.rs) | Rust 1.75 x64 | math | O(D²) per term | AC | 0.015 s | 356 KB | 11279196 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1108_math_optimized.java](1108_math_optimized.java) \* | Java 1.8 | math | O(D²) arithmetic/output bound; O(D) working digits | AC | 0.125 s | 516 KB | 11309742 |
| [1108_math_optimized.py](1108_math_optimized.py) \* | Python 3.12 x64 | math | O(D²) arithmetic/output bound; O(D) working digits | AC | 0.015 s | 788 KB | 11309753 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
