# 1597. El águila de Chernóbil en el tejado. Versión 2

[Timus 1597](https://acm.timus.ru/problem.aspx?space=1&num=1597) · dificultad 1776 · binary_search

Problema original preparado por Sergey Vedernikov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los huevos sobreviven hasta un piso E desconocido, 0 ≤ E ≤ n, y se
rompen por encima. Con k huevos, y pudiendo reutilizar los que no se
rompen, hay que hallar el menor número de lanzamientos que determina E en
el peor caso. Hasta 1000 casos, con k y n hasta 10¹⁸, terminan con
`0 0`. Es el [problema 1223](../../1200-1299/1223/README.es.md) con números
mucho mayores.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

Líneas con k y n, y luego `0 0`.

## Salida

El menor número de lanzamientos para cada caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 10
2 5
0 0
```

Salida:

```
10
3
```

## Solución

Se da la vuelta a la pregunta: con t lanzamientos y k huevos, ¿cuántos
pisos se pueden resolver? El primer lanzamiento parte el edificio: si el
huevo se rompe, quedan t − 1 lanzamientos y k − 1 huevos para los pisos
de abajo; si no, t − 1 lanzamientos y k huevos para los de arriba, así
que f(t, k) = f(t − 1, k − 1) + f(t − 1, k) + 1. La solución de esta
recurrencia es f(t, k) = C(t, 1) + C(t, 2) + … + C(t, k). La respuesta es
el menor t con f(t, k) ≥ n, y f crece con t, así que una búsqueda binaria
lo encuentra.

Con un solo huevo solo se puede ir piso a piso, y la respuesta es el
propio n. Con dos o más, f(t, 2) = t(t + 1)/2 ya llega a 10¹⁸ para t
menor que 1,5·10⁹, así que la búsqueda recorre t hasta U = 2·10⁹. La suma se
construye término a término, C(t, i) = C(t, i − 1)·(t − i + 1)/i, y se
detiene en cuanto supera n, lo que también cubre los k enormes: los
términos crecen tan deprisa que solo hacen falta unas decenas. Como mucho
31 pasos de unos 60 términos por caso.

Los resultados se contrastaron con la programación dinámica clásica
sobre pisos y huevos para todos los edificios de hasta 120 pisos y hasta
8 huevos.

Detalles a tener en cuenta:

- el producto C(t, i − 1)·(t − i + 1) desborda 64 bits; las soluciones en
  C++, Go, Java y Rust descomponen C(t, i − 1) = q·i + r y calculan
  q·(t − i + 1) + r·(t − i + 1)/i, que es exacto, y abandonan en cuanto
  q·(t − i + 1) superaría n;
- con k ≥ 60 huevos la respuesta es simplemente la búsqueda binaria
  sobre los pisos, la longitud en bits de n, y el mismo bucle la da;
- un solo huevo necesita n lanzamientos, que pueden superar el rango de
  búsqueda, y se trata aparte.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1597_binary_search.cpp](1597_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.015 s | 128 KB |
| [1597_binary_search.go](1597_binary_search.go) | Go 1.14 x64 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.031 s | 1140 KB |
| [1597_binary_search.java](1597_binary_search.java) | Java 1.8 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.140 s | 892 KB |
| [1597_binary_search.py](1597_binary_search.py) | Python 3.12 x64 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.140 s | 752 KB |
| [1597_binary_search.rs](1597_binary_search.rs) | Rust 1.75 x64 | binary_search | O(log U · min(k, log(n + 1))) | AC | 0.046 s | 300 KB |
