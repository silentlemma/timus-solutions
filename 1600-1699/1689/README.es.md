# 1689. El pescador y la barra

[Timus 1689](https://acm.timus.ru/problem.aspx?space=1&num=1689) · dificultad 915 · prefix_sums

Problema original de Stanislav Vasilyev, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un canal de longitud g contiene n gusanos de longitud w que no se
solapan. Una barra de longitud total b lleva un disco de anchura p en
cada extremo. Un gusano queda herido si cualquier parte suya está bajo
un disco. Colocar la barra en el canal hiriendo el menor número de
gusanos y, entre esas posiciones, tomar la más a la izquierda.

## Entrada

g y w (1 ≤ w ≤ g ≤ 100000), b y p (1 ≤ p ≤ b/2 ≤ g/2), n
(1 ≤ n ≤ 100000), y luego los extremos izquierdos de los gusanos, de 0
a g − w. Todos los valores son enteros.

## Salida

La distancia del extremo izquierdo del canal al extremo izquierdo de la
barra.

## Ejemplos

### Ejemplo 1

Entrada:

```
1000 4
500 60
10
47 68 22 237 585 417 666 996 888 555
```

Salida:

```
149
```

### Ejemplo 2

Entrada:

```
20 1
2 1
11
1 2 3 4 6 8 10 12 14 16 19
```

Salida:

```
17
```

## Solución

Un disco [a, a + p] hiere al gusano [x, x + w] cuando se solapan en una
longitud positiva: a < x + w y a + p > x. Solo tocarlo no hace daño,
como muestra el segundo ejemplo. Para enteros eso es
x − p + 1 ≤ a ≤ x + w − 1. El disco izquierdo empieza en la posición s
de la barra y el derecho en s + b − p, así que cada gusano queda herido
en dos rangos de s. Todos los extremos son enteros, de modo que entre
las mejores posiciones siempre hay un s entero.

Se suma +1 en ambos rangos en un arreglo de diferencias sobre
s = 0, …, g − b y −1 en su intersección, para que un gusano bajo ambos
discos cuente una vez. Las sumas prefijas dan el número de gusanos
heridos para cada s. Se toma el primer mínimo. `O(n + g)`.

Trampas:

- tocar un gusano no lo hiere, así que los rangos son abiertos en
  ambos extremos (ejemplo 2);
- un gusano largo puede estar bajo ambos discos a la vez; contarlo dos
  veces cambia la respuesta del test 04;
- los rangos se recortan a 0, …, g − b; con b = g solo existe s = 0
  (test 03).

Las respuestas coinciden con un conteo directo en cada posición en 150
casos pequeños y con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1689_prefix_sums.cpp](1689_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(n + g) | AC | 0.078 s | 584 KB |
| [1689_prefix_sums.go](1689_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(n + g) | AC | 0.078 s | 3540 KB |
| [1689_prefix_sums.java](1689_prefix_sums.java) | Java 1.8 | prefix_sums | O(n + g) | AC | 0.093 s | 884 KB |
| [1689_prefix_sums.py](1689_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(n + g) | AC | 0.359 s | 11728 KB |
| [1689_prefix_sums.rs](1689_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(n + g) | AC | 0.046 s | 2712 KB |
