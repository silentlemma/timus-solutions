# 1113. El menor combustible para un viaje de ida con depósitos

[Timus 1113](https://acm.timus.ru/problem.aspx?space=1&num=1113) · dificultad 264 · math

Problema original de la Olimpiada Nacional Búlgara de Informática, segundo día.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un vehículo debe cruzar `N` km de desierto gastando un litro por
kilómetro. Lleva como mucho `M` litros, con `M < N ≤ 5M` y `N < 32000`.
En la salida hay combustible ilimitado, y el vehículo puede dejar
cualquier cantidad de combustible en cualquier punto del camino y
recogerla después. Halla la menor cantidad total de combustible, en
litros, necesaria para llegar al destino, redondeada hacia arriba.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N M` en una línea.

## Salida

La menor cantidad de combustible, redondeada hacia arriba.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
1000 500
```

Salida:

```
3837
```

## Solución

Es el problema del jeep de ida. Se razona hacia atrás desde el destino.
Los últimos `M` km necesitan una carga completa. Para llevar dos cargas
al inicio de ese tramo, un tramo de `M/3` km anterior se recorre tres
veces (ida, vuelta, ida), lo que cuesta exactamente una carga más; en
general un tramo de `M/(2k − 1)` km transporta `k` cargas al precio de una
más. Así que se suman tramos `M, M/3, M/5, …` hasta llegar a la salida;
si hacen falta `k` cargas y los tramos anteriores al último cubren `s`
km, el combustible es `(k − 1)·M + (N − s)·(2k − 1)`. Con `5M ≥ N` hay
como mucho unos 3000 tramos. `O(k)`.

Detalles a tener en cuenta:

- el redondeo hacia arriba debe ser exacto: el combustible es a menudo un
  entero, y la suma en coma flotante de `M/(2i − 1)` queda justo por
  encima y añade un litro de más (por ejemplo, `N = 59, M = 35` da
  exactamente 143, pero un cálculo simple con `double` imprime 144);
- los tramos solo decrecen como la serie armónica de los impares, así que
  con `N = 5M` hay unos 3000, y la fracción exacta crece hasta varios
  miles de cifras.

Las respuestas se comprobaron con otra formulación con fracciones
exactas: la distancia alcanzable con `F` litros es
`M · Σ_{i≤q} 1/(2i − 1) + (F − qM)/(2q + 1)` con `q = ⌊F/M⌋`, y una
búsqueda binaria halla el menor `F` entero que alcanza `N`; los 12 viajes
hechos a mano y 150 aleatorios, muchos con capacidades divisibles por
`3 · 5 · 7 · 9`, coincidieron.

## Notas por lenguaje

- Python guarda los tramos como fracciones exactas.
- C++, Rust, Java y Go hallan `k` en coma flotante (un error cerca del
  límite no cambia el resultado) y después calculan exactamente la parte
  fraccionaria del combustible como una sola fracción sobre el mínimo
  común múltiplo de los denominadores impares: con su propia aritmética
  de enteros grandes en C++ y Rust, y con `BigInteger` y `math/big` en
  Java y Go. Sumar fracciones normales con un `gcd` de enteros grandes en
  cada uno de los 3000 pasos no cabe en medio segundo en Java y Go.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1113_math.cpp](1113_math.cpp) | G++ 13.2 x64 | math | O(k), k ≤ 3000 stretches | AC | 0.031 s | 616 KB |
| [1113_math.go](1113_math.go) | Go 1.14 x64 | math | O(k), k ≤ 3000 stretches | AC | 0.046 s | 3364 KB |
| [1113_math.java](1113_math.java) | Java 1.8 | math | O(k), k ≤ 3000 stretches | AC | 0.125 s | 6344 KB |
| [1113_math.py](1113_math.py) | Python 3.12 x64 | math | O(k), k ≤ 3000 stretches | AC | 0.125 s | 908 KB |
| [1113_math.rs](1113_math.rs) | Rust 1.75 x64 | math | O(k), k ≤ 3000 stretches | AC | 0.062 s | 536 KB |
