# 1454. Rectángulos 2

[Timus 1454](https://acm.timus.ru/problem.aspx?space=1&num=1454) · dificultad 2532 · backtracking

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan cinco rectángulos W[i] × H[i] (1 ≤ W[i], H[i] ≤ 1000). Hay que
decidir si los cinco, girados como haga falta y sin solaparse ni
cortarse, pueden juntarse en un único rectángulo grande.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Cinco líneas, con W[i] y H[i] en cada una.

## Salida

«YES» o «NO».

## Ejemplos

### Ejemplo 1

Entrada:

```
2 4
3 2
5 3
2 5
2 5
```

Salida:

```
YES
```

## Solución

El rectángulo grande tiene el área total A, así que su anchura w es un
divisor de A, y por simetría basta probar anchuras con w² ≤ A. Para un
tamaño fijo las piezas se colocan llenando por el «perfil»: se guarda
el contorno de la parte llena como tramos de igual nivel, se toma el
tramo más bajo (el más a la izquierda entre los más bajos) y se pone en
su esquina izquierda alguna pieza sin usar, en cualquier orientación. En
cualquier embaldosado la casilla libre más baja y más a la izquierda es
la esquina inferior izquierda de alguna pieza, y esa pieza no puede ser
más ancha que el tramo, limitado por vecinos más altos o por el borde;
así la búsqueda encuentra todo embaldosado.

Cinco piezas permiten como mucho 5! · 2⁵ órdenes con orientaciones por
tamaño, y los límites de anchura y altura cortan la mayoría; una pieza
de la misma forma no se prueba dos veces en la misma esquina. El área tiene como
mucho unos cientos de divisores, así que la búsqueda entera es mínima.

Detalles a tener en cuenta:

- un molinete, donde ninguna pieza ocupa un lado entero del rectángulo
  grande (pruebas 02, 06, 14);
- un área total prima solo deja tiras de anchura 1 (prueba 04);
- hay que probar las piezas en ambas orientaciones (pruebas 07, 10, 11).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1454_backtracking.cpp](1454_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.015 s | 188 KB |
| [1454_backtracking.go](1454_backtracking.go) | Go 1.14 x64 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.031 s | 1268 KB |
| [1454_backtracking.java](1454_backtracking.java) | Java 1.8 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.140 s | 2356 KB |
| [1454_backtracking.py](1454_backtracking.py) | Python 3.12 x64 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.093 s | 680 KB |
| [1454_backtracking.rs](1454_backtracking.rs) | Rust 1.75 x64 | backtracking | O(√A + d · 5! · 2^5) | AC | 0.031 s | 396 KB |
