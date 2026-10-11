# 1273. Traviesas

[Timus 1273](https://acm.timus.ru/problem.aspx?space=1&num=1273) · dificultad 463 · dp

Problema original de Magaz Asanov (preparado por Leonid Volkov), del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los dos rieles son las rectas x = 0 y x = 1. Cada una de las K ≤ 100
traviesas une (0, Y1) con (1, Y2) en puntos enteros, |Y1|, |Y2| ≤ 1000;
no hay dos traviesas con el mismo extremo izquierdo ni con el mismo
extremo derecho. Hay que quitar las menos traviesas posibles para que
no se crucen dos de las que quedan.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

K y luego K pares Y1 Y2.

## Salida

El menor número de traviesas que hay que quitar.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 1
3 0
1 2
```

Salida:

```
1
```

## Solución

Como los extremos nunca coinciden, dos traviesas se cruzan justo cuando
sus extremos izquierdos y derechos van en orden opuesto. Ordenando las
traviesas por el extremo izquierdo, un conjunto sin cruces es uno con
extremos derechos crecientes, y lo más que se puede conservar es la
subsecuencia creciente más larga de los extremos derechos. La respuesta
es K menos su longitud, hallada con la DP cuadrática sobre la última
traviesa conservada. `O(K²)`.

Detalles a tener en cuenta:

- la entrada no está ordenada por ningún extremo (prueba 06);
- K puede ser 0 (prueba 02);
- las coordenadas pueden ser negativas.

Las respuestas se compararon con probar todos los subconjuntos de
traviesas en 119 casos aleatorios de hasta 12 traviesas.

## Notas por lenguaje

- Todos los lenguajes ordenan los pares y hacen la misma DP.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1273_dp.cpp](1273_dp.cpp) | G++ 13.2 x64 | dp | O(K²) | AC | 0.015 s | 192 KB |
| [1273_dp.go](1273_dp.go) | Go 1.14 x64 | dp | O(K²) | AC | 0.015 s | 1140 KB |
| [1273_dp.java](1273_dp.java) | Java 1.8 | dp | O(K²) | AC | 0.140 s | 2780 KB |
| [1273_dp.py](1273_dp.py) | Python 3.12 x64 | dp | O(K²) | AC | 0.093 s | 392 KB |
| [1273_dp.rs](1273_dp.rs) | Rust 1.75 x64 | dp | O(K²) | AC | 0.015 s | 232 KB |
