# 1403. El mensajero

[Timus 1403](https://acm.timus.ru/problem.aspx?space=1&num=1403) · dificultad 350 · greedy

Problema original de Nikita Rybak, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de N ≤ 1000 pedidos tarda un día en entregarse y tiene un
plazo y una recompensa; un pedido atrasado no da nada y no debe
entregarse. Hay que elegir los pedidos y su orden de entrega para la
mayor recompensa total.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego el plazo y la recompensa de cada pedido.

## Salida

El número de pedidos entregados y luego sus números en el orden de
entrega. Se acepta cualquier mejor plan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 17
5 15
2 10
2 11
```

Salida:

```
3
1 4 2
```

## Solución

Un conjunto de pedidos se puede entregar a tiempo justo cuando, ordenado
por plazo, el k-ésimo vence el día k o más tarde. Así que se recorren
los pedidos por plazo y los elegidos se guardan en un montículo de
mínimos por recompensa: se añade cada pedido y, cuando el montículo
tiene más pedidos de los que su plazo permite, se descarta el más
barato. Cada paso conserva el mejor conjunto factible de los pedidos
vistos, porque siempre cede el sitio la recompensa más pequeña. Los
pedidos que quedan, ordenados por plazo, son el plan. `O(N log N)`.

Detalles a tener en cuenta:

- los plazos pueden pasar de 100 000 (el foro lo cuenta de la prueba 9),
  así que nada depende de ese límite (prueba 06);
- si todos los pedidos vencen el primer día, solo se entrega la mayor
  recompensa (prueba 07).

Las respuestas se compararon con una búsqueda sobre todos los
subconjuntos en 400 casos pequeños aleatorios. Las pruebas se juzgan con
un verificador que halla el mejor total de otra forma, colocando los
pedidos más valiosos en los últimos días libres.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1403_greedy.cpp](1403_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 228 KB |
| [1403_greedy.go](1403_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1348 KB |
| [1403_greedy.java](1403_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 2860 KB |
| [1403_greedy.py](1403_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 812 KB |
| [1403_greedy.rs](1403_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.046 s | 268 KB |
