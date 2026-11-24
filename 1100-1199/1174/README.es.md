# 1174. La posición de una permutación en el orden de intercambios vecinos

[Timus 1174](https://acm.timus.ru/problem.aspx?space=1&num=1174) · dificultad 716 · math

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001; el programa generador del enunciado se basa en programas de Frank Ruskey.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un programa dado lista las `N!` permutaciones de `1..N` (`N ≤ 100`),
empezando por `1 2 … N` e intercambiando cada vez dos vecinos. Lo hace de
forma recursiva: el elemento `k` recorre paso a paso la disposición de los
elementos menores, alternando su sentido, y entre sus pasos los elementos
mayores hacen todos sus movimientos. Dada una permutación, hay que hallar
su número de línea en esa lista.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego la permutación.

## Salida

La posición, contando desde 1; puede tener más de 150 dígitos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 
2 3 1 4
```

Salida:

```
17
```

## Solución

Se miran solo los elementos `1..k` y se ignoran los mayores. Su orden
relativo cambia solo cuando se mueve `k` o uno menor, así que la lista de
esos órdenes es la misma lista para `k` elementos. En ella, el elemento
`k` hace una pasada de `k` posiciones por cada orden de `1..k−1`, y las
pasadas se alternan: la primera va del extremo derecho a la izquierda, la
siguiente de izquierda a derecha, y así sucesivamente.

Así que si `rank(k−1)` es la posición desde 0 del orden de `1..k−1`, el
orden de `1..k` está en la pasada número `rank(k−1)`, con desplazamiento
`s` dentro de ella, donde `s` es el número de elementos menores a la
izquierda de `k` cuando la pasada va a la derecha (pasadas impares), y
`k − 1` menos ese número cuando va a la izquierda (pares). Entonces
`rank(k) = rank(k−1)·k + s`, y la respuesta es `rank(N) + 1`. `O(N²)` para
las cuentas más los pasos con números grandes.

Detalles a tener en cuenta:

- el sentido depende de la paridad de `rank(k−1)`, un número grande, pero
  solo hace falta su última cifra;
- el programa empieza con el elemento `k` en el extremo derecho
  moviéndose a la izquierda, lo que hace que las pasadas pares vayan a la
  izquierda;
- `100!` tiene 158 dígitos, así que 64 bits no bastan ni de lejos.

Las respuestas se comprobaron ejecutando directamente el programa que
genera la lista para cada permutación con `N ≤ 6`, y se compararon con una
solución escrita aparte en permutaciones aleatorias de hasta 100
elementos.

## Notas por lenguaje

- Python, Go y Java usan sus enteros grandes; C++ y Rust guardan la
  posición en dígitos de base 10⁹ con una sola operación: multiplicar y
  sumar un número pequeño.

## Soluciones optimizadas

Un árbol de Fenwick cuenta las posiciones ya insertadas a la izquierda en O(log N) por elemento. La actualización multiplica un entero de hasta O(N log N) dígitos por un número pequeño y suma el desplazamiento. La tabla incluye esa aritmética.

**Envíos de las versiones optimizadas en Timus**

`1174_fenwick_math.java` (Java 1.8) №11318411 · `1174_fenwick_math.py` (Python 3.12 x64) №11318414.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321892 · Go 1.14 x64 №11322234 · Java 1.8 №11322236 · Python 3.12 x64 №11322237 · Rust 1.75 x64 №11322238.

Go 1.14 x64, envío 11321990. Tiempo 0,015 → 0,031 s, memoria 1204 → 840 KB.

Rust cuenta los números menores con máscaras de bits y actualiza el rango por grupos de dígitos de base mixta. Rust 1.75 x64, envío 11323143. Tiempo 0,031 → 0,046 s, memoria 232 → 60 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1174_math.cpp](1174_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.001 s | 180 KB | 11321892 |
| [1174_math.go](1174_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1204 KB | 11322234 |
| [1174_math.java](1174_math.java) | Java 1.8 | math | O(N²) | AC | 0.125 s | 1748 KB | 11322236 |
| [1174_math.py](1174_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.078 s | 380 KB | 11322237 |
| [1174_math.rs](1174_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.031 s | 232 KB | 11322238 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1174_fenwick_math.java](1174_fenwick_math.java) \* | Java 1.8 | fenwick, math | O(N² log N) | AC | 0.125 s | 404 KB | 11318411 |
| [1174_fenwick_math.py](1174_fenwick_math.py) | Python 3.12 x64 | fenwick, math | O(N² log N) | AC | 0.093 s | 508 KB | 11318414 |
| [1174_fenwick_math.go](1174_fenwick_math.go) \* | Go 1.14 x64 | fenwick, math | O(N² log N) | AC | 0.031 s | 840 KB | 11321990 |
| [1174_bitmask_math.rs](1174_bitmask_math.rs) \* | Rust 1.75 x64 | bitmask, math | O(N² log N) | AC | 0.046 s | 60 KB | 11323143 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
