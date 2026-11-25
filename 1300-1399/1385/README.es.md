# 1385. Número interesante

[Timus 1385](https://acm.timus.ru/problem.aspx?space=1&num=1385) · dificultad 247 · math

Problema original de Alexander Ipatov, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número de 2N cifras sin cero inicial es interesante si es divisible
tanto por el número formado por sus primeras N cifras como por el
formado por sus últimas N cifras. Hay que contar los números
interesantes de 2N cifras, 1 ≤ N ≤ 10 000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

La cantidad.

## Evaluación

Comparar un token entero. Cada una de las cinco fuentes añadidas tiene 13 pruebas del repositorio y 67 ejecuciones extra, incluidas N=1,2,3,4,4300,4301,9999,10000. Solo Python se ejecutó además para todos los N=1..10000. Los conteos pequeños se comprobaron por divisibilidad literal hasta N=3 y múltiplos explícitos para N=4. No son 10000 ejecuciones de cada lenguaje.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
14
```

Los catorce números son 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77,
88 y 99.

## Solución

Escribir `A*M+B`, con `M=10^N`, `M/10≤A<M` y `0≤B<M`. El segundo bloque
puede tener ceros iniciales, pero debe ser distinto de cero para dividir
el número. La divisibilidad por A implica `B=k*A`, `1≤k≤9`. Entonces
`k*A | A*M+B` equivale a `k | M`. Cada k válido permite
`A=M/10..M/k−1`, es decir `M/k−M/10` opciones. Las opciones de distintos k
son disjuntas y se suman.

Go, Java y Python didácticos calculan M con sus enteros grandes estándar,
prueban k=1..9 y dividen exactamente. Usan `O(N)` dígitos; una cota
conservadora de aritmética y conversión decimal es `O(N²)`. Python desactiva
el límite predeterminado de dígitos para admitir todo N legal. El resultado
no cabe en enteros de ancho fijo. Se conservan las fórmulas anteriores;
C++ y Rust usan la forma cerrada demostrada porque sus bibliotecas estándar
no tienen un tipo equivalente de precisión arbitraria.

## Soluciones optimizadas

`1385_math_optimized.go`. Conserva coeficiente derivado por divisibilidad usando10^min(N,3) y sufijo de ceros en flujo. syscall.Read/Write Go1.14 y buffers fijos256bytes sustituyen inicialización os.File/buffers4096, reintentan EINTR/escrituras parciales y tratan EOF cero. Sin tabla de respuestas ni enteros grandes. O(N) salida,O(1) espacio auxiliar. Nuestro Accepted usa280KB,74,9% menos que base corta1116KB; conserva fuentes sencillas de fórmula y aritmética grande.

Frente a `1385_math.go`: tiempo 0.031 s → 0.015 s; memoria 1116 KB → 280 KB.

`1385_math_optimized.rs`. Conserva Σ(10^N/d-10^(N-1)) para d=1..9 que dividen10^N, calculando el coeficiente solo con10^min(N,3). Desde N=3 los d son1,2,4,5,8: obtiene14,155 o1575 y emite N-3 ceros cuando procede. Los valores derivan del pequeño bucle, no son respuestas guardadas. Ambas versiones escriben el sufijo directamente, sin Repeat/repeat ni concatenar toda la respuesta. Hay N+1 dígitos: tiempo O(N), estado auxiliar O(1) y E/S acotada, sin entero arbitrario ni búfer de tamaño N. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1385_math.rs`: tiempo 0.015 s → 0.015 s; memoria 224 KB → 56 KB.

Entre k=1..9 solo pueden dividir `10^N` los que tienen factores primos 2 y 5.
Para N=1 son 1,2,5:9+4+1=14. Para N=2 son 1,2,4,5:90+40+15+10=155.
Desde N=3 se estabilizan en 1,2,4,5,8. Al sacar `10^(N−3)` queda
`(1000−100)+(500−100)+(250−100)+(200−100)+(125−100)=1575`.
Emitir `1575` seguido de N−3 ceros. Las constantes se deducen del conteo
divisible; no son respuestas guardadas para entradas particulares. Hay N+1
dígitos y `O(N)` tiempo de salida. Las fórmulas previas construyen la cadena
completa, `O(N)` espacio; C++/Java nuevos emiten bloques acotados de ceros,
con `O(1)` espacio auxiliar respecto a N.

La fórmula Python conservada ahorra 35,5% memoria contra la base didáctica
de enteros grandes, con el mismo tiempo 0,078 s. El Java nuevo es más lento
que su base grande pero ahorra memoria: se indican ambos efectos. No llegar
al objetivo de ranking no invalida una reducción real; se marca con estrella.

- `1385_math.py`: 0.078 s / 392 KB; base `1385_math_number_theory.py`: 0.078 s / 608 KB; cambio respecto a la base: tiempo -0.0%, memoria -35.5%.
- `1385_math_optimized.cpp`: 0.015 s / 120 KB; base `1385_math.cpp`: 0.015 s / 372 KB; cambio respecto a la base: tiempo -0.0%, memoria -67.7%.
- `1385_math_optimized.java`: 0.093 s / 432 KB; base `1385_math_number_theory.java`: 0.078 s / 1388 KB; cambio respecto a la base: tiempo +19.2%, memoria -68.9%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1385_math_optimized.go`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

`1385_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1385_math.cpp](1385_math.cpp) | G++ 13.2 x64 | math | O(N) output time; O(N) string space | AC | 0.015 s | 372 KB | 11285827 |
| [1385_math_number_theory.go](1385_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(N^2) conservative arithmetic/conversion; O(N) digits | AC | 0.031 s | 1428 KB | 11308776 |
| [1385_math_number_theory.java](1385_math_number_theory.java) | Java 1.8 | math, number_theory | O(N^2) conservative arithmetic/conversion; O(N) digits | AC | 0.078 s | 1388 KB | 11308767 |
| [1385_math_number_theory.py](1385_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(N^2) conservative arithmetic/conversion; O(N) digits | AC | 0.078 s | 608 KB | 11308764 |
| [1385_math.rs](1385_math.rs) | Rust 1.75 x64 | math | O(N) output time; O(N) string space | AC | 0.015 s | 224 KB | 11285843 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1385_math.go](1385_math.go) | Go 1.14 x64 | math | O(N) output time; O(N) string space | AC | 0.031 s | 1116 KB | 11285831 |
| [1385_math.java](1385_math.java) | Java 1.8 | math | O(N) output time; O(N) string space | AC | 0.109 s | 1648 KB | 11285839 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1385_math.py](1385_math.py) | Python 3.12 x64 | math | O(N) output time; O(N) string space | AC | 0.078 s | 392 KB | 11285836 |
| [1385_math_optimized.cpp](1385_math_optimized.cpp) | G++ 13.2 x64 | math | O(N) output time; O(1) auxiliary space | AC | 0.015 s | 120 KB | 11308752 |
| [1385_math_optimized.java](1385_math_optimized.java) | Java 1.8 | math | O(N) output time; O(1) auxiliary space | AC | 0.093 s | 432 KB | 11308759 |
| [1385_math_optimized.go](1385_math_optimized.go) | Go 1.14 x64 | math | O(N) time; O(1) space | AC | 0.015 s | 280 KB | 11328274 |
| [1385_math_optimized.rs](1385_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 56 KB | 11325098 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
