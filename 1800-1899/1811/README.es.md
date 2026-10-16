# 1811. Teléfono Dual-SIM

[Timus 1811](https://acm.timus.ru/problem.aspx?space=1&num=1811) · dificultad 1419 · binary_search

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n operadores móviles y k rutas «a través del operador x a un número
del operador y por el precio c». Un teléfono dual-SIM lleva dos
operadores y envía cada mensaje por el más barato que alcance el
destino. Elegir dos operadores que alcancen números de todos los
operadores, de modo que el mensaje más caro sea lo más barato posible.

## Entrada

n y k (2 ≤ n ≤ 10⁴, 0 ≤ k ≤ 10⁵), luego k líneas x y c
(1 ≤ x, y ≤ n, 1 ≤ c ≤ 10⁹).

## Salida

El menor precio posible del mensaje más caro, o "No solution".

## Ejemplos

### Ejemplo 1

Entrada:

```
4 13
1 1 1
1 2 3
1 3 3
1 4 5
2 1 2
2 2 1
2 3 2
3 1 4
3 3 4
3 4 1
4 1 2
4 2 3
4 4 3
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
2 2
1 1 3
2 1 4
```

Salida:

```
No solution
```

## Solución

Búsqueda binaria sobre la respuesta. Para un límite de precio se
conservan solo las rutas que no lo superan y cada operador x recibe el
conjunto de destinos que alcanza, como conjunto de bits. Hay una buena
pareja cuando dos conjuntos lo cubren todo. Sus tamaños suman al menos
n, así que uno de ellos, a, cubre al menos la mitad. Para cada tal a,
los destinos que a no alcanza deben estar todos en el conjunto de la
pareja. Se toma el destino omitido con menos rutas de entrada en total: la
pareja tiene que ser uno de los operadores que lo alcanzan, y cada uno
se prueba con una comprobación de bits de que cubre todo lo que a
omite. Las rutas están ordenadas por precio y el límite es un prefijo
de ellas, así que pasar de un límite a otro solo añade o quita las
rutas intermedias, lo que mantiene al día todos los conjuntos con unos
k cambios en total. `O(n²/64 + k log(k+1) · n/64)` en el peor caso, mucho menos en
la práctica.

En el primer ejemplo, con el límite 2 el operador 2 alcanza 1, 2 y 3, y
el operador 3 alcanza 4 por 1, así que la pareja 2 y 3 sirve. Con el
límite 1 ninguna pareja alcanza a la vez a los operadores 1 y 3.

Trampas:

- rutas repetidas entre los mismos operadores: se queda la más barata;
- un operador al que nadie alcanza hace que la respuesta sea
  "No solution";
- un operador que alcanza a todos basta, con cualquier pareja.

Las respuestas coinciden con una búsqueda directa de todas las parejas
en 90 casos pequeños, y con una implementación aceptada independiente
con hasta 10⁵ rutas entre unos cientos de operadores, con 10⁴
operadores donde unos pocos cubren la mitad cada uno, y con tablas de
precios completas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1811_binary_search.cpp](1811_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n²/64 + k log(k+1) n / 64) | AC | 0.234 s | 21604 KB |
| [1811_binary_search.go](1811_binary_search.go) | Go 1.14 x64 | binary_search | O(n²/64 + k log(k+1) n / 64) | AC | 0.125 s | 24504 KB |
| [1811_binary_search.java](1811_binary_search.java) | Java 1.8 | binary_search | O(n²/64 + k log(k+1) n / 64) | AC | 0.281 s | 19976 KB |
| [1811_binary_search.py](1811_binary_search.py) | Python 3.12 x64 | binary_search | O(n log n + k log(k+1) n / 64) | AC | 0.625 s | 61252 KB |
| [1811_binary_search.rs](1811_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n²/64 + k log(k+1) n / 64) | AC | 0.031 s | 25552 KB |
