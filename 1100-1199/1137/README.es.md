# 1137. Unir rutas de autobús circulares en una sola ruta por todos los tramos

[Timus 1137](https://acm.timus.ru/problem.aspx?space=1&num=1137) · dificultad 322 · graphs

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad tiene `n ≤ 100` rutas de autobús circulares, cada una una
secuencia cerrada de hasta 200 paradas con números de 1 a 1000; dos rutas
no comparten ningún tramo de calle, y desde cualquier parada se puede
llegar a cualquier otra. Construye una sola ruta circular que recorra
cada tramo antiguo exactamente una vez, en su sentido antiguo, sin usar
otros tramos. Imprime `0` si es imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y luego `n` líneas: el número de paradas `m` de una ruta y sus `m + 1`
paradas, la última igual a la primera.

## Salida

El número de paradas `k` de la nueva ruta y sus `k + 1` paradas en el
mismo formato, o `0`.

## Evaluación

Se acepta cualquier ruta válida. El comprobador verifica el número, que
la ruta termina donde empieza y que sus tramos son exactamente los
antiguos, contados con multiplicidad.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
6 1 2 5 7 5 2 1
4 1 4 7 4 1
5 2 3 6 5 4 2
```

Salida:

```
15 1 2 5 7 5 2 1 4 7 4 2 3 6 5 4 1
```

## Solución

Los tramos son las aristas de un grafo dirigido, y la nueva ruta es un
circuito euleriano suyo. Cada ruta antigua es un ciclo, así que sale de
cada parada tantas veces como entra; sumando todas las rutas, cada parada
tiene grado de entrada igual al de salida. Junto con la promesa de que
todas las paradas están conectadas, esa es justo la condición del
circuito euleriano, así que la respuesta nunca es `0`.

El algoritmo de Hierholzer encuentra el circuito. Se mantiene una pila,
empezando por cualquier parada de la primera ruta. Se mira la parada de
arriba: si aún tiene un tramo de salida sin usar, se toma el siguiente y
se apila su final; si no, se desapila la parada y se añade al circuito.
El circuito sale al revés. Un puntero por parada al siguiente tramo sin
usar hace que todo el recorrido sea `O(E)` para `E ≤ 20000` tramos.

Detalles a tener en cuenta:

- un recorrido simple que sigue tramos hasta atascarse puede cerrar un
  bucle demasiado pronto; la pila inserta los bucles que faltan;
- el número impreso es el de tramos, y la lista tiene una parada más
  porque la primera se repite al final;
- el recorrido usa una pila explícita, ya que puede tener 20000 pasos de
  profundidad;
- una ruta puede pasar varias veces por la misma parada y usar una calle
  en ambos sentidos.

Las respuestas se comprobaron con el comprobador en todas las pruebas y
en 150 conjuntos aleatorios de rutas.

## Notas por lenguaje

- Todos los lenguajes hacen el mismo recorrido con el mismo orden de
  tramos, así que sus respuestas son idénticas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1137_graphs.cpp](1137_graphs.cpp) | G++ 13.2 x64 | graphs | O(E) | AC | 0.015 s | 468 KB |
| [1137_graphs.go](1137_graphs.go) | Go 1.14 x64 | graphs | O(E) | AC | 0.062 s | 3648 KB |
| [1137_graphs.java](1137_graphs.java) | Java 1.8 | graphs | O(E) | AC | 0.093 s | 2104 KB |
| [1137_graphs.py](1137_graphs.py) | Python 3.12 x64 | graphs | O(E) | AC | 0.093 s | 3688 KB |
| [1137_graphs.rs](1137_graphs.rs) | Rust 1.75 x64 | graphs | O(E) | AC | 0.015 s | 1268 KB |
