# 1169. Una red conexa con exactamente K pares críticos de ordenadores

[Timus 1169](https://acm.timus.ru/problem.aspx?space=1&num=1169) · dificultad 725 · constructive

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que conectar `N ≤ 100` ordenadores con conexiones bidireccionales en
una sola red. Un par de ordenadores es crítico si quitar alguna conexión
los separa. Hay que construir una red con exactamente `K` pares críticos o
indicar que no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `K`.

## Salida

Las conexiones, un par de ordenadores por línea, o `-1`.

## Evaluación

Se acepta cualquier red cuyas conexiones sean distintas, unan ordenadores
distintos, los conecten todos y den exactamente `K` pares críticos; el
comprobador busca los puentes y cuenta los pares por sí mismo. `-1` debe
coincidir con la respuesta guardada.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 12
```

Salida:

```
1 2
1 3
2 3
3 4
4 5
4 6
4 7
5 6
5 7
6 7
```

## Solución

Al quitar los puentes de una red conexa queda dividida en partes
2-arista-conexas, y dos ordenadores forman un par no crítico exactamente
cuando están en la misma parte. Una parte tiene un ordenador o al menos
tres (dos ordenadores necesitarían dos conexiones entre ellos), y
cualquier tamaño así se puede realizar: cada parte de tamaño `s ≥ 3` es un
ciclo y las partes se unen en cadena con conexiones sueltas, que son los
puentes. Así que la pregunta es si `N` se puede repartir en tamaños de
`{1, 3, 4, …}` con `Σ s·(s − 1)/2 = N·(N − 1)/2 − K`.

Es una mochila pequeña: `reach[m][t]` dice si `m` ordenadores se pueden
repartir con `t` pares no críticos. Añadir una parte de tamaño `s` lleva
`reach[m − s][t]` a `reach[m][t + s(s − 1)/2]`. Recorriendo hacia atrás
desde `reach[N][target]` se recuperan los tamaños. `O(N²·N²)` pasos de
bits en el peor caso, unos 20 millones, o muchos menos con conjuntos de
bits.

Detalles a tener en cuenta:

- no existe una parte de dos ordenadores, así que por ejemplo un triángulo
  más un árbol es posible, pero un único par no crítico no;
- con `N = 1` no hace falta ninguna conexión y el único `K` posible es 0;
- un árbol hace críticos todos los pares, un solo ciclo ninguno.

Todos los veredictos se compararon con una solución escrita aparte para
todo `K` con `N ≤ 12` y para 300 pares aleatorios hasta `N = 100`, y cada
red impresa pasó el comprobador.

## Notas por lenguaje

- C++ guarda cada `reach[m]` como bitset y Python como entero grande, así
  que una parte se añade con un desplazamiento; Go, Java y Rust usan
  tablas booleanas normales.

## Soluciones optimizadas

Go usa una mochila ilimitada unidimensional. Para cada número de pares no críticos, minimiza los vértices que pertenecen a ciclos. Los restantes quedan aislados en sus componentes, y los tamaños guardados permiten reconstruir la solución. El envío 11317280 tardó 0.031 s y usó 1104 KB frente a 0.062 s y 1680 KB en la base.

Rust usa una mochila ilimitada unidimensional. Para cada número de pares no críticos, minimiza los vértices que pertenecen a ciclos. Los restantes quedan aislados en sus componentes, y los tamaños guardados permiten reconstruir la solución. El envío 11317285 tardó 0.015 s y usó 200 KB frente a 0.031 s y 616 KB en la base.

Java usa una mochila ilimitada unidimensional. Para cada número de pares no críticos, minimiza los vértices que pertenecen a ciclos. Los restantes quedan aislados en sus componentes, y los tamaños guardados permiten reconstruir la solución. El envío 11317286 tardó 0.109 s y usó 492 KB frente a 0.343 s y 2136 KB en la base.

Python prueba tamaños de ciclos en orden decreciente y memoriza los estados fallidos por vértices y pares restantes y tamaño máximo del ciclo. El envío 11317371 usó 692 KB frente a 572 KB de la versión sencilla. En la clasificación guardada, el envío quedó segundo en tiempo y primero en memoria. Ambas versiones tardaron 0,078580 KB de la versión sencilla. En la clasificación guardada, el envío quedó segundo en tiempo y primero en memoria. Ambas versiones tardaron 0,093 s.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321735 · Go 1.14 x64 №11322174 · Java 1.8 №11322176 · Python 3.12 x64 №11322178 · Rust 1.75 x64 №11322180.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1169_constructive.cpp](1169_constructive.cpp) | G++ 13.2 x64 | constructive | O(N⁴) bit steps | AC | 0.015 s | 236 KB | 11321735 |
| [1169_constructive.go](1169_constructive.go) | Go 1.14 x64 | constructive | O(N⁴) bit steps | AC | 0.062 s | 1680 KB | 11322174 |
| [1169_constructive.java](1169_constructive.java) | Java 1.8 | constructive | O(N⁴) bit steps | AC | 0.343 s | 2136 KB | 11322176 |
| [1169_constructive.py](1169_constructive.py) | Python 3.12 x64 | constructive | O(N⁴) bit steps | AC | 0.078 s | 580 KB | 11322178 |
| [1169_constructive.rs](1169_constructive.rs) | Rust 1.75 x64 | constructive | O(N⁴) bit steps | AC | 0.031 s | 616 KB | 11322180 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1169_dp.go](1169_dp.go) \* | Go 1.14 x64 | dp | O(N³) | AC | 0.031 s | 1104 KB | 11317280 |
| [1169_dp.rs](1169_dp.rs) \* | Rust 1.75 x64 | dp | O(N³) | AC | 0.015 s | 200 KB | 11317285 |
| [1169_dp.java](1169_dp.java) | Java 1.8 | dp | O(N³) | AC | 0.109 s | 492 KB | 11317286 |
| [1169_backtracking.py](1169_backtracking.py) \* | Python 3.12 x64 | backtracking | O(N^5) | AC | 0.093 s | 692 KB | 11317371 |

\* El objetivo de clasificación de Go sigue pendiente. El objetivo de clasificación de Rust sigue pendiente. El objetivo de clasificación de Python sigue pendiente.
