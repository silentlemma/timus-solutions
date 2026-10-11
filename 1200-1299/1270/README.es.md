# 1270. Unicubo

[Timus 1270](https://acm.timus.ru/problem.aspx?space=1&num=1270) · dificultad 2239 · matching

Problema original de Alexander Mironenko, del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay 1 ≤ N ≤ 30 cubos, cada cara pintada de uno de 30 colores, dados en el
orden delante, arriba, derecha, abajo, izquierda, detrás. Una figura
tiene 1 ≤ M ≤ 30 celdas, cada una con exigencias sobre los colores de sus
seis caras (0 significa cualquier color). Hay que poner un cubo
distinto, girado como haga falta, en cada celda para cumplir todas las
exigencias, e imprimir el número de cubo de cada celda, o 0 si es
imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, los N cubos, M y luego M líneas `X Y Z F U R D L B`.

## Salida

M números de cubo, o 0.

## Evaluación

Puede haber varias asignaciones válidas, así que el evaluador acepta
cualquiera: los números deben ser distintos y cada cubo debe cumplir las
exigencias de su celda en uno de los 24 giros. La respuesta 0 solo se
acepta cuando la respuesta esperada es 0.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
6 1 3 4 5 2
1
0 0 0 1 2 3 6 5 4
```

Salida:

```
1
```

## Solución

La posición de la celda no importa: las exigencias son solo sobre caras
y los cubos vecinos no interactúan. Así que es un emparejamiento
bipartito entre celdas y cubos. Un cubo puede ir a una celda si uno de
sus 24 giros cumple todas las exigencias de la celda. Los giros se
obtienen cerrando bajo composición dos cuartos de vuelta, sobre el eje
vertical y sobre el eje izquierda-derecha. Salen exactamente los 24
giros propios y ninguna imagen especular. Luego el algoritmo de Kuhn
busca un camino de aumento desde cada celda; si alguno falla, la
respuesta es 0. `O(M · N · 24 · 6 + M · N · M)`.

Detalles a tener en cuenta:

- solo se permiten giros: un cubo cuya imagen especular encaja en una
  celda puede no encajar él mismo (prueba 02);
- una elección voraz puede bloquear una celda posterior, así que el
  emparejamiento debe poder mover cubos ya colocados (prueba 05);
- con más celdas que cubos no hay respuesta (prueba 03).

La existencia de asignación se comparó con probar todas las
asignaciones inyectivas en 300 casos pequeños aleatorios.

## Notas por lenguaje

- Todos los lenguajes construyen los giros igual y ejecutan el algoritmo
  de Kuhn de forma recursiva; la profundidad es como mucho 30.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1270_matching.cpp](1270_matching.cpp) | G++ 13.2 x64 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.015 s | 212 KB |
| [1270_matching.go](1270_matching.go) | Go 1.14 x64 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.031 s | 1184 KB |
| [1270_matching.java](1270_matching.java) | Java 1.8 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.093 s | 716 KB |
| [1270_matching.py](1270_matching.py) | Python 3.12 x64 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.093 s | 752 KB |
| [1270_matching.rs](1270_matching.rs) | Rust 1.75 x64 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.015 s | 452 KB |
