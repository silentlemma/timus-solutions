# 2154. La recta por dos puntos más cercana al origen

[Timus 2154](https://acm.timus.ru/problem.aspx?space=1&num=2154) · dificultad 2318 · geometry, sorting

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n baterías de cañones en puntos enteros distintos. Desde una batería
se puede volar en una bala de cañón hacia cualquier otra batería, saltar
sobre cualquier batería del camino, y la bala sigue volando sin fin.
Hallar la menor distancia al origen que se puede alcanzar así, con error
absoluto o relativo a lo sumo 10⁻⁶. Los límites son 2 segundos y 256 MB.

## Entrada

n, 2 ≤ n ≤ 10⁵, y luego los puntos, |xᵢ|, |yᵢ| ≤ 10⁵.

## Salida

La menor distancia.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 0
0 1
-1 0
0 -1
```

Salida:

```
0.0000000000
```

### Ejemplo 2

Entrada:

```
5
0 3
1 2
1 3
1 4
2 3
```

Salida:

```
0.7071067812
```

## Solución

Cada batería se alcanza desde cualquier otra, y un vuelo desde A por
encima de B seguido de otro desde B por encima de A cubre toda la recta
AB. Así que la respuesta es la menor distancia del origen a una recta por
dos baterías, |A × B| / |A − B|, y 0 si hay una batería en el origen.

Probar todos los pares es demasiado lento, pero solo hacen falta los
pares vecinos en el orden de las direcciones módulo π: se ordenan los
puntos por el ángulo de la recta del origen por ellos, con x / y como
clave, y se toma cada par de vecinos cíclicos: los dos puntos de la recta más
cercana siempre son vecinos en ese orden cíclico, por un lado o por el
otro. Los puntos de
una misma recta por el origen tienen claves iguales, son vecinos y dan 0.
Una comparación exhaustiva con todos los pares en muchos conjuntos
pequeños aleatorios lo confirma. El trabajo es O(n log n).

Trampa: hay que comparar los valores con un error absoluto o relativo de
como máximo 10⁻⁶, en vez de comparar el texto. En la prueba 01, tanto `0`
como `0.0000000000` son salidas válidas. El comprobador acepta ambos
formatos y rechaza valores no finitos y tokens adicionales.

En el primer ejemplo la recta por (1, 0) y (−1, 0) pasa por el origen.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2154_geometry_sorting.cpp](2154_geometry_sorting.cpp) | G++ 13.2 x64 | geometry, sorting | O(n log n) | AC | 0.062 s | 1580 KB |
| [2154_geometry_sorting.go](2154_geometry_sorting.go) | Go 1.14 x64 | geometry, sorting | O(n log n) | AC | 0.062 s | 9244 KB |
| [2154_geometry_sorting.java](2154_geometry_sorting.java) | Java 1.8 | geometry, sorting | O(n log n) | AC | 0.187 s | 9136 KB |
| [2154_geometry_sorting.py](2154_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O(n log n) | AC | 0.312 s | 30008 KB |
| [2154_geometry_sorting.rs](2154_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(n log n) | AC | 0.062 s | 6320 KB |
