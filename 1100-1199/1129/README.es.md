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

C++ y Python cuentan las puertas de cada par de habitaciones. Las orientaciones opuestas de dos puertas paralelas se cancelan en ambas habitaciones, así que queda como máximo una arista real por par. Tras añadir las aristas auxiliares, todos los grados son pares. Se siguen aristas libres hasta cerrar cada recorrido y se orientan en el sentido recorrido. Los cursores recorren una vez la matriz y los recuentos originales reconstruyen la salida en orden de entrada.

Las implementaciones base aceptadas [1129_graphs.go](1129_graphs.go), [1129_graphs.java](1129_graphs.java), [1129_graphs.rs](1129_graphs.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes hacen el mismo recorrido con pila explícita.
- Python empareja las menciones con listas indexadas por el par de salas;
  cada lista contiene como mucho un índice, así que las operaciones de cola
  tardan `O(1)`.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1129_graphs.cpp](1129_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + D log D) | AC | 0.015 s | 2096 KB | 11279361 |
| [1129_graphs.go](1129_graphs.go) \* | Go 1.14 x64 | graphs | O(N + D) expected | AC | 0.015 s | 2424 KB | 11279362 |
| [1129_graphs.java](1129_graphs.java) \* | Java 1.8 | graphs | O(N + D) expected | AC | 0.156 s | 3876 KB | 11279365 |
| [1129_graphs.py](1129_graphs.py) | Python 3.12 x64 | graphs | O(N + D) expected | AC | 0.093 s | 2592 KB | 11279363 |
| [1129_graphs.rs](1129_graphs.rs) \* | Rust 1.75 x64 | graphs | O(N + D) expected | AC | 0.015 s | 1172 KB | 11279366 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1129_graphs_optimized.cpp](1129_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(N² + D) | AC | 0.015 s | 160 KB | 11310449 |
| [1129_graphs_optimized.py](1129_graphs_optimized.py) \* | Python 3.12 x64 | graphs | O(N² + D) | AC | 0.093 s | 676 KB | 11310450 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
