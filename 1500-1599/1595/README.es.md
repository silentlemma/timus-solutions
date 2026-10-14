# 1595. Sucesión perfecta

[Timus 1595](https://acm.timus.ru/problem.aspx?space=1&num=1595) · dificultad 1154 · constructive

Problema original de Alexander Bacherikov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que imprimir una sucesión de enteros positivos distintos, cada uno
como mucho 10¹³, que contenga todos los números 1, 2, …, N
(1 ≤ N ≤ 250000), tenga como mucho 2N términos y en la que la suma de
los k primeros términos sea divisible entre k para todo k. Vale
cualquier sucesión así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

La sucesión, separada por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
1 3 2 6 8
```

## Solución

Se colocan los números 1, 2, …, N en orden, cada uno tras un término
extra x: con S la suma hasta ahora y k la posición de x, x debe hacer
S + x divisible entre k, y luego S + x + m divisible entre k + 1 para el
siguiente número m. Así que x ≡ a = −S (mod k) y
x ≡ b = −S − m (mod k + 1). Como k y k + 1 son coprimos, el teorema
chino del resto da una clase módulo k(k + 1), y es fácil escribirla:
x = a + k·t, y k ≡ −1 (mod k + 1), así que t ≡ a − b (mod k + 1), sin
necesidad de inversos. Tomar el primer x de la clase por encima de N lo
separa de 1..N, y avanzar de k(k + 1) en k(k + 1) para saltar los
pocos términos extra anteriores mantiene todos los términos distintos.
La sucesión tiene exactamente 2N términos y se construye en `O(N)` pasos
con un conjunto hash.

Cada x no supera N + k(k + 1) salvo que tenga que saltar un
valor usado, y k < 2N, así que los términos quedan muy por debajo de
10¹³; para N = 250000 el mayor ronda 5·10⁸. Las pruebas usan un
verificador, que se ejecutó con todos los N hasta 300 y con el mayor N.

Detalles a tener en cuenta:

- la respuesta del ejemplo es solo una de muchas; el verificador acepta
  cualquier sucesión válida;
- las sumas de prefijos llegan a unos 6·10¹³, más de lo que cabe en
  enteros de 32 bits;
- 500000 números son varios megabytes de salida, así que la salida pasa
  por un búfer en vez de escribirse número a número.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1595_constructive.cpp](1595_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.109 s | 17152 KB |
| [1595_constructive.go](1595_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.109 s | 11600 KB |
| [1595_constructive.java](1595_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.328 s | 34196 KB |
| [1595_constructive.py](1595_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.500 s | 18112 KB |
| [1595_constructive.rs](1595_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.078 s | 12540 KB |
