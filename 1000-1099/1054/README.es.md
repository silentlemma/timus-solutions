# 1054. El número de paso de una posición de la Torre de Hanói

[Timus 1054](https://acm.timus.ru/problem.aspx?space=1&num=1054) · dificultad 643 · math

Problema original de la Academia Estatal de Aviación de Rybinsk.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` discos (`1 ≤ N ≤ 31`, el disco 1 es el más pequeño) empiezan en la
varilla 1 y se llevan a la varilla 2 con la recursión óptima clásica

```text
Hanoi(n, from, to, via):
    si n > 0:
        Hanoi(n − 1, from, via, to)
        mover el disco n de `from` a `to`
        Hanoi(n − 1, via, to, from)
```

llamada como `Hanoi(N, 1, 2, 3)`. Una posición da la varilla de cada
disco. Halla tras cuántos movimientos aparece la posición dada, o `-1` si
no aparece nunca.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego las varillas `D1 … DN` de los discos `1 … N`, una por línea.

## Salida

El número de movimientos, o `-1`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
3
3
1
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
1
3
```

Salida:

```
-1
```

## Solución

Se sigue la recursión desde el disco más grande hacia abajo. Mientras los
discos `1 … k` se llevan de `a` a `b` pasando por `c`, el disco `k` se
mueve exactamente una vez, tras los primeros `2^(k−1) − 1` movimientos
(que llevan los discos `1 … k − 1` a `c`). Así:

- el disco `k` sigue en `a`: estamos en la primera mitad; se sigue con los
  discos `1 … k − 1` que van de `a` a `c` pasando por `b`;
- el disco `k` está en `b`: la primera mitad y el movimiento del disco
  `k` ya se hicieron, son `2^(k−1)` movimientos; se sigue con los discos
  `1 … k − 1` que van de `c` a `b` pasando por `a`;
- el disco `k` está en `c`: esto nunca ocurre, la respuesta es `-1`.

La suma de `2^(k−1)` de todos los discos que están en su varilla de
destino da el número de paso. `O(N)`.

Detalles a tener en cuenta:

- las varillas intercambian sus papeles en cada nivel; que el disco más
  pequeño vaya primero a la varilla 2 o a la 3 depende de la paridad de
  `N`;
- la posición final de 31 discos se alcanza tras `2^31 − 1` movimientos,
  el máximo de un entero de 32 bits con signo;
- un solo disco en la varilla «equivocada» hace inalcanzable toda la
  posición.

## Notas por lenguaje

- Todos los lenguajes recorren los discos con el mismo bucle y tres
  variables para los papeles de las varillas.

## Soluciones optimizadas

La versión en C++ guarda las posiciones de hasta 31 discos en un búfer fijo. Al recorrerlos desde el mayor añade un bit al número de movimientos. El bit vale cero en la clavija de origen y uno en la de destino. Un disco en la clavija auxiliar indica que la posición es inalcanzable. El tiempo es O(N) y el espacio adicional al búfer es O(1). Las métricas corresponden al envío 11316991.

La versión de Python que ahorra memoria elimina los espacios de los bytes de entrada y recorre las varillas en orden inverso, añadiendo un bit al número de movimientos por disco. El envío aceptado 11322407 usó 280 KB con PyPy 3.10 x64, un 30% menos que los 400 KB de la versión sencilla con Python 3.12 x64. El tiempo subió de 0.078 s a 0.140 s.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322200 · Go 1.14 x64 №11322203 · Python 3.12 x64 №11321923 · Rust 1.75 x64 №11322205 · Java 1.8 №11321869.

El envío 11317962 en Rust tardó 0.015 s y usó 204 KB. La versión sencilla tardó 0.046 s y usó 204 KB.

Se leen los números de las varillas como dígitos ASCII y se recorren los discos de mayor a menor. Cada disco añade un bit al número de movimientos. Un disco en la varilla auxiliar indica una posición inalcanzable.

Go guarda las posiciones de los discos en un arreglo fijo y recorre del mayor al menor. Cada posición determina el siguiente bit del número de movimientos o demuestra que la configuración es inalcanzable. Go 1.14 x64, envío 11322837. Tiempo 0,031 → 0,015 s, memoria 1076 → 276 KB.

Java guarda los números de las varillas en un arreglo de bytes y recorre los discos del mayor al menor, añadiendo un bit al número de movimientos. Calcula la varilla auxiliar a partir de la suma de los tres números. El envío 11323975 tardó 0.109 s y usó 356 KB, frente a 0.125 s y 1608 KB de la versión sencilla.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1054_math.cpp](1054_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 180 KB | 11322200 |
| [1054_math.go](1054_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1076 KB | 11322203 |
| [1054_math.java](1054_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 1608 KB | 11321869 |
| [1054_math.py](1054_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 400 KB | 11321923 |
| [1054_math.rs](1054_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 204 KB | 11322205 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1054_math_optimized.cpp](1054_math_optimized.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 112 KB | 11316991 |
| [1054_math_optimized.py](1054_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N) | AC | 0.140 s | 280 KB | 11322407 |
| [1054_math_optimized.rs](1054_math_optimized.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 204 KB | 11317962 |
| [1054_math_optimized.go](1054_math_optimized.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 276 KB | 11322837 |
| [1054_math_optimized.java](1054_math_optimized.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 356 KB | 11323975 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
