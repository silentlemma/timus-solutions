# 1204. Idempotentes módulo un producto de dos primos

[Timus 1204](https://acm.timus.ru/problem.aspx?space=1&num=1204) · dificultad 229 · number_theory

Problema original de Pavel Atnashev, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número `x` es idempotente módulo `n` si `x·x ≡ x (mod n)`. Para hasta
1000 valores `n < 10⁹`, cada uno producto de dos primos distintos `p` y
`q`, hay que listar todos los idempotentes de `0` a `n − 1` en orden
creciente.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número de pruebas `k` y luego `n` para cada prueba.

## Salida

Para cada prueba, sus idempotentes en una línea en orden creciente.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
6
15
910186311
```

Salida:

```
0 1 3 4
0 1 6 10
0 1 303395437 606790875
```

## Solución

`x(x − 1) ≡ 0 (mod pq)` significa que cada uno de `p` y `q` divide a `x`
o a `x − 1`, así que módulo cada primo `x` vale 0 o 1. Por el teorema
chino del resto eso da exactamente cuatro idempotentes: 0, 1, el número
que vale 1 módulo `p` y 0 módulo `q`, y el que vale 0 módulo `p` y 1
módulo `q`. El tercero es `x = q·(q⁻¹ mod p)`, con el inverso obtenido
por el algoritmo de Euclides extendido, y el cuarto es `n + 1 − x`,
porque ambos suman 1 módulo los dos primos.

Para factorizar `n` se prueban los primos hasta `√10⁹ < 31623`, hallados
una vez con una criba; el factor menor está entre ellos. Como mucho unas
3400 divisiones por prueba. `O(k·π(√n))`.

Detalles a tener en cuenta:

- los dos idempotentes no triviales deben imprimirse en orden creciente,
  y cualquiera de los dos puede ser el menor;
- solo hay que hallar por división el factor menor; el mayor, de hasta
  `5·10⁸`, es simplemente `n / p`;
- `p` puede ser tan pequeño como 2.

Las respuestas se compararon con una solución escrita aparte en 3000
productos generados de los tres tipos.

## Notas por lenguaje

- Python calcula el inverso con `pow(q, -1, p)`; los demás lenguajes
  usan el algoritmo de Euclides extendido.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1204_number_theory.cpp](1204_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 228 KB |
| [1204_number_theory.go](1204_number_theory.go) | Go 1.14 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 1320 KB |
| [1204_number_theory.java](1204_number_theory.java) | Java 1.8 | number_theory | O(k·π(√n)) | AC | 0.171 s | 1088 KB |
| [1204_number_theory.py](1204_number_theory.py) | Python 3.12 x64 | number_theory | O(k·π(√n)) | AC | 0.312 s | 1016 KB |
| [1204_number_theory.rs](1204_number_theory.rs) | Rust 1.75 x64 | number_theory | O(k·π(√n)) | AC | 0.015 s | 268 KB |
