# 1638. Ratón de biblioteca

[Timus 1638](https://acm.timus.ru/problem.aspx?space=1&num=1638) · dificultad 66 · math

Problema original de Alex Samsonov, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cien tomos están en una estantería, juntos y en orden creciente de
izquierda a derecha. Cada tomo tiene páginas de un grosor total dado y
dos tapas de un grosor dado. Un gusano empieza en la primera página de
un tomo y roe en línea recta hasta llegar a la última página de otro
tomo. ¿Qué longitud tiene su camino?

## Entrada

Cuatro enteros positivos hasta 100: el grosor de las páginas de un tomo,
el grosor de una tapa, el tomo donde empieza el gusano y el tomo donde
se detiene.

## Salida

La longitud del camino.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 1 1 2
```

Salida:

```
2
```

## Solución

El truco está en dónde quedan las páginas. Un libro colocado en la
estantería con el lomo hacia fuera tiene la primera página a la derecha
y la última a la izquierda, así que la primera página del tomo a toca la
tapa que mira al tomo a + 1, y la última página del tomo b toca la tapa
que mira al tomo b − 1. Con w = páginas + 2 · tapa para un tomo entero:

- a < b: solo la tapa derecha de a, los tomos intermedios y la tapa
  izquierda de b: 2 · cover + (b − a − 1) · w; el ejemplo da 2;
- a > b: el gusano atraviesa además todas las páginas de ambos tomos:
  2 · pages + 2 · cover + (a − b − 1) · w;
- a = b: solo las páginas de ese tomo.

`O(1)`.

Detalles a tener en cuenta:

- la respuesta intuitiva para los tomos 1 y 2 es un libro entero o dos,
  pero el gusano solo atraviesa las dos tapas (el ejemplo);
- en sentido contrario el camino es mucho más largo (prueba 02).

Las respuestas coinciden con una implementación aceptada independiente
en 200 pruebas aleatorias.

## Soluciones optimizadas

La solución optimizada en Java analiza los cuatro números a mano desde
un búfer pequeño en lugar de usar `Scanner`, lo que necesita mucha menos
memoria: 380 KB en lugar de 1616 KB, con el mismo tiempo. La fórmula es
la misma.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1638_math.cpp](1638_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11288456 |
| [1638_math.go](1638_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1060 KB | 11288457 |
| [1638_math.java](1638_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1616 KB | 11288459 |
| [1638_math.py](1638_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 364 KB | 11288458 |
| [1638_math.rs](1638_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB | 11303473 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1638_math_optimized.java](1638_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.140 s | 380 KB | 11303627 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
