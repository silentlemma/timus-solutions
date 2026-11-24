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

`1108_math_optimized.rs`. Conserva recurrencia de Sylvester a_next=a²-a+1 con limbs u32 de base 10^4. Cuadra diagonales una vez y duplica productos cruzados; normaliza scratch u64 reutilizable, resta a y suma uno. Reutiliza vectores y emite grupos de cuatro cifras. Evita calcular el siguiente término inútil después del último impreso, que sí calculaba la base. Con D limbs del mayor término requerido, O(D²) trabajo escolar total y O(D) espacio incluyendo scratch. N<=18 mantiene coeficientes en u64. Conserva la sencilla de base 10^9.

Frente a `1108_math.rs`: tiempo 0.015 s → 0.015 s; memoria 356 KB → 188 KB.

Se conservan las cinco recurrencias Sylvester claras. Las rápidas calculan a[1]=2,a[k+1]=a[k]^2-a[k]+1 y no construyen un término tras la última salida. Java guarda dígitos int en base 10000, eleva simétricamente por multiplicación escolar en acumuladores long, resta el valor anterior y suma uno con acarreos exactos. Para N <= 18, a[18]<2^131072<10^40960. Por eso, 11000 bloques bastan y cada coeficiente cabe en long. Emite bloques de cuatro dígitos sin cadena gigante. Python mantiene enteros nativos, pero divide recursivamente la salida en conversiones de hasta 1000 dígitos, bajo el límite normal. Una cota racional de log10(2) y comparación exacta con potencia de diez dan el ancho. Cada dígito sale una vez. Cota conservadora O(D²) de tiempo y O(D) dígitos. Se verificaron los 18 prefijos. Un tick de tiempo Python no justifica admisión: su memoria baja más del 30%.

- `1108_math_optimized.java`: 0.125 s / 516 KB; base `1108_math.java`: 0.187 s / 6508 KB; cambio respecto a la base: tiempo -33.2%, memoria -92.1%.
- `1108_math_optimized.py`: 0.015 s / 788 KB; base `1108_math.py`: 0.031 s / 1144 KB; cambio respecto a la base: tiempo -51.6%, memoria -31.1%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1108_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1108_math_optimized.java](1108_math_optimized.java) | Java 1.8 | math | O(D²) arithmetic/output bound; O(D) working digits | AC | 0.125 s | 516 KB | 11309742 |
| [1108_math_optimized.py](1108_math_optimized.py) | Python 3.12 x64 | math | O(D²) arithmetic/output bound; O(D) working digits | AC | 0.015 s | 788 KB | 11309753 |
| [1108_math_optimized.rs](1108_math_optimized.rs) | Rust 1.75 x64 | math | O(D²) limb work; O(D) space | AC | 0.015 s | 188 KB | 11325539 |
