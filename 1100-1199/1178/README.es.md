# 1178. Emparejar ciudades con carreteras rectas que no se crucen

[Timus 1178](https://acm.timus.ru/problem.aspx?space=1&num=1178) · dificultad 150 · geometry

Problema original de Pavel Atnashev, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay un número par `N ≤ 10000` de ciudades en puntos enteros con
coordenadas de hasta `10⁹` en valor absoluto, sin tres en una misma
recta. Hay que unirlas por parejas con carreteras rectas, cada ciudad en
exactamente una carretera, sin que dos carreteras se crucen.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego las coordenadas de las ciudades.

## Salida

`N/2` líneas, cada una con los números de las dos ciudades que une una
carretera.

## Evaluación

Se acepta cualquier plan que empareje cada ciudad exactamente una vez y en
el que dos carreteras nunca se toquen; el comprobador compara las
carreteras cuyos rangos de `x` se solapan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 2
1 1
3 4
4 4
```

Salida:

```
1 3
2 4
```

## Solución

Se ordenan las ciudades por `x` y se une la primera con la segunda, la
tercera con la cuarta, y así sucesivamente. Cada carretera queda en su
propia franja vertical entre las `x` de sus extremos, y las franjas de
carreteras distintas se solapan como mucho en una recta de borde. En esa
recta cada carretera solo tiene un extremo, y esos extremos son ciudades
distintas, así que ahí no se tocan. Una carretera puede ser vertical si
sus dos ciudades comparten `x`, pero entonces no hay otra ciudad en esa
recta, pues no hay tres ciudades alineadas. Así que dos carreteras nunca
se tocan. `O(N log N)`.

Detalles a tener en cuenta:

- los empates en `x` no necesitan cuidado especial, aunque las soluciones
  los ordenan por `y` para que la salida sea reproducible;
- las coordenadas llegan a `10⁹`, así que se leen como enteros de 64
  bits, aunque la solución solo las compara.

Cada plan impreso pasó el comprobador en todas las pruebas, incluidas diez
mil ciudades sobre cónicas con muchos valores de `x` compartidos.

## Notas por lenguaje

- Todos los lenguajes ordenan los números de las ciudades por el par
  `(x, y)`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1178_geometry.cpp](1178_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 388 KB |
| [1178_geometry.go](1178_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1676 KB |
| [1178_geometry.java](1178_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 6872 KB |
| [1178_geometry.py](1178_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 3276 KB |
| [1178_geometry.rs](1178_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.015 s | 764 KB |
