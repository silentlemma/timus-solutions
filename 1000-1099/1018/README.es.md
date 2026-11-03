# 1018. Conservar las ramas conexas más valiosas de un árbol binario

[Timus 1018](https://acm.timus.ru/problem.aspx?space=1&num=1018) · dificultad 281 · dp, graphs, trees

Problema original del Ural State University Internal Contest '99 #2.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un árbol tiene `N` vértices (`2 ≤ N ≤ 100`) numerados `1..N` con raíz `1`;
cada vértice tiene cero o dos hijos. Cada una de las `N - 1` aristas (ramas)
lleva entre 0 y 30 000 manzanas. Conserva exactamente `Q` ramas
(`1 ≤ Q ≤ N - 1`) de modo que sigan conectadas a la raíz —una rama quitada
se lleva todo lo que hay por encima— y el número de manzanas en las ramas
conservadas sea máximo. Imprime ese número.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `Q`, y luego `N - 1` líneas `a b c`: una rama entre los vértices `a`
y `b` (en cualquier orden) con `c` manzanas.

## Salida

El mayor número de manzanas.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `1018_dp_graphs.java` (Java 1.8): 12 pruebas del repositorio; 514 comparaciones adicionales de fuente exacta.

- `1018_dp_graphs.py` (PyPy 3.10 x64): 12 pruebas del repositorio.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 3
1 2 1
1 3 5
2 4 9
2 5 9
3 6 2
3 7 3
```

Salida:

```
19
```

### Ejemplo 2

Entrada:

```
3 1
2 1 30000
1 3 0
```

Salida:

```
30000
```

## Solución

Las ramas conservadas forman un subárbol que contiene la raíz. Se enraíza el
árbol en 1 (la entrada da las aristas en dirección arbitraria) y se calcula,
para cada vértice `v`, la tabla `best_v[k]`: el máximo de manzanas en `k`
ramas conservadas en el subárbol de `v` y conectadas a `v`.

**Mochila en árbol.** Se empieza con `best = [0]` (nada conservado). Para
cada hijo `c` de `v` con `w` manzanas en la arista `v–c`: conservar `j ≥ 1`
ramas de ese lado significa conservar la propia arista y `j - 1` ramas bajo
`c`, lo que vale `w + best_c[j - 1]`. Se combina con la tabla actual como en
una mochila:

`new[i + j] = max(new[i + j], best[i] + (j = 0 ? 0 : w + best_c[j - 1]))`.

La respuesta es `best_1[Q]`. Cortando cada tabla a `Q + 1` entradas, las
combinaciones cuestan en total `O(N · Q^2)`, como mucho unos `10^6` pasos;
con tablas del tamaño del subárbol es incluso `O(N^2)`.

Por qué se mantiene la conexión: una rama bajo `c` solo se cuenta junto con
la arista `v–c` (el caso `j ≥ 1`), así que ninguna rama conservada queda en
el aire.

Detalles a tener en cuenta:

- cada vértice del árbol de entrada debe tener cero o dos hijos, así que el
  árbol válido más pequeño tiene tres vértices; se permite conservar una sola
  rama (prueba 02);
- una arista puede venir como «hijo padre»: construye una lista de
  adyacencia no dirigida y enraízala con una DFS desde 1;
- elegir con voracidad la rama disponible más pesada falla: una rama ligera
  puede llevar a otras pesadas.

## Soluciones optimizadas

Se conserva la mochila sobre subárboles. El preorden convierte cada vértice no raíz y sus descendientes en[pos,end), con los pesos de sus aristas entrantes. Para maximizar aristas conservadas, tomar la actual avanza una posición; descartarla salta todo el subárbol. Para minimizar eliminadas, conservar cuesta cero eliminaciones, o se quita el intervalo completo con suma prefija. Saltar un ancestro salta sus descendientes: todo estado alcanzado ya conserva sus ancestros. Con K=min(Q,N-1-Q), maximizar Q conservadas o minimizar la pérdida complementaria y restarla del total. Dos transiciones por celda dan O(N(1+K)) tiempo/espacio incluida preparación; conservar todas devuelve directamente la suma. Python usa listas nativas de enteros del PyPy indicado.

- `1018_dp_graphs.java`: 0.125 s / 368 KB; base `1018_dp_trees.java`: 0.140 s / 1912 KB; cambio respecto a la base: tiempo -10.7%, memoria -80.8%.
- `1018_dp_graphs.py`: 0.125 s / 408 KB; base `1018_dp_trees.py`: 0.078 s / 596 KB; cambio respecto a la base: tiempo +60.3%, memoria -31.5%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1018_dp_trees.cpp`; fuente que cubre `1018_dp_trees.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 126/126.

- Go: base didáctica preferida `1018_dp_trees.go`; fuente que cubre `1018_dp_trees.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1018_dp_trees.java`; fuente que cubre `1018_dp_graphs.java`; puestos tiempo/memoria 4/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `1018_dp_trees.py`; fuente que cubre `1018_dp_graphs.py`; puestos tiempo/memoria 11/1, registros de otros autores 13/13.

- Rust: base didáctica preferida `1018_dp_trees.rs`; fuente que cubre `1018_dp_trees.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1018_dp_trees.cpp](1018_dp_trees.cpp) | G++ 13.2 x64 | dp, trees | O(N · Q^2) | AC | 0.015 s | 212 KB | 11278199 |
| [1018_dp_trees.go](1018_dp_trees.go) | Go 1.14 x64 | dp, trees | O(N · Q^2) | AC | 0.031 s | 1152 KB | 11278201 |
| [1018_dp_trees.java](1018_dp_trees.java) | Java 1.8 | dp, trees | O(N · Q^2) | AC | 0.140 s | 1912 KB | 11278206 |
| [1018_dp_trees.py](1018_dp_trees.py) | Python 3.12 x64 | dp, trees | O(N · Q^2) | AC | 0.078 s | 596 KB | 11278203 |
| [1018_dp_trees.rs](1018_dp_trees.rs) | Rust 1.75 x64 | dp, trees | O(N · Q^2) | AC | 0.015 s | 260 KB | 11278211 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1018_dp_graphs.java](1018_dp_graphs.java) \* | Java 1.8 | dp, graphs | O(N(1+min(Q,N-1-Q))) time and space | AC | 0.125 s | 368 KB | 11309309 |
| [1018_dp_graphs.py](1018_dp_graphs.py) \* | PyPy 3.10 x64 | dp, graphs | O(N(1+min(Q,N-1-Q))) time and space | AC | 0.125 s | 408 KB | 11309731 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
