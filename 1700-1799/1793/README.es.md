# 1793. Bandeja 2

[Timus 1793](https://acm.timus.ru/problem.aspx?space=1&num=1793) · dificultad 403 · geometry

Problema original de Sofia Tekhazheva, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una bandeja tiene un fondo de a × b y bordes verticales de altura d. Dos
platos son troncos de cono de la misma altura h, cada uno con un radio
de base y un radio superior mayor. ¿Pueden ponerse ambos platos con la
base entera apoyada en la bandeja?

## Entrada

a, b y d; luego el radio de base y el superior de cada plato; luego h.
Todos los números son enteros, de 1 a 1000.

## Salida

"YES" si los platos caben; si no, "NO".

## Ejemplos

### Ejemplo 1

Entrada:

```
10 10 10
1 2
1 2
5
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
8 4 1
1 2
1 3
1
```

Salida:

```
NO
```

## Solución

Un plato se ensancha hacia arriba, así que dentro de los bordes es más
ancho a la altura min(d, h), donde su radio es
w = r + (R − r)·min(d, h)/h. Por encima de los bordes puede sobresalir.
Por tanto el centro de cada plato debe quedar al menos a w de cada
lado, lo que requiere 2w ≤ a y 2w ≤ b. Dos platos de la misma altura
están más lejos de tocarse abajo y más cerca arriba, así que sus
centros deben estar al menos a R₁ + R₂. Los centros quedan lo más
lejos posible en esquinas opuestas de sus rectángulos permitidos, a
a − w₁ − w₂ en un sentido y a b − w₁ − w₂ en el otro. Multiplicar todo
por h deja números enteros, y comparar distancias al cuadrado evita
raíces, así que la prueba es exacta. `O(1)`.

En el primer ejemplo los bordes son más altos que los platos, así que
w = 2 para ambos; los centros pueden separarse 6 en cada sentido, unos
8,49 en total, y solo se necesitan 4.

Trampas:

- con bordes bajos la parte superior de un plato puede ser más ancha
  que la bandeja;
- los platos chocan por arriba, no a la altura de los bordes;
- platos que apenas se tocan sí caben, y una prueba en coma flotante
  puede fallar ahí.

Las respuestas coinciden con una implementación aceptada independiente
en 600 casos aleatorios, entre ellos platos que se tocan exactamente a
lo largo de una diagonal 3-4-5.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1793_geometry.cpp](1793_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 384 KB |
| [1793_geometry.go](1793_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1076 KB |
| [1793_geometry.java](1793_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1592 KB |
| [1793_geometry.py](1793_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 432 KB |
| [1793_geometry.rs](1793_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 220 KB |
