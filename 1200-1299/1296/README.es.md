# 1296. Hipersalto

[Timus 1296](https://acm.timus.ru/problem.aspx?space=1&num=1296) · dificultad 60 · dp

Problema original de Den Raskovalov, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una sucesión de N ≤ 60 000 enteros de −30 000 a 30 000, hay que
hallar la mayor suma de un tramo contiguo. Se permite el tramo vacío,
que da 0.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N números, uno por línea. N puede ser 0.

## Salida

La mayor suma.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
31
-41
59
26
-53
58
97
-93
-23
84
```

Salida:

```
187
```

### Ejemplo 2

Entrada:

```
3
-1
-5
-6
```

Salida:

```
0
```

## Solución

Es el problema del subarreglo de suma máxima, que el algoritmo de
Kadane resuelve en una pasada. Se guarda `ending`, la mayor suma de un
tramo que termina en el número actual, contando el tramo vacío. Cada
número nuevo p o bien alarga ese tramo o, si la suma fuera a quedar
negativa, conviene dejarlo fuera:

ending = max(ending + p, 0).

La respuesta es el mayor valor que toma `ending`, que empieza en 0 por
el tramo vacío. Se lee cada entero con signo, se suma a `ending`, se
reemplaza un `ending` negativo por 0 y se actualiza `best`. El tiempo es
`O(N)` y la memoria auxiliar es `O(1)`; las soluciones sencillas en
Python y Rust almacenan la entrada en `O(N)` de memoria.

Detalles a tener en cuenta:

- si todos los números son negativos la respuesta es 0, no el mayor de
  ellos (prueba 02);
- se permite N = 0 (prueba 03);
- se permite un signo más explícito: Java debe saltarlo antes de leer
  el token numérico para interpretar `+0` como 0 (prueba 09);
- la suma llega a 60 000 · 30 000 = 1,8 · 10⁹, cerca del límite de 32
  bits, así que las soluciones usan 64 bits (prueba gen2).

Las respuestas se compararon con revisar todos los tramos en 1500
sucesiones aleatorias.

## Soluciones optimizadas

La solución optimizada en Python lee los números línea a línea, uno por
línea, en lugar de dividir toda la entrada, y compara las sumas
parciales directamente en lugar de llamar a `max()`: 0.078 s en lugar de
0.125 s y 388 KB en lugar de 4788 KB. La solución optimizada en Rust lee
los números línea a línea a través de un búfer de 1 KB en lugar de leer
toda la entrada en una cadena: 228 KB en lugar de 1260 KB, con el mismo
tiempo.

## Notas por lenguaje

- Todos los lenguajes mantienen solo dos sumas, `best` y `ending`.
- C++, Go y Java, y las soluciones optimizadas en Python y Rust, usan
  `O(1)` de memoria total; las soluciones sencillas en Python y Rust
  usan `O(N)` de memoria total porque almacenan la entrada.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1296_dp.cpp](1296_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.046 s | 132 KB | 11297977 |
| [1296_dp.go](1296_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1512 KB | 11297978 |
| [1296_dp.java](1296_dp.java) | Java 1.8 | dp | O(N) | AC | 0.109 s | 464 KB | 11297980 |
| [1296_dp.py](1296_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.125 s | 4788 KB | 11297981 |
| [1296_dp.rs](1296_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 1260 KB | 11297982 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1296_dp_optimized.py](1296_dp_optimized.py) | Python 3.12 x64 | dp | O(N) | AC | 0.078 s | 388 KB | 11303735 |
| [1296_dp_optimized.rs](1296_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 228 KB | 11303736 |
