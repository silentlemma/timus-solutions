# 2146. Menor periodo circular tras cambiar como mucho k letras

[Timus 2146](https://acm.timus.ru/problem.aspx?space=1&num=2146) · dificultad 641 · strings

Problema original de Valentin Zuev, del Concurso por Equipos de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tambor tiene n sectores en círculo, cada uno con una letra minúscula.
Tiene periodo p cuando cada sector coincide con el que está p posiciones
más allá. Cambiar como mucho k letras para que el menor periodo sea lo
más pequeño posible, e imprimir ese periodo y el tambor nuevo. Se acepta
cualquier tambor óptimo. Los límites son 5 segundos y 256 MB.

## Entrada

n y k, 1 ≤ n ≤ 10⁵, 0 ≤ k ≤ n, y luego las n letras.

## Salida

El menor periodo y el tambor tras los cambios.

## Evaluación

Un comprobador verifica el periodo, el número de cambios y que el tambor
impreso tenga exactamente ese menor periodo.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 3
abcdef
```

Salida:

```
3
abcabc
```

### Ejemplo 2

Entrada:

```
4 1
aaab
```

Salida:

```
1
aaaa
```

### Ejemplo 3

Entrada:

```
4 0
aaab
```

Salida:

```
4
aaab
```

## Solución

En un círculo, los periodos p y n dan el periodo gcd(p, n), así que el
menor periodo siempre divide a n y solo hay que probar los divisores de
n. Para un divisor d los sectores se reparten en d clases de posiciones
con el mismo resto módulo d, y el periodo d significa que cada clase
tiene una sola letra. Lo más barato es conservar la letra más frecuente
de cada clase, así que el número de cambios es n menos la suma de esas
frecuencias.

Los divisores se prueban desde el menor, y el primero que necesita como
mucho k cambios es la respuesta, rellenando cada clase con su letra más
frecuente. Ese tambor no puede tener un periodo menor d′: sería entonces
un tambor con periodo d′ a no más de k cambios, y d′ se habría aceptado
antes. Contar las letras cuesta O(n) por divisor, y n ≤ 10⁵ tiene a lo
sumo 128 divisores.

En el primer ejemplo el periodo 3 deja las clases "ad", "be" y "cf" con
una letra cada una con tres cambios, y los periodos 1 y 2 necesitan más.

## Soluciones optimizadas

La versión optimizada en C++ procesa una clase de residuos a la vez y reutiliza los contadores de letras. Descarta un divisor en cuanto el total de cambios supera el presupuesto. Guarda un solo período y lo repite al escribir la salida. Las métricas corresponden al envío 11317091.

Go, Java y Rust también cuentan una clase de residuos a la vez con una tabla pequeña de frecuencias. Python extrae segmentos de bytes con paso y cuenta sus letras con operaciones sobre cadenas de bytes. Los envíos aceptados fueron 11317238, 11317242, 11317237 y 11317245, respectivamente.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11318161 · Java 1.8 №11318171.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2146_strings.cpp](2146_strings.cpp) | G++ 13.2 x64 | strings | O(n d(n)) | AC | 0.046 s | 10404 KB | 11318161 |
| [2146_strings.go](2146_strings.go) | Go 1.14 x64 | strings | O(n d(n)) | AC | 0.203 s | 51504 KB | 11322045 |
| [2146_strings.java](2146_strings.java) | Java 1.8 | strings | O(n d(n)) | AC | 0.156 s | 15172 KB | 11318171 |
| [2146_strings.py](2146_strings.py) | Python 3.12 x64 | strings | O(n d(n)) | AC | 1.375 s | 2528 KB | 11322046 |
| [2146_strings.rs](2146_strings.rs) | Rust 1.75 x64 | strings | O(n d(n)) | AC | 0.109 s | 20756 KB | 11322048 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2146_strings_optimized.cpp](2146_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n d(n)) | AC | 0.031 s | 264 KB | 11317091 |
| [2146_strings_optimized.go](2146_strings_optimized.go) \* | Go 1.14 x64 | strings | O(n d(n)) | AC | 0.031 s | 1360 KB | 11317238 |
| [2146_strings_optimized.java](2146_strings_optimized.java) | Java 1.8 | strings | O(n d(n)) | AC | 0.109 s | 680 KB | 11317242 |
| [2146_strings_optimized.py](2146_strings_optimized.py) \* | Python 3.12 x64 | strings | O(n d(n)) | AC | 1.046 s | 924 KB | 11317245 |
| [2146_strings_optimized.rs](2146_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(n d(n)) | AC | 0.031 s | 368 KB | 11317237 |

\* El corte guardado no contiene envíos de otros autores en Go o Rust con el mismo compilador. Python ocupa el segundo lugar en tiempo y el primero en memoria, y cumple el criterio de ahorro de memoria.
