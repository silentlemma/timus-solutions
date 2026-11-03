# 1377. Distancia entre celdas en una espiral rectangular

[Timus 1377](https://acm.timus.ru/problem.aspx?space=1&num=1377) · dificultad 295 · simulation

Problema original de Stanislav Vasiliev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Recorre una cuadrícula `N × M`, `2 ≤ N,M ≤ 100`, desde `(1,1)` hacia
la derecha. Sigue recto si la siguiente celda está dentro y sin visitar;
en otro caso gira en sentido horario. Se dan dos celdas distintas mediante
fila y columna, ambas dentro de la cuadrícula. Halla la diferencia absoluta
entre sus índices de visita. Tiempo: 1 segundo. Memoria: 64 MB.

## Entrada

`N M`, después `r₁ c₁` y `r₂ c₂`, con índices desde uno.

## Salida

La diferencia absoluta de los índices de visita.

## Evaluación

Se comparan los enteros como tokens separados por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
2 2
5 3
```

Salida:

```
6
```

## Solución

Simula la espiral horaria. Marca un marco exterior como visitado,
numera cada celda al entrar y gira a la derecha si la siguiente ya está
visitada. Cada paso visita una celda nueva y el marco evita salir de la
cuadrícula. La respuesta es la diferencia absoluta de ambos números.
Tiempo y espacio `O(N·M)`. Cualquiera de las dos celdas puede aparecer
primero; los rectángulos estrechos y la franja final usan las mismas reglas.

## Soluciones optimizadas

Para una celda `(r,c)` con índices desde cero, su capa es
`d = min(r,c,N−1−r,M−1−c)`. Quitando las `d` capas exteriores quedan
`h=N−2d` filas y `w=M−2d` columnas; antes se han visitado `N·M−h·w`
celdas. Se resta `d` a las coordenadas. Probando arriba, derecha, abajo e
izquierda, el desplazamiento es `c`, `w−1+r`, `w−1+h−1+w−1−c` o
`2(h+w−2)−r`, respectivamente. Si queda una sola fila o columna, es `c`
o `r`. Cada celda recibe un índice único en orden espiral; la respuesta
es la diferencia absoluta de los dos índices. Tiempo y espacio `O(1)`.

Se conservan las simulaciones como versiones sencillas. La fórmula reduce
la memoria un 57,8% en C++, 73,4% en Java y 50,2% en Python; Go pasa de
0,046 a 0,015 s (67,4% menos). C++ y Java cumplen la meta en la instantánea
del 1 de noviembre de 2026. Python ocupa el tercer puesto por tiempo y el
primero por memoria: no logra la meta más estricta de ser primero en ambas
para este lenguaje y lleva asterisco. Go no tiene competidores en la muestra
filtrada. Rust ahorra solo un 25% de memoria y un tick: no se añade como
fuente optimizada. Las fórmulas se contrastaron con una espiral generada
independientemente, incluidas franjas finales y todas las celdas pequeñas.

## Notas por lenguaje

Las cinco fuentes base simulan la misma espiral. Debajo figuran cuatro implementaciones distintas de la fórmula.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1377_simulation.cpp](1377_simulation.cpp) | G++ 13.2 x64 | simulation | O(N·M) | AC | 0.001 s | 256 KB | 11285700 |
| [1377_simulation.go](1377_simulation.go) | Go 1.14 x64 | simulation | O(N·M) | AC | 0.046 s | 1172 KB | 11285703 |
| [1377_simulation.java](1377_simulation.java) | Java 1.8 | simulation | O(N·M) | AC | 0.109 s | 1640 KB | 11285709 |
| [1377_simulation.py](1377_simulation.py) | Python 3.12 x64 | simulation | O(N·M) | AC | 0.093 s | 924 KB | 11285705 |
| [1377_simulation.rs](1377_simulation.rs) | Rust 1.75 x64 | simulation | O(N·M) | AC | 0.031 s | 272 KB | 11285712 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1377_math.cpp](1377_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 108 KB | 11308023 |
| [1377_math.go](1377_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1052 KB | 11308026 |
| [1377_math.java](1377_math.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 436 KB | 11308028 |
| [1377_math.py](1377_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 460 KB | 11308022 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
