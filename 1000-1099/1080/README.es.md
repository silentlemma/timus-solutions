# 1080. Colorear un mapa con dos colores

[Timus 1080](https://acm.timus.ru/problem.aspx?space=1&num=1080) · dificultad 186 · bfs, graphs, dsu

Problema original de Emil Kelevedzhiev, del Torneo de Informática del Festival Matemático de Invierno, Varna 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mapa tiene `N` países (`0 < N < 99`); desde cualquier país se llega a
cualquier otro cruzando fronteras. Colorea los países de rojo (0) y azul
(1) de modo que los vecinos siempre difieran, con el país 1 en rojo.
Imprime los colores como una cadena de cifras, o `-1` si no se puede.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas: la línea `i` lista los vecinos del país `i` con
números mayores y termina en 0.

## Salida

La cadena de colores, o `-1`.

## Evaluación

El candidato Python congelado exacto se volvió a comparar con BFS
independiente en todos los 27.476 grafos simples conexos etiquetados
de hasta seis vértices, más 701 grafos conexos aleatorios o máximos,
incluidos ciclos impares y el bipartito completo de 98 vértices.
El oráculo fija el país 1 a 0 y compara la coloración única o `-1`.
La exhaustividad de grafos pequeños no implica probar todos los mapas
de 98 vértices. Los cuatro candidatos DSU reales pasaron además 11 entradas
del repositorio cada uno en Docker y tienen sus propios Accepted de
fuente exacta. Los 28.177 casos del oráculo fueron ejecuciones Python,
no 28.177 ejecuciones de cada lenguaje compilado.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 0
3 0
0
```

Salida:

```
010
```

## Solución

Una coloración válida es una bipartición del grafo no dirigido de
fronteras. Aunque la entrada solo lista cada frontera en su extremo
menor, se guarda en ambos sentidos. BFS parte del país 1 con color 0
y asigna a cada nuevo vecino el color opuesto. Una frontera en conflicto
prueba imposibilidad: los dos caminos BFS y esa frontera forman un paseo
cerrado impar, que contiene un ciclo impar. Sin conflictos, cada frontera
une colores distintos. La conectividad alcanza todos los países y el
primer color fijo determina una única coloración.

Las versiones BFS legibles usan tiempo y espacio `O(N + E)`, incluidas
listas de adyacencia y cola; `E` es el número de fronteras. Se conservan
sin cambios las cinco bases Accepted originales. Imprimimos dígitos sin
separadores o `-1` al detectar conflicto. Una fila con solo `0` no añade
fronteras de entrada; `N = 1` también es válido.

## Soluciones optimizadas

El BFS compacto conserva colores opuestos en los extremos de cada arista, con cola y colores acotados. La alternativa Go usa conjuntos disjuntos con paridad: cada arista exige paridades distintas. La compresión mantiene la paridad hasta el representante y una contradicción detecta un ciclo impar. Se normaliza el componente del primer país para fijar su color. Las aristas se procesan sin guardar la lista de adyacencia.

- `1080_dsu.cpp`: 0.015 s / 104 KB; base `1080_bfs.cpp`: 0.001 s / 284 KB; cambio respecto a la base: tiempo -0.0%, memoria -63.4%.
- `1080_dsu.java`: 0.078 s / 348 KB; base `1080_bfs.java`: 0.125 s / 5556 KB; cambio respecto a la base: tiempo -37.6%, memoria -93.7%.
- `1080_dsu.py`: 0.093 s / 524 KB; base `1080_bfs.py`: 0.078 s / 816 KB; cambio respecto a la base: tiempo +19.2%, memoria -35.8%.
- `1080_dsu.rs`: 0.046 s / 200 KB; base `1080_bfs.rs`: 0.031 s / 296 KB; cambio respecto a la base: tiempo +48.4%, memoria -32.4%.
- `1080_dsu.go`: 0.031 s / 780 KB; base `1080_bfs.go`: 0.031 s / 1364 KB; cambio respecto a la base: tiempo -0.0%, memoria -42.8%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1080_bfs.cpp`; versión que cubre `1080_dsu.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 542/541.

- Go: base didáctica preferida `1080_bfs.go`; versión que cubre `1080_dsu.go`; puestos tiempo/memoria 3/1, registros de otros autores 6/6.

- Java: base didáctica preferida `1080_bfs.java`; versión que cubre `1080_dsu.java`; puestos tiempo/memoria 1/1, registros de otros autores 128/128.

- Python/PyPy: base didáctica preferida `1080_bfs.py`; versión que cubre `1080_dsu.py`; puestos tiempo/memoria 69/9, registros de otros autores 113/113.

- Rust: base didáctica preferida `1080_bfs.rs`; versión que cubre `1080_dsu.rs`; puestos tiempo/memoria 2/1, registros de otros autores 1/1.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1080_bfs.cpp](1080_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M) | AC | 0.001 s | 284 KB | 11279001 |
| [1080_bfs.go](1080_bfs.go) | Go 1.14 x64 | bfs | O(N + M) | AC | 0.031 s | 1364 KB | 11279002 |
| [1080_bfs.java](1080_bfs.java) | Java 1.8 | bfs | O(N + M) | AC | 0.125 s | 5556 KB | 11279004 |
| [1080_bfs.py](1080_bfs.py) | Python 3.12 x64 | bfs | O(N + M) | AC | 0.078 s | 816 KB | 11279003 |
| [1080_bfs.rs](1080_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M) | AC | 0.031 s | 296 KB | 11279005 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1080_dsu.cpp](1080_dsu.cpp) | G++ 13.2 x64 | dsu | O((N+M) alpha(N)) | AC | 0.015 s | 104 KB | 11308353 |
| [1080_dsu.java](1080_dsu.java) | Java 1.8 | dsu | O((N+M) alpha(N)) | AC | 0.078 s | 348 KB | 11308358 |
| [1080_dsu.py](1080_dsu.py) \* | Python 3.12 x64 | dsu | O((N+M) alpha(N)) | AC | 0.093 s | 524 KB | 11308342 |
| [1080_dsu.rs](1080_dsu.rs) \* | Rust 1.75 x64 | dsu | O((N+M) alpha(N)) | AC | 0.046 s | 200 KB | 11308363 |
| [1080_dsu.go](1080_dsu.go) \* | Go 1.14 x64 | dsu | O((N+M) alpha(N)) | AC | 0.031 s | 780 KB | 11309360 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
