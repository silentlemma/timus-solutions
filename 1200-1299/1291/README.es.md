# 1291. Engranajes

[Timus 1291](https://acm.timus.ru/problem.aspx?space=1&num=1291) · dificultad 383 · bfs

Problema original de Pavel Egorov, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 1000 engranajes, cada uno con 1 a 1000 dientes, engranan por
parejas, y las uniones no forman ciclos. Un engranaje gira en sentido
antihorario a una velocidad de 1 a 1000. Hay que imprimir la velocidad
de cada engranaje como fracción irreducible: positiva en sentido
antihorario, negativa en sentido horario y 0/1 si no gira.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y, para cada engranaje, su número de dientes y la lista de engranajes
con los que engrana, terminada en 0. La última línea tiene el engranaje
motor y su velocidad.

## Salida

N líneas con las velocidades como `p/q`, con el signo menos delante de
p.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
10 2 3 0
20 1 0
40 1 4 0
100 3 0
1 6
```

Salida:

```
6/1
-3/1
-3/2
3/5
```

## Solución

Dos engranajes unidos hacen pasar el mismo número de dientes por unidad
de tiempo, así que velocidad × dientes es igual en ambos, y giran en
sentidos opuestos. A lo largo de cualquier cadena desde el engranaje
motor r, velocidad × dientes no cambia, de modo que cada engranaje j al
que llega el movimiento gira a

± velocidad · dientes(r) / dientes(j),

y el signo cambia en cada unión: + a distancia par de r y − a distancia
impar. Como no hay ciclos, la distancia está bien definida, y una
búsqueda en anchura desde r da su paridad. Los engranajes no alcanzados
están quietos. Cada fracción se reduce con el mcd de
velocidad · dientes(r) ≤ 10⁶ y dientes(j), que cabe en 32 bits.
`O(N + L)`, con L el número de uniones listadas.

Detalles a tener en cuenta:

- los engranajes fuera del árbol del motor imprimen 0/1 (prueba 03);
- el enunciado no promete que una unión aparezca en ambos extremos, así
  que cada unión se guarda en los dos sentidos (prueba 04);
- las fracciones deben reducirse (prueba 05).

Las respuestas se compararon con una propagación directa de fracciones
exactas en 40 bosques aleatorios.

## Soluciones optimizadas

Go procesa los engranajes al leerlos con unión de conjuntos y paridad del sentido de giro. Una entrada negativa de 16 bits guarda el tamaño del componente raíz; las demás empaquetan el padre y un bit de sentido relativo. La compresión de caminos y unión por tamaño evitan listas de adyacencia. Dentro del componente impulsado las velocidades de los dientes tienen igual magnitud, así que cada velocidad angular es ±speed·teeth[driven]/teeth[gear], reducida con el máximo común divisor. Los otros componentes quedan inmóviles. Usa búferes fijos de bytes. El envío aceptado usa 800 KB frente a 1192 KB del BFS, un 32,9% menos; ambos tardan 0,015 s. Se conservan las versiones sencillas con búsqueda en anchura.

Las implementaciones base aceptadas [1291_bfs.cpp](1291_bfs.cpp), [1291_bfs.java](1291_bfs.java), [1291_bfs.py](1291_bfs.py), [1291_bfs.rs](1291_bfs.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- La búsqueda usa una cola explícita, así que un camino de 1000
  engranajes no necesita recursión profunda.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1291_bfs.cpp](1291_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + L) | AC | 0.015 s | 248 KB | 11284578 |
| [1291_bfs.go](1291_bfs.go) | Go 1.14 x64 | bfs | O(N + L) | AC | 0.015 s | 1192 KB | 11284580 |
| [1291_bfs.java](1291_bfs.java) | Java 1.8 | bfs | O(N + L) | AC | 0.078 s | 784 KB | 11284584 |
| [1291_bfs.py](1291_bfs.py) \* | Python 3.12 x64 | bfs | O(N + L) | AC | 0.078 s | 988 KB | 11284582 |
| [1291_bfs.rs](1291_bfs.rs) | Rust 1.75 x64 | bfs | O(N + L) | AC | 0.015 s | 264 KB | 11284587 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1291_dsu.go](1291_dsu.go) | Go 1.14 x64 | dsu | O((N + L) α(N)) | AC | 0.015 s | 800 KB | 11310858 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
