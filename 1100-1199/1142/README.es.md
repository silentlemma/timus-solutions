# 1142. Contar las ordenaciones con empates de N objetos

[Timus 1142](https://acm.timus.ru/problem.aspx?space=1&num=1142) · dificultad 155 · combinatorics

Problema original de Timus; no se indican autor ni fuente.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Entre dos cualesquiera de `N` objetos comparables se cumple una de
`a = b`, `a < b`, `b < a`. Cuenta las formas distintas de ordenar `N`
objetos en este sentido, con empates permitidos: para tres objetos hay
13, de `a = b = c` a `c < b < a`. Responde para varios `N` de 2 a 10; la
entrada termina con `-1`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Valores de `N`, uno por línea, y luego `-1`.

## Salida

La cantidad para cada `N`, una por línea.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
3
-1
```

Salida:

```
3
13
```

## Solución

Una ordenación con empates es una sucesión de grupos de objetos iguales,
con los grupos estrictamente crecientes. Mirando el primer grupo: es
cualquier conjunto no vacío de `k` objetos, elegido de `C(n, k)` formas,
y los `n − k` objetos restantes forman su propia ordenación con empates.
Así que, con `a(0) = 1`,

`a(n) = Σ_{k=1..n} C(n, k)·a(n − k)`.

Son los números de Bell ordenados (números de Fubini) 1, 1, 3, 13, 75,
541, …; el mayor que hace falta, `a(10) = 102247563`, cabe en 32 bits. La
tabla se construye una vez con el triángulo de Pascal, y cada consulta es
una búsqueda. `O(10²)` para construirla.

Detalles a tener en cuenta:

- la entrada no trae la cantidad; se lee hasta `-1`;
- el mismo `N` puede preguntarse varias veces.

Los valores se compararon con la fórmula independiente
`a(n) = Σ k!·S(n, k)` con números de Stirling de segunda especie, y para
`n ≤ 6` con un listado de todas las ordenaciones.

## Soluciones optimizadas

`1142_combinatorics_optimized.go`. Recurrencia y matriz Pascal completa 11×11 se conservan. Precalcula particiones ordenadas para L=10 y procesa Q consultas hasta negativo o EOF. Esta revisión Go cambia coste de E/S, no algoritmo combinatorio ni tablas. Buffers acotados de entrada de 256 bytes y salida de 64 usan syscall.Read/Write de Go 1.14, reintentan EINTR/escrituras parciales y tratan EOF de cero bytes. Elimina inicialización fmt/bufio/os.File. Pruebas Linux y compilación cruzada Windows validan funcionamiento y construcción; las métricas pareadas siguientes vienen de nuestro Accepted exacto en juez Windows. Se conserva fuente didáctica legible.

Frente a `1142_combinatorics.go`: tiempo 0.001 s → 0.015 s; memoria 1084 KB → 272 KB.

`1142_combinatorics_optimized.py`. Mantiene la recurrencia de órdenes débiles, calculando C(n,k) como choose*(n-k+1)//k sin triángulo de Pascal. Guarda L+1 respuestas, L=10, con precomputación O(L²). Python aún retiene entrada dividida y salida acumulada: espacio total O(L+I+O), donde I,O son sus tamaños. Termina en la primera consulta negativa. La fila Accepted indica el runtime real y sus medidas emparejadas. Vacía salida antes de os._exit(0), que omite cierre del intérprete; la mejora medida de memoria depende del runtime y no implica aceleración asintótica.

Frente a `1142_combinatorics.py`: tiempo 0.031 s → 0.125 s; memoria 436 KB → 220 KB.

`1142_combinatorics_optimized.rs`. Mantiene recurrencia de órdenes débiles, genera binomiales incrementalmente y elimina matriz de Pascal 11×11. Guarda once u64, lee consultas hasta negativo o EOF y emite bytes del runtime C sin cadenas de entrada/salida retenidas. Para L=10 y Q consultas, O(L²+Q) tiempo y O(L) espacio auxiliar. Conserva versión didáctica con tabla.

Frente a `1142_combinatorics.rs`: tiempo 0.001 s → 0.001 s; memoria 220 KB → 44 KB.

`1142_combinatorics_optimized.java`. Conserva la recurrencia de particiones ordenadas. Lee enteros con un búfer de bytes de 1 KB y guarda solo ways[0..L], L=10; genera cada coeficiente binomial por multiplicaciones y divisiones sucesivas, sin matriz de Pascal. Elimina StreamTokenizer, BufferedReader y PrintWriter. Acumula las respuestas en StringBuilder hasta una consulta negativa o EOF y luego las imprime juntas. Para Q consultas, tiempo O(L²+Q) y espacio O(L+Q), incluida la salida almacenada; ese espacio no es constante. Se conserva la versión simple.

Accepted del fuente exacto #11326631: 0.046 s / 336 KB. En la muestra Java 1.8 guardada el 2026-11-20: puesto de tiempo 3/44, de memoria 2/44. El asterisco sigue indicando el objetivo de clasificación propio del lenguaje.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1142_combinatorics_optimized.java`: reducción de tiempo +50.54%; reducción de memoria +79.05%; base: `1142_combinatorics.java`.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1142_combinatorics_optimized.py`: puesto de tiempo 25/26 y de memoria 2/26 en esta muestra comparable.

`1142_combinatorics_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics.cpp](1142_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(1) per query | AC | 0.001 s | 128 KB | 11279451 |
| [1142_combinatorics.go](1142_combinatorics.go) | Go 1.14 x64 | combinatorics | O(1) per query | AC | 0.001 s | 1084 KB | 11279453 |
| [1142_combinatorics.java](1142_combinatorics.java) | Java 1.8 | combinatorics | O(1) per query | AC | 0.093 s | 1604 KB | 11279455 |
| [1142_combinatorics.py](1142_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) per query | AC | 0.031 s | 436 KB | 11279454 |
| [1142_combinatorics.rs](1142_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(1) per query | AC | 0.001 s | 220 KB | 11279457 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics_optimized.java](1142_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(L²+Q) time; O(L+Q) space | AC | 0.046 s | 336 KB | 11326631 |
| [1142_combinatorics_optimized.py](1142_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(L²+I+O) time; O(L+I+O) space | AC | 0.125 s | 220 KB | 11325472 |
| [1142_combinatorics_optimized.rs](1142_combinatorics_optimized.rs) \* | Rust 1.75 x64 | combinatorics | O(L²+Q) time; O(L) space | AC | 0.001 s | 44 KB | 11325499 |
| [1142_combinatorics_optimized.go](1142_combinatorics_optimized.go) \* | Go 1.14 x64 | combinatorics | O(L²+Q) time; O(L²) space | AC | 0.015 s | 272 KB | 11325652 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
