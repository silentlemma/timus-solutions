# 1150. Cuántas veces aparece cada cifra en los números de página de 1 a N

[Timus 1150](https://acm.timus.ru/problem.aspx?space=1&num=1150) · dificultad 249 · math

Problema original de Evgeny Bryzgalov, del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las páginas se numeran de 1 a `N`, `N < 10⁹`. Cuenta cuántas veces se
escribe cada cifra de 0 a 9.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

Diez líneas: la cantidad de ceros, unos, …, nueves.

## Evaluación

Comparar diez conteos enteros exactos para las cifras 0..9; ignorar espacios. El nuevo código Python exacto pasó 12 pruebas del repositorio con PyPy 3.10. Las otras variantes conservan sus propias pruebas de destino y Accepted exactos. La salida se compara según el verificador del problema.

## Ejemplos

### Ejemplo 1

Entrada:

```
12
```

Salida:

```
1
5
2
1
1
1
1
1
1
1
```

## Solución

Se cuenta cada posición decimal por separado. Para la posición de peso
`p` (1, 10, 100, …) se parte `N` en la parte de encima, `high = N / (10p)`,
la cifra `cur` en ella y la parte de debajo, `low = N mod p`. Se miran los
números de 1 a `N` según su parte por encima de esta posición:

- cada parte superior de `0` a `high − 1` va seguida de los `10p` finales
  inferiores, así que para cada una cada cifra aparece `p` veces en esta
  posición;
- con la parte superior igual a `high`, una cifra `d < cur` aparece `p`
  veces más, `d = cur` aparece `low + 1` veces más (para los finales de `0`
  a `low`), y las cifras mayores no aparecen.

Los ceros son distintos: un cero en esta posición solo se escribe si hay
alguna cifra no nula encima, así que la parte superior `0` no cuenta. Eso
da `(high − 1)·p` para las partes superiores completas desde 1, y luego
`p` o `low + 1` como antes, todo solo cuando `high > 0`. Hay como mucho
nueve posiciones. `O(log N)`.

Detalles a tener en cuenta:

- los ceros a la izquierda no se escriben, por eso los ceros necesitan la
  regla aparte;
- las cantidades llegan a `9·10⁸` para `N = 999999999`, aún dentro de 32
  bits;
- `N` también se incluye.

Las respuestas se compararon con escribir cada número para todos los `N`
hasta 3000 y muchos hasta 30000, y con un recuento cifra a cifra sobre la
escritura decimal de `N` en todas las pruebas.

## Soluciones optimizadas

`1150_math_optimized.go`. Conserva conteo por partes alta/actual/baja y corrección de ceros iniciales. Protege multiplicación del peso y compara mediante limit/place/radix contra desbordamiento. O(log N) tiempo, espacio constante, sin enumerar números. Buffers acotados de entrada de 256 bytes y salida de 64 usan syscall.Read/Write de Go 1.14, reintentan EINTR/escrituras parciales y tratan EOF de cero bytes. Elimina inicialización fmt/bufio/os.File. Pruebas Linux y compilación cruzada Windows validan funcionamiento y construcción; las métricas pareadas siguientes vienen de nuestro Accepted exacto en juez Windows. Se conserva fuente didáctica legible.

Frente a `1150_math.go`: tiempo 0.031 s → 0.015 s; memoria 1084 KB → 292 KB.

`1150_math_optimized.rs`. Mantiene fórmulas posicionales high/current/low y corrección de ceros iniciales. Entrada numérica directa y diez líneas enteras sustituyen texto/formato estándar; diez contadores y algoritmo no cambian. O(log(N+1)) tiempo y O(1) espacio bajo límites enteros del enunciado. Conserva la fuente legible junto a la variante de runtime medido menor.

Frente a `1150_math.rs`: tiempo 0.015 s → 0.046 s; memoria 236 KB → 40 KB.

No cambia el conteo por posiciones: separar N en cifras superiores, cifra actual e inferiores para cada posición. Cada cifra no nula recibe ciclos completos y la fracción final; el cero excluye el bloque de ceros iniciales. Se mantienen diez contadores y se multiplica la posición por diez. Las variantes compactas reducen costes de entrada/salida, sin otra fórmula. Python tiene su propio Accepted en PyPy y cambia mayor tiempo por menor memoria; se preservan todas las bases.

- `1150_math_optimized.java`: 0.078 s / 320 KB; base `1150_math.java`: 0.109 s / 1568 KB; cambio respecto a la base: tiempo -28.4%, memoria -79.6%.
- `1150_math_optimized.py`: 0.140 s / 316 KB; base `1150_math.py`: 0.062 s / 460 KB; cambio respecto a la base: tiempo +125.8%, memoria -31.3%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1150_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1150_math.cpp](1150_math.cpp) | G++ 13.2 x64 | math | O(log N) | AC | 0.015 s | 128 KB | 11280268 |
| [1150_math.go](1150_math.go) | Go 1.14 x64 | math | O(log N) | AC | 0.031 s | 1084 KB | 11280291 |
| [1150_math.java](1150_math.java) | Java 1.8 | math | O(log N) | AC | 0.109 s | 1568 KB | 11280333 |
| [1150_math.py](1150_math.py) | Python 3.12 x64 | math | O(log N) | AC | 0.062 s | 460 KB | 11280317 |
| [1150_math.rs](1150_math.rs) | Rust 1.75 x64 | math | O(log N) | AC | 0.015 s | 236 KB | 11280335 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1150_math_optimized.java](1150_math_optimized.java) | Java 1.8 | math | O(log N) | AC | 0.078 s | 320 KB | 11308801 |
| [1150_math_optimized.py](1150_math_optimized.py) \* | PyPy 3.10 x64 | math | O(log N) | AC | 0.140 s | 316 KB | 11309691 |
| [1150_math_optimized.rs](1150_math_optimized.rs) | Rust 1.75 x64 | math | O(log(N+1)) time; O(1) space | AC | 0.046 s | 40 KB | 11325542 |
| [1150_math_optimized.go](1150_math_optimized.go) \* | Go 1.14 x64 | math | O(log N) time; O(1) space | AC | 0.015 s | 292 KB | 11325653 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
