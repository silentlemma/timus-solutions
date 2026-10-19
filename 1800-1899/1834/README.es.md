# 1834. Raqueta de tenis

[Timus 1834](https://acm.timus.ru/problem.aspx?space=1&num=1834) · dificultad 4436 · constructive

Problema original de Daniil Aizenshtein, del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tren de n vagones se ordena en una vía muerta con forma de raqueta.
En una pasada los vagones se desenganchan uno a uno por la cola, el
primero entra en la vía y cada siguiente se engancha a la cabeza o a la
cola del tren que se forma allí; luego el tren nuevo sale con la
cabeza por delante. Hallar el menor número de pasadas que dejan los
vagones en el orden 1, …, n, y el orden tras cada pasada.

## Entrada

n (2 ≤ n ≤ 10000), luego los vagones de cabeza a cola, una permutación
de 1, …, n.

## Salida

El menor número de pasadas k y luego k líneas con el orden tras cada
pasada. Se acepta cualquier secuencia óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
2 5 3 1 6 4
```

Salida:

```
3
5 1 6 4 3 2
1 2 3 4 6 5
1 2 3 4 5 6
```

## Solución

Los vagones enganchados a la cabeza salen en su orden anterior antes
del primer vagón que entró, y los enganchados a la cola salen después
de él en orden inverso. Así que una pasada elige cualquier conjunto de
vagones, los mantiene en orden y añade los demás al revés.

En k pasadas cada vagón reúne un código de k bits con sus elecciones.
Ordenando por la última pasada y desplegando hacia atrás, los vagones
quedan ordenados por sus códigos en el orden del código Gray reflejado,
y los vagones con el mismo código conservan su orden mutuo, invertido
una vez por cada uno del código. La paridad de esos unos es la del
rango Gray del código. Así que el tren ordenado se corta en como mucho
2ᵏ tramos de valores consecutivos en orden de rango, y un tramo de
rango par ya debe crecer en las posiciones originales, y uno de rango
impar debe decrecer.

Se cortan los valores con avidez en los tramos alternantes más largos,
una vez empezando con uno creciente y otra con uno decreciente. Dar los
rangos 0, 1, … al primer corte exige 2ᵏ ≥ R; dar los rangos 1, 2, … al
segundo, dejando vacío el rango 0, exige 2ᵏ ≥ F + 1. Los rangos vacíos
en medio nunca ayudan, porque un solo vagón es a la vez creciente y
decreciente. La respuesta es el menor k, y la pasada j mueve justo los
tramos cuyo código Gray tiene el bit j. `O(n log n)` con la salida.

En el ejemplo el corte que empieza creciendo es 1 | 2 | 3–4 | 5 | 6,
cinco tramos, y el que empieza decreciendo es 1–2 | 3–4 | 5 | 6, cuatro
tramos que con el rango 0 vacío también ocupan cinco rangos: tres
pasadas.

Trampas:

- el primer vagón que entra no es especial: simplemente queda entre los
  vagones conservados y los invertidos;
- un tren que empieza decreciendo no necesita menos pasadas con
  el rango 0 vacío que con su corte creciente, ni siquiera uno invertido;
- un tren ordenado no necesita pasadas y solo imprime 0.

Los números de pasadas coinciden con una búsqueda en anchura sobre
todas las permutaciones de hasta 7 vagones, y cada secuencia impresa se
comprobó pasada a pasada para todas las permutaciones de 4 a 6 vagones
y para las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1834_constructive.cpp](1834_constructive.cpp) | G++ 13.2 x64 | constructive | O(n log n) | AC | 0.031 s | 1168 KB |
| [1834_constructive.go](1834_constructive.go) | Go 1.14 x64 | constructive | O(n log n) | AC | 0.031 s | 5308 KB |
| [1834_constructive.java](1834_constructive.java) | Java 1.8 | constructive | O(n log n) | AC | 0.109 s | 5944 KB |
| [1834_constructive.py](1834_constructive.py) | Python 3.12 x64 | constructive | O(n log n) | AC | 0.140 s | 7600 KB |
| [1834_constructive.rs](1834_constructive.rs) | Rust 1.75 x64 | constructive | O(n log n) | AC | 0.031 s | 2552 KB |
