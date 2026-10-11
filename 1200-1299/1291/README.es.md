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

## Notas por lenguaje

- La búsqueda usa una cola explícita, así que un camino de 1000
  engranajes no necesita recursión profunda.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1291_bfs.cpp](1291_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + L) | AC | 0.015 s | 248 KB |
| [1291_bfs.go](1291_bfs.go) | Go 1.14 x64 | bfs | O(N + L) | AC | 0.015 s | 1192 KB |
| [1291_bfs.java](1291_bfs.java) | Java 1.8 | bfs | O(N + L) | AC | 0.078 s | 784 KB |
| [1291_bfs.py](1291_bfs.py) | Python 3.12 x64 | bfs | O(N + L) | AC | 0.078 s | 988 KB |
| [1291_bfs.rs](1291_bfs.rs) | Rust 1.75 x64 | bfs | O(N + L) | AC | 0.015 s | 264 KB |
