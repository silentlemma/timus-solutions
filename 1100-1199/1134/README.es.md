# 1134. Comprobar si son posibles los números leídos en cartas que muestran k − 1 y k

[Timus 1134](https://acm.timus.ru/problem.aspx?space=1&num=1134) · dificultad 197 · greedy

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `n ≤ 1000` cartas; la carta `k` muestra `k − 1` por un lado y `k` por
el otro. Un niño tomó `m ≤ n` cartas distintas en algún orden y leyó un
lado de cada una. Dados los `m` números leídos, decide si pudieron salir
de alguna elección de cartas y lados.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y `m`, y luego los `m` números, cada uno de `0` a `n`.

## Salida

`YES` si la lectura es posible, y `NO` en otro caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
2 0 1 2
```

Salida:

```
NO
```

## Solución

La pregunta es si cada lectura puede recibir su propia carta. El número
`x` aparece en las cartas `x` y `x + 1` (`0` solo en la carta 1, `n` solo
en la carta `n`), así que cada lectura puede usar una de dos cartas
vecinas. Se cuentan las lecturas de cada número y se sube desde `0`. Las
lecturas de `x` toman primero la carta `x` y luego la carta `x + 1`. Tomar
primero la carta inferior es seguro: la carta `x` solo muestra `x − 1` y
`x`, y todas las lecturas de `x − 1` ya están colocadas, así que nada
posterior puede usarla. Si alguna lectura de `x` encuentra ocupadas sus
dos cartas, no hay asignación posible. `O(n + m)`.

Detalles a tener en cuenta:

- `0` y `n` aparecen cada uno en una sola carta;
- el mismo número puede leerse varias veces, como mucho dos para una
  respuesta `YES`;
- las lecturas vienen en orden arbitrario; solo importan sus cantidades.

Las respuestas se compararon con el emparejamiento bipartito de Kuhn en
todas las pruebas y en 400 casos aleatorios.

## Notas por lenguaje

- Todos los lenguajes cuentan las lecturas y hacen la misma pasada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1134_greedy.cpp](1134_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.015 s | 192 KB |
| [1134_greedy.go](1134_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.031 s | 1104 KB |
| [1134_greedy.java](1134_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.078 s | 432 KB |
| [1134_greedy.py](1134_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.078 s | 492 KB |
| [1134_greedy.rs](1134_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.015 s | 204 KB |
