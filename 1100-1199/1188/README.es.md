# 1188. Reorganizar los estantes de una librería para que quepa un tomo grande

[Timus 1188](https://acm.timus.ru/problem.aspx?space=1&num=1188) · dificultad 2174 · geometry

Problema original de Elena Kryuchkova y Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un hueco de ancho `XN` y alto `YN` tiene `N ≤ 100` tablas horizontales a
alturas distintas, cada una sobre dos clavijas con el centro de la tabla
entre ellas. Un tomo de ancho `XT` y alto `YT` debe quedar de pie sobre un
estante, entero sobre él, sin que otro estante o clavija entre en su
interior. Cada estante puede quedarse igual, deslizarse, acortarse en
pulgadas enteras, tener una clavija movida a otro sitio a la misma altura
(deslizando y cortando también) o quitarse con sus dos clavijas; todo
estante que quede debe seguir bien apoyado en sus clavijas dentro del
hueco. Hay que minimizar primero las clavijas movidas (quitar mueve dos)
y después las pulgadas cortadas (quitar corta la tabla entera).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`XN YN XT YT`, `N` y luego, para cada estante, su altura, su extremo
izquierdo, su longitud y las distancias de sus dos clavijas al extremo
izquierdo. Todo en pulgadas enteras de hasta 1000.

## Salida

El menor número de clavijas movidas y después el menor número de pulgadas
cortadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
11 8 3 4
4
1 1 7 1 4
4 3 7 1 6
7 2 6 3 4
2 0 3 0 3
```

Salida:

```
0 0
```

### Ejemplo 2

Entrada:

```
11 8 4 6
4
1 1 7 1 4
4 3 7 1 6
7 2 6 3 4
2 0 3 0 3
```

Salida:

```
1 3
```

## Solución

Se prueba el tomo en cada estante `i` y en cada posición entera `x`. El
coste se divide en el de hacer que el estante `i` sostenga el tomo y, para
cada estante estrictamente entre la base y la parte de arriba del tomo, el
de sacarlo de la franja `(x, x + XT)`. Estas partes son independientes.

Sacar un estante de la franja es poner su tabla entera en `[0, x]` o en
`[x + XT, XN]`; llamemos a ese sitio `[F, G]`. Si no se mueve ninguna
clavija, las dos clavijas `a < b` deben estar en el sitio, y una tabla de
longitud `t` se puede colocar sobre ellas con su centro entre ambas
exactamente cuando `b − a ≤ t ≤ min(2(b − F), G − F, 2(G − a))`. Así que
el corte es la longitud de la tabla menos el mayor `t` permitido, si este
es al menos `b − a`. Si puede moverse una clavija, la nueva siempre puede
equilibrar la tabla, así que solo la clavija que queda tiene que estar en
el sitio, y el corte es lo que no cabe: una clavija más
`max(0, longitud − (G − F))`. Quitar cuesta dos clavijas y la longitud
entera. El mejor de todo esto es el coste del estante.

El estante que sostiene el tomo nunca necesita cortes, pues una tabla más
corta cubre menos. Con sus clavijas fijas, los extremos izquierdos
posibles de la tabla forman un intervalo, que se comprueba con
coordenadas dobladas para que el centro sea entero. Si no, mover una
clavija funciona siempre que la tabla sea lo bastante larga para cubrir el
tomo y la clavija que queda.

El coste de despejar cada estante solo depende de `x`, así que, con los
estantes ordenados por altura, unas sumas prefijas sobre los estantes dan
de una vez el total de los que están sobre el estante `i`. Un coste se
guarda como clavijas por un millón más pulgadas, lo que los ordena bien.
`O(N·XN)`.

Detalles a tener en cuenta:

- los estantes justo a la altura de la parte de arriba del tomo o a su
  misma altura pueden tocarlo y no cuestan nada;
- una tabla movida debe quedar dentro del hueco, y eso es lo que obliga a
  cortar cerca de las paredes;
- un tomo tan ancho como el hueco no deja sitio a un lado, así que un
  estante en medio solo puede ir al otro lado o quitarse.

Las respuestas se compararon con una solución escrita aparte en 667
librerías aleatorias y en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes usan los mismos costes en forma cerrada y las mismas
  sumas prefijas sobre los estantes ordenados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1188_geometry.cpp](1188_geometry.cpp) | G++ 13.2 x64 | geometry | O(N·XN) | AC | 0.015 s | 604 KB |
| [1188_geometry.go](1188_geometry.go) | Go 1.14 x64 | geometry | O(N·XN) | AC | 0.031 s | 1960 KB |
| [1188_geometry.java](1188_geometry.java) | Java 1.8 | geometry | O(N·XN) | AC | 0.171 s | 7384 KB |
| [1188_geometry.py](1188_geometry.py) | Python 3.12 x64 | geometry | O(N·XN) | AC | 0.281 s | 4880 KB |
| [1188_geometry.rs](1188_geometry.rs) | Rust 1.75 x64 | geometry | O(N·XN) | AC | 0.015 s | 900 KB |
