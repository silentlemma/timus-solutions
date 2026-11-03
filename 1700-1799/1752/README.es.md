# 1752. Árbol 2

[Timus 1752](https://acm.timus.ru/problem.aspx?space=1&num=1752) · dificultad 259 · graphs

Problema original de Petr Lezhankin, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un árbol de n vértices, la distancia entre dos vértices es el número
de aristas del camino entre ellos. Para cada consulta, un vértice v y un
número d, hallar un vértice a distancia exactamente d de v.

## Entrada

n (1 ≤ n ≤ 20000) y q (1 ≤ q ≤ 50000), luego las n − 1 aristas y luego
q consultas v (1 ≤ v ≤ n) y d (0 ≤ d ≤ n).

## Salida

Para cada consulta, un vértice a distancia d de v, o 0 si no lo hay. Se
acepta cualquier vértice válido.

## Evaluación

Para cada consulta se verifica la distancia del vértice devuelto y la respuesta de imposibilidad cuando no existe.

## Ejemplos

### Ejemplo 1

Entrada:

```
9 10
1 8
1 5
1 4
2 7
2 5
3 6
5 9
6 9
5 4
8 1
4 3
2 4
9 3
1 1
5 2
3 5
6 4
7 3
```

Salida:

```
0
1
2
3
4
5
6
7
8
9
```

## Solución

Para cualquier diámetro fijo del árbol, su camino más largo, al menos
uno de sus extremos es un vértice más lejano de cada vértice v. Así que
si existe un vértice a distancia d, uno de los dos extremos, a o b, está
a distancia al menos d, y el camino de v hacia él pasa por un vértice
a distancia exactamente d.

Los extremos se hallan del modo habitual: el vértice más profundo visto
desde el vértice 1 es a, y el más profundo visto desde a es b. Al
recorrer el árbol en profundidad desde una raíz, el camino actual desde
la raíz se guarda en un arreglo por profundidad. Cuando el recorrido
llega a v a profundidad h, cada consulta aún sin responder en v con
d ≤ h se responde con el vértice a profundidad h − d de ese camino.
Tres recorridos, desde 1, desde a y desde b, responden todas las consultas
que tienen respuesta; el resto recibe 0. El tiempo y el espacio son
`O(n + q)`.

Los enteros se separan por caracteres en blanco, incluidos los tabuladores.
Las cinco versiones apilan los vecinos en orden inverso al de entrada y
conservan la primera respuesta encontrada, por lo que eligen los mismos vértices.

El programa puede imprimir vértices distintos de los del ejemplo, por
ejemplo 9 en la tercera consulta en lugar de 2; ambos están a distancia
3 del vértice 4.

Trampas:

- se deben saltar todos los caracteres en blanco antes de cada entero,
  incluido el tabulador inicial de la prueba 06; de lo contrario, una
  consulta válida puede leerse como una consulta al vértice 0;
- una consulta con d = 0 se responde con el propio v;
- un camino de 20000 vértices es demasiado profundo para la recursión en
  algunos lenguajes, así que el recorrido usa su propia pila;
- las consultas son muchas, así que se agrupan por vértice en lugar de
  hacer un recorrido para cada una.

Las respuestas coinciden con búsquedas en anchura independientes en 1200
entradas aleatorias pequeñas con distintos caracteres en blanco. Las cinco
versiones imprimen respuestas idénticas en estas entradas y en los casos
estáticos, generados y de tamaño máximo.

## Soluciones optimizadas

No cambia el algoritmo lineal del árbol con extremos del diámetro y caminos DFS. Las cotas de índices de vértices, aristas, consultas y distancias permiten almacenamiento sin signo de 16 bits, con operaciones intermedias suficientemente anchas. Se eliminan campos de consultas ya innecesarios y se reutilizan arreglos. El mismo invariante de camino elige los mismos ancestros y distancias: solo cambia la representación. La entrada y salida usan búferes acotados.

- `1752_graphs_optimized.cpp`: 0.031 s / 372 KB; base `1752_graphs.cpp`: 0.109 s / 1492 KB; cambio respecto a la base: tiempo -71.6%, memoria -75.1%.
- `1752_graphs_optimized.go`: 0.046 s / 1756 KB; base `1752_graphs.go`: 0.062 s / 6500 KB; cambio respecto a la base: tiempo -25.8%, memoria -73.0%.
- `1752_graphs_optimized.java`: 0.125 s / 1100 KB; base `1752_graphs.java`: 0.109 s / 3748 KB; cambio respecto a la base: tiempo +14.7%, memoria -70.7%.
- `1752_graphs_optimized.py`: 0.296 s / 4832 KB; base `1752_graphs.py`: 0.265 s / 21232 KB; cambio respecto a la base: tiempo +11.7%, memoria -77.2%.
- `1752_graphs_optimized.rs`: 0.031 s / 2124 KB; base `1752_graphs.rs`: 0.078 s / 4136 KB; cambio respecto a la base: tiempo -60.3%, memoria -48.6%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1752_graphs.cpp`; versión que cubre `1752_graphs_optimized.cpp`; puestos tiempo/memoria 2/1, registros de otros autores 75/75.

- Go: base didáctica preferida `1752_graphs.go`; versión que cubre `1752_graphs.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1752_graphs.java`; versión que cubre `1752_graphs.java`; puestos tiempo/memoria 1/1, registros de otros autores 5/5.

- Python/PyPy: base didáctica preferida `1752_graphs.py`; versión que cubre `1752_graphs_optimized.py`; puestos tiempo/memoria 1/1, registros de otros autores 6/6.

- Rust: base didáctica preferida `1752_graphs.rs`; versión que cubre `1752_graphs.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1752_graphs.cpp](1752_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + q) | AC | 0.109 s | 1492 KB | 11308923 |
| [1752_graphs.go](1752_graphs.go) | Go 1.14 x64 | graphs | O(n + q) | AC | 0.062 s | 6500 KB | 11298038 |
| [1752_graphs.java](1752_graphs.java) | Java 1.8 | graphs | O(n + q) | AC | 0.109 s | 3748 KB | 11308924 |
| [1752_graphs.py](1752_graphs.py) | Python 3.12 x64 | graphs | O(n + q) | AC | 0.265 s | 21232 KB | 11298042 |
| [1752_graphs.rs](1752_graphs.rs) | Rust 1.75 x64 | graphs | O(n + q) | AC | 0.078 s | 4136 KB | 11308925 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1752_graphs_optimized.cpp](1752_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(N+Q) | AC | 0.031 s | 372 KB | 11308204 |
| [1752_graphs_optimized.go](1752_graphs_optimized.go) | Go 1.14 x64 | graphs | O(N+Q) | AC | 0.046 s | 1756 KB | 11308205 |
| [1752_graphs_optimized.java](1752_graphs_optimized.java) | Java 1.8 | graphs | O(N+Q) | AC | 0.125 s | 1100 KB | 11309392 |
| [1752_graphs_optimized.py](1752_graphs_optimized.py) | Python 3.12 x64 | graphs | O(N+Q) | AC | 0.296 s | 4832 KB | 11308203 |
| [1752_graphs_optimized.rs](1752_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(N+Q) | AC | 0.031 s | 2124 KB | 11308207 |
