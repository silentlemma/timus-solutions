# 1049. La última cifra del número de divisores de un producto

[Timus 1049](https://acm.timus.ru/problem.aspx?space=1&num=1049) · dificultad 249 · number_theory

Problema original de Stanislav Vasiliev, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan diez enteros `a1 … a10`, cada uno de 1 a 10000. Halla la última
cifra del número de divisores positivos del producto `a1 · … · a10`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Diez enteros, uno por línea.

## Salida

Una cifra: la última cifra del número de divisores.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
2
6
1
3
1
1
1
1
1
```

Salida:

```
9
```

### Ejemplo 2

Entrada:

```
1
1
1
1
1
1
1
1
1
1
```

Salida:

```
1
```

## Solución

Si `P = p1^e1 · p2^e2 · … · pk^ek`, un divisor de `P` elige cada
exponente de forma independiente entre `0` y `ei`, así que `P` tiene
`(e1 + 1)(e2 + 1)…(ek + 1)` divisores.

El producto puede tener 40 cifras, pero no hace falta: se factoriza cada
número por división de prueba hasta su raíz cuadrada (como mucho 100
pasos), se suman los exponentes de los primos iguales y se multiplican los
`(e + 1)` módulo 10. `O(10 · √10000)`.

Detalles a tener en cuenta:

- los exponentes deben sumarse sobre los diez números antes del `+ 1`:
  `2 · 2` tiene 3 divisores, no `2 · 2`;
- un factor primo mayor que la raíz cuadrada queda tras la división de
  prueba y también cuenta;
- la última cifra puede ser 0 (48 = `2^4 · 3` tiene 10 divisores).

## Notas por lenguaje

- Todos los lenguajes usan la misma división de prueba y un mapa de
  primos a exponentes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1049_number_theory.cpp](1049_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 184 KB |
| [1049_number_theory.go](1049_number_theory.go) | Go 1.14 x64 | number_theory | O(10 · √10000) | AC | 0.031 s | 1108 KB |
| [1049_number_theory.java](1049_number_theory.java) | Java 1.8 | number_theory | O(10 · √10000) | AC | 0.140 s | 3880 KB |
| [1049_number_theory.py](1049_number_theory.py) | Python 3.12 x64 | number_theory | O(10 · √10000) | AC | 0.078 s | 456 KB |
| [1049_number_theory.rs](1049_number_theory.rs) | Rust 1.75 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 416 KB |
