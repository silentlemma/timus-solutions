# 1351. Gnusmas bueno, gnusmas muerto

[Timus 1351](https://acm.timus.ru/problem.aspx?space=1&num=1351) · dificultad 524 · geometry

Problema original de Denis Musin, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ametralladora en el origen cubre un sector entre dos rayos: el borde
derecho pasa por (X1, Y1) y el izquierdo por (X2, Y2); el sector es
menor que media vuelta. Su alcance es D ≤ 30 000. Para cada uno de
N ≤ 30 000 puntos hay que imprimir `YES` si el punto está en el sector y
a distancia no mayor que D, y `NO` en otro caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

D, X1, Y1, X2, Y2, luego N, luego N líneas con los puntos. Todos los
números son enteros de valor absoluto a lo sumo 30 000, y ningún punto
es el origen.

## Salida

N líneas con `YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 1 0 0 1
6
1 1
5 6
3 0
-1 2
0 5
-3 0
```

Salida:

```
YES
NO
YES
NO
YES
NO
```

## Solución

El sector va en sentido antihorario del borde derecho R al borde
izquierdo L. Un punto P está en él si no queda en sentido horario de R
ni en sentido antihorario de L:

- cross(R, P) = X1·y − Y1·x ≥ 0;
- cross(P, L) = x·Y2 − y·X2 ≥ 0.

Cada condición corta un semiplano, y como el sector es menor que media
vuelta, los dos semiplanos se cortan exactamente en el sector, con una
excepción: si los dos bordes están en el mismo rayo (un sector de ancho
cero), la prolongación hacia atrás de ese rayo también pasa las dos
condiciones. Así que un punto en la recta de un borde pero detrás de la
ametralladora, con producto cruzado cero y producto escalar negativo,
se descarta aparte. El
alcance se comprueba como x² + y² ≤ D², todo en enteros y sin raíces.
`O(N)`.

Detalles a tener en cuenta:

- los puntos en los bordes y en la circunferencia cuentan: `3 0` y `0 5`
  en el ejemplo;
- un punto en el rayo opuesto a un borde tiene producto cruzado cero con
  ese borde; lo descarta la otra condición, salvo en un sector de ancho
  cero, donde solo lo hace la comprobación aparte (pruebas 02 y 06);
- los productos llegan a 1,8·10⁹, más de lo que cabe en 32 bits;
- con D = 30 000 el punto (30 000, 1) queda justo fuera de alcance
  (prueba 04).

Las respuestas se compararon con una comprobación de ángulos con `atan2`
en 18 pruebas generadas y con una solución independiente en 300
sectores aleatorios, incluidos los de ancho cero.

## Notas por lenguaje

- Las cinco soluciones usan enteros de 64 bits para los productos
  cruzados y los cuadrados.
- Java lee con `StreamTokenizer`; sus valores double guardan estos
  enteros con exactitud.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1351_geometry.cpp](1351_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.031 s | 320 KB |
| [1351_geometry.go](1351_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1392 KB |
| [1351_geometry.java](1351_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.140 s | 1328 KB |
| [1351_geometry.py](1351_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 6832 KB |
| [1351_geometry.rs](1351_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1236 KB |
