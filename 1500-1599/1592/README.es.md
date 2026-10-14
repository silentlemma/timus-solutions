# 1592. Relojes chinos

[Timus 1592](https://acm.timus.ru/problem.aspx?space=1&num=1592) · dificultad 588 · math

Problema original de Andrey Demidov, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n ≤ 50000 relojes de esfera de 12 horas, y cada uno marca una hora
h:mm:ss. Las agujas solo se pueden girar hacia delante, y el esfuerzo es
el tiempo total que se mueven las agujas. Hay que elegir una hora para
poner en todos los relojes con el menor esfuerzo total.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y luego la hora de cada reloj como h:mm:ss, con 1 ≤ h ≤ 12.

## Salida

La hora elegida en el mismo formato.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
11:30:00
12:10:01
6:10:18
```

Salida:

```
12:10:01
```

## Solución

Se cuentan los segundos desde las 12, así que una hora es un número t de
0 a 43199. Pasar un reloj de la hora a a la hora t cuesta
(t − a) mod 43200 segundos de movimiento de agujas. Para un objetivo t,
los relojes que marcan como mucho t cuestan t − a, y los que marcan una
hora posterior cuestan una vuelta entera más, así que el total es
n·t − Σa + 43200·(número de relojes después de t). Retroceder t hasta la
hora de reloj más cercana no aumenta el esfuerzo total, así que el
mejor objetivo es una de las horas de los relojes. Tras ordenar, un
puntero mantiene el número mientras t recorre las horas de los relojes:
`O(n log n)`.

El enunciado no dice qué hora imprimir cuando varias son igual de
buenas; las soluciones imprimen la más temprana contando desde las 12.
Los resultados se contrastaron con probar las 43200 horas en entradas
pequeñas.

Detalles a tener en cuenta:

- las 12 son el inicio de la esfera: valen 0 segundos, y una respuesta
  de 0 segundos se imprime como 12:00:00;
- el esfuerzo total llega a unos 50000·43200 ≈ 2·10⁹, más de lo que
  cabe en enteros de 32 bits;
- los minutos y los segundos se imprimen con dos cifras, y la hora sin
  cero inicial.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1592_math.cpp](1592_math.cpp) | G++ 13.2 x64 | math | O(n log n) | AC | 0.062 s | 584 KB |
| [1592_math.go](1592_math.go) | Go 1.14 x64 | math | O(n log n) | AC | 0.046 s | 5708 KB |
| [1592_math.java](1592_math.java) | Java 1.8 | math | O(n log n) | AC | 0.109 s | 6124 KB |
| [1592_math.py](1592_math.py) | Python 3.12 x64 | math | O(n log n) | AC | 0.156 s | 6344 KB |
| [1592_math.rs](1592_math.rs) | Rust 1.75 x64 | math | O(n log n) | AC | 0.046 s | 1268 KB |
