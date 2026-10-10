# 1129. Pintar puertas verdes por un lado y naranjas por el otro para que cada sala quede equilibrada

[Timus 1129](https://acm.timus.ru/problem.aspx?space=1&num=1129) · dificultad 406 · graphs

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

Las salas son vértices y las puertas, aristas. Pintar una puerta de verde
en la sala `u` y de naranja en la sala `v` es lo mismo que orientar la
arista de `u` a `v`, así que se pide una orientación en la que cada
vértice tenga grados de salida y de entrada que difieran como mucho en
uno. Esa orientación siempre existe. Se añade un vértice ficticio unido
por una arista extra a cada vértice de grado impar; de esos hay un número
par, así que ahora todos los grados son pares. Cada parte conexa tiene
entonces un circuito euleriano, y al recorrerlo se sale de cada vértice
tantas veces como se entra. Se orienta cada arista en el sentido del
recorrido y se quitan las aristas extra: un vértice pierde como mucho una
arista, así que sus dos cuentas difieren como mucho en uno. `O(N + D)`
para `D` puertas, más el coste del mapa que empareja las menciones.

Detalles a tener en cuenta:

- `Impossible` nunca es la respuesta;
- una puerta aparece en las filas de sus dos salas, y hay que emparejar
  las dos menciones: la `k`-ésima mención de `v` en la sala `u` va con la
  `k`-ésima mención de `u` en la sala `v`; las puertas entre las mismas
  salas son intercambiables, así que sirve cualquier emparejamiento
  coherente;
- el circuito se recorre con una pila explícita y un puntero a la
  siguiente arista sin usar de cada vértice, así que cada arista se mira un
  número constante de veces;
- una sala sin puertas imprime una línea vacía.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
edificios aleatorios con muchas puertas repetidas entre las mismas salas.

## Notas por lenguaje

- Todos los lenguajes hacen el mismo recorrido con pila explícita.
- Python empareja las menciones con listas indexadas por el par de salas;
  con unos pocos miles de puertas, las operaciones de cola son baratas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1129_graphs.cpp](1129_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + D log D) | AC | 0.015 s | 2096 KB |
| [1129_graphs.go](1129_graphs.go) | Go 1.14 x64 | graphs | O(N + D log D) | AC | 0.015 s | 2424 KB |
| [1129_graphs.java](1129_graphs.java) | Java 1.8 | graphs | O(N + D log D) | AC | 0.156 s | 3876 KB |
| [1129_graphs.py](1129_graphs.py) | Python 3.12 x64 | graphs | O(N + D log D) | AC | 0.093 s | 2592 KB |
| [1129_graphs.rs](1129_graphs.rs) | Rust 1.75 x64 | graphs | O(N + D log D) | AC | 0.015 s | 1172 KB |
