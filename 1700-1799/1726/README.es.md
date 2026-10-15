# 1726. Visitas

[Timus 1726](https://acm.timus.ru/problem.aspx?space=1&num=1726) · dificultad 126 · sorting

Problema original de Denis Dublennykh, del Concurso Regional Escolar de Programación de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los n miembros de un comité viven en cruces de calles de una ciudad en
cuadrícula y se visitan caminando por las calles por caminos más
cortos. Todos visitan a todos con la misma frecuencia. Hallar la
distancia media recorrida, redondeada hacia abajo.

## Entrada

n (2 ≤ n ≤ 10⁵) y luego n pares de coordenadas x e y
(1 ≤ x, y ≤ 10⁶).

## Salida

La distancia media entre las casas de dos miembros, redondeada hacia
abajo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10 10
20 20
10 20
```

Salida:

```
13
```

## Solución

Un camino más corto por las calles mide |dx| + |dy|, así que la suma
sobre todos los pares se separa en la suma de |x_i − x_j| y la de
|y_i − y_j|. Se ordenan los x: el i-ésimo (desde 0) es al menos cada
uno de los i anteriores, así que aporta i·x_i menos la suma de ellos,
que lleva un total acumulado. Con y igual. La media sobre los
n(n − 1)/2 pares es esa suma dividida entre el número de pares,
redondeada hacia abajo. `O(n log n)`.

En el ejemplo las distancias son 20, 10 y 10, así que la media es
40/3, que redondeada hacia abajo da 13.

Trampas:

- la suma llega a unos 5·10¹⁵ cuando la mitad de las casas está en una
  esquina lejana y la otra mitad en la opuesta, así que necesita 64
  bits;
- comparar todos los pares cuesta unos 5·10⁹ pasos, demasiados;
- con 2·10⁵ números que leer, la solución en Go analiza la entrada a
  mano para quedar holgadamente dentro del límite de tiempo.

Las medias coinciden con una suma sobre todos los pares en 300 mapas
pequeños aleatorios, y con una implementación aceptada independiente en
las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1726_sorting.cpp](1726_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.156 s | 1764 KB |
| [1726_sorting.go](1726_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.078 s | 2732 KB |
| [1726_sorting.java](1726_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.171 s | 2044 KB |
| [1726_sorting.py](1726_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.203 s | 20712 KB |
| [1726_sorting.rs](1726_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 4740 KB |
