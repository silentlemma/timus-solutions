# 1328. Bola de fuego

[Timus 1328](https://acm.timus.ru/problem.aspx?space=1&num=1328) · dificultad 1400 · geometry

Problema original de Pavel Egorov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una habitación rectangular va de (0, 0) a (W, H), con
2 ≤ W, H ≤ 1000. Un punto lanzado desde A se mueve en línea recta y
rebota en las paredes con ángulo de incidencia igual al de reflexión.
Un impacto justo en una esquina lo devuelve exactamente hacia atrás y
cuenta como dos rebotes. Hay que hallar la dirección en que lanzarlo
desde A para que llegue a B tras exactamente N rebotes, 0 ≤ N ≤ 10, por
el camino más corto de ese tipo. Entre caminos igual de cortos se
imprime el menor ángulo. A y B están dentro de la habitación y todos
los números son enteros. Hasta su último rebote el punto
atraviesa todo salvo las paredes, el blanco incluido.

El ángulo va en grados, contado en sentido antihorario desde la
dirección del eje x, de 0 a 360, con dos cifras tras el punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

W y H, luego N, luego las coordenadas de A y de B.

## Salida

El ángulo.

## Ejemplos

### Ejemplo 1

Entrada:

```
1000 10
3
101 5 128 8
```

Salida:

```
45.00
```

## Solución

Se refleja la habitación en lugar del camino. Reflejando la habitación
una y otra vez por sus paredes se cubre el plano, y un camino con
rebotes se vuelve una recta a través de las copias. La copia (i, j), i
habitaciones a un lado y j hacia arriba, contiene una imagen de B en

x = i · W + (Bx si i es par, si no W − Bx),
y = j · H + (By si j es par, si no H − By),

y la recta desde A hasta ella cruza |i| paredes verticales y |j|
horizontales, así que rebota |i| + |j| veces. Una esquina es a la vez
una pared vertical y una horizontal, lo que concuerda con la regla de
contarla dos veces, y reflejar en ambas paredes es justo devolverlo
hacia atrás.

Así que los candidatos son las 4N imágenes con |i| + |j| = N (una sola
para N = 0), comparadas por la longitud al cuadrado, exactamente en
enteros, y luego por el ángulo. Una recta puede pasar por una imagen
con menos rebotes, pero eso solo significa que el punto
atraviesa el blanco antes de su último rebote, lo que no lo daña.
`O(N)`.

Detalles a tener en cuenta:

- el camino más corto puede cruzar el blanco antes del último rebote:
  en una habitación de 2 por 2 con el blanco en el centro la diagonal
  lo cruza entre cada dos esquinas y aun así gana (prueba 08);
- el blanco puede estar donde está quien lanza, y entonces salen caminos
  de la misma longitud en varias direcciones (prueba 05);
- un lanzamiento a una esquina son dos rebotes (prueba 06);
- el ángulo va de 0 a 360, así que a los resultados negativos de atan2
  se les suma 360 (prueba 03).

Las respuestas se compararon con una simulación que sigue cada rebote
con fracciones exactas, para cada dirección hacia una imagen a menos de
N + 1 habitaciones, en 600 habitaciones pequeñas aleatorias, y con un
programa independiente en 300 habitaciones aleatorias.

## Notas por lenguaje

- C++, Go, Python y Rust usan atan2 · 180 / π; Java usa Math.toDegrees.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1328_geometry.cpp](1328_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 212 KB |
| [1328_geometry.go](1328_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.015 s | 1116 KB |
| [1328_geometry.java](1328_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 1864 KB |
| [1328_geometry.py](1328_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 512 KB |
| [1328_geometry.rs](1328_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 268 KB |
