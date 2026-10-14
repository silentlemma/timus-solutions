# 1613. Para los aficionados a la estadística

[Timus 1613](https://acm.timus.ru/problem.aspx?space=1&num=1613) · dificultad 142 · binary_search

Problema original de Alexander Ipatov, del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los tranvías de cada una de n ciudades (n ≤ 69 999) llevaron cierto
número de pasajeros, menor que 10⁹. Para cada una de q consultas
(q ≤ 69 999) `l r x`, di si alguna ciudad numerada de l a r llevó
exactamente x pasajeros. Imprime una cadena de q caracteres, `1` para sí
y `0` para no.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n, los n números, q, y luego q líneas `l r x`.

## Salida

La cadena de respuestas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1234567 666666 3141593 666666 4343434
5
1 5 3141593
1 5 578202
2 4 666666
4 4 7135610
1 1 1234567
```

Salida:

```
10101
```

## Solución

Ordena los pares (número, ciudad). Las ciudades con número x forman
entonces un bloque, ordenado por número de ciudad. Para una consulta, una
búsqueda binaria halla el primer par no menor que (x, l): la respuesta es
sí si su número es x y su ciudad es a lo sumo r. `O((n + q) log n)`.

Detalles a tener en cuenta:

- la respuesta es una sola cadena sin separadores;
- la ciudad debe encontrarse en l o después, no solo en algún sitio con
  número x (prueba 04).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1613_binary_search.cpp](1613_binary_search.cpp) | G++ 13.2 x64 | binary_search | O((n + q) log n) | AC | 0.171 s | 748 KB |
| [1613_binary_search.go](1613_binary_search.go) | Go 1.14 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 5876 KB |
| [1613_binary_search.java](1613_binary_search.java) | Java 1.8 | binary_search | O((n + q) log n) | AC | 0.140 s | 1964 KB |
| [1613_binary_search.py](1613_binary_search.py) | Python 3.12 x64 | binary_search | O((n + q) log n) | AC | 0.343 s | 26612 KB |
| [1613_binary_search.rs](1613_binary_search.rs) | Rust 1.75 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 3692 KB |
