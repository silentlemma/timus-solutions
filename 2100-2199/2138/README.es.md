# 2138. Invertir el orden de bytes de un número de 32 bits

[Timus 2138](https://acm.timus.ru/problem.aspx?space=1&num=2138) · dificultad 111 · math

Problema original de Aidar Islamov, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número de hasta 2³² − 1 se envía como cuatro cifras en base 256. Los
ordenadores "buenos" leen las cifras desde la más significativa y los
"malos" desde la menos significativa. Un ordenador de un tipo recibió un
número de uno del otro tipo y lo leyó como v. Imprimir el número que se
envió en realidad. Los límites son 0.5 segundos y 256 MB.

## Entrada

El tipo del emisor, GOOD o BAD, y luego v, 0 ≤ v ≤ 4 294 967 295.

## Salida

El número enviado.

## Ejemplos

### Ejemplo 1

Entrada:

```
GOOD
16777216
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
BAD
1000
```

Salida:

```
3892510720
```

## Solución

Sea quien sea el emisor, el receptor lee las mismas cuatro cifras en el
orden opuesto. Así que la respuesta es v con sus cuatro cifras en base
256 invertidas, y el tipo del emisor no importa. Se toman las cifras de v
desde la más baja con % 256 y / 256 y se construye el resultado desde
arriba, o se usa un intercambio de bytes.

En el primer ejemplo 16 777 216 tiene las cifras 1;0;0;0, que invertidas
dan 1.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2138_math.cpp](2138_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 140 KB |
| [2138_math.go](2138_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB |
| [2138_math.java](2138_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1600 KB |
| [2138_math.py](2138_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 424 KB |
| [2138_math.rs](2138_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB |
