# 1181. Cortar un polígono de tres colores en triángulos tricolores

[Timus 1181](https://acm.timus.ru/problem.aspx?space=1&num=1181) · dificultad 455 · constructive

Problema original de Dmitry Filimonenkov, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los vértices de un polígono convexo de `4 ≤ N ≤ 1000` vértices están
pintados de R, G y B; aparecen los tres colores y ningún par de vecinos
comparte color. Hay que cortar el polígono con diagonales que no se
crucen en triángulos que tengan un vértice de cada color, o imprimir 0 si
es imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los colores en orden alrededor del polígono.

## Salida

El número de diagonales y luego las diagonales como pares de números de
vértice.

## Evaluación

Se acepta cualquier corte cuyas `N − 3` diagonales distintas no se crucen
y en el que cada triángulo tenga los tres colores. Un corte así siempre
existe, así que `0` nunca es correcto.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
RBGBRGB
```

Salida:

```
4
1 3
3 7
5 7
5 3
```

## Solución

Si algún color aparece una sola vez, se trazan todas las diagonales desde
ese vértice. Cada triángulo del abanico tiene ese vértice y dos vértices
vecinos del resto, que difieren entre sí y de él.

Si no, cada color aparece al menos dos veces. Hay un vértice cuyos dos
vecinos tienen colores distintos: si todo vértice tuviera vecinos iguales,
los colores se repetirían con periodo dos alrededor del polígono y solo
habría dos colores. Se corta ese vértice con la diagonal entre sus
vecinos; el triángulo tiene tres colores, el resto sigue teniendo los
tres colores (el del vértice quitado aparece en otra parte) y ningún par
de vecinos iguales. Se repite hasta que un color quede solo o quede un
triángulo. Así que la respuesta siempre existe, con `N − 3` diagonales.
`O(N²)` borrando de una lista sin más.

Detalles a tener en cuenta:

- la respuesta nunca es 0, aunque el enunciado lo mencione;
- tras un corte cambian las cuentas de colores, así que un color puede
  quedar solo más tarde, y entonces el abanico termina el trabajo;
- un polígono impar no puede alternar dos colores, otra forma de ver que
  la búsqueda de un vértice con vecinos distintos nunca falla.

Cada corte impreso pasó el comprobador en 200 polígonos aleatorios de
hasta 33 vértices y en todas las pruebas, incluidos polígonos de mil
vértices.

## Notas por lenguaje

- Todos los lenguajes guardan los vértices restantes en una lista y
  borran de ella el vértice cortado.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1181_constructive.cpp](1181_constructive.cpp) | G++ 13.2 x64 | constructive | O(N²) | AC | 0.015 s | 408 KB |
| [1181_constructive.go](1181_constructive.go) | Go 1.14 x64 | constructive | O(N²) | AC | 0.031 s | 1188 KB |
| [1181_constructive.java](1181_constructive.java) | Java 1.8 | constructive | O(N²) | AC | 0.218 s | 6632 KB |
| [1181_constructive.py](1181_constructive.py) | Python 3.12 x64 | constructive | O(N²) | AC | 0.203 s | 760 KB |
| [1181_constructive.rs](1181_constructive.rs) | Rust 1.75 x64 | constructive | O(N²) | AC | 0.031 s | 476 KB |
