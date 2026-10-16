# 1773. Metro a cada casa

[Timus 1773](https://acm.timus.ru/problem.aspx?space=1&num=1773) · dificultad 850 · constructive

Problema original de Alexander Ipatov (preparado por Marina Mukhacheva), del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n tiras de papel pintado del mismo ancho y de altura h llevan cada una
un segmento recto del borde izquierdo, a altura l, al derecho, a altura
r. Una tira puede ponerse cabeza abajo. Pegar todas las tiras una junto
a otra para que los segmentos formen una sola recta a lo ancho de la
pared.

## Entrada

h y n (1 ≤ h ≤ 100000, 1 ≤ n ≤ 50000) y luego l y r de cada tira
(0 ≤ l, r ≤ h).

## Salida

Los números de las tiras de izquierda a derecha, con un menos delante
de la tira girada, o 0 si ningún orden sirve. Se acepta cualquier orden
válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
3 2
2 1
2 1
```

Salida:

```
-3 1 2
```

### Ejemplo 2

Entrada:

```
5 3
3 2
2 1
3 2
```

Salida:

```
0
```

## Solución

Girar una tira cambia sus extremos a h − r a la izquierda y h − l a la
derecha, así que su subida d = r − l no cambia. Todas las tiras deben
tener el mismo d, y entonces los extremos izquierdos de las tiras en
orden son start, start + d, …, start + (n − 1)·d. Una tira con extremo
izquierdo x puede ocupar el lugar de x o, girada, el de h − d − x.

Si una tira puede ocupar dos lugares i y j, tanto x como h − d − x están
en la recta, así que i + j es igual para todas esas tiras: los lugares
se emparejan como i y K − i, y solo compiten tiras del mismo par. Por
eso primero las tiras con un único lugar posible ocupan cada una el
suyo, y luego cada tira con dos lugares toma el que siga libre; si
alguna tira no encuentra lugar, ese start falla. Para el propio start
hay dos candidatos: la tira con el extremo más extremo, el más bajo si
d > 0 y el más alto si d < 0, o bien empieza con él la recta o, girada,
la termina con el extremo opuesto. Una recta horizontal se comprueba en
las dos alturas de la primera tira. `O(n)`.

En el primer ejemplo d = −1. El extremo más alto es 4, de la tira 2 o 3
girada, así que la recta empieza en 4: la tira 3 girada va de 4 a 3, la
tira 1 de 3 a 2 y la tira 2 de 2 a 1.

Trampas:

- girar una tira no cambia su pendiente, así que pendientes distintas
  no tienen remedio;
- una tira cuyos dos extremos izquierdos coinciden no debe contarse dos
  veces;
- el orden no es único, así que el verificador une las tiras él mismo.

Las respuestas coinciden con una búsqueda sobre todos los órdenes y
giros en unos 500 casos aleatorios de hasta 5 tiras, y con una
implementación aceptada independiente, comprobadas en ambos sentidos,
en 100 casos de hasta 50000 tiras.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1773_constructive.cpp](1773_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.093 s | 1060 KB |
| [1773_constructive.go](1773_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.078 s | 6100 KB |
| [1773_constructive.java](1773_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.140 s | 6076 KB |
| [1773_constructive.py](1773_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.296 s | 34732 KB |
| [1773_constructive.rs](1773_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 4816 KB |
