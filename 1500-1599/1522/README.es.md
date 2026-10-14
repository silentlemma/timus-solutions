# 1522. Fábrica

[Timus 1522](https://acm.timus.ru/problem.aspx?space=1&num=1522) · dificultad 1764 · greedy

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N juguetes (1 ≤ N ≤ 10⁵) pasan por las máquinas A, B y C en este orden,
tardando ai, bi y ci unidades de tiempo (cada una de 1 a 10⁶); cada
máquina trata un juguete a la vez, y los juguetes pueden ir en
cualquier orden, el mismo en todas las máquinas. La máquina B es
rápida: max bi ≤ min ai o max bi ≤ min ci. Hay que hallar el menor
tiempo para terminar todos los juguetes y un orden que lo logre.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego ai, bi y ci de cada juguete.

## Salida

El menor tiempo y luego un orden óptimo de los juguetes. Se acepta
cualquier orden óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
3 1 6
1 1 2
5 2 5
7 1 4
10 2 8
```

Salida:

```
33
2 1 3 5 4
```

### Ejemplo 2

Entrada:

```
1
5 4 7
```

Salida:

```
16
1
```

## Solución

Cuando B está dominada así, la línea se comporta como dos máquinas con
tiempos ai + bi y bi + ci, y la regla de Johnson para dos máquinas da
un orden óptimo: primero los juguetes con ai + bi < bi + ci, por ai + bi
creciente, y luego el resto por bi + ci decreciente. El tiempo se
obtiene simulando el orden: cada máquina empieza un juguete cuando
están libres tanto ella como la etapa anterior del juguete.
`O(N log N)`.

Detalles a tener en cuenta:

- la regla se apoya en la condición sobre B; el problema general de tres
  máquinas es mucho más difícil;
- B puede estar dominada por C en lugar de A (prueba 04, gen2);
- los juguetes con tiempos combinados iguales pueden ir en cualquiera
  de los dos grupos (pruebas 03, 05);
- el total llega a unos 3·10¹¹, más de 32 bits (gen3);
- puede haber muchos órdenes óptimos, así que las pruebas usan un
  comprobador (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1522_greedy.cpp](1522_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.187 s | 4564 KB |
| [1522_greedy.go](1522_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.062 s | 9752 KB |
| [1522_greedy.java](1522_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.281 s | 10816 KB |
| [1522_greedy.py](1522_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.343 s | 50996 KB |
| [1522_greedy.rs](1522_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.078 s | 11432 KB |
