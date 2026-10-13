# 1431. Diplomas

[Timus 1431](https://acm.timus.ru/problem.aspx?space=1&num=1431) · dificultad 362 · greedy

Problema original de Stanislav Vasiliev, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N tipos de diplomas (N ≤ 18), de 1 a 30 de cada uno. Todos los
diplomas de un tipo cuelgan en una fila. Una fila tiene un tipo, o dos
tipos que se alternan estrictamente, y cada fila debe ser simétrica
respecto al centro de la pared. Hay que hallar el menor número de filas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego el número de diplomas de cada tipo.

## Salida

El menor número de filas.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
8 15 13 8 14 8
```

Salida:

```
5
```

## Solución

Una fila de un solo tipo siempre vale. Dos tipos que se alternan
estrictamente forman ABAB…, y esa fila se lee igual al revés solo si
empieza y acaba con el mismo tipo, A B A … B A, así que las cantidades
difieren exactamente en uno. La respuesta es N menos el mayor número de
pares disjuntos de tipos cuyas cantidades difieren en uno.

Los pares unen valores vecinos de una cadena 1, 2, …, 30. Subiendo por
la cadena, los tipos de cantidad c aún sin pareja solo pueden
emparejarse ya con la cantidad c + 1, así que emparejar en seguida tantos
como se pueda nunca es peor. `O(N + 30)`.

Detalles a tener en cuenta:

- cantidades iguales no pueden compartir fila: una fila alterna de
  longitud par no es simétrica (prueba 06);
- en 1, 2, 3, 4 los pares son 1–2 y 3–4, no 2–3 (prueba 07);
- varios tipos pueden tener la misma cantidad (pruebas 08, 12).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1431_greedy.cpp](1431_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + 30) | AC | 0.015 s | 128 KB |
| [1431_greedy.go](1431_greedy.go) | Go 1.14 x64 | greedy | O(N + 30) | AC | 0.015 s | 1076 KB |
| [1431_greedy.java](1431_greedy.java) | Java 1.8 | greedy | O(N + 30) | AC | 0.156 s | 1644 KB |
| [1431_greedy.py](1431_greedy.py) | Python 3.12 x64 | greedy | O(N + 30) | AC | 0.078 s | 420 KB |
| [1431_greedy.rs](1431_greedy.rs) | Rust 1.75 x64 | greedy | O(N + 30) | AC | 0.015 s | 220 KB |
