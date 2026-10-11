# 1303. Cobertura mínima

[Timus 1303](https://acm.timus.ru/problem.aspx?space=1&num=1303) · dificultad 174 · greedy

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados entre 1 y 99 999 segmentos [Li, Ri] con extremos enteros
(−50 000 ≤ Li < Ri ≤ 50 000), hay que elegir el menor número de ellos
que juntos cubran [0, M], 1 ≤ M ≤ 5000. Se imprime cuántos son y los
segmentos elegidos en orden creciente de extremo izquierdo, o
`No solution`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

M y luego los segmentos, un par por línea, terminados por el par `0 0`.

## Salida

La cantidad y luego los segmentos, uno por línea, o `No solution`.

## Evaluación

Se acepta cualquier cobertura mínima. El verificador comprueba que la
cantidad es la mínima, que cada segmento impreso aparece en la entrada
(no más veces que allí), que los extremos izquierdos no decrecen y que
los segmentos no dejan ningún punto de [0, M] sin cubrir. Si no existe
cobertura, la salida debe ser `No solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
-1 0
-5 -3
2 5
0 0
```

Salida:

```
No solution
```

### Ejemplo 2

Entrada:

```
1
-1 0
0 1
0 0
```

Salida:

```
1
0 1
```

## Solución

El voraz clásico. Se guarda el extremo derecho c de la parte [0, c] ya
cubierta, empezando con c = 0. Entre los segmentos con L ≤ c se toma el
de mayor R. Si ni ese R pasa de c, un punto justo a la derecha de c no
se puede cubrir nunca: `No solution`. Si no, se toma y c = R. Se para
cuando c ≥ M.

Tomar el que llega más lejos es seguro: el segmento que use una
cobertura óptima en ese punto no termina más lejos, así que cambiarlo
por el nuestro mantiene la cobertura y la cantidad.

Con los segmentos ordenados por extremo izquierdo, un puntero los
recorre una sola vez, porque un segmento que se pasó una vez no puede
ayudar después (su R no supera el c actual). Los segmentos elegidos
salen solos en orden creciente de extremo izquierdo. `O(N log N)` por
la ordenación.

Detalles a tener en cuenta:

- cubrir significa no dejar huecos dentro de [0, M]: segmentos que
  solo se tocan en un punto, como [0, 2] y [2, 5], valen (prueba 04),
  pero [0, 4] y [5, 10] dejan un hueco (prueba 06);
- un segmento que termina en 0 no ayuda (pruebas 02 y 09);
- el par `0 0` es solo la marca de fin, porque todo segmento real
  tiene L < R.

Las cantidades del voraz se compararon con una búsqueda en anchura
sobre los extremos derechos alcanzables en 400 entradas aleatorias
pequeñas.

## Notas por lenguaje

- Todos los lenguajes deshacen los empates igual, con el primer
  segmento en el orden de clasificación, así que imprimen la misma
  cobertura.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1303_greedy.cpp](1303_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.125 s | 1372 KB |
| [1303_greedy.go](1303_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.046 s | 8068 KB |
| [1303_greedy.java](1303_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.218 s | 8312 KB |
| [1303_greedy.py](1303_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.250 s | 24780 KB |
| [1303_greedy.rs](1303_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 3716 KB |
