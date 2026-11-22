# 2194. Menos turnos en un tablero de serpientes donde un seis vuelve a tirar

[Timus 2194](https://acm.timus.ru/problem.aspx?space=1&num=2194) · dificultad 495 · bfs

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ficha empieza en la casilla 1 de un tablero de N casillas. Una
tirada de k la lleva a min(i + k, N); caer en N gana, y caer en una
serpiente de longitud pᵢ la manda a i − pᵢ, quizá sobre otra serpiente.
Un seis permite volver a tirar en el mismo turno. Hallar el menor número
de turnos para ganar si el dado colabora, o −1. Los límites son 1
segundo y 256 MB.

## Entrada

N, 2 ≤ N ≤ 2 · 10⁵, y luego p₂ … p_{N−1} con 0 ≤ pᵢ < i.

## Salida

El menor número de turnos, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
0 1 1 1 1 1 1 0
```

Salida:

```
-1
```

### Ejemplo 2

Entrada:

```
10
1 2 1 2 0 1 1 1
```

Salida:

```
1
```

### Ejemplo 3

Entrada:

```
10
1 1 2 2 0 6 7 8
```

Salida:

```
2
```

## Solución

Las serpientes solo mandan la ficha a la izquierda, así que la casilla
donde termina tras llegar a i se calcula una vez de izquierda a derecha:
land(i) = land(i − pᵢ), o i si no hay serpiente.

Un estado es la casilla donde la ficha está a punto de tirar, con el
número de turnos empezados. Una tirada de uno a cinco acaba el turno, una
arista de peso 1, y un seis lo continúa, una arista de peso 0. Al inicio
hay un turno empezado, y la primera tirada que llega a N da la respuesta
con el número de turnos actual. Una búsqueda en anchura 0-1 con cola
doble trata los dos pesos en O(6N).

En el segundo ejemplo un seis desde la casilla 1 cae en la 7, baja a la
6, y un cuatro desde allí llega a la 10 en el mismo turno.

## Soluciones optimizadas

C++ calcula land[i] al leer cada salto izquierdo, sin arreglo jump. Por turno, completar primero todos los caminos gratuitos de seis, ampliando la frontera actual; solo después añadir resultados uno a cinco al turno siguiente. Por inducción, la primera visita usa el mínimo de turnos: un mapa de bits sustituye distancias. Si alguna tirada permite llegar a N, un seis también llega o lo rebasa. Basta comprobar el seis en el turno actual para detectar cualquier victoria. Las celdas viejas ya expandieron sus movimientos antes. Cada celda entra una vez en la cola uint32; dos arreglos O(N), bits O(N/64) palabras, tiempo O(6N)=O(N). Se conservan los BFS 0–1 con deque; las otras cuatro familias reutilizan las bases admitidas.

Las implementaciones base aceptadas [2194_bfs.go](2194_bfs.go), [2194_bfs.java](2194_bfs.java), [2194_bfs.py](2194_bfs.py), [2194_bfs.rs](2194_bfs.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2194_bfs.cpp](2194_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.14 s | 2740 KB | 11328352 |
| [2194_bfs.go](2194_bfs.go) \* | Go 1.14 x64 | bfs | O(N) | AC | 0.156 s | 8952 KB | 11295296 |
| [2194_bfs.java](2194_bfs.java) \* | Java 1.8 | bfs | O(N) | AC | 0.171 s | 6876 KB | 11328354 |
| [2194_bfs.py](2194_bfs.py) \* | Python 3.12 x64 | bfs | O(N) | AC | 0.296 s | 21880 KB | 11328355 |
| [2194_bfs.rs](2194_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.062 s | 7856 KB | 11328356 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2194_bfs_optimized.cpp](2194_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.015 s | 1196 KB | 11315428 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
