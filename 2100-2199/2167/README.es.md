# 2167. La menor clave XOR que convierte un número en primo

[Timus 2167](https://acm.timus.ru/problem.aspx?space=1&num=2167) · dificultad 503 · bitmask, number_theory

Problema original de Vadim Barinov, del Concurso por Equipos de Programación de los Urales 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada uno de los T números a menores que 2²⁰, hallar la menor clave
no negativa k tal que a XOR k sea primo. Los límites son 2 segundos y
256 MB.

## Entrada

T, 1 ≤ T ≤ 10⁵, y luego los números, 0 ≤ a ≤ 1 048 575.

## Salida

La menor clave de cada número.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
5
6
1
```

Salida:

```
0
1
2
```

## Solución

Para un a fijo, la clave k = a XOR p está en biyección con el primo p,
así que hay que hallar el primo p que minimiza a XOR p. Las claves
menores que 2²⁰ ya alcanzan todos los primos menores que 2²⁰, entre
ellos el 2, y un primo mayor necesitaría una clave de al menos 2²⁰, así
que solo importan los primos menores que 2²⁰.

El XOR es menor cuanto más bits altos de p coinciden con a. Se criban
los primos menores que 2²⁰ y se construye, para cada j, una tabla que
dice si algún primo empieza por un prefijo dado de j bits; cada tabla es
el OR de pares de entradas de la siguiente. Una consulta elige los bits
de p desde arriba: conserva el bit de a si algún primo tiene ese prefijo
más largo, y toma el otro bit si no. Son 20 pasos por número tras una
preparación de O(2²⁰ log log 2²⁰).

En el ejemplo 5 es primo, 6 XOR 1 = 7 y 1 XOR 2 = 3.

La versión didáctica en C++ criba los primos menores que U = 2²⁰. Para cada a prueba claves en orden creciente hasta que a XOR k sea primo. La primera es la mínima. Existe una clave menor que U porque a XOR 2 permite obtener el primo 2. La comprobación exhaustiva de los U valores dio 95 como respuesta máxima. La criba requiere O(U log log U) tiempo y O(U) espacio. En este rango cada consulta hace como máximo 96 accesos a la tabla.

## Soluciones optimizadas

C++ empaqueta el mismo árbol de prefijos en un bit por nodo de montón. U=2²⁰ exige 2U bits, 262144 bytes. Las hojas son la criba: iniciar impares y dos, borrar uno y compuestos impares. La máscara de paridad no almacena primos ni respuestas. Cada bit interno es OR de hijos. Desde la raíz uno se prefiere el hijo con el bit de entrada si contiene algún primo. Así el bit XOR pendiente más alto queda a cero cuando es posible. Si esa rama está vacía, se toma la otra. El índice de la hoja menos U da el primo p y se imprime el XOR de la consulta con p. Búferes acotados sustituyen la cadena creciente. Tiempo O(U log log U+T log U), espacio O(U) bits. Se conservan bases; las otras familias reutilizan las admitidas.

Las implementaciones base aceptadas [2167_bitmask_number_theory.go](2167_bitmask_number_theory.go), [2167_bitmask_number_theory.java](2167_bitmask_number_theory.java), [2167_bitmask_number_theory.py](2167_bitmask_number_theory.py), [2167_bitmask_number_theory.rs](2167_bitmask_number_theory.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`2167_bitmask_number_theory_optimized.py`. Se precalculan las respuestas XOR de cada bloque de 16 valores con sus ocho posiciones impares, tratando el primo 2 aparte. Solo si el bloque actual no contiene primos se busca en un trie de los 16 bits superiores. La criba y las tablas se generan al ejecutar; se verificó independientemente todo el dominio de 20 bits. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328685 (Python 3.12 x64): **0.312 s / 13876 KB**. Comparación archivada: `2167_bitmask_number_theory.py` (Python 3.12 x64) — 0.64 s / 16760 KB (#11328350).

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`2167_number_theory_optimized.rs`. Se genera una criba de bits de primos impares y se prueban claves XOR crecientes hasta el primer primo. XOR permuta el dominio finito, por lo que existe solución. No se usa un límite precalculado; se verificaron todas las consultas de 20 bits.

Accepted #11328991 (Rust 1.75 x64): **0.031 s / 128 KB**. Comparación archivada: `2167_bitmask_number_theory.rs` (Rust 1.75 x64) — 0.046 s / 4172 KB (#11328351).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2167_bitmask_number_theory.cpp](2167_bitmask_number_theory.cpp) | G++ 13.2 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.093 s | 2268 KB | 11328348 |
| [2167_bitmask_number_theory.go](2167_bitmask_number_theory.go) | Go 1.14 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.031 s | 3080 KB | 11295059 |
| [2167_bitmask_number_theory.java](2167_bitmask_number_theory.java) | Java 1.8 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.171 s | 4856 KB | 11328349 |
| [2167_bitmask_number_theory.py](2167_bitmask_number_theory.py) | Python 3.12 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.64 s | 16760 KB | 11328350 |
| [2167_bitmask_number_theory.rs](2167_bitmask_number_theory.rs) | Rust 1.75 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.046 s | 4172 KB | 11328351 |
| [2167_number_theory.cpp](2167_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(U log log U + 96 T) | AC | 0.109 s | 1136 KB | 11315938 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2167_bitmask_number_theory_optimized.cpp](2167_bitmask_number_theory_optimized.cpp) | G++ 13.2 x64 | bitmask, number_theory | O(U log log U + T log U) | AC | 0.031 s | 336 KB | 11315846 |
| [2167_bitmask_number_theory_optimized.py](2167_bitmask_number_theory_optimized.py) | Python 3.12 x64 | bitmask, number_theory | O(2^20 log log 2^20 + 20 T) | AC | 0.312 s | 13876 KB | 11328685 |
| [2167_number_theory_optimized.rs](2167_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(L log log L + sum(K_i)) time; O(L) bits, L=2^20 | AC | 0.031 s | 128 KB | 11328991 |
