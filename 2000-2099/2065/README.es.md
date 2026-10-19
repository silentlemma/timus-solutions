# 2065. Pocas sumas distintas en segmentos

[Timus 2065](https://acm.timus.ru/problem.aspx?space=1&num=2065) · dificultad 318 · constructive

Problema original de Nikita Sivukhin, preparado por Alexey Danilyuk y Nikita Sivukhin, del Concurso Regional por Equipos de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Construir un arreglo de n enteros con al menos k valores distintos tal
que las sumas de sus segmentos contiguos tomen la menor cantidad posible
de valores distintos. Todos los valores deben tener valor absoluto a lo
sumo 10⁶. Los límites son 1 segundo y 64 MB.

## Entrada

Dos enteros n y k, 1 ≤ k ≤ n ≤ 500.

## Salida

Los n enteros en una línea. Se acepta cualquier arreglo óptimo.

## Evaluación

Un comprobador verifica los valores y la cantidad de valores distintos
y cuenta las sumas de segmentos distintas, que deben ser exactamente k.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1
```

Salida:

```
-987654
```

### Ejemplo 2

Entrada:

```
3 2
```

Salida:

```
0 7 0
```

## Solución

Cada elemento por sí solo es un segmento, así que un arreglo con k
valores distintos tiene al menos k sumas de segmentos distintas. Esta
cota siempre se alcanza: tomar n − k + 1 ceros seguidos de 1, −1, 2, −2,
3, … hasta tener n números. Los ceros y los otros k − 1 números dan
exactamente k valores distintos.

La suma de un segmento es la diferencia de dos sumas prefijas. Las sumas
prefijas de este arreglo son 0, …, 0, 1, 0, 2, 0, 3, …: ceros que
alternan con 1, 2, …, m, donde m es el mayor número usado. Si el arreglo
termina en −m, las diferencias de una suma prefija anterior y otra
posterior cubren exactamente −m, …, m, es decir, 2m + 1 = k valores. Si
termina en m, la suma prefija m va al final, así que −m no aparece y las
sumas son −(m − 1), …, m, de nuevo 2m = k valores. Por tanto el arreglo
es óptimo y la respuesta se construye en O(n).

En el segundo ejemplo el arreglo 0 0 1 tiene los valores 0 y 1 y las
sumas de segmentos 0 y 1, dos de cada, igual que la respuesta del
ejemplo 0 7 0.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2065_constructive.cpp](2065_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 132 KB |
| [2065_constructive.go](2065_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1056 KB |
| [2065_constructive.java](2065_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1640 KB |
| [2065_constructive.py](2065_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.078 s | 456 KB |
| [2065_constructive.rs](2065_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 276 KB |
