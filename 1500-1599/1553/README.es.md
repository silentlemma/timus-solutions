# 1553. Cuevas y túneles

[Timus 1553](https://acm.timus.ru/problem.aspx?space=1&num=1553) · dificultad 282 · trees

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 100000 cuevas forman un árbol. Cada cueva tiene un nivel de
radiación, 0 al principio. Hay que responder Q ≤ 100000 consultas:
«I U V» sube el nivel de la cueva U en V ≤ 10000, y «G U V» pregunta el
nivel más alto en el camino de U a V.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

N, los N − 1 túneles, Q y las consultas.

## Salida

La respuesta a cada consulta G, una por línea.

## Evaluación

Comparar respuestas en orden. Java pasó 106 main: 100 árboles aleatorios pequeños con BFS literal, cadena de 100000 vértices/100000 operaciones, estrella de 99999 y 4 casos del repositorio; incluir incrementos cero y valores hasta 10^9.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 2
2 3
2 4
6
I 1 1
G 1 1
G 3 4
I 2 3
G 1 1
G 3 4
```

Salida:

```
1
0
1
3
```

## Solución

Descomposición en caminos pesados: se enraíza el árbol en la cueva 1 y
cada cueva continúa su cadena por el hijo con el subárbol más grande.
Cualquier camino de una cueva hacia la raíz cruza como mucho ⌊log₂ N⌋ + 1
cadenas, porque al bajar por cada arista ligera el tamaño del subárbol
se reduce al menos a la mitad. Las cadenas se colocan una tras otra, de modo que cada una
ocupa posiciones consecutivas, y se mantiene un árbol de segmentos de
máximos sobre las posiciones.

Un aumento cambia una hoja y los máximos sobre ella. Una consulta de
camino sube desde el extremo cuya cabeza de cadena es más profunda,
tomando el máximo en ese tramo de la cadena, hasta que los dos extremos
comparten cadena, y termina con el tramo entre ellos. El árbol se
construye sin recursión, a partir de un orden de búsqueda en anchura,
porque un camino de 100000 cuevas desbordaría una búsqueda recursiva.
`O((N + Q) log² N)`.

Detalles a tener en cuenta:

- una consulta de una cueva a sí misma es el nivel de esa cueva
  (pruebas 01, 02, 03);
- se permiten aumentos de 0 (prueba 04);
- el nivel no supera 10⁹ (10⁵ aumentos de 10⁴) y cabe en 32 bits
  con signo; las bases compiladas conservan 64 bits, las variantes
  compactas usan 32 bits y la base Python usa enteros de Python;
- un camino puede dividirse en dos cadenas si la cueva 1 es interior:
  gen2 tiene cadenas de 52487 y 47513 cuevas, en vez de una de 100000 cuevas.

## Soluciones optimizadas

`1553_trees_optimized.go`. Conserva la descomposición heavy-light y el árbol de segmentos iterativo. Sustituye listas por vértice por arreglos planos first/to/next y guarda enlaces, orden, padres, profundidades, tamaños, cabeceras, posiciones y máximos en int32. N<=100000 acota índices; hasta 100000 incrementos de 10000 limitan cada nivel a 10^9, haciendo seguro estrechar el árbol int64. Construye orden y cadenas iterativamente, sin pila recursiva. Preparación O(N), actualización puntual O(log N), máximo de camino O(log² N), espacio O(N); bytes sustituyen Scanner.Text y strconv por token. os.Stdin.Read/os.Stdout.Write portables y conversión entera directa usan búferes fijos de entrada y salida de 4096 bytes. Se atienden escrituras parciales antes de reutilizar el búfer de salida. Se conserva la fuente sencilla original con Accepted.

Frente a `1553_trees.go`: tiempo 0.203 s → 0.062 s; memoria 19108 KB → 6132 KB.

Se conservan HLD iterativo y máximos de caminos. C++/Python compactos usan arrays planos, máximos de 32 bits y entrada/salida acotada. Hasta 100000 aumentos de 10000 dejan valores ≤10^9, dentro de 32 bits con signo. Como los incrementos no son negativos, un ancestro sin cambio permite parar la propagación.

Java reutiliza espacio al terminar su significado anterior: las cabeceras de adyacencia pasan a hijos pesados; tamaños de subárbol a posiciones; orden de recorrido a cabeceras de cadenas. Luego enumera raíces de cadena por número de vértice, sin leer el orden sobrescrito. Tras numerar cadenas, limpia las 2N celdas de destinos de aristas y las usa como árbol de segmentos. Padres y profundidades siguen intactos. Elimina tres asignaciones de N celdas y el árbol separado de 2N, sin solapar usos vivos. Preparación `O(N)`, actualización `O(log N)`, consulta `O(log² N)`, memoria `O(N)`. Se conservan las bases HLD claras.

- `1553_trees_optimized.cpp`: 0.046 s / 5200 KB; base `1553_trees.cpp`: 0.390 s / 9584 KB; cambio respecto a la base: tiempo -88.2%, memoria -45.7%.
- `1553_trees_optimized.java`: 0.187 s / 6968 KB; base `1553_trees.java`: 0.203 s / 10684 KB; cambio respecto a la base: tiempo -7.9%, memoria -34.8%.
- `1553_trees_optimized.py`: 1.703 s / 5432 KB; base `1553_trees.py`: 2.140 s / 60768 KB; cambio respecto a la base: tiempo -20.4%, memoria -91.1%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1553_trees_optimized.go`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1553_trees.cpp](1553_trees.cpp) | G++ 13.2 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.390 s | 9584 KB | 11287607 |
| [1553_trees.go](1553_trees.go) | Go 1.14 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.203 s | 19108 KB | 11287610 |
| [1553_trees.java](1553_trees.java) | Java 1.8 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.203 s | 10684 KB | 11287615 |
| [1553_trees.py](1553_trees.py) | Python 3.12 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 2.140 s | 60768 KB | 11287612 |
| [1553_trees.rs](1553_trees.rs) | Rust 1.75 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.140 s | 19664 KB | 11287616 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1553_trees_optimized.cpp](1553_trees_optimized.cpp) | G++ 13.2 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.046 s | 5200 KB | 11309316 |
| [1553_trees_optimized.java](1553_trees_optimized.java) \* | Java 1.8 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.187 s | 6968 KB | 11309559 |
| [1553_trees_optimized.py](1553_trees_optimized.py) \* | Python 3.12 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 1.703 s | 5432 KB | 11309314 |
| [1553_trees_optimized.go](1553_trees_optimized.go) \* | Go 1.14 x64 | trees | O(N) prep; O(log N) update; O(log² N) query | AC | 0.062 s | 6132 KB | 11328277 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
