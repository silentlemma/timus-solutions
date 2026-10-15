# 1703. Brazo robótico

[Timus 1703](https://acm.timus.ru/problem.aspx?space=1&num=1703) · dificultad 1226 · geometry

Problema original de Pavel Atnashev, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El brazo de un robot tiene un brazo superior de longitud a, fijo en el
hombro (el origen) y libre de girar en cualquier dirección, y un
antebrazo de longitud b. El antebrazo se dobla en el codo alrededor de
un eje perpendicular a ambos segmentos, y el ángulo no puede ser agudo.
La pinza del extremo del antebrazo se cierra sobre una barandilla de
diámetro unidad solo si el eje de la barandilla es paralelo al eje del
codo. Dado el eje de la barandilla, hallar una posición del codo y el
ángulo de flexión que permitan cerrar la pinza, o decir que no existe.

## Entrada

a y b, y luego dos puntos distintos del eje de la barandilla. Todos los
números son enteros de valor absoluto a lo sumo 100, a, b ≥ 4, y el eje
no pasa por el hombro.

## Salida

Las coordenadas del codo y el ángulo de flexión en [π/2, π], o
«No solution.». Se acepta cualquier posición válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 6
-10 10 0
10 10 0
```

Salida:

```
0 6.4 4.8 1.5707963267948966
```

### Ejemplo 2

Entrada:

```
5 10
-10 10 0
10 10 0
```

Salida:

```
No solution.
```

## Solución

El eje del codo es perpendicular a ambos segmentos y paralelo a la
barandilla, así que el hombro, el codo y la pinza están en el plano que
pasa por el hombro perpendicular a la barandilla. La pinza sujeta la
barandilla donde su eje corta ese plano: el punto h del eje más cercano
al hombro. Con r = |h|, el hombro, el codo y h forman un triángulo de
lados a, b y r, y la flexión es el ángulo opuesto a r. No es agudo
exactamente cuando a² + b² ≤ r², y el triángulo cierra cuando
r ≤ a + b.

Ambas pruebas son exactas en enteros. Con un punto p del eje y su
dirección d, r² = |p × d|² / |d|², así que se comparan a² + b² y
(a + b)², multiplicados por |d|², con |p × d|². Si se cumplen, el codo
se pone en ese plano: x = (a² − b² + r²) / (2r) a lo largo de h y
√(a² − x²) en perpendicular, y la flexión es
arccos((a² + b² − r²) / (2ab)). `O(1)`.

Trampas:

- un ángulo recto (a² + b² = r², el primer ejemplo) y un brazo recto
  (r = a + b, test 04) están permitidos, por eso la comparación es
  exacta;
- una barandilla demasiado cerca del hombro hace la flexión aguda
  (tests 02 y 08), aunque el brazo llegaría;
- el codo puede reflejarse respecto a la recta hacia h, y vale
  cualquiera de los dos lados.

El verificador comprueba las longitudes de los segmentos, el plano y el
ángulo dado. Los veredictos coinciden con una implementación aceptada
independiente en 150 casos aleatorios, muchos en los límites.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1703_geometry.cpp](1703_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 156 KB |
| [1703_geometry.go](1703_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1084 KB |
| [1703_geometry.java](1703_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1880 KB |
| [1703_geometry.py](1703_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 708 KB |
| [1703_geometry.rs](1703_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 292 KB |
