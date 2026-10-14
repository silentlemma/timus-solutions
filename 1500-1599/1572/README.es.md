# 1572. El Gran Pozo de Yekaterinozavodsk

[Timus 1572](https://acm.timus.ru/problem.aspx?space=1&num=1572) · dificultad 146 · geometry

Problema original de Alexander Ipatov y Alex Samsonov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La boca de un pozo y hasta 100 tapas de alcantarilla son cada una un
círculo (tipo 1, tamaño = radio), un cuadrado (tipo 2) o un triángulo
equilátero (tipo 3, tamaño = lado), con tamaños enteros 1 … 100. Una
tapa plana se puede girar y mover en el espacio de cualquier manera. Hay
que contar las tapas que se pueden echar al pozo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El tipo y el tamaño del pozo, y luego N y el tipo y el tamaño de cada
tapa.

## Salida

El número de tapas que caben.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 10
3
3 20
1 5
2 11
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
1 5
2
2 10
1 6
```

Salida:

```
1
```

## Solución

Una tapa puesta de canto y empujada hacia abajo corta el plano de la
boca a lo largo de cuerdas paralelas de sí misma, así que pasa cuando,
en alguna dirección, su cuerda más larga cabe en la boca. La mejor
dirección da para un círculo el diámetro 2r, para un cuadrado el lado a
y para un triángulo la altura a·√3/2 (las cuerdas paralelas a una
altura). La boca admite segmentos hasta el más largo suyo: el diámetro
del círculo 2R, la diagonal del cuadrado A·√2 y el lado del triángulo A.

Elevadas al cuadrado y multiplicadas por 4, todas estas longitudes son
enteras: 16r², 4a² y 3a² para las tapas, 16R², 8A² y 4A² para el pozo,
así que la comparación es exacta y una tapa que justo toca los bordes
pasa. `O(N)`. Las respuestas coinciden con un programa independiente
para cada par de pozo y tapa de cualquier forma y tamaño.

Detalles a tener en cuenta:

- el tamaño de un círculo es su radio, no su diámetro;
- un triángulo pasa por su altura, no por su lado, así que un triángulo
  de lado 16 aún entra en un pozo cuadrado de lado 10 (prueba 06);
- los tamaños iguales pasan: un cuadrado de lado 10 pasa por un círculo
  de radio 5 (el segundo ejemplo), así que las comparaciones en coma
  flotante requieren cuidado.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1572_geometry.cpp](1572_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 128 KB |
| [1572_geometry.go](1572_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1072 KB |
| [1572_geometry.java](1572_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.140 s | 1776 KB |
| [1572_geometry.py](1572_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 384 KB |
| [1572_geometry.rs](1572_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 228 KB |
