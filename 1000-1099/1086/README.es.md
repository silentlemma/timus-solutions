# 1086. El n-ésimo número primo

[Timus 1086](https://acm.timus.ru/problem.aspx?space=1&num=1086) · dificultad 107 · number_theory

Problema original del folclore, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada uno de `k` números `n` (`1 ≤ n ≤ 15000`) imprime el `n`-ésimo
número primo. El 1 no es primo.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`k` (`1 ≤ k ≤ 15000`) y luego `k` líneas con `n`.

## Salida

El `n`-ésimo primo para cada `n`, uno por línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
2
5
7
```

Salida:

```
5
3
11
17
```

## Solución

El primo número 15000 es 163 841, así que una criba de Eratóstenes hasta
ese número lista todos los primos que se pueden pedir, y cada consulta es
un índice en la lista. `O(L log log L)` para la criba con `L = 163 842`,
`O(1)` por consulta.

Detalles a tener en cuenta:

- el primer primo es 2, no 1;
- el límite de la criba debe cubrir el propio primo número 15000; se puede
  hallar una vez por cualquier método y escribirlo en el programa;
- puede haber hasta 15000 consultas, así que los primos se calculan
  una sola vez y no en cada consulta.

Las respuestas se comprobaron con primos hallados uno a uno por división
de prueba.

## Soluciones optimizadas

La solución optimizada en Go criba solo los números impares, lo que
reduce la criba a la mitad, guarda exactamente 15000 primos como
`uint32`, que basta porque todos son menores que 163 842, en lugar de un
slice de `int` que crece, y lee los números byte a byte y los imprime
con `strconv` en lugar de `fmt`: {1086_number_theory_optimized.go}.

La solución optimizada en Java criba solo los números impares, lo que
reduce la criba a la mitad, guarda un arreglo de exactamente 15000
primos en lugar de 163 842 casillas, analiza la entrada en bloques de
8 KB en lugar de usar `StreamTokenizer` e imprime los dígitos a través
de un búfer de bytes de 8 KB en lugar de acumular toda la salida en un
`StringBuilder`: {1086_number_theory_optimized.java}.

La solución optimizada en Python criba solo los números impares, lo que
reduce el `bytearray` a la mitad, guarda los primos en un `array` de
enteros sin signo de 32 bits, que basta porque todos son menores que
163 842, en lugar de una lista de enteros de Python, lee las consultas
línea a línea en lugar de dividir toda la entrada de una vez e imprime
las respuestas en tandas de 1024: {1086_number_theory_optimized.py}.

La solución optimizada en Rust criba solo los números impares, lo que
reduce la criba a la mitad, guarda exactamente 15000 primos como `u32`,
que basta porque todos son menores que 163 842, en un vector reservado
de antemano en lugar de un `Vec<usize>` que crece, y escribe las
respuestas con un `BufWriter` en lugar de crear una cadena por respuesta
y unirlas: {1086_number_theory_optimized.rs}.

La versión optimizada de C++ conserva la misma criba, pero representa solo los impares en un vector de bits compacto (unos 10 KB). La lista ordenada guarda los 16 bits bajos de cada uno de los 15000 primos en 30 KB. Todos son menores que tres veces `2^16`; dos índices límite, calculados al generar los primos, indican si hay que añadir cero, uno o dos múltiplos de `2^16` al responder. Las consultas siguen siendo constantes y no hay una tabla de respuestas precalculada. El tiempo total es `O(L log log L + k)` y el espacio `O(L + P)`, con límite de criba `L` y cantidad de primos `P`. La implementación con vectores normales se conserva como básica.

Ejecuciones Accepted correspondientes al código: versión básica 0.031 s / 212 KB; esta versión 0.015 s / 148 KB (envío 11307512). La memoria baja un 30.19%; la diferencia de un solo salto del reloj no se usa como prueba de aceleración. Cumple el objetivo en la clasificación actualizada.

{1086_number_theory_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1086_number_theory_optimized.cpp`: reducción de tiempo +51.61%;
  reducción de memoria +30.19%; base: `1086_number_theory.cpp`.

- `1086_number_theory_optimized.go`: reducción de tiempo +0.00%;
  reducción de memoria +48.87%; base: `1086_number_theory.go`.

- `1086_number_theory_optimized.java`: reducción de tiempo +16.13%;
  reducción de memoria +72.98%; base: `1086_number_theory.java`.

- `1086_number_theory_optimized.py`: reducción de tiempo +0.00%;
  reducción de memoria +64.25%; base: `1086_number_theory.py`.

- `1086_number_theory_optimized.rs`: reducción de tiempo +0.00%;
  reducción de memoria +50.79%; base: `1086_number_theory.rs`.

## Notas por lenguaje

- Python tacha los múltiplos asignando cortes en un `bytearray`.
- C++, Go, Java y Rust empiezan a tachar en `p²`; C++ y Java lo calculan
  en 64 bits en la versión básica de C++ y en Java para evitar desbordamientos.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1086_number_theory.cpp](1086_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L) | AC | 0.031 s | 212 KB | 11279046 |
| [1086_number_theory.go](1086_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L) | AC | 0.001 s | 2308 KB | 11279049 |
| [1086_number_theory.java](1086_number_theory.java) | Java 1.8 | number_theory | O(L log log L) | AC | 0.093 s | 2132 KB | 11279053 |
| [1086_number_theory.py](1086_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L) | AC | 0.093 s | 2764 KB | 11279050 |
| [1086_number_theory.rs](1086_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L) | AC | 0.001 s | 1268 KB | 11279055 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1086_number_theory_optimized.cpp](1086_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(L log log L) | AC | 0.015 s | 148 KB | 11307512 |
| [1086_number_theory_optimized.go](1086_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(L log log L) | AC | 0.015 s | 1180 KB | 11304263 |
| [1086_number_theory_optimized.java](1086_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(L log log L) | AC | 0.078 s | 576 KB | 11304023 |
| [1086_number_theory_optimized.py](1086_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(L log log L) | AC | 0.093 s | 988 KB | 11304024 |
| [1086_number_theory_optimized.rs](1086_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(L log log L) | AC | 0.001 s | 624 KB | 11304043 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
