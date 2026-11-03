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

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1191_math.cpp`; fuente que cubre `1191_math.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 38/38.

- Go: base didáctica preferida `1191_math.go`; fuente que cubre `1191_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1191_math.java`; fuente que cubre `1191_math_optimized.java`; puestos tiempo/memoria 2/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1191_math.py`; fuente que cubre `1191_dp.py`; puestos tiempo/memoria 8/1, registros de otros autores 12/12.

- Rust: base didáctica preferida `1191_math.rs`; fuente que cubre `1191_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

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

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
