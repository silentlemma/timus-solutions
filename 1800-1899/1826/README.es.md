# 1826. Campo de minas

[Timus 1826](https://acm.timus.ru/problem.aspx?space=1&num=1826) · dificultad 309 · greedy

Problema original de Dmitry Teryaev, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grupo de n personas cruza un campo de minas con un único detector:
dos cruzan juntas, luego una vuelve con el detector, y así
sucesivamente. Cada una tarda su propio tiempo, y una pareja avanza al
ritmo de la más lenta. Hallar el menor tiempo total para que crucen
todas.

## Entrada

n (2 ≤ n ≤ 100), luego n tiempos de cruce, enteros positivos de hasta
600.

## Salida

El menor tiempo total.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1
10
5
2
```

Salida:

```
17
```

## Solución

Es el acertijo del puente y la linterna. Se ordenan los tiempos
a ≤ b ≤ … ≤ y ≤ z. Mientras esperan más de tres, se pasa a las dos más
lentas de una de dos maneras, la más barata:

- la más rápida escolta a cada una: z + a + y + a = 2a + y + z;
- cruzan las dos más rápidas, vuelve a, cruzan juntas las dos más
  lentas, vuelve b: b + a + z + b = a + 2b + z.

En ambos casos las dos más rápidas vuelven al inicio y quedan dos
menos. Tres personas tardan a + b + c (a escolta a ambas), dos tardan
el tiempo de la más lenta. Un argumento de intercambio muestra que
algún plan óptimo siempre pasa así a las dos más lentas.
El algoritmo tarda `O(n log n)`, pero la implementación en Python tarda
`O(n^2)` porque cada corte `times[:-2]` copia la lista restante.
El espacio máximo es `O(n)` en las cinco implementaciones.

En el ejemplo (1, 2, 5, 10) emparejar cuesta 1 + 2·2 + 10 = 15 frente
a 2 + 5 + 10 = 17 escoltando, y las dos últimas tardan 2: 17.

Trampas:

- escoltar siempre con la más rápida no es óptimo: 1, 2, 5, 10
  tardaría 19;
- emparejar siempre a las lentas tampoco lo es cuando la segunda más
  rápida es lenta;
- la elección se hace de nuevo en cada ronda;
- los cortes de listas de Python copian elementos: en el test 07, con
  n = 100, se copian 98 + 96 + … + 2 = 2450 elementos, así que la
  ordenación no domina su tiempo de ejecución.

Las respuestas coinciden con una búsqueda de Dijkstra sobre todos los
estados para grupos de hasta 7 y con una implementación aceptada
independiente en grupos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1826_greedy.cpp](1826_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.015 s | 192 KB |
| [1826_greedy.go](1826_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.031 s | 1096 KB |
| [1826_greedy.java](1826_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.109 s | 1764 KB |
| [1826_greedy.py](1826_greedy.py) | Python 3.12 x64 | greedy | O(n^2) | AC | 0.078 s | 464 KB |
| [1826_greedy.rs](1826_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 240 KB |
