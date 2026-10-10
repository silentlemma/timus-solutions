# 1152. El menor daño de los monstruos en los balcones de una sala

[Timus 1152](https://acm.timus.ru/problem.aspx?space=1&num=1152) · dificultad 155 · bitmask

Problema original de Evgeny Bryzgalov, del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` balcones, `3 ≤ N ≤ 20`, forman un círculo, cada uno con 1 a 100
monstruos. Un disparo destruye tres balcones vecinos (el balcón `N` es
vecino del 1). Tras cada disparo, cada monstruo que sigue vivo causa una
unidad de daño. Los disparos siguen hasta que no queda ningún monstruo.
Halla el menor daño total.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego el número de monstruos de cada balcón.

## Salida

El menor daño total.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
3 4 2 2 1 4 1
```

Salida:

```
9
```

## Solución

El estado es el conjunto de balcones aún ocupados, una máscara de `N`
bits. Desde un estado, un disparo al balcón `i` limpia `i − 1`, `i` e
`i + 1` y deja el conjunto `rest`; cuesta el número de monstruos de `rest`,
y después sigue el mejor juego desde `rest`. Así, con `damage(∅) = 0`,

`damage(mask) = mínimo, sobre los disparos que aciertan algo, de alive(rest) + damage(rest)`.

Solo importan los estados alcanzables desde el círculo completo: sus
partes limpiadas son uniones de tramos de tres vecinos, y para `N = 20`
hay solo 15126. La recursión con memoria visita solo esos, con `N`
disparos cada uno, y la profundidad es como mucho `⌈N / 3⌉`. Los disparos
que no tocan ningún balcón ocupado se saltan; nunca ayudan.

Detalles a tener en cuenta:

- el círculo se cierra, así que el disparo al balcón 1 también limpia el
  balcón `N`;
- el daño tras el último disparo es cero, porque no queda nadie;
- el orden de los disparos importa, porque conviene eliminar pronto los
  grupos grandes.

Las respuestas se compararon con una tabla de abajo arriba sobre los
`2^N` subconjuntos en 120 entradas aleatorias de hasta 13 balcones y en
todas las pruebas con 20.

## Notas por lenguaje

- Todos los lenguajes memorizan la misma recursión; Python guarda los
  valores en una caché por máscara y los demás en un array de `2^N`
  elementos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1152_bitmask.cpp](1152_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(S·N²) | AC | 0.015 s | 3868 KB |
| [1152_bitmask.go](1152_bitmask.go) | Go 1.14 x64 | bitmask | O(S·N²) | AC | 0.031 s | 10052 KB |
| [1152_bitmask.java](1152_bitmask.java) | Java 1.8 | bitmask | O(S·N²) | AC | 0.125 s | 5356 KB |
| [1152_bitmask.py](1152_bitmask.py) | Python 3.12 x64 | bitmask | O(S·N²) | AC | 0.625 s | 2420 KB |
| [1152_bitmask.rs](1152_bitmask.rs) | Rust 1.75 x64 | bitmask | O(S·N²) | AC | 0.001 s | 1592 KB |
