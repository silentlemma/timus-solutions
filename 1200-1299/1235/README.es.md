# 1235. El mayor campo cuadrado entre los árboles

[Timus 1235](https://acm.timus.ru/problem.aspx?space=1&num=1235) · dificultad 772 · geometry

Problema original de Andrey Demidov, del concurso regional ACM ICPC del noreste de Europa 2002–2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un parque de W × H (1 ≤ W, H ≤ 10 000) con una esquina en el origen
tiene N árboles (0 ≤ N ≤ 100) en puntos enteros distintos. Hay que hallar
el mayor cuadrado con lados paralelos a los del parque que quede dentro
del parque y sin ningún árbol estrictamente dentro; los árboles en su
borde están permitidos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, W y H, y luego los N árboles como `x y`.

## Salida

La esquina suroeste P, Q de un cuadrado máximo y su lado L. Sirve
cualquier cuadrado máximo.

## Evaluación

Puede haber varios cuadrados máximos, así que el verificador acepta
cualquiera: L debe ser igual al lado de referencia, el cuadrado debe
quedar dentro del parque y ningún árbol puede estar estrictamente dentro.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 10 7
3 2
4 2
7 0
7 3
4 5
2 4
1 7
```

Salida:

```
4 3 4
```

## Solución

Tomamos un cuadrado máximo y lo deslizamos a la izquierda: puede moverse
hasta que su lado izquierdo llega al borde del parque o a un árbol cuya
altura queda estrictamente entre su base y su techo. Después lo
deslizamos hacia abajo igual. Sigue vacío y del mismo tamaño, y ahora su
esquina tiene x igual a 0 o a la x de un árbol, e y igual a 0 o a la y de
un árbol.

Así que basta probar todas esas esquinas, como mucho 101 × 101. Desde la
esquina (p, q) el lado lo limita el parque, `min(W − p, H − q)`, y cada
árbol arriba a la derecha, x > p e y > q: ese árbol queda estrictamente
dentro salvo que el lado se detenga en `max(x − p, y − q)`. Los árboles a
la izquierda o debajo nunca entran. El mayor lado entre todas las
esquinas es la respuesta. `O(N³)` con N ≤ 100.

Detalles a tener en cuenta:

- las coordenadas de la esquina vienen de árboles distintos, así que se
  prueban todos los pares, no árbol por árbol;
- un árbol en el borde está permitido, por eso las comparaciones son
  estrictas: en el ejemplo el campo 4 3 4 tiene árboles en dos de sus
  lados y su techo sobre el borde del parque;
- sin árboles la respuesta es el lado menor del parque (prueba 02).

## Notas por lenguaje

- Python descarta, para cada p, los árboles que no quedan a su derecha
  antes de probar los valores de q.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1235_geometry.cpp](1235_geometry.cpp) | G++ 13.2 x64 | geometry | O(N³) | AC | 0.015 s | 200 KB |
| [1235_geometry.go](1235_geometry.go) | Go 1.14 x64 | geometry | O(N³) | AC | 0.031 s | 1084 KB |
| [1235_geometry.java](1235_geometry.java) | Java 1.8 | geometry | O(N³) | AC | 0.093 s | 520 KB |
| [1235_geometry.py](1235_geometry.py) | Python 3.12 x64 | geometry | O(N³) | AC | 0.218 s | 524 KB |
| [1235_geometry.rs](1235_geometry.rs) | Rust 1.75 x64 | geometry | O(N³) | AC | 0.015 s | 244 KB |
