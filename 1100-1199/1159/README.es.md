# 1159. El área más grande que puede encerrar una valla de bloques dados

[Timus 1159](https://acm.timus.ru/problem.aspx?space=1&num=1159) · dificultad 755 · geometry

Problema original de Nick Durov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que usar todos los `N` bloques rectos, `3 ≤ N ≤ 100`, de longitudes
enteras hasta 100, puestos uno tras otro, como lados de una valla
cerrada. Halla el área más grande que puede encerrar la valla, con dos
cifras decimales, o `0.00` si no se puede construir ninguna valla.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego las `N` longitudes.

## Salida

El área más grande con dos decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
10
5
5
4
```

Salida:

```
28.00
```

## Solución

Un polígono con lados dados existe justo cuando el lado más largo es más
corto que la suma de los demás. Entre todos los polígonos con esos lados,
el de mayor área es el inscrito en una circunferencia (un resultado
clásico; el orden de los lados no cambia su área). Así que la tarea es
hallar esa circunferencia.

Un lado de longitud `l` en una circunferencia de radio `R` se ve desde el
centro con el ángulo `2·asin(l / 2R)`. Si el centro está dentro del
polígono, los ángulos de todos los lados suman `2π`. Si está fuera, queda
más allá del lado más largo, y el ángulo de ese lado es igual a la suma
de los de todos los demás. Con el menor radio posible, la mitad del lado
más largo, los ángulos suman al menos `2π` justo cuando el centro está
dentro; en ambos casos la ecuación correspondiente tiene una sola raíz en
`R`, que se halla por bisección con doubles. El área es la suma de los
triángulos desde el centro, `R²·sin(ángulo)/2`, restando el triángulo del
lado más largo cuando el centro está fuera.

Detalles a tener en cuenta:

- un lado más largo igual a la suma de los demás da una valla plana, de
  área `0.00`;
- con el centro fuera, el triángulo del lado más largo se resta, no se
  suma;
- el argumento de `asin` se recorta a 1 por los errores de redondeo.

Las respuestas se compararon con la fórmula de Herón en triángulos
aleatorios y con la de Brahmagupta en cuadriláteros aleatorios (300
entradas), y los bloques iguales con la fórmula del polígono regular.

## Notas por lenguaje

- Todos los lenguajes hacen la misma bisección.
- Java redondea el área mediante `BigDecimal` con empates al par, como
  `printf` en C.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1159_geometry.cpp](1159_geometry.cpp) | G++ 13.2 x64 | geometry | O(N·STEPS) | AC | 0.015 s | 224 KB |
| [1159_geometry.go](1159_geometry.go) | Go 1.14 x64 | geometry | O(N·STEPS) | AC | 0.031 s | 1112 KB |
| [1159_geometry.java](1159_geometry.java) | Java 1.8 | geometry | O(N·STEPS) | AC | 0.171 s | 4220 KB |
| [1159_geometry.py](1159_geometry.py) | Python 3.12 x64 | geometry | O(N·STEPS) | AC | 0.078 s | 596 KB |
| [1159_geometry.rs](1159_geometry.rs) | Rust 1.75 x64 | geometry | O(N·STEPS) | AC | 0.015 s | 264 KB |
