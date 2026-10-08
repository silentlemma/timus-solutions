# 1012. Contar números en base K sin dos ceros seguidos, con aritmética de precisión arbitraria

[Timus 1012](https://acm.timus.ru/problem.aspx?space=1&num=1012) · dificultad 180 · dp

Problema original: una versión más difícil del [problema 1009](../1009/README.es.md).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuenta los números de `N` dígitos en base `K` (el primer dígito no es cero)
cuyos dígitos no contienen dos ceros seguidos. `2 ≤ K ≤ 10`, `N ≥ 2`,
`N + K ≤ 1800`.

Límite de tiempo: 0.5 segundos. Límite de memoria: 16 MB.

## Entrada

`N` y `K`, cada uno en su propia línea.

## Salida

La cantidad completa.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
2
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
3
10
```

Salida:

```
891
```

## Solución

La recurrencia es la del [problema 1009](../1009/README.es.md): se cuentan
los prefijos válidos según su último dígito, `zero` terminan en `0` y
`other` en un dígito no nulo:

- `zero' = other`;
- `other' = (zero + other) · (K - 1)`;

empezando con `zero = 0`, `other = K - 1`; la respuesta es `zero + other`
tras `N` dígitos.

Lo que cambia es el tamaño: la respuesta se acerca a `(K - 1)^N` y tiene
hasta unas 1 800 cifras decimales, así que hace falta aritmética de
precisión arbitraria. Solo se usan dos operaciones —la suma de dos números
grandes y el producto de un número grande por uno pequeño—, ambas lineales
en la longitud. Un número grande se guarda como un arreglo de «dígitos» en
base `10^9`, el menos significativo primero: un dígito por `K - 1` más el
acarreo cabe en 64 bits. Son `N` pasos de trabajo `O(L)`, donde `L` es la
longitud de la respuesta en bloques: unas `1800 · 200` operaciones.

Solo se guardan los dos valores actuales, así que la memoria es `O(L)`;
la tabla completa de `N` números grandes también cabría, pero no hace falta.

Detalles a tener en cuenta:

- los enteros de 64 bits se desbordan pasadas unas 20 cifras: la solución
  de la versión fácil aquí es incorrecta;
- al imprimir bloques en base `10^9`, todos salvo el más significativo
  deben rellenarse con ceros a la izquierda hasta 9 cifras.

## Notas por lenguaje

- **Python**, **Go** (`math/big`) y **Java** (`BigInteger`) tienen enteros
  grandes incorporados.
- **C++** y **Rust** implementan las dos operaciones con bloques en base
  `10^9`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1012_dp.cpp](1012_dp.cpp) | G++ 13.2 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 268 KB |
| [1012_dp.go](1012_dp.go) | Go 1.14 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 2056 KB |
| [1012_dp.java](1012_dp.java) | Java 1.8 | dp | O(N·L), L = length of the answer | AC | 0.125 s | 3860 KB |
| [1012_dp.py](1012_dp.py) | Python 3.12 x64 | dp | O(N·L), L = length of the answer | AC | 0.062 s | 340 KB |
| [1012_dp.rs](1012_dp.rs) | Rust 1.75 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 520 KB |
