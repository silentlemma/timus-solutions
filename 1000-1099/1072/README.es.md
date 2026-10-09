# 1072. La ruta más corta entre dos ordenadores a través de subredes IP

[Timus 1072](https://acm.timus.ru/problem.aspx?space=1&num=1072) · dificultad 502 · bfs, graphs

Problema original de Evgeny Kobzev, del Ural State University Personal Contest Online, febrero de 2001, Students Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de `N` ordenadores (`2 ≤ N ≤ 90`) tiene hasta 5 interfaces de
red; una interfaz es una dirección IP y una máscara de subred (unos
seguidos de ceros). Dos interfaces están en la misma subred cuando
`IP1 AND mask1` es igual a `IP2 AND mask2`. Un paquete va directamente
entre ordenadores que comparten una subred, y de una subred a otra solo a
través de un ordenador con interfaces en ambas. Halla un camino por el
menor número de ordenadores entre dos ordenadores dados.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`; luego, para cada ordenador, el número de interfaces `K` y `K` líneas
con una dirección IP y una máscara en notación con puntos; al final los
números de los dos ordenadores.

## Salida

`Yes` y los ordenadores del camino en orden, o `No` si no hay camino.

## Evaluación

Se acepta cualquier camino más corto. El comprobador verifica que el
camino va del primer ordenador al segundo, que cada dos vecinos en él
comparten una subred y que tiene el menor número posible de ordenadores.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
2
10.0.0.1 255.0.0.0
192.168.0.1 255.255.255.0
1
10.0.0.2 255.0.0.0
3
192.168.0.2 255.255.255.0
212.220.31.1 255.255.255.0
212.220.35.1 255.255.255.0
1
212.220.31.2 255.255.255.0
2
212.220.35.2 255.255.255.0
195.38.54.65 255.255.255.224
1 
195.38.54.94 255.255.255.224
1 6
```

Salida:

```
Yes
1 3 5 6
```

## Solución

Cada interfaz se reduce al número `IP AND mask`. Dos ordenadores están
unidos cuando tienen un número igual entre sus interfaces; un salto entre
ordenadores unidos es exactamente una transferencia directa, y un
ordenador en medio del camino tiene interfaces en las subredes de ambos
lados. Así que la tarea es un camino más corto en este grafo de
ordenadores, y una búsqueda en anchura desde el primer ordenador lo
encuentra. Siguiendo los padres guardados hacia atrás desde el segundo
ordenador se obtiene el camino. `O(N^2 · K^2)`.

Detalles a tener en cuenta:

- la prueba de subred usa la máscara propia de cada interfaz:
  `10.0.0.77/255.0.0.0` y `10.0.0.5/255.255.255.0` están en la misma
  subred, porque ambas dan `10.0.0.0`, mientras que `10.1.0.1/255.0.0.0` y
  `10.1.0.2/255.255.0.0` no lo están, aunque cada dirección cae dentro del
  rango de la otra;
- las máscaras `0.0.0.0` y `255.255.255.255` están permitidas y no
  necesitan un caso especial;
- las direcciones son números sin signo de 32 bits; un tipo con signo
  también sirve, siempre que solo se compare la igualdad.

Las longitudes de los caminos se comprobaron con Floyd–Warshall sobre el
mismo grafo, construido por separado y comprobando que las máscaras
tienen la forma de unos seguidos de ceros.

## Notas por lenguaje

- C++ lee una dirección con `scanf("%u")` y `".%u"` para las cuatro
  partes; los demás lenguajes parten el token por los puntos.
- Java guarda las direcciones en `int`, que se desborda a valores
  negativos para direcciones altas, pero a `AND` y a la igualdad no les
  importa.
- Python guarda las subredes de un ordenador en un conjunto y prueba
  `isdisjoint`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1072_bfs.cpp](1072_bfs.cpp) | G++ 13.2 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 208 KB |
| [1072_bfs.go](1072_bfs.go) | Go 1.14 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 1180 KB |
| [1072_bfs.java](1072_bfs.java) | Java 1.8 | bfs | O(N^2 · K^2) | AC | 0.078 s | 776 KB |
| [1072_bfs.py](1072_bfs.py) | Python 3.12 x64 | bfs | O(N^2 · K^2) | AC | 0.078 s | 612 KB |
| [1072_bfs.rs](1072_bfs.rs) | Rust 1.75 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 224 KB |
