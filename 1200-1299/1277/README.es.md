# 1277. Policías y ladrones

[Timus 1277](https://acm.timus.ru/problem.aspx?space=1&num=1277) · dificultad 861 · flow

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una red conexa de N ≤ 100 estaciones tiene M canales de doble sentido.
Controlar la estación i requiere x_i policías (Σ x_i ≤ 10 000). Los
ladrones van de la estación F a la S, y ninguna de las dos se puede
ocupar. Con K ≤ 10 000 policías, ¿se pueden cortar todas las rutas de
F a S?

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

K; luego N, M, S y F; los N costes; y después los M canales.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
5 5 1 5
1 6 6 11 1
1 2
1 3
2 4
3 4
4 5
```

Salida:

```
NO
```

### Ejemplo 2

Entrada:

```
10
5 5 1 5
1 4 4 11 1
1 2
1 3
2 4
3 4
4 5
```

Salida:

```
YES
```

## Solución

El conjunto de estaciones más barato que separa S de F es un corte
mínimo de vértices, que coincide con un flujo máximo si cada estación se
desdobla. La estación v pasa a ser una entrada y una salida unidas por
un arco de capacidad x_v, y cada canal da dos arcos de la salida de una
estación a la entrada de la otra. Los arcos de los canales, y los arcos
de estación de S y F, que no se pueden ocupar, tienen capacidad
ilimitada. La respuesta es YES justo cuando el flujo máximo de la salida
de S a la entrada de F no pasa de K.

"Ilimitada" solo tiene que superar K, así que vale K + 1, y el algoritmo
de Dinic se detiene en cuanto el flujo pasa de K. `O(V² E)` en general,
con V = 2N nodos y E arcos, pero mucho menos aquí.

Detalles a tener en cuenta:

- S puede coincidir con F, y entonces no se puede cortar nada
  (prueba 03);
- un canal directo entre S y F tampoco se puede cortar: el flujo por él
  supera cualquier K (prueba 04);
- el límite es inclusivo: basta un corte que cueste justo K
  (pruebas 05, 06).

Las respuestas se compararon con probar todos los conjuntos de
estaciones en 199 galaxias aleatorias de hasta diez estaciones, también
con K justo en el coste del corte más barato y uno por debajo.

## Notas por lenguaje

- Todos los lenguajes ejecutan el mismo algoritmo de Dinic con una
  búsqueda recursiva de caminos de aumento.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1277_flow.cpp](1277_flow.cpp) | G++ 13.2 x64 | flow | O(V² E) | AC | 0.015 s | 384 KB |
| [1277_flow.go](1277_flow.go) | Go 1.14 x64 | flow | O(V² E) | AC | 0.031 s | 3860 KB |
| [1277_flow.java](1277_flow.java) | Java 1.8 | flow | O(V² E) | AC | 0.109 s | 804 KB |
| [1277_flow.py](1277_flow.py) | Python 3.12 x64 | flow | O(V² E) | AC | 0.125 s | 2732 KB |
| [1277_flow.rs](1277_flow.rs) | Rust 1.75 x64 | flow | O(V² E) | AC | 0.031 s | 1268 KB |
