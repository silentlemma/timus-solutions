# 1645. Carrera de esquí

[Timus 1645](https://acm.timus.ru/problem.aspx?space=1&num=1645) · dificultad 200 · fenwick

Problema original de Eugene Kurpilyansky y Alexey Samsonov, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los esquiadores 1 a n salen uno tras otro con 30 segundos de diferencia,
y la clasificación final los ordena por su propio tiempo. Solo se conoce
el orden de llegada. Para cada esquiador hay que hallar el mejor y el
peor puesto que puede ocupar.

## Entrada

n (1 ≤ n ≤ 2000) y luego los esquiadores en el orden de llegada.

## Salida

Para cada esquiador i, el mejor y el peor puesto posibles.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
3 5 1 4 2 6
```

Salida:

```
3 6
4 6
1 4
2 5
1 3
1 6
```

## Solución

Se compara el esquiador i con el j:

- j salió después y llegó antes: j fue seguro más rápido;
- j salió antes y llegó después: j fue seguro más lento;
- en otro caso cabe cualquiera de las dos cosas: solo se conoce el orden
  de llegada, no los tiempos, así que los huecos entre llegadas pueden
  compensar los 30 segundos entre salidas o no.

Así, el mejor puesto es uno más el número de los que salieron después y
llegaron antes, y el peor es uno más todos salvo los que salieron antes y
llegaron después. Sea e el número de los que salieron antes y también
llegaron antes, y p la posición de llegada de i. Los que salieron después
y llegaron antes son p − 1 − e, así que el mejor puesto es p − e y el peor
(n − i) + e + 1: todos los que salieron después más esos e. Un árbol de
Fenwick sobre las posiciones de llegada, llenado en orden de salida, da
e para cada esquiador. `O(n log n)`.

Detalles a tener en cuenta:

- llegar pronto no es quedar arriba: en el ejemplo el esquiador 1 llega
  tercero tras dos que salieron después, así que a lo sumo es tercero;
- llegar en el orden de salida no decide nada, todos los puestos quedan
  abiertos (prueba 03); llegar en orden inverso lo decide todo
  (prueba 04).

Las respuestas coinciden con una implementación aceptada independiente
en 90 carreras aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1645_fenwick.cpp](1645_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n) | AC | 0.015 s | 204 KB |
| [1645_fenwick.go](1645_fenwick.go) | Go 1.14 x64 | fenwick | O(n log n) | AC | 0.031 s | 1176 KB |
| [1645_fenwick.java](1645_fenwick.java) | Java 1.8 | fenwick | O(n log n) | AC | 0.093 s | 652 KB |
| [1645_fenwick.py](1645_fenwick.py) | Python 3.12 x64 | fenwick | O(n log n) | AC | 0.093 s | 852 KB |
| [1645_fenwick.rs](1645_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n log n) | AC | 0.046 s | 268 KB |
