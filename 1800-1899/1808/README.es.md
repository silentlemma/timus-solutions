# 1808. Chapáev en el planeta Océano

[Timus 1808](https://acm.timus.ru/problem.aspx?space=1&num=1808) · dificultad 1863 · geometry

Problema original de Alexander Mironenko, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un planeta es un disco de agua de radio r centrado en el origen, con
índice de refracción η. Dos observadores fuera de él miran a lo largo
de vectores dados y cada uno ve a un hombre en algún punto del agua.
¿Podían ver al mismo hombre?

## Entrada

r (1 ≤ r ≤ 1000) y η (1 ≤ η ≤ 100, como mucho dos decimales), luego
para cada observador la posición y la dirección de la mirada, enteros
de valor absoluto hasta 1000. Ambos observadores están fuera del
planeta y ven puntos estrictamente dentro. Si la respuesta es "Yes", el
punto común está al menos a 10⁻⁴ de la orilla.

## Salida

"Yes" o "No".

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2.0
5 10 0 -1
-5 10 0 -1
```

Salida:

```
Yes
```

### Ejemplo 2

Entrada:

```
10 1.5
5 10 0 -1
-5 10 0 -1
```

Salida:

```
No
```

## Solución

Un observador puede ver cualquier punto del rayo refractado dentro del
agua, que es una cuerda del disco. La línea de visión toca primero la
circunferencia en la raíz menor de |P + tD|² = r². En ese punto se
descompone la dirección unitaria en su parte a lo largo de la normal
interior y su parte tangencial, de longitud sin α. La ley de Snell
divide la parte tangencial entre η, y la parte normal pasa a ser
√(1 − sin²β), lo que da la dirección v dentro. Desde el punto de
entrada E la cuerda mide −2·(E·v). Las dos cuerdas comparten un punto
exactamente cuando se cruzan con parámetros estrictamente entre 0 y 1,
o cuando están en una misma recta, lo que ocurre con dos miradas a lo
largo de la misma recta por el planeta. `O(1)`.

En los ejemplos ambos miran hacia abajo en x = ±5. Con η = 2 los rayos
se desvían hacia el centro lo bastante para cruzarse en el eje dentro
del planeta; con η = 1,5 solo se encontrarían más allá de su lado
lejano.

Trampas:

- el rayo refractado se acerca a la normal, así que encoge la parte
  tangencial, no la normal;
- dos miradas a lo largo de una recta dan la misma cuerda, lo que
  cuenta como un hombre común;
- la línea de visión debe seguirse hasta el primer cruce, la raíz con
  signo menos.

Las respuestas coinciden con una implementación aceptada independiente
en 300 casos aleatorios con planetas e índices pequeños y grandes,
incluidos casos construidos para dar No, todos elegidos lejos de
cuerdas tangentes o paralelas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1808_geometry.cpp](1808_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 144 KB |
| [1808_geometry.go](1808_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1160 KB |
| [1808_geometry.java](1808_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1844 KB |
| [1808_geometry.py](1808_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 800 KB |
| [1808_geometry.rs](1808_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 244 KB |
