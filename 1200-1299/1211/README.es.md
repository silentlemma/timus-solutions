# 1211. Acusaciones sin círculo y con una sola confesión

[Timus 1211](https://acm.timus.ru/problem.aspx?space=1&num=1211) · dificultad 311 · graphs

Problema original de Leonid Volkov, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los `N ≤ 25000` niños o confiesa haber roto la taza (anotado
como 0) o señala a un niño como culpable. Las declaraciones parecen
coherentes si confesó exactamente un niño y ningún grupo de niños se
acusa en círculo. Hay que responder `YES` o `NO` para cada una de hasta
16 pruebas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

La primera línea contiene el entero `1 ≤ T ≤ 16`. Cada prueba ocupa dos líneas: entero `1 ≤ N ≤ 25000`, seguido de N enteros `0 ≤ a_i ≤ N`. La posición i corresponde al niño i: 0 significa confesión; un valor positivo nombra a ese niño con índice desde 1, incluido posiblemente el propio i.

## Salida

`YES` o `NO` para cada prueba, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1
0
1
1
5
3 3 0 2 4
6
2 3 2 0 4 5
4
0 0 2 3
```

Salida:

```
YES
NO
YES
NO
NO
```

## Solución

Cada niño, salvo quien confiesa, señala exactamente a uno, así que las
declaraciones forman un grafo en el que de cada vértice sale como mucho
una arista. Con exactamente una confesión, no hay círculo justo cuando,
siguiendo las acusaciones desde cualquier niño, siempre se llega a quien
confesó.

Se camina desde cada niño por turno, marcando los niños del camino
actual. El camino se detiene en quien confesó o en un niño del que ya se
sabe que lleva allí; entonces cada niño del camino también lleva allí. Si
en cambio choca con un niño marcado en el camino actual, las acusaciones
forman un círculo. Cada niño se recorre una vez. `O(N)` por prueba.

Detalles a tener en cuenta:

- un niño que se señala a sí mismo es un círculo de uno;
- ninguna confesión, o dos, ya significa `NO`;
- las cadenas pueden tener 25000 niños, así que el recorrido es un bucle
  y no una recursión.

Las respuestas se compararon con una solución escrita aparte en 200
archivos de 16 pruebas aleatorias de todos los tipos.

El recorrido de cadenas usa `O(N)` espacio de trabajo por prueba para acusaciones, estados y camino actual. Para las T pruebas, tiempo `O(Σ N_i)`. Sean I los bytes de toda la entrada y H la línea más larga. Python sencillo retiene todos los tokens separados y Rust su String completo: espacio `O(I + max N_i + T)`. C++ y Go leen flujos con búferes acotados y `O(max N_i)` espacio del grafo. Java también conserva la línea actual y T palabras de salida: `O(max N_i + H + T)` más búferes de biblioteca. Rust optimizado guarda búfer/token acotados, acusaciones, estados, camino y T palabras: `O(max N_i + T + B)`, con B fijo. DSU procesa acusaciones al leerlas, en tiempo amortizado `O(N α(N))` por prueba; sus arrays estáticos reales de 25001 enteros con signo de 16 bits y búferes usan `O(M + B)` con M=25000, incluso en pruebas pequeñas. Índices hasta 25000 y tamaños negativos hasta −25000 caben en 16 bits con signo.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

C++ y Go procesan las acusaciones al leerlas mediante conjuntos disjuntos. Una acusación entre vértices ya conectados cierra un ciclo no dirigido. Cada vértice del ciclo puede emitir como máximo una acusación, así que cada uno aporta exactamente una arista y el ciclo resulta dirigido. Esto incluye la autoacusación y la acusación mutua. Se exige una sola confesión y ningún ciclo. Cada entrada con signo de 16 bits guarda un índice de padre o el tamaño negativo de la componente.

La caché de fuentes exactos aplica los [criterios compartidos](../../RATING_CRITERIA.md). Java y Python sencillos ya cumplen y se reutilizan sin copias. Ambos Go cumplen mediante el grupo del mismo lenguaje, pues no tienen rivales de compilador exacto. La cobertura rápida C++ es `1211_dsu.cpp`; Rust, `1211_graphs_implementation_optimized.rs` (#11328956, 0.031 s / 580 KB). Rust sencillo #11283644 con 0.031 s / 5212 KB falla la memoria exigida y C++ sencillo falla tiempo; ambos quedan didácticos sin estrella. Bajo 1024 KB solo se compara tiempo; los Go/Java/Python que cumplen por encima exigen ambas métricas. No hay meta separada de primer puesto.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1211_graphs_implementation_optimized.rs`. Se leen tokens con un búfer nativo acotado; los cortos se guardan dentro del objeto y solo los largos reservan espacio extra. La conversión decimal conserva las cotas con signo sin guardar toda la entrada de comandos. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328956 (Rust 1.75 x64): **0.031 s / 580 KB**. Comparación archivada: `1211_graphs.rs` (Rust 1.75 x64) — 0.031 s / 5212 KB (#11283644).

La fila Accepted #11328956 y su admisión anterior corresponden al fuente histórico exacto. Esta revisión solo nombra la capacidad existente de 32 bytes como `INLINE_TOKEN_BYTES`; sustituir 32 reproduce exactamente los bytes previos. Se conservan comentarios y Rust sencillo.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes recorren las cadenas de forma iterativa con los
  mismos tres estados.

## Evaluación

`tests/tests.json` usa `tokens`: compara exactamente T tokens YES/NO en orden de prueba, ignorando espacios y saltos de línea. Habitualmente se imprime un resultado por línea. El ejemplo propio incluye una confesión individual, un ciclo propio, caminos fusionados a una confesión, un ciclo separado y dos confesiones. Los demás casos cubren cadenas largas, ciclos tardíos, máximos y reinicio de estados.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1211_graphs.cpp](1211_graphs.cpp) | G++ 13.2 x64 | graphs | O(N) per test | AC | 0.265 s | 592 KB | 11283637 |
| [1211_graphs.go](1211_graphs.go) | Go 1.14 x64 | graphs | O(N) per test | AC | 0.218 s | 6820 KB | 11283638 |
| [1211_graphs.java](1211_graphs.java) | Java 1.8 | graphs | O(N) per test | AC | 0.156 s | 5760 KB | 11283643 |
| [1211_graphs.py](1211_graphs.py) | Python 3.12 x64 | graphs | O(N) per test | AC | 0.343 s | 26364 KB | 11283642 |
| [1211_graphs.rs](1211_graphs.rs) | Rust 1.75 x64 | graphs | O(N) per test | AC | 0.031 s | 5212 KB | 11283644 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1211_dsu.cpp](1211_dsu.cpp) | G++ 13.2 x64 | dsu | O(N α(N)) per test | AC | 0.015 s | 136 KB | 11310412 |
| [1211_dsu.go](1211_dsu.go) | Go 1.14 x64 | dsu | O(N α(N)) per test | AC | 0.046 s | 3228 KB | 11310413 |
| [1211_graphs_implementation_optimized.rs](1211_graphs_implementation_optimized.rs) | Rust 1.75 x64 | graphs, implementation | O(N) per test | AC | 0.031 s | 592 KB | 11331113 |
