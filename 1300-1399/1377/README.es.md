# 1377. Lara Croft

[Timus 1377](https://acm.timus.ru/problem.aspx?space=1&num=1377) · dificultad 296 · simulation

Problema original de Stanislav Vasiliev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cementerio tiene N filas de M tumbas, 2 ≤ N, M ≤ 100. Cada noche Lara
excava bajo una tumba, empezando en (1, 1) hacia el este: el túnel sigue
recto mientras la tumba siguiente está intacta y gira a la derecha ante
el muro o una tumba ya excavada. Dos tumbas dadas guardan tesoros, y
Lara acaba de encontrar uno. Hay que imprimir cuántas noches después se
encuentra el otro.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego las dos tumbas con tesoro (r₁, c₁) y (r₂, c₂).

## Salida

El número de noches entre los dos hallazgos.

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

El túnel es la misma espiral en sentido horario que en
[1364](../1364/README.es.md). Se excava entera, numerando cada tumba por
la noche en que se excava, con un marco de celdas «excavadas» alrededor
del cementerio en lugar del muro. La respuesta es la diferencia de los
dos números sin signo, porque cualquiera de los tesoros puede salir
primero. `O(N · M)`.

Detalles a tener en cuenta:

- los tesoros pueden darse en cualquier orden (prueba 03);
- la primera y la última tumba de un cementerio de 100 × 100 distan
  9 999 noches (prueba 04);
- en un cementerio de dos columnas la espiral baja por una columna y
  sube por la otra (prueba 07).

## Notas por lenguaje

- Las cinco soluciones excavan la misma espiral.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1377_simulation.cpp](1377_simulation.cpp) | G++ 13.2 x64 | simulation | O(N·M) | AC | 0.001 s | 256 KB |
| [1377_simulation.go](1377_simulation.go) | Go 1.14 x64 | simulation | O(N·M) | AC | 0.046 s | 1172 KB |
| [1377_simulation.java](1377_simulation.java) | Java 1.8 | simulation | O(N·M) | AC | 0.109 s | 1640 KB |
| [1377_simulation.py](1377_simulation.py) | Python 3.12 x64 | simulation | O(N·M) | AC | 0.093 s | 924 KB |
| [1377_simulation.rs](1377_simulation.rs) | Rust 1.75 x64 | simulation | O(N·M) | AC | 0.031 s | 272 KB |
