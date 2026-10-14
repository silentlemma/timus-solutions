# 1508. Nonograma japonés

[Timus 1508](https://acm.timus.ru/problem.aspx?space=1&num=1508) · dificultad 1563 · dp

Problema original de Stanislav Vasiliev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una línea de un nonograma tiene L casillas (1 ≤ L ≤ 400) y una pista de
K longitudes de grupos (0 ≤ K ≤ L): las casillas negras forman K tramos
de esas longitudes, en ese orden, con al menos una casilla vacía entre
vecinos. Algunas casillas ya se saben vacías ('.') o negras ('X'), el
resto son desconocidas ('?'). Hay que deducir todo lo que se sigue:
marcar una casilla '.' o 'X' cuando tiene ese color en toda línea que
encaja, o escribir «Impossible» si ninguna encaja.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

L y K, una línea con las K longitudes (vacía si K = 0) y las L casillas
conocidas.

## Salida

Las L casillas tras la deducción, o «Impossible».

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2
4 2
?????.?X??
```

Salida:

```
?XXX?.?X?.
```

### Ejemplo 2

Entrada:

```
9 0

??????.X?
```

Salida:

```
Impossible
```

## Solución

Sea pre[i][j] si las primeras i casillas pueden contener los primeros j
grupos y suf[i][j] si las casillas desde i pueden contener los grupos
desde j. pre[i][j] se cumple si la casilla i − 1 puede estar vacía y se
cumple pre[i − 1][j], o si el grupo j puede terminar en la casilla
i − 1: sus casillas no tienen '.', y la casilla justo anterior puede
estar vacía con pre cierto para los j − 1 grupos anteriores (o el grupo
empieza la línea y es el primero). suf es la imagen especular. Un
conteo prefijo de las casillas '.' comprueba el sitio de un grupo en
`O(1)`.

La línea tiene solución si se cumple pre[L][K]. La casilla c puede
estar vacía si no es 'X' y para algún j se cumplen pre[c][j] y
suf[c + 1][j]. La casilla c puede ser negra si algún grupo j puede ir
en un tramo que la cubra: el tramo no tiene '.', las casillas de
alrededor pueden estar vacías, pre da los j grupos de la izquierda y
suf el resto a la derecha. Cada tramo posible suma uno a sus casillas
mediante un arreglo de diferencias. Una casilla que puede ser de ambos
colores es '?'. `O(L·K)`.

Detalles a tener en cuenta:

- con K = 0 la línea de longitudes está vacía, así que la entrada se
  lee por tokens (pruebas 02, 04, 07, gen6);
- una sola casilla negra conocida basta para que no tener grupos sea
  imposible (pruebas 02, 04);
- los grupos vecinos necesitan una casilla vacía entre ellos incluso si
  llenan la línea (prueba 05);
- un grupo largo es negro en su centro vaya donde vaya (prueba 06);
- demasiados grupos para la línea dan «Impossible» (prueba 09, gen5).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1508_dp.cpp](1508_dp.cpp) | G++ 13.2 x64 | dp | O(L * K) | AC | 0.015 s | 584 KB |
| [1508_dp.go](1508_dp.go) | Go 1.14 x64 | dp | O(L * K) | AC | 0.031 s | 1304 KB |
| [1508_dp.java](1508_dp.java) | Java 1.8 | dp | O(L * K) | AC | 0.109 s | 752 KB |
| [1508_dp.py](1508_dp.py) | Python 3.12 x64 | dp | O(L * K) | AC | 0.250 s | 2108 KB |
| [1508_dp.rs](1508_dp.rs) | Rust 1.75 x64 | dp | O(L * K) | AC | 0.015 s | 412 KB |
