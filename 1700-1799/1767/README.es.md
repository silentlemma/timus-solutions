# 1767. La casa del doctor Dee

[Timus 1767](https://acm.timus.ru/problem.aspx?space=1&num=1767) · dificultad 732 · geometry

Problema original de Alex Samsonov, del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las calles forman una cuadrícula. Un recorrido va de A a B y otro de C
a D, cada uno por algún camino más corto de la cuadrícula. Elegir los
dos caminos para que la longitud total de las calles que comparten sea
la mayor posible, e imprimir esa longitud.

## Entrada

Los puntos A, B, C y D, uno por línea, con coordenadas enteras de valor
absoluto a lo sumo 10⁹.

## Salida

La mayor longitud compartida.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
4 4
5 5
3 3
```

Salida:

```
2
```

## Solución

Un camino más corto no sale del rectángulo que abarcan sus extremos,
así que las calles compartidas están en la intersección de los dos
rectángulos, un rectángulo de w por h, o en ninguna parte si los
rectángulos no se tocan. Un camino más corto avanza en un solo sentido
por cada eje: sube hacia la derecha o hacia la izquierda, o es una
recta, que sirve para ambos casos.

Si los dos recorridos suben en el mismo sentido, ambos pueden llegar a
una esquina de la intersección, seguir la misma escalera hasta la
esquina opuesta y continuar hacia sus extremos, compartiendo w + h, y
ningún camino dentro de la intersección es más largo. Si uno sube hacia
la derecha y el otro hacia la izquierda, un tramo compartido debe
avanzar en un solo sentido por cada eje para ambos, así que es un único
segmento recto, de a lo sumo max(w, h), y ambos pueden seguir un lado de
la intersección. `O(1)`.

En el ejemplo ambos recorridos suben hacia la derecha, la intersección
es el cuadrado de (3, 3) a (4, 4) y comparten 1 + 1 = 2.

Trampas:

- para compartir, un recorrido no tiene sentido: de C a D subiendo
  hacia la derecha es lo mismo que de D a C;
- rectángulos que solo se tocan en un punto o a lo largo de una línea
  comparten 0 o esa línea;
- las longitudes llegan a 4·10⁹, más de 32 bits con signo.

Las respuestas coinciden con la enumeración de todos los pares de
caminos más cortos en 400 casos aleatorios con coordenadas de hasta 5 y
con una implementación aceptada independiente en 90 casos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1767_geometry.cpp](1767_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 128 KB |
| [1767_geometry.go](1767_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1084 KB |
| [1767_geometry.java](1767_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1648 KB |
| [1767_geometry.py](1767_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 452 KB |
| [1767_geometry.rs](1767_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 244 KB |
