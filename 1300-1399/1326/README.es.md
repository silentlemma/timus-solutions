# 1326. Chapas

[Timus 1326](https://acm.timus.ru/problem.aspx?space=1&num=1326) · dificultad 391 · bitmask

Problema original con idea de Evgeny Kobzev, preparado por Pavel Atnashev y Alexander Mironenko, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

A una colección le faltan N ≤ 20 chapas de botella. Cada una se puede
comprar suelta por su propio precio, y hay M ≤ 100 ofertas de lotes de
chapas, cada una con un precio por el lote entero. Todos los precios son
positivos y como mucho 1000. Hay que hallar el menor dinero que compra
todas las chapas de una lista dada.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

N y los N precios sueltos, luego M y M líneas, cada una con el precio de
un lote, el número de chapas que contiene y sus números. La última línea
tiene el número de chapas deseadas y sus números.

## Salida

El menor precio total.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
10
11
12
13
3
17 2 1 3
25 3 2 3 4
15 2 3 4
3 1 3 4
```

Salida:

```
25
```

## Solución

Solo importan las chapas deseadas, así que reciben los bits de una
máscara de como mucho 20 bits, y cada oferta, una chapa suelta o un
lote, se convierte en un precio y la máscara de las chapas deseadas que
contiene. Sea cheapest[s] el menor dinero que compra al menos las chapas
de s. Alguna oferta comprada tiene que contener la chapa más baja de s,
y tras ella solo quedan las chapas de s que no están en esa oferta:

cheapest[s] = mínimo sobre las ofertas o que contienen la chapa más baja
de s de price(o) + cheapest[s sin las chapas de o].

El conjunto restante es un número menor, así que basta recorrer s en
orden creciente, y cheapest[conjunto completo] es la respuesta. Ninguna
oferta hace falta dos veces: el resto ya no contiene ninguna de sus
chapas. `O(2^K · (N + M))` para K chapas deseadas.

Detalles a tener en cuenta:

- un lote puede salir más barato que una sola de sus chapas suelta, y
  puede contener chapas no deseadas (pruebas 03 y 04);
- la lista de chapas deseadas puede estar vacía, y entonces la respuesta
  es 0 (prueba 02);
- puede no haber ningún lote (prueba 05).

Las respuestas se compararon con probar todas las combinaciones de
ofertas en 400 casos aleatorios de hasta 6 chapas y 7 lotes.

## Notas por lenguaje

- Python pone en los bits bajos las chapas que están en menos ofertas,
  porque la chapa más baja de s decide qué ofertas se prueban. También
  descarta cada oferta a la que gana otra con tantas chapas por no más
  dinero. Aun así CPython necesita unos 4 segundos cuando los lotes
  valen parecido, así que la solución en Python se envía con PyPy 3.10,
  donde tarda unos 0,2 segundos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1326_bitmask.cpp](1326_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K·(N + M)) | AC | 0.078 s | 3884 KB |
| [1326_bitmask.go](1326_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K·(N + M)) | AC | 0.125 s | 10076 KB |
| [1326_bitmask.java](1326_bitmask.java) | Java 1.8 | bitmask | O(2^K·(N + M)) | AC | 0.218 s | 4428 KB |
| [1326_bitmask.py](1326_bitmask.py) | PyPy 3.10 x64 | bitmask | O(2^K·(N + M)) | AC | 0.296 s | 11124 KB |
| [1326_bitmask.rs](1326_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K·(N + M)) | AC | 0.078 s | 8308 KB |
