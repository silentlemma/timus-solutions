# 2116. Componentes del grafo de un caballo generalizado en un tablero enorme

[Timus 2116](https://acm.timus.ru/problem.aspx?space=1&num=2116) · dificultad 870 · dfs

Problema original de Kirill Deviatkin, de la Olimpiada Académica Universitaria Escolar de Informática 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un caballo generalizado se mueve B casillas a lo largo de un eje y A a
lo largo del otro. Colocar en un tablero N × N el mayor número de
caballos de modo que ninguno pueda llegar a la casilla de otro con
cualquier número de saltos. Los límites son 1 segundo y 256 MB.

## Entrada

N, 1 ≤ N ≤ 10⁹, y luego A y B, 0 ≤ A ≤ B ≤ 3.

## Salida

El mayor número de caballos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1
1
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
3
0
1
```

Salida:

```
1
```

## Solución

Dos caballos deben estar en componentes conexas distintas del grafo de
saltos, y un caballo por componente sirve, así que la respuesta es el
número de componentes. Con A = B = 0 un salto no lleva a ningún sitio,
cada casilla es su propia componente y la respuesta es N², que necesita
64 bits.

Si no, el tablero es enorme pero los saltos son cortos. Cada componente
es una clase de algún invariante de los saltos, como la paridad de x + y
con A = B = 1 o los restos de x e y módulo B con A = 0, y en un tablero
lo bastante grande cada clase es conexa. Para cada uno de los nueve pares
(A, B) con B > 0 el número de componentes deja de cambiar a partir de
N = 2B: una búsqueda exhaustiva en todos los tableros hasta 40 × 40 lo
confirma. Así que una búsqueda en profundidad en un tablero de lado
min(N, 2B), a lo sumo 6 × 6, da la respuesta.

Detalle a tener en cuenta: tratar A = B = 0 antes de limitar el tamaño
del tablero. Su número de componentes es N² y nunca se estabiliza; en
el test [25](tests/25.in), N = 2 y la respuesta es 4.

En el primer ejemplo A = B = 1 salta en diagonal: las dos diagonales del
tablero 2 × 2 están separadas, así que caben dos caballos. En el segundo
los saltos de longitud 1 conectan todas las casillas del tablero 3 × 3.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2116_dfs.cpp](2116_dfs.cpp) | G++ 13.2 x64 | dfs | O(B^2) | AC | 0.015 s | 412 KB |
| [2116_dfs.go](2116_dfs.go) | Go 1.14 x64 | dfs | O(B^2) | AC | 0.031 s | 1136 KB |
| [2116_dfs.java](2116_dfs.java) | Java 1.8 | dfs | O(B^2) | AC | 0.156 s | 1620 KB |
| [2116_dfs.py](2116_dfs.py) | Python 3.12 x64 | dfs | O(B^2) | AC | 0.093 s | 572 KB |
| [2116_dfs.rs](2116_dfs.rs) | Rust 1.75 x64 | dfs | O(B^2) | AC | 0.062 s | 240 KB |
