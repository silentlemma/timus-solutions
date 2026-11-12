# 1358. Cables

[Timus 1358](https://acm.timus.ru/problem.aspx?space=1&num=1358) · dificultad 540 · graphs

Problema original de Den Raskovalov (enunciado de Aleksandr Bikbaev), del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 1000 ordenadores están unidos por N − 1 cables en una red conexa,
es decir, un árbol. Hay que colocar los ordenadores como puntos del
plano, con coordenadas de valor absoluto a lo sumo 1000, de modo que los
cables, dibujados como segmentos rectos, no se crucen, y que cada dos
ordenadores estén a distancia mayor que 1.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N − 1 líneas con los extremos a, b de cada cable.

## Salida

N líneas con las coordenadas de los ordenadores 1 a N. Se acepta
cualquier colocación válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2
2 3
```

Salida:

```
0 0
10 0
0 10
```

## Solución

Se enraíza el árbol en el ordenador 1 y se recorre en profundidad. Cada
ordenador va a la columna que indica su lugar en ese recorrido,
x = 2 · índice − 999, y a la fila que indica su profundidad,
y = profundidad. Cada ordenador tiene su propia columna, a dos unidades
de la siguiente, así que todas las distancias son al menos 2, y todas
las coordenadas quedan en [−999, 999].

Los cables nunca se cruzan. Cada cable une un ordenador de una fila con
un hijo en la fila siguiente, así que dos cables solo pueden cruzarse
si están en la misma franja entre dos filas. El recorrido en
profundidad visita cada subárbol como un bloque de columnas
consecutivas, y los ordenadores de una misma fila tienen subárboles
disjuntos; por eso los cables que salen de dos ordenadores distintos de
una fila quedan en dos rangos de columnas disjuntos, y los que salen del
mismo ordenador solo comparten ese extremo. `O(N)`.

Detalles a tener en cuenta:

- un camino de 1000 ordenadores con raíz en un extremo alcanza una
  profundidad de 999 y cabe en los límites (prueba generada 8);
- con N = 1 no hay ningún cable (prueba 02);
- el recorrido debe ser iterativo o tener pila suficiente para una
  profundidad de 999.

Las pruebas se juzgan con un verificador que comprueba los límites, cada
par de puntos y cada par de cables, incluidos los cables que comparten
un extremo y se solapan.

La versión didáctica en C++ asigna el punto al entrar en el vértice con un DFS recursivo. La columna empieza en −999 y avanza dos unidades en cada entrada. La fila es la profundidad que recibe la llamada. Se visita a cada vecino salvo al padre. Como la entrada es un árbol, se visita cada vértice una vez y cada subárbol ocupa columnas consecutivas. El tiempo y el espacio son O(N), con a lo sumo N llamadas en la pila.

## Soluciones optimizadas

Go/Rust mantienen x=2·preorden−999, y=profundidad. Columnas distintas separadas por 2 garantizan una distancia mayor que 1. N ≤ 1000 da x∈[−999,999], y∈[0,999]. Cada arista queda entre dos niveles consecutivos y dentro del intervalo de columnas del subárbol del padre. Los padres de un mismo nivel tienen intervalos disjuntos. Las aristas de un padre llegan a puntos distintos de la siguiente fila y solo se tocan en el padre. Las nuevas versiones usan arreglos planos de 16 bits para las listas de adyacencia, el preorden, la profundidad y la pila. Los índices de arista llegan hasta 1998, y los vértices y la profundidad más uno, hasta 1000. Una profundidad de cero marca un vértice pendiente de visitar. Insertar al frente y luego LIFO conserva el orden de los hijos. Ambos usan arreglos fijos para 1000 vértices. Go lee y escribe con búferes fijos de 256 bytes y descriptores estándar. Rust usa entrada y salida de caracteres y un punto de entrada de C. Tiempo y espacio O(N). Se conservan bases; C++/Java/Python reutilizan admitidas.

Las implementaciones base aceptadas [1358_graphs.cpp](1358_graphs.cpp), [1358_graphs.java](1358_graphs.java), [1358_graphs.py](1358_graphs.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes visitan los hijos en el orden de entrada y dan la
  misma colocación; el verificador también acepta otras respuestas válidas.
- Java guarda las listas de adyacencia en arreglos planos para caber en
  el corto límite de tiempo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1358_graphs.cpp](1358_graphs.cpp) | G++ 13.2 x64 | graphs | O(N) | AC | 0.015 s | 260 KB | 11285300 |
| [1358_graphs.go](1358_graphs.go) | Go 1.14 x64 | graphs | O(N) | AC | 0.031 s | 1208 KB | 11285313 |
| [1358_graphs.java](1358_graphs.java) | Java 1.8 | graphs | O(N) | AC | 0.140 s | 624 KB | 11285343 |
| [1358_graphs.py](1358_graphs.py) \* | Python 3.12 x64 | graphs | O(N) | AC | 0.093 s | 820 KB | 11285322 |
| [1358_graphs.rs](1358_graphs.rs) | Rust 1.75 x64 | graphs | O(N) | AC | 0.046 s | 308 KB | 11285353 |
| [1358_dfs.cpp](1358_dfs.cpp) | G++ 13.2 x64 | dfs | O(N) | AC | 0.015 s | 564 KB | 11315912 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1358_graphs_optimized.rs](1358_graphs_optimized.rs) \* | Rust 1.75 x64 | graphs | O(N) | AC | 0.015 s | 56 KB | 11315908 |
| [1358_graphs_optimized.go](1358_graphs_optimized.go) \* | Go 1.14 x64 | graphs | O(N) | AC | 0.015 s | 324 KB | 11315964 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
