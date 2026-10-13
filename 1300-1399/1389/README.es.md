# 1389. Obras en las carreteras

[Timus 1389](https://acm.timus.ru/problem.aspx?space=1&num=1389) · dificultad 552 · dp

Problema original de Dmitry Ivankov y Alexander Ipatov, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 100 000 ciudades están unidas por N − 1 carreteras de doble sentido
de modo que se puede ir de cualquier ciudad a cualquier otra: las
carreteras forman un árbol. Hay que cerrar por obras tantas carreteras
como sea posible, con a lo sumo una carretera cerrada en cada ciudad.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M = N − 1, y luego las M carreteras como pares de ciudades.

## Salida

El número K de carreteras cerradas y luego las K carreteras escritas
como en la entrada.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
1 2
2 3
3 4
```

Salida:

```
2
1 2
3 4
```

## Solución

Las carreteras cerradas forman un emparejamiento, y el emparejamiento
máximo de un árbol se halla de forma voraz desde las hojas. Tomemos una
hoja y su único vecino: algún emparejamiento máximo usa la carretera
entre ellos, porque un emparejamiento que use otra carretera en ese
vecino puede cambiarla por esta. Así que se recorren las ciudades en
orden inverso de una búsqueda en anchura desde la ciudad 1 y se cierra
la carretera al padre siempre que sus dos extremos sigan libres. El
orden de la búsqueda en anchura sustituye a la recursión, que
puede desbordar la pila en un camino de 100 000 ciudades. `O(N)`.

Detalles a tener en cuenta:

- las carreteras se imprimen como están escritas en la entrada y en el
  orden de la entrada; el juez parece rechazar otros órdenes de una
  respuesta correcta, así que las soluciones marcan las carreteras
  elegidas y las imprimen en una sola pasada;
- un camino de 100 000 ciudades puede ser demasiado profundo para la
  recursión (prueba generada 1);
- una estrella solo permite una carretera (prueba 03 y prueba generada
  3).

Las respuestas se compararon en 300 árboles aleatorios de hasta 11
ciudades con una búsqueda sobre todos los conjuntos de carreteras. Las
pruebas se juzgan con un verificador que exige el número esperado de
carreteras, cada una escrita como en la entrada, en el orden de la
entrada y sin ninguna ciudad en dos de ellas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1389_dp.cpp](1389_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.156 s | 6968 KB |
| [1389_dp.go](1389_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.078 s | 16820 KB |
| [1389_dp.java](1389_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 7304 KB |
| [1389_dp.py](1389_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.343 s | 49940 KB |
| [1389_dp.rs](1389_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 16272 KB |
