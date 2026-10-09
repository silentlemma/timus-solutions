# 1037. Bloques de memoria que caducan

[Timus 1037](https://acm.timus.ru/problem.aspx?space=1&num=1037) · dificultad 1170 · simulation

Problema original de Alexander Klepinin, del V Campeonato por Equipos de Programación de la Universidad Estatal de los Urales, octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Simula un gestor de memoria con `30000` bloques numerados desde 1. Al
principio todos los bloques están libres. Las peticiones llegan en orden de
tiempo no decreciente:

- una **reserva** toma el bloque libre de menor número;
- un **acceso** al bloque `b` tiene éxito si `b` está ocupado, y falla en
  otro caso.

Un acceso con éxito o una reserva en el instante `t` mantiene el bloque
ocupado hasta el instante `t + 600`: en ese momento, si no llegó ninguna
otra petición con éxito, vuelve a quedar libre. Hay como mucho 80000
peticiones, los tiempos son enteros de 0 a 65000 y siempre hay un bloque
libre para una reserva.

Límite de tiempo: 0,4 segundos. Límite de memoria: 64 MB.

## Entrada

Una petición por línea: `T +` es una reserva en el instante `T`, `T . B`
es un acceso al bloque `B` (`1 ≤ B ≤ 30000`) en el instante `T`.

## Salida

Para cada petición, en orden: el número del bloque reservado, o `+` / `-`
para un acceso con éxito / fallido.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 +
1 +
1 +
2 . 2
2 . 3
3 . 30000
601 . 1
601 . 2
602 . 3
602 +
602 +
1202 . 2
```

Salida:

```
1
2
3
+
+
-
-
+
-
1
3
-
```

### Ejemplo 2

Entrada:

```
0 +
0 +
300 . 1
599 . 2
600 . 2
900 . 1
900 +
900 . 1
1199 +
1200 +
```

Salida:

```
1
2
+
+
+
-
1
+
3
2
```

## Solución

Para cada bloque se guarda si está ocupado y su instante de caducidad.
Antes de atender una petición en el instante `t`, se liberan todos los
bloques cuya caducidad es `≤ t`.

Como los tiempos nunca decrecen, cada nueva caducidad `t + 600` es al
menos tan grande como todas las anteriores, así que las caducidades caben
en una cola FIFO normal en el orden en que se fijaron. Un acceso no borra
la entrada antigua de su bloque; esa entrada está obsoleta y se reconoce
al llegar al frente: la caducidad actual del bloque es otra, o el bloque ya
está libre. Un bloque liberado va a un montículo de mínimos de bloques
libres.

Una reserva toma la cima del montículo; si está vacío, toma el siguiente
bloque nunca usado (`1, 2, 3, ...`), todos mayores que cualquier bloque
liberado. Un acceso responde `+` si el bloque está ocupado y luego mueve su
caducidad. Cada petición añade como mucho una entrada a la cola y una al
montículo, así que el total es `O(Q log Q)` para `Q` peticiones.

Detalles a tener en cuenta:

- el bloque queda libre exactamente en `t + 600`: una petición en ese
  instante ya lo ve libre;
- un acceso fallido no ocupa el bloque ni cambia nada;
- varias peticiones en el mismo instante se atienden en el orden de la
  entrada, y los bloques liberados a la vez se reutilizan desde el menor;
- un bloque accedido dos veces en el mismo instante tiene dos entradas
  iguales en la cola: hay que liberarlo una sola vez.

Una alternativa es un árbol de segmentos sobre los bloques con el mínimo
de las caducidades: el primer bloque con caducidad `≤ t` es el menor libre.
Las pruebas se comprobaron con él.

## Notas por lenguaje

- **C++**, **Rust**: colas de prioridad y colas estándar.
- **Go**: un pequeño montículo escrito a mano y un slice como cola; la
  entrada se lee con `bufio.Scanner` por palabras.
- **Java**: lectura de la entrada byte a byte, porque `StreamTokenizer`
  leería `.` como un número; `PriorityQueue` y dos arreglos como cola.
- **Python**: `heapq` y `deque`; toda la entrada se lee de una vez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1037_simulation.cpp](1037_simulation.cpp) | G++ 13.2 x64 | simulation | O(Q log Q) | AC | 0.093 s | 984 KB |
| [1037_simulation.go](1037_simulation.go) | Go 1.14 x64 | simulation | O(Q log Q) | AC | 0.031 s | 7772 KB |
| [1037_simulation.java](1037_simulation.java) | Java 1.8 | simulation | O(Q log Q) | AC | 0.140 s | 6620 KB |
| [1037_simulation.py](1037_simulation.py) | Python 3.12 x64 | simulation | O(Q log Q) | AC | 0.171 s | 16500 KB |
| [1037_simulation.rs](1037_simulation.rs) | Rust 1.75 x64 | simulation | O(Q log Q) | AC | 0.046 s | 3180 KB |
