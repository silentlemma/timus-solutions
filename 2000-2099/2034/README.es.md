# 2034. El mayor cuello de botella entre rutas mínimas

[Timus 2034](https://acm.timus.ru/problem.aspx?space=1&num=2034) · dificultad 283 · bfs, dp

Problema original de Oleg Merkurev, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple no dirigido y conexo tiene aristas de longitud uno y
tres vértices distintos `s,f,r`. Solo puede elegirse un camino mínimo de
`s` a `f`. Su puntuación es la menor distancia desde `r` a cualquier
vértice del camino, incluidos ambos extremos. Maximiza esa puntuación
entre todos los caminos mínimos. Las distancias desde `r` usan todo el
grafo; un rodeo más largo no es admisible.

Límites: `3 ≤ n ≤ 100000`, `2 ≤ m ≤ 100000`, sin bucles ni aristas repetidas,
grafo conexo; 1 segundo, 64 MB.

## Entrada

Primero `n m`, luego `m` parejas de extremos en `1..n`.
La última línea es `s f r`, todos diferentes.

## Salida

Un entero: la máxima puntuación entre rutas mínimas. Cero es válido si todas
pasan por `r`. Los extremos `s` y `f` también pueden ser el vértice más cercano.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
7 7
1 2
2 4
2 5
3 4
4 6
5 6
6 7
1 7 3
```

```
2
```

## Solución

Un BFS desde `s` obtiene `ds` y el orden de visita; otro desde `r` obtiene `dr`.
Usa la transición `u→v` solo si `ds[v]=ds[u]+1`. Estas aristas forman un grafo
acíclico ordenado por capas BFS. Sea `best[v]` el mayor mínimo de `dr` entre
los caminos mínimos de `s` a `v`. Inicializa `best[s]=dr[s]` y los demás `-1`.
Recorre el orden del primer BFS y actualiza cada transición válida con
`best[v]=max(best[v],min(best[u],dr[v]))`. La respuesta es `best[f]`.

### Corrección

Todo prefijo de una ruta mínima es mínimo: reemplazar uno más largo
acortaría la ruta completa. Por ello cada arista aumenta `ds`
exactamente uno. A la inversa, un camino `s-f` de tales aristas tiene
longitud `ds[f]` y es mínimo. La base incluye el inicio. Toda ruta
mínima a `v` acaba en algún `u` de la capa anterior; su puntuación es el
mínimo de la del prefijo y `dr[v]`. Este mínimo es monótono respecto al
prefijo: basta conservar el mejor en cada `u`. El máximo sobre todos los
predecesores produce exactamente `best[v]`. El orden BFS los procesa
primero, demostrando el resultado por inducción.

También pueden procesarse vértices fuera de todas las rutas mínimas `s-f`.
Si su contribución alcanza `f` por capas crecientes, la ruta completa sigue
teniendo longitud `ds[f]` y es válida; si no, no puede afectar la respuesta.

En el ejemplo, `1-2-4-6-7` tiene distancia mínima uno desde el vértice 3,
alcanzada en 4. La ruta `1-2-5-6-7` tiene mínimo dos en 2 o 6.
El máximo de las dos puntuaciones es dos.

Dos BFS y un recorrido de aristas cuestan `O(n+m)`. Adyacencia, distancias,
orden y programación dinámica ocupan `O(n+m)` memoria.

Trampas:

- Toma primero el mínimo por vértices de cada ruta y después el máximo
  por rutas.
- Avanza exactamente una capa BFS por transición.
- Usa distancias desde `r` en todo el grafo e incluye `s` y `f`.
- Cero es válido si `r` es inevitable en las rutas mínimas.
- Un rodeo seguro pero más largo queda excluido.

## Soluciones optimizadas

`2034_bfs_dp_optimized.rs`. Conserva dos BFS y DP max–min solo por aristas que avanzan una capa de camino mínimo. Aristas planas u32 sustituyen vectores anidados/extremos retenidos, reutiliza un orden BFS y salida directa. Distancias de grafo conectado caben u32,MAX para no alcanzado. O(N+M) tiempo/espacio; conserva explicación sencilla.

Frente a `2034_bfs_dp.rs`: tiempo 0.078 s → 0.062 s; memoria 13112 KB → 3 448 KB.

`2034_bfs_dp_optimized.go`. Conserva dos BFS y la DP de cuello de botella por aristas que aumentan en uno la distancia desde s. En orden BFS, best[v] maximiza la mínima distancia desde r entre caminos mínimos s-v; propaga min(best[v],clearance[u]) y maximiza en u. Construye al leer arreglos planos int32 first/to/next, sin lista separada de pares ni listas anidadas de int nativo. Distancias, colas y DP usan int32, seguro con n,m<=100000; ambas BFS aún asignan sus propios arreglos. El grafo conexo define todas las distancias necesarias. Tiempo y espacio O(n+m). os.Stdin.Read/os.Stdout.Write portables y conversión entera directa usan búferes fijos de entrada y salida de 4096 bytes. Se atienden escrituras parciales antes de reutilizar el búfer de salida. Se conserva la fuente sencilla original con Accepted.

Frente a `2034_bfs_dp.go`: tiempo 0.109 s → 0.031 s; memoria 11080 KB → 5244 KB.

Tras obtener distancias desde el primer origen, el segundo BFS se fusiona con la DP de cuello de botella por capas de caminos mínimos. FIFO garantiza que al extraer un vértice sus capas predecesoras estén completas y su valor sea definitivo. Se para al extraer el destino, no al descubrirlo. Adyacencia plana, cola reutilizada y distancias compactas conservan el mismo algoritmo lineal.

- `2034_bfs_dp_optimized.cpp`: 0.031 s / 3228 KB; base `2034_bfs_dp.cpp`: 0.078 s / 6892 KB; cambio respecto a la base: tiempo -60.3%, memoria -53.2%.
- `2034_bfs_dp_optimized.py`: 0.468 s / 4072 KB; base `2034_bfs_dp.py`: 0.515 s / 28236 KB; cambio respecto a la base: tiempo -9.1%, memoria -85.6%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2034_bfs_dp_optimized.go`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2034_bfs_dp.cpp](2034_bfs_dp.cpp) | G++ 13.2 x64 | bfs, dp | O(n+m) | AC | 0.078 s | 6892 KB | 11293137 |
| [2034_bfs_dp.go](2034_bfs_dp.go) | Go 1.14 x64 | bfs, dp | O(n+m) | AC | 0.109 s | 11080 KB | 11293143 |
| [2034_bfs_dp.java](2034_bfs_dp.java) | Java 1.8 | bfs, dp | O(n+m) | AC | 0.171 s | 8272 KB | 11309217 |
| [2034_bfs_dp.py](2034_bfs_dp.py) | Python 3.12 x64 | bfs, dp | O(n+m) | AC | 0.515 s | 28236 KB | 11293145 |
| [2034_bfs_dp.rs](2034_bfs_dp.rs) | Rust 1.75 x64 | bfs, dp | O(n+m) | AC | 0.078 s | 13112 KB | 11293149 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2034_bfs_dp_optimized.cpp](2034_bfs_dp_optimized.cpp) | G++ 13.2 x64 | bfs, dp | O(N+M) | AC | 0.031 s | 3228 KB | 11309340 |
| [2034_bfs_dp_optimized.py](2034_bfs_dp_optimized.py) \* | Python 3.12 x64 | bfs, dp | O(N+M) | AC | 0.468 s | 4072 KB | 11309323 |
| [2034_bfs_dp_optimized.go](2034_bfs_dp_optimized.go) \* | Go 1.14 x64 | bfs, dp | O(n+m) | AC | 0.031 s | 5244 KB | 11328337 |
| [2034_bfs_dp_optimized.rs](2034_bfs_dp_optimized.rs) \* | Rust 1.75 x64 | bfs, dp | O(N+M) time; O(N+M) space | AC | 0.062 s | 3448 KB | 11325553 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
