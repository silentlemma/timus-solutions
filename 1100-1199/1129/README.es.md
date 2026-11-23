# 1129. Pintar puertas verdes por un lado y naranjas por el otro para que cada sala quede equilibrada

[Timus 1129](https://acm.timus.ru/problem.aspx?space=1&num=1129) · dificultad 378 · graphs

Problema original de Magaz Asanov, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un edificio tiene `N ≤ 100` salas unidas por puertas; dos salas pueden
compartir varias puertas. Cada puerta se pinta de verde por un lado y de
naranja por el otro. Pinta las puertas de modo que en cada sala el número
de caras verdes y naranjas difiera como mucho en uno. Imprime
`Impossible` si no se puede.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas: el número de puertas de una sala y luego los
números de las salas a las que llevan, en orden creciente.

## Salida

`N` líneas: los colores de las puertas de cada sala en el orden de la
entrada, `G` para verde e `Y` para naranja, o la palabra `Impossible`.

## Evaluación

Se acepta cualquier coloreado válido. El comprobador verifica que cada
sala recibe un color por cada puerta listada, que cada sala está
equilibrada con diferencia de como mucho uno y que, para cada par de
salas, las puertas entre ellas son verdes exactamente por un lado. Las
puertas entre las mismas dos salas son indistinguibles, así que cuenta las
marcas verdes por par en vez de emparejar puertas sueltas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
3 2 3 4
3 1 3 5
4 1 2 4 5
3 1 3 5
3 2 3 4
```

Salida:

```
G Y G
Y G Y
G Y Y G
Y G G
G Y Y
```

## Solución

Las salas son vértices y las puertas, aristas. El código sustituye cada
par de puertas paralelas por un bucle en cada sala. Pintar una puerta de verde
en la sala `u` y de naranja en la sala `v` es lo mismo que orientar la
arista de `u` a `v`, así que se pide una orientación en la que cada
vértice tenga grados de salida y de entrada que difieran como mucho en
uno. Esa orientación siempre existe. Se añade un vértice ficticio unido
por una arista extra a cada vértice de grado impar; de esos hay un número
par, así que ahora todos los grados son pares. Cada parte conexa tiene
entonces un circuito euleriano, y al recorrerlo se sale de cada vértice
tantas veces como se entra. Se orienta cada arista en el sentido del
recorrido y se quitan las aristas extra: un vértice pierde como mucho una
arista, así que sus dos cuentas difieren como mucho en uno. Para `D` puertas,
`O(N + D)` esperado con mapas hash, `O(N + D log D)` con el mapa ordenado de C++.

Detalles a tener en cuenta:

- `Impossible` nunca es la respuesta;
- una puerta aparece en las filas de sus dos salas; las menciones de cada
  par de salas se emparejan consecutivamente en orden de lectura. Las
  puertas entre las mismas salas son intercambiables;
- el circuito se recorre con una pila explícita y un puntero a la
  siguiente arista sin usar de cada vértice, así que cada arista se mira un
  número constante de veces;
- una sala sin puertas imprime una línea vacía.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
edificios aleatorios con muchas puertas repetidas entre las mismas salas.

## Soluciones optimizadas

`1129_graphs_optimized.py`. Conserva la cancelación exacta de pares de puertas paralelas opuestas y orientación Euler tras conectar habitaciones impares a una ficticia. Los vecinos ordenados permiten contar rachas con itertools.groupby nativo. Python usa bitsets enteros, elimina la arista menor por XOR y expande colores según multiplicidades; pares hacia la misma habitación quedan equilibrados. No usa huellas de respuestas. N habitaciones, D menciones, B=ceil(N/w) miembros enteros: O(D+N²B) trabajo, O(N²+grado máximo de fila) espacio con entrada/salida por fila. N<=100 limita los bitsets a pocos miembros; conserva bases. Aquí w es el número de bits por miembro de un entero grande Python.

Accepted exacto CPython 3.12 #11327005: 0.078 s / 752 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 1/83, memoria 1/83. Por debajo de 1024 KB, admisión estricta solo por tiempo.

- `1129_graphs_optimized.py`: 0.078 s / 752 KB; base didáctica conservada `1129_graphs.py` (Python 3.12 x64): 0.078 s / 2560 KB; cambio de tiempo +0.0%; cambio de memoria -70.6%.

`1129_graphs_optimized.java`. Conserva orientación por recorrido de Euler tras unir virtualmente salas impares a una ficticia. Aplana D menciones de lados con offsets, posiciones originales y parejas. Ordena claves long (par no ordenado de salas,posición): puertas paralelas emparejan mitades de extremos por posición y bucles se emparejan consecutivamente. N<=100 mantiene el par bajo10000, separado de los32 bits bajos de posición. Aristas reales reciben G/Y opuestos; virtuales solo equilibran y no se imprimen. Pila primitiva y colores byte reemplazan adyacencia con objetos, colas hash y salida completa. Espacio O(N+D). Si S(D) es el coste de ordenar, lo demás es O(N+D); Java8 suele costar O(D log D), con cota conservadora O(D²) para el peor caso, sin prometer logaritmo estricto.

Frente a `1129_graphs.java`: tiempo 0.156 s → 0.109 s; memoria 3876 KB → 832 KB.

C++ y Python cuentan las puertas de cada par de habitaciones. Las orientaciones opuestas de dos puertas paralelas se cancelan en ambas habitaciones, así que queda como máximo una arista real por par. Tras añadir las aristas auxiliares, todos los grados son pares. Se siguen aristas libres hasta cerrar cada recorrido y se orientan en el sentido recorrido. C++ recorre la matriz con cursores monótonos; Python recorre los bitsets enteros residuales indicados arriba. Ambos expanden multiplicidades originales en el orden de entrada.

Las bases Accepted conservadas [1129_graphs.go](1129_graphs.go), [1129_graphs.rs](1129_graphs.rs) pasan también diez primeros o 15% superior en las métricas exigidas de la comparación guardada. Se reutilizan sin duplicados; conserva las demás bases. El asterisco indica la meta propia del lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1129_graphs_parsing_optimized.rs`. Se liberan las colas temporales antes de recorrer el grafo construido y los dos colores se guardan como bytes. Se mantienen las actualizaciones voraces y la partición. Se leen tokens con un búfer nativo acotado; los cortos se guardan dentro del objeto y solo los largos reservan espacio extra. La conversión decimal conserva las cotas con signo sin guardar toda la entrada de comandos. Esta alternativa conserva el inicio y cierre habituales de Rust con el mismo estado compacto.

Accepted #11329034 (Rust 1.75 x64): **0.015 s / 884 KB**. Comparación archivada: `1129_graphs.rs` (Rust 1.75 x64) — 0.015 s / 1172 KB (#11279366).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1129_graphs_optimized.java`: puesto de tiempo 1/23 y de memoria 1/23 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1129_graphs.cpp](1129_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + D log D) | AC | 0.015 s | 2096 KB | 11279361 |
| [1129_graphs.go](1129_graphs.go) | Go 1.14 x64 | graphs | O(N + D) expected | AC | 0.015 s | 2424 KB | 11279362 |
| [1129_graphs.java](1129_graphs.java) | Java 1.8 | graphs | O(N + D) expected | AC | 0.156 s | 3876 KB | 11279365 |
| [1129_graphs.py](1129_graphs.py) | Python 3.12 x64 | graphs | O(N + D) expected | AC | 0.078 s | 2560 KB | 11328266 |
| [1129_graphs.rs](1129_graphs.rs) | Rust 1.75 x64 | graphs | O(N + D) expected | AC | 0.015 s | 1172 KB | 11279366 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1129_graphs_optimized.cpp](1129_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(N² + D) | AC | 0.015 s | 160 KB | 11310449 |
| [1129_graphs_optimized.py](1129_graphs_optimized.py) | Python 3.12 x64 | graphs | O(D+N² ceil(N/w)) time; O(N²+max row degree) space | AC | 0.078 s | 752 KB | 11327005 |
| [1129_graphs_optimized.java](1129_graphs_optimized.java) | Java 1.8 | graphs | O(N+D+S(D)) | AC | 0.109 s | 832 KB | 11325013 |
| [1129_graphs_parsing_optimized.rs](1129_graphs_parsing_optimized.rs) | Rust 1.75 x64 | graphs, parsing | O(N + D) expected | AC | 0.015 s | 884 KB | 11329034 |
