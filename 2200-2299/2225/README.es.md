# 2225. Menos golpes de un martillo que cubre dos clavos

[Timus 2225](https://acm.timus.ru/problem.aspx?space=1&num=2225) · dificultad 422 · dsu, sorting

Problema original de Vadim Barinov, del Campeonato de los Urales 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N clavos sobresalen lᵢ centímetros. Un golpe cae sobre dos clavos
vecinos: el más alto baja 1, o ambos si están igual de altos. Hallar el
menor número de golpes para clavarlos todos. Los límites son 1 segundo y
256 MB.

## Entrada

N, 2 ≤ N ≤ 10⁵, y luego l₁ … l_N con 1 ≤ lᵢ ≤ 10⁹.

## Salida

El menor número de golpes.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
4 1 3
```

Salida:

```
7
```

### Ejemplo 2

Entrada:

```
4
2 2 6 6
```

Salida:

```
8
```

## Solución

Se miran los clavos nivel por nivel, desde arriba. En el nivel h los
clavos de altura al menos h forman rachas maximales de vecinos. Un golpe
baja a lo sumo dos clavos, y solo dos clavos de la misma altura que
están juntos, así que una racha de k clavos en ese nivel necesita
⌈k / 2⌉ golpes, y clavar las rachas nivel a nivel desde arriba alcanza
exactamente esa cuenta. La respuesta es la suma de ⌈k / 2⌉ sobre todas
las rachas de todos los niveles, lo que también confirma una fuerza
bruta en casos pequeños.

Hay hasta 10⁹ niveles, pero las rachas solo cambian en las alturas de
los clavos. Se procesan los clavos del más alto hacia abajo y se une
cada uno con los vecinos ya procesados en una unión de conjuntos
disjuntos. Un clavo nuevo es una racha de longitud 1, que suma 1 en cada
nivel hasta su altura, así que suma su altura. Unir dos rachas cambia
⌈a / 2⌉ + ⌈b / 2⌉ por ⌈(a + b) / 2⌉, uno menos exactamente cuando ambas
longitudes son impares, y la racha unida dura en todos los niveles hasta
la altura actual, así que esa unión resta la altura actual.

En el primer ejemplo los niveles tienen la racha {1} en la altura 4,
{1} y {3} en las alturas 3 y 2, y {1, 2, 3} en la altura 1, así que la
respuesta es 1 + 2 + 2 + 2 = 7.

La ordenación da O(N log N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2225_dsu_sorting.cpp](2225_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.031 s | 1788 KB |
| [2225_dsu_sorting.go](2225_dsu_sorting.go) | Go 1.14 x64 | dsu, sorting | O(N log N) | AC | 0.125 s | 5764 KB |
| [2225_dsu_sorting.java](2225_dsu_sorting.java) | Java 1.8 | dsu, sorting | O(N log N) | AC | 0.187 s | 2624 KB |
| [2225_dsu_sorting.py](2225_dsu_sorting.py) | PyPy 3.10 x64 | dsu, sorting | O(N log N) | AC | 0.359 s | 19808 KB |
| [2225_dsu_sorting.rs](2225_dsu_sorting.rs) | Rust 1.75 x64 | dsu, sorting | O(N log N) | AC | 0.062 s | 4660 KB |
