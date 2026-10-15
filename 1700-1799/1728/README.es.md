# 1728. La maldición de Team.GOV

[Timus 1728](https://acm.timus.ru/problem.aspx?space=1&num=1728) · dificultad 524 · implementation

Problema original de Eugene Kurpilyansky (idea de Mikhail Rubinchik), del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Efremov y Kantorov eligen a un tercer miembro de una lista de
candidatos. La fuerza de un equipo es la suma de las puntuaciones de
sus miembros. Si el equipo elegido ya jugó en algún torneo anterior,
Efremov no acude; si el equipo sin él también jugó, queda
descalificado. Elegir al candidato que da el equipo más fuerte que
juega, o indicar que toda elección acaba en descalificación.

## Entrada

n (1 ≤ n ≤ 100) equipos anteriores, cada uno con un tamaño de 1 a 3 y
los apellidos en orden alfabético; todo equipo tiene a Kantorov y todo
equipo de tres tiene a Efremov. Luego las puntuaciones de Efremov y
Kantorov, m (1 ≤ m ≤ 100) y m candidatos con sus puntuaciones. Las
puntuaciones van de 1 a 666.

## Salida

`Win` y un candidato que da el equipo más fuerte, o `Fail`. Se acepta
cualquier candidato óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
3 Efremov Kantorov Rubinchik
2 Efremov Kantorov
3 Efremov Kantorov Kokovin
3 Burmistrov Efremov Kantorov
3 Efremov Kantorov Pervukhin
2 Kantorov Pervukhin
100 10
6
Fominykh 200
Komarov 34
Pervukhin 250
Golubev 23
Soboleva 50
Gein 50
```

Salida:

```
Win
Fominykh
```

### Ejemplo 2

Entrada:

```
2
3 Efremov Fominykh Kantorov
2 Fominykh Kantorov
99 666
1
Fominykh 100
```

Salida:

```
Fail
```

## Solución

Cada equipo anterior se guarda como un conjunto de apellidos. Para cada
candidato c: si {Efremov, Kantorov, c} es nuevo, juegan los tres y la
fuerza es la suma de tres puntuaciones; si no, y {Kantorov, c} es
nuevo, juegan los dos sin Efremov; si no, c no sirve. Se toma el más
fuerte de los candidatos que quedan, o `Fail` si no queda ninguno.
Tiempo esperado `O(n + m)`; `O((n + m) log n)` en C++.

En el primer ejemplo Fominykh aporta 100 + 10 + 200 = 310. Pervukhin
ya jugó con ambos y también solo con Kantorov, así que ese equipo
quedaría descalificado.

Trampas:

- un equipo se compara como conjunto de apellidos, no solo por el
  candidato: un candidato que jugó solo con Kantorov sigue trayendo a
  Efremov;
- los equipos de Efremov con Kantorov, o de Kantorov solo, nunca
  coinciden con un equipo con candidato;
- un candidato más fuerte que aleja a Efremov puede perder ante uno más
  débil con el que Efremov sí acude.

El comprobador recalcula la fuerza de cada candidato y acepta
cualquiera óptimo. Las respuestas coinciden con una implementación
aceptada independiente en 200 casos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1728_implementation.cpp](1728_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m) log n) | AC | 0.031 s | 476 KB |
| [1728_implementation.go](1728_implementation.go) | Go 1.14 x64 | implementation | O(n + m) | AC | 0.031 s | 1156 KB |
| [1728_implementation.java](1728_implementation.java) | Java 1.8 | implementation | O(n + m) | AC | 0.140 s | 2172 KB |
| [1728_implementation.py](1728_implementation.py) | Python 3.12 x64 | implementation | O(n + m) | AC | 0.109 s | 548 KB |
| [1728_implementation.rs](1728_implementation.rs) | Rust 1.75 x64 | implementation | O(n + m) | AC | 0.046 s | 464 KB |
