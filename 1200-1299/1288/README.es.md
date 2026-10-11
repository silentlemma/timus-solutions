# 1288. Astrolocalización

[Timus 1288](https://acm.timus.ru/problem.aspx?space=1&num=1288) · dificultad 2191 · simulation

Problema original de Alexander Mironenko, del Concurso Individual de la Universidad Estatal de los Urales 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un localizador da N ≤ 10 000 lecturas de 0 a 100. Hay que encontrar:

- la pared delantera: la primera lectura de 95 o más que tiene antes
  alguna lectura de 35 o menos;
- tras la pared delantera en la posición f, la lectura de la posición m
  se multiplica por 1 + (m − f) · A (0 ≤ A ≤ 0,1, como mucho tres
  decimales), y desde ahí solo se usan esos valores;
- la pared trasera: el primer valor de 95 o más al menos D posiciones
  después de la delantera, con algún valor de 35 o menos entre ambas;
- en cada una de dos zonas, posiciones de f + S a f + E pero nunca en la
  pared trasera ni más allá, el mayor valor (el primero de los iguales);
  hay un objeto si ese valor alcanza el nivel L de la zona.

Se informa de la posición de la pared delantera, la distancia de la
trasera a ella y, para cada zona, la distancia del objeto, que no hay
objeto, o que no hubo búsqueda si la zona no contiene ninguna lectura.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, D, S1, E1, L1, S2, E2, L2 y A, y luego las N lecturas.

## Salida

Las líneas del informe, palabra por palabra como en el ejemplo.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 4 1 1 50 2 2 56 0.09
9
26
96
56
21
73
73
93
96
97
```

Salida:

```
Surface found at 3.
Bottom found at 4.
Channel 1: Object at 1.
Channel 2: No object.
```

## Solución

La tarea es una simulación cuidadosa de esas reglas: una pasada por
cada pared y un recorrido por cada zona. `O(N)`.

El redondeo se evita con enteros escalados. A tiene como mucho tres decimales,
así que 1 + (m − f) · A es un número exacto de milésimas. Las lecturas
se almacenan en millonésimas (hasta seis decimales), así que cada valor
corregido es un número entero exacto de 10⁻⁹. Así los umbrales 95, 35 y
L, las comparaciones entre valores y la búsqueda del primer máximo no
necesitan tolerancia: 50 atenuado por 1 + 9 · 0,1 es exactamente 95, una
pared (prueba 06).

Detalles a tener en cuenta:

- una lectura de 95 o más antes de cualquier lectura de 35 o menos no
  es la pared delantera (prueba 03);
- un valor alto a menos de D de la pared delantera no es la trasera,
  pero puede ser un objeto (prueba 04);
- la pared trasera y lo que hay tras ella nunca se buscan, y una zona
  que cae entera allí imprime «No search.» (prueba 08);
- una zona puede pasar del final de las lecturas (prueba 07);
- sin pared delantera solo se imprime «No surface.» (prueba 02).

Las respuestas se compararon con una implementación independiente en
300 señales aleatorias.

## Notas por lenguaje

- Los decimales se analizan a mano en enteros escalados: de 64 bits,
  o de precisión arbitraria en Python.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1288_simulation.cpp](1288_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.015 s | 348 KB |
| [1288_simulation.go](1288_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.031 s | 1452 KB |
| [1288_simulation.java](1288_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.109 s | 3492 KB |
| [1288_simulation.py](1288_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.078 s | 1464 KB |
| [1288_simulation.rs](1288_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 380 KB |
