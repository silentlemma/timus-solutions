# 1525. Camino

[Timus 1525](https://acm.timus.ru/problem.aspx?space=1&num=1525) · dificultad 375 · implementation

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un robot está en una casilla desconocida de una caja de n × m × k
(1 ≤ n, m, k ≤ 10⁵) y ejecuta un programa de como mucho 10⁵ pasos: 'l'
y 'r' a lo ancho, 'd' y 'u' a lo alto, 'b' y 'f' a lo largo. Un paso
que saldría de la caja se ignora. Hay que contar las casillas en las
que el robot puede terminar.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n, m y k, y luego el programa en una línea.

## Salida

El número de casillas finales posibles.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1 1
uuuur
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
2 2 2
ulf
```

Salida:

```
1
```

### Ejemplo 3

Entrada:

```
13 14 15
uudlbdrruffbr
```

Salida:

```
1560
```

## Solución

Los tres ejes no se influyen, así que la respuesta es el producto de
las cuentas de cada eje. En un eje, cada paso desplaza cada inicio una
unidad o lo deja contra la pared, de modo que dos inicios vecinos
siguen en orden y a distancia de como mucho uno. Por tanto, los finales
de todos los inicios llenan todo el tramo entre los finales de los
inicios extremos 1 y L, y el eje aporta f(L) − f(1) + 1. Basta simular
esos dos inicios. `O(len)`.

Detalles a tener en cuenta:

- la cuenta llega a unos 10¹⁵ y necesita 64 bits (prueba 04, gen1);
- el programa puede estar vacío, y entonces vale cualquier casilla
  (prueba 05);
- una racha larga de pasos empuja todos los inicios contra una pared
  (pruebas 01, 06, gen3).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1525_implementation.cpp](1525_implementation.cpp) | G++ 13.2 x64 | implementation | O(len) | AC | 0.015 s | 528 KB |
| [1525_implementation.go](1525_implementation.go) | Go 1.14 x64 | implementation | O(len) | AC | 0.015 s | 1748 KB |
| [1525_implementation.java](1525_implementation.java) | Java 1.8 | implementation | O(len) | AC | 0.140 s | 2212 KB |
| [1525_implementation.py](1525_implementation.py) | Python 3.12 x64 | implementation | O(len) | AC | 0.109 s | 692 KB |
| [1525_implementation.rs](1525_implementation.rs) | Rust 1.75 x64 | implementation | O(len) | AC | 0.046 s | 468 KB |
