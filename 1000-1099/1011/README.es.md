# 1011. La menor población con una proporción estrictamente entre dos porcentajes

[Timus 1011](https://acm.timus.ru/problem.aspx?space=1&num=1011) · dificultad 248 · math, number_theory

Problema original del Campeonato de la Universidad Estatal de los Urales 1997.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados dos porcentajes `P` y `Q` (`0.01 ≤ P, Q ≤ 99.99`, como mucho dos
cifras tras el punto decimal, `P < Q`), encuentra el menor entero positivo
`n` para el que exista un entero `c` con `P% < c / n < Q%`, ambas
desigualdades estrictas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`P` y `Q`, separados por un espacio o un salto de línea. Pueden escribirse
como enteros (`13`) o con uno o dos decimales (`14.1`, `12.50`).

## Salida

El menor `n`.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `1011_number_theory_optimized.cpp` (G++ 13.2 x64): 14 pruebas del repositorio; 115 comparaciones adicionales de fuente exacta.

- `1011_number_theory.go` (Go 1.14 x64): 14 pruebas del repositorio; 14 comparaciones adicionales de fuente exacta.

- `1011_number_theory.java` (Java 1.8): 14 pruebas del repositorio; 115 comparaciones adicionales de fuente exacta.

- `1011_number_theory_optimized.py` (PyPy 3.10 x64): 14 pruebas del repositorio.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 12
```

Salida:

```
9
```

### Ejemplo 2

Entrada:

```
12.5
12.6
```

Salida:

```
127
```

## Solución

Primero, evitamos los números en coma flotante. Ambos límites tienen como
mucho dos decimales, así que `p = 100·P` y `q = 100·Q` son enteros
(centésimas de punto porcentual), y la condición se vuelve
`p·n < 10000·c < q·n`.

**Recorrer n.** Para un `n` dado, el menor `c` por encima del límite
inferior es `c = ⌊p·n / 10000⌋ + 1`; `n` sirve exactamente cuando ese `c`
sigue por debajo del límite superior, `10000·c < q·n`. Se prueba
`n = 1, 2, ...`. El intervalo mide al menos `1/10000`, así que siempre sirve
algún `n ≤ 10000` (la mayor respuesta es 5001); el recorrido es instantáneo.

**Árbol de Stern–Brocot.** La respuesta es el menor denominador de una
fracción estrictamente dentro de `(p/10000, q/10000)`. Se desciende por el
árbol de Stern–Brocot desde los límites `0/1` y `1/0`: se toma la mediante
`(a + c)/(b + d)` de los límites actuales; si está en el límite inferior o
por debajo pasa a ser el nuevo límite izquierdo, si está en el superior o
por encima pasa a ser el derecho, y si no, es la respuesta. La primera
fracción del árbol que cae dentro de un intervalo es la de menor
denominador.

Detalles a tener en cuenta:

- leer los límites como números en coma flotante: `14.1` no es exacto en
  binario, y la comparación con `c / n` en el borde puede salir de
  cualquier lado;
- ambas desigualdades son estrictas: con `P = 12.5`, `1/8` no está dentro;
- `n = 1` nunca sirve, porque `0 < P` y `Q < 100`.

## Soluciones optimizadas

Se conservan el barrido de denominadores y el árbol Stern–Brocot paso a paso. Las versiones rápidas mantienen fracciones vecinas a/b y c/d fuera del intervalo abierto. Su medianta es la fracción más sencilla entre ellas. Si aún queda fuera, un cociente entero exacto salta la máxima serie por ese lado; ninguna fracción omitida es válida. La primera medianta interior tiene, por tanto, denominador mínimo. Los porcentajes se convierten en centésimas enteras y se comparan productos cruzados con WHOLE=10000, excluyendo igualdades. Los saltos siguen fracciones continuas: O(log WHOLE) pasos y estado numérico constante. Go usa búferes syscall portables y acotados; Python, flujos de texto y el PyPy declarado.

- `1011_number_theory_optimized.cpp`: 0.015 s / 104 KB; base `1011_math.cpp`: 0.015 s / 352 KB; cambio respecto a la base: tiempo -0.0%, memoria -70.5%.
- `1011_number_theory.go`: 0.031 s / 312 KB; base `1011_math.go`: 0.015 s / 1088 KB; cambio respecto a la base: tiempo +106.7%, memoria -71.3%.
- `1011_number_theory.java`: 0.125 s / 332 KB; base `1011_math.java`: 0.125 s / 1580 KB; cambio respecto a la base: tiempo -0.0%, memoria -79.0%.
- `1011_number_theory_optimized.py`: 0.156 s / 292 KB; base `1011_number_theory.py`: 0.109 s / 468 KB; cambio respecto a la base: tiempo +43.1%, memoria -37.6%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1011_math.cpp`; fuente que cubre `1011_number_theory_optimized.cpp`; puestos tiempo/memoria 1/3, registros de otros autores 155/155.

- Go: base didáctica preferida `1011_math.go`; fuente que cubre `1011_number_theory.go`; puestos tiempo/memoria 2/1, registros de otros autores 1/1.

- Java: base didáctica preferida `1011_math.java`; fuente que cubre `1011_number_theory.java`; puestos tiempo/memoria 2/1, registros de otros autores 5/5.

- Python/PyPy: base didáctica preferida `1011_number_theory.py`; fuente que cubre `1011_number_theory_optimized.py`; puestos tiempo/memoria 25/2, registros de otros autores 25/25.

- Rust: base didáctica preferida `1011_math.rs`; fuente que cubre `1011_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1011_math.cpp](1011_math.cpp) | G++ 13.2 x64 | math | O(answer) | AC | 0.015 s | 352 KB | 11278050 |
| [1011_math.go](1011_math.go) | Go 1.14 x64 | math | O(answer) | AC | 0.015 s | 1088 KB | 11278054 |
| [1011_math.java](1011_math.java) | Java 1.8 | math | O(answer) | AC | 0.125 s | 1580 KB | 11278060 |
| [1011_number_theory.py](1011_number_theory.py) | Python 3.12 x64 | number_theory | O(answer) tree steps | AC | 0.109 s | 468 KB | 11278057 |
| [1011_math.rs](1011_math.rs) | Rust 1.75 x64 | math | O(answer) | AC | 0.015 s | 228 KB | 11278063 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1011_number_theory.cpp](1011_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(answer) tree steps | AC | 0.015 s | 352 KB | 11278050 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1011_number_theory_optimized.cpp](1011_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.015 s | 104 KB | 11308795 |
| [1011_number_theory.go](1011_number_theory.go) \* | Go 1.14 x64 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.031 s | 312 KB | 11309756 |
| [1011_number_theory.java](1011_number_theory.java) \* | Java 1.8 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.125 s | 332 KB | 11308797 |
| [1011_number_theory_optimized.py](1011_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.156 s | 292 KB | 11309727 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
