# 1191. ¿Puede un policía atrapar a un ladrón que cambia de tranvía?

[Timus 1191](https://acm.timus.ru/problem.aspx?space=1&num=1191) · dificultad 249 · dp, math

Problema original de Leonid Volkov, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ladrón lleva `L` minutos de ventaja a un policía y corren a la misma
velocidad. En cada una de `N` paradas el ladrón espera un tranvía de una
línea que pasa cada `Ki` minutos, con una fase desconocida, y lo toma
hasta la parada siguiente; el policía llega a la misma parada y toma el
siguiente tranvía de la misma línea, y detiene al ladrón si lo encuentra
todavía esperando. Todos los tranvías van a la misma velocidad. Hay que
decidir si el policía puede llegar a atrapar al ladrón antes de que
terminen los `N` viajes.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`L` y `N`, y luego `K1 … KN`, todos enteros positivos menores que 100.

## Salida

`YES` si es posible atraparlo, si no `NO`.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 3
6 4 3
```

Salida:

```
NO
```

### Ejemplo 2

Entrada:

```
15 4
7 3 13 6
```

Salida:

```
YES
```

## Solución

Sea `g` el retraso de llegada del policía y `K` el intervalo.
El ladrón espera `w`, `0≤w<K`. Si `g<K`, elige `g<w<K`: el policía llega
mientras aún espera. Si `g≥K`, no puede atraparlo en esa parada.

Sin captura, el policía sale un número entero de tranvías después:
`K·ceil((g−w)/K)`. Escribe `g=qK+r`, `0≤r<K`. Como `w<K`, la diferencia
es al menos `qK`. Elegir `w=r+(K−r)/2`, estrictamente entre `r` y `K`,
alcanza esa cota sin empates entre llegada y salida. Los iguales tiempos
de viaje conservan la diferencia al llegar a la siguiente parada.

El mejor siguiente estado es `g−g%K`, con cero como captura posible.
La función no decrece con `g`: un retraso alcanzable menor nunca perjudica
en paradas futuras. Inducción por rutas prueba que seguir estos mínimos
detecta captura exactamente cuando algún horario admisible la permite.
Devuelve YES al llegar a cero; tras `N` tranvías sin cero, NO. `g=K`
permanece `K`, sin captura; intervalo uno no reduce un retraso entero positivo.

Tiempo `O(N)`. C++/Go/Java mantienen estado aritmético constante; Python/Rust
anteriores guardan `O(N)` tokens. Los números están en 1..99, los divisores
son positivos y el mínimo no crece: el resto entero es seguro y exacto.

## Soluciones optimizadas

**Java.** El Java añadido mantiene la aritmética y retorno temprano; cambia
`Scanner` por `StreamTokenizer` sobre `InputStreamReader`. Hasta 101 tokens
enteros no requieren el analizador de patrones Scanner; sus valores pequeños
se representan exactamente en el tokenizer. Misma idea, otra implementación:
`_optimized`. El Accepted exacto registra 0,125 s y 408 KB frente a 0,125 s
y 1636 KB de la base inalterada: 75,1% menos memoria y mismo tiempo.
Ambas versiones se conservan, sin atribuirlo a otra recurrencia o intérprete.

**Python/PyPy.** Se conserva la simulación directa como base educativa. El algoritmo nuevo recorre al revés: el menor desfase final positivo es 1. Como la transformación directa es k*floor(gap/k), para conservar needed se necesita antes al menos ceil(needed/k)*k. Actualizar ese umbral en orden inverso. Nunca disminuye: needed>L demuestra que no sobrevive ningún desfase positivo y la captura es posible. De lo contrario L sobrevive y no hay captura. Se consume la lista de enteros desde el final, sin una copia invertida. O(N)tiempo y almacenamiento de entrada; la ventaja medida es de memoria, no de tiempo.

- `1191_math_optimized.java`: 0.125 s / 408 KB; base `1191_math.java`: 0.125 s / 1636 KB; cambio respecto a la base: tiempo -0.0%, memoria -75.1%.
- `1191_dp.py`: 0.109 s / 236 KB; base `1191_math.py`: 0.062 s / 352 KB; cambio respecto a la base: tiempo +75.8%, memoria -33.0%.

`1191_math_optimized.rs`. Conserva solo la separación actual y la redondea hacia abajo a un múltiplo de cada intervalo siguiente. Cuando llega a cero, las operaciones posteriores no pueden alterarla y se imprime de inmediato. Tiempo máximo O(N), espacio auxiliar O(1). Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `1191_math.rs`: tiempo 0.015 s → 0.015 s; memoria 212 KB → 52 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1191_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1191_math.cpp](1191_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 124 KB | 11283443 |
| [1191_math.go](1191_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1060 KB | 11283445 |
| [1191_math.java](1191_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 1636 KB | 11283449 |
| [1191_math.py](1191_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 352 KB | 11283447 |
| [1191_math.rs](1191_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 212 KB | 11283451 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1191_math_optimized.java](1191_math_optimized.java) \* | Java 1.8 | math | O(N) | AC | 0.125 s | 408 KB | 11308408 |
| [1191_dp.py](1191_dp.py) \* | PyPy 3.10 x64 | dp | O(N) time, O(N) input integers | AC | 0.109 s | 236 KB | 11309781 |
| [1191_math_optimized.rs](1191_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 52 KB | 11325089 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
