# 1227. Una ruta de rally de longitud dada por carreteras de un solo sentido

[Timus 1227](https://acm.timus.ru/problem.aspx?space=1&num=1227) · dificultad 302 · graphs

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `M ≤ 100` ciudades y `N ≤ 10⁴` carreteras de doble sentido de
longitudes dadas. Por seguridad, cada carretera de la ruta del rally se
recorre en un solo sentido, y la ruta puede empezar y acabar en cualquier
punto de una carretera. Hay que decidir si existe una ruta de longitud
exactamente `S ≤ 2·10⁶`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`M`, `N` y `S`, y luego cada carretera como dos ciudades y una longitud.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2 20
1 2 10
2 3 5
```

Salida:

```
NO
```

### Ejemplo 2

Entrada:

```
3 3 1000
1 2 1
2 3 1
1 3 1
```

Salida:

```
YES
```

## Solución

Si las carreteras contienen un ciclo, la ruta puede darle vueltas una y
otra vez en el mismo sentido, así que cualquier longitud es posible. Un
bucle de una ciudad a sí misma, o una segunda carretera entre las mismas
dos ciudades, también es un ciclo. Una estructura de conjuntos disjuntos
detecta la primera carretera cuyos extremos ya están conectados.

Si no, las carreteras forman un bosque. Recorrer cada carretera en un
solo sentido significa que la ruta nunca puede dar la vuelta, así que
sigue un camino simple, y como puede empezar y parar a mitad de una
carretera, se alcanza cualquier longitud hasta la del camino más largo.
El camino más largo de un árbol es su diámetro: desde cualquier ciudad se
va a la más lejana, y desde allí otra vez a la más lejana. La respuesta
es `YES` exactamente cuando el diámetro de algún árbol es al menos `S`.
`O(N + M²)`, o `O(N + M log M)` en Python.

Detalles a tener en cuenta:

- una carretera de una ciudad a sí misma cuenta como ciclo;
- dos carreteras entre el mismo par de ciudades también permiten dar
  vueltas sin fin;
- el bosque puede tener varios árboles, y cada uno necesita su propio
  diámetro;
- una ruta exactamente tan larga como el diámetro está permitida.

Las respuestas se compararon con una solución escrita aparte en 200
mapas aleatorios con y sin ciclos, con `S` cerca del diámetro.

## Soluciones optimizadas

Las versiones en Go, Rust y Python siguen detectando ciclos con conjuntos disjuntos. En el bosque basta un recorrido por árbol. Cada hijo aporta su camino descendente más largo. Antes de guardar la mayor rama, se combina la nueva con la mejor ya vista en esa ciudad. Un camino que pasa por la ciudad usa dos ramas distintas o empieza en la propia ciudad, así que basta comprobar esas sumas. Python guarda el orden del recorrido y lo procesa al revés para combinar las ramas de los hijos antes que las de sus padres. Go guarda las listas de adyacencia en un solo vector con índices de vértice y de arista de un byte. El recorrido es lineal en el tamaño del bosque.

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 212 KB frente a 464 KB.

Las implementaciones base aceptadas [1227_graphs.cpp](1227_graphs.cpp), [1227_graphs.java](1227_graphs.java) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes usan conjuntos disjuntos con compresión de caminos
  a la mitad y una pila explícita para las distancias.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1227_graphs.cpp](1227_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M²) | AC | 0.015 s | 204 KB | 11283720 |
| [1227_graphs.go](1227_graphs.go) | Go 1.14 x64 | graphs | O(N + M²) | AC | 0.031 s | 1268 KB | 11283721 |
| [1227_graphs.java](1227_graphs.java) | Java 1.8 | graphs | O(N + M²) | AC | 0.093 s | 800 KB | 11283729 |
| [1227_graphs.py](1227_graphs.py) | Python 3.12 x64 | graphs | O(N + M log M) | AC | 0.078 s | 2608 KB | 11283726 |
| [1227_graphs.rs](1227_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M²) | AC | 0.015 s | 464 KB | 11283730 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1227_dsu_dp.go](1227_dsu_dp.go) \* | Go 1.14 x64 | dsu, dp | O(N + M²) | AC | 0.015 s | 792 KB | 11310847 |
| [1227_dsu_dp.rs](1227_dsu_dp.rs) \* | Rust 1.75 x64 | dsu, dp | O(N + M²) | AC | 0.031 s | 212 KB | 11310397 |
| [1227_dsu_dp.py](1227_dsu_dp.py) \* | Python 3.12 x64 | dsu, dp | O(N + M²) | AC | 0.078 s | 720 KB | 11310339 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
