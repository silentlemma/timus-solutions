# 1078. La cadena más larga de segmentos anidados uno dentro del siguiente

[Timus 1078](https://acm.timus.ru/problem.aspx?space=1&num=1078) · dificultad 354 · dp

Problema original de Emil Kelevedzhiev, del Torneo de Informática del Festival Matemático de Invierno, Varna 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` segmentos en una recta (`0 < N < 500`) tienen extremos enteros en
`[−10000, 10000]`. Un segmento está dentro de otro si cabe en él y ninguno
de sus extremos coincide con un extremo del otro. Halla la secuencia más
larga de segmentos en la que cada uno está dentro del siguiente, e
imprime su longitud y los números de sus segmentos del más corto al más
largo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con los extremos izquierdo y derecho de un
segmento.

## Salida

La longitud de la secuencia y luego los números de sus segmentos.

## Evaluación

Se acepta cualquier secuencia más larga. El comprobador verifica que su
longitud es la mayor posible y que cada segmento listado está
estrictamente dentro del siguiente.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
-2 2
-1 1
-3 3
4 5
```

Salida:

```
3
2 1 3
```

## Solución

«Dentro» significa `L₂ < L₁` y `R₁ < R₂`, así que un segmento dentro de
otro es estrictamente más corto. Ordenados por longitud, los segmentos
forman un orden topológico de la relación de anidamiento, y el camino más
largo en este orden es una programación dinámica sencilla:
`best[i] = 1 + max best[j]` sobre los segmentos más cortos `j` que están
dentro de `i`, y `prev[i]` recuerda la elección. La respuesta termina en
el segmento con el mayor `best`, y siguiendo `prev` se obtiene la cadena
de fuera hacia dentro, así que se imprime al revés. `O(N^2)`.

Detalles a tener en cuenta:

- los extremos comunes no cuentan: `[0, 1]` no está dentro de `[0, 3]`, y
  los segmentos iguales no están uno dentro del otro;
- un segmento de longitud cero puede estar dentro de otro, y nada puede
  estar dentro de él;
- el orden debe ir del segmento más corto al más largo;
- si un segmento viene con los extremos en el otro orden, las soluciones
  los intercambian, lo que describe el mismo segmento.

El comprobador halla la mayor longitud con una búsqueda memorizada sobre
todos los segmentos y comprueba la cadena listada.

## Notas por lenguaje

- Python lee los extremos con cortes con paso y construye `left` y
  `right` con `min` y `max`.
- Rust elige el último segmento con `max_by_key`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1078_dp.cpp](1078_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 204 KB |
| [1078_dp.go](1078_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 3448 KB |
| [1078_dp.java](1078_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.140 s | 4608 KB |
| [1078_dp.py](1078_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 888 KB |
| [1078_dp.rs](1078_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.031 s | 292 KB |
