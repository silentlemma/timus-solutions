# 1630. Talismán

[Timus 1630](https://acm.timus.ru/problem.aspx?space=1&num=1630) · dificultad 1004 · graphs

Problema original de Sergey Pupyrev (preparado por Daniil Ayzenshteyn), del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un talismán es un conjunto de bolitas de radio 1 mm en el espacio, con
algunos pares unidos por varillas de 8 mm, de modo que los centros
vecinos quedan a 1 cm exacto. Siempre que se pueda llegar de una bolita
a otra por varillas, el menor número de varillas en ese camino debe ser
igual a la distancia en centímetros entre sus centros. Dado el esquema
(qué bolitas están unidas), hay que decidir si se puede construir el
talismán.

## Entrada

La primera línea contiene N y M (1 ≤ N ≤ 100, 0 ≤ M ≤ 10000), el número
de bolitas y de varillas. Cada una de las M líneas siguientes da dos
bolitas unidas por una varilla; ningún par se une dos veces y ninguna
varilla une una bolita consigo misma.

## Salida

`Luck is possible` si el talismán se puede construir y `Unlucky Petr` en
caso contrario.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
1 2
1 3
2 3
```

Salida:

```
Luck is possible
```

### Ejemplo 2

Entrada:

```
4 4
1 2
1 3
1 4
2 3
```

Salida:

```
Unlucky Petr
```

## Solución

Las componentes distintas se pueden alejar mucho, así que cada una se
comprueba por separado: sus distancias en el grafo deben realizarse con
puntos del espacio. Eso deja solo dos formas.

Sea v una bolita con dos vecinas u y w. Están a 1 de v, así que entre sí
están a 1 o a 2; a 2 son los extremos de un diámetro que pasa por v.
Entonces una tercera vecina x tendría distancias al cuadrado a u y a w
que suman 4, cosa que ninguna elección de 1 o 4 da, así que esa v tiene
exactamente dos vecinas.

- Si la componente tiene un triángulo a, b, c, cualquier otra vecina d
  de c debe estar a 1 de a (si no, c quedaría entre a y d y tendría tres
  vecinas), y lo mismo de b; repitiendo, cada bolita queda unida a todas
  las demás. Puntos equidistantes en el espacio hay a lo sumo cuatro, así
  que es una clique de como mucho 4 bolitas.
- Sin triángulos, las vecinas de cada bolita son opuestas entre sí, así
  que todo grado es a lo sumo 2 y cada bolita intermedia es el punto
  medio de sus vecinas: las bolitas están en una recta, donde un ciclo no
  puede cerrarse. Así que es un camino.

Ambas formas funcionan: un camino sobre una recta, y un punto, un
segmento, un triángulo equilátero o un tetraedro regular de lado 1. Una
estructura union-find reúne por componente su número de bolitas k, de
varillas e y su mayor grado; vale cuando e = k − 1 con grados a lo sumo
2, o cuando e = k(k − 1)/2 con k ≤ 4. `O(N + M log N)`.

Detalles a tener en cuenta:

- un triángulo con una bolita más colgada no vale (el segundo ejemplo);
- un cuadrado o un hexágono es un ciclo, no un camino (pruebas 04, 09);
- cinco bolitas unidas entre sí necesitarían cuatro dimensiones
  (prueba 05).

Las respuestas coinciden con una implementación aceptada independiente
en los 1024 grafos de 5 bolitas y en 360 esquemas aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1630_graphs.cpp](1630_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M log N) | AC | 0.015 s | 216 KB |
| [1630_graphs.go](1630_graphs.go) | Go 1.14 x64 | graphs | O(N + M log N) | AC | 0.031 s | 1248 KB |
| [1630_graphs.java](1630_graphs.java) | Java 1.8 | graphs | O(N + M log N) | AC | 0.093 s | 508 KB |
| [1630_graphs.py](1630_graphs.py) | Python 3.12 x64 | graphs | O(N + M log N) | AC | 0.093 s | 936 KB |
| [1630_graphs.rs](1630_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M log N) | AC | 0.031 s | 292 KB |
