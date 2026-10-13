# 1477. Aviones

[Timus 1477](https://acm.timus.ru/problem.aspx?space=1&num=1477) · dificultad 2918 · geometry

Problema original de Dmitry Ivankov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N aviones (1 ≤ N ≤ 150) son puntos de una esfera centrada en el origen,
dados por vectores de dirección enteros (X, Y, Z) con coordenadas de
hasta 600 en valor absoluto; no hay dos con la misma dirección. Desde
muy lejos se ve un hemisferio abierto. Hay que hallar cuántos aviones
pueden verse a la vez como máximo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N líneas X Y Z.

## Salida

El mayor número de aviones visibles.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
0 0 1
0 0 -1
0 1 0
0 -1 0
1 0 0
-1 0 0
```

Salida:

```
3
```

## Solución

Un hemisferio abierto con polo d muestra los puntos p con d·p > 0. Se
gira un d óptimo manteniendo sus puntos visibles antes del límite;
salvo que todas las direcciones sean colineales, el plano frontera
límite puede contener dos aviones no paralelos. Así que basta probar
cada plano que pasa por el origen y dos aviones no paralelos, con normal
n = p × q normalizada por signo y mcd para probar cada plano una sola
vez. Los aviones fuera del plano quedan a un lado o al otro.

Los aviones sobre el plano forman una circunferencia, y una ligera
inclinación del polo hacia una dirección u del plano muestra los que
cumplen u·p > 0: el mismo problema con una dimensión menos. Ahí el
borde de la mejor semicircunferencia abierta puede acercarse a un avión
z: la mitad mayor a un lado del diámetro por z, más el propio z, que
añade un giro ligero más. Así cada plano da max(encima, debajo) + la
mejor mitad de su circunferencia, y la respuesta es el mayor de estos
valores, pero al menos 1. `O(N³)` en total, porque cada par no paralelo
determina un solo plano.

Detalles a tener en cuenta:

- el hemisferio es abierto: los aviones de su borde no se ven, así que
  las seis direcciones de los ejes dan 3, no 5 (prueba 01);
- si todos los aviones están en una recta por el origen no hay plano
  que probar y la respuesta es 1 (pruebas 02, 03);
- muchos aviones en una misma circunferencia máxima necesitan el paso
  sobre la circunferencia (pruebas 04, 06, gen3);
- los productos escalares llegan a unos 7,3·10¹¹, más de 32 bits (gen1).

## Notas por lenguaje

- Python se ejecuta con PyPy: CPython excede el límite de 1 s en la
  prueba 13 del juez, y PyPy tarda 0,81 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1477_geometry.cpp](1477_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^3) | AC | 0.031 s | 472 KB |
| [1477_geometry.go](1477_geometry.go) | Go 1.14 x64 | geometry | O(N^3) | AC | 0.046 s | 3116 KB |
| [1477_geometry.java](1477_geometry.java) | Java 1.8 | geometry | O(N^3) | AC | 0.187 s | 7416 KB |
| [1477_geometry.py](1477_geometry.py) | PyPy 3.10 x64 | geometry | O(N^3) | AC | 0.812 s | 11780 KB |
| [1477_geometry.rs](1477_geometry.rs) | Rust 1.75 x64 | geometry | O(N^3) | AC | 0.062 s | 1224 KB |
