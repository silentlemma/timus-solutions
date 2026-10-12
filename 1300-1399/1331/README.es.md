# 1331. Vladislava

[Timus 1331](https://acm.timus.ru/problem.aspx?space=1&num=1331) · dificultad 980 · geometry

Problema original de Alexander Bikbaev, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un planeta esférico de radio R ≤ 1000 tiene M ≤ 5000 zonas de aterrizaje
y N ≤ 5000 artefactos, cada uno dado por latitud y longitud en grados.
Para cada artefacto hay que imprimir la distancia por la superficie
hasta la zona más cercana, con dos cifras tras el punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego R, luego M líneas con las zonas y N líneas con los
artefactos, cada uno como latitud y longitud.

## Salida

N líneas con las distancias.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2
1
0 0
1 1
0 0
```

Salida:

```
0.00
```

### Ejemplo 2

Entrada:

```
2 1
1
0 0
0 90
0 45
```

Salida:

```
1.57
0.79
```

## Solución

Cada lugar se pone en la esfera unidad como un punto del espacio:
(cos φ cos λ, cos φ sin λ, sin φ). La distancia por la superficie crece
con la cuerda recta entre dos puntos, así que la zona más cercana es la
de cuerda más corta, que se halla probando todas las zonas. Comparar
cuerdas al cuadrado no necesita raíces ni trigonometría dentro del
bucle. La distancia es entonces R · 2 · asin(cuerda / 2). Esta fórmula
conserva la precisión para puntos cercanos, a diferencia de R · acos del
producto escalar, que ahí pierde cifras. `O(N · M)`, 25 millones de
pares.

Detalles a tener en cuenta:

- en los polos la longitud no importa (prueba 04);
- las longitudes −179.5 y 179.5 están a un grado a través de la línea
  de cambio de fecha, no a 359 (prueba 05);
- los puntos opuestos están a π · R, y el redondeo puede dejar
  cuerda / 2 un poco por encima de 1, así que se limita (prueba 03).

Las distancias se compararon con la fórmula del haversine en 300 casos
pequeños aleatorios.

## Notas por lenguaje

- CPython necesita unos 2 segundos para los 25 millones de pares, así
  que la solución en Python se envía con PyPy 3.10, donde tarda unos
  0,1 segundos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1331_geometry.cpp](1331_geometry.cpp) | G++ 13.2 x64 | geometry | O(N·M) | AC | 0.125 s | 408 KB |
| [1331_geometry.go](1331_geometry.go) | Go 1.14 x64 | geometry | O(N·M) | AC | 0.078 s | 1572 KB |
| [1331_geometry.java](1331_geometry.java) | Java 1.8 | geometry | O(N·M) | AC | 0.359 s | 6312 KB |
| [1331_geometry.py](1331_geometry.py) | PyPy 3.10 x64 | geometry | O(N·M) | AC | 0.296 s | 5412 KB |
| [1331_geometry.rs](1331_geometry.rs) | Rust 1.75 x64 | geometry | O(N·M) | AC | 0.046 s | 672 KB |
