# 1854. Negociaciones con los partos

[Timus 1854](https://acm.timus.ru/problem.aspx?space=1&num=1854) · dificultad 425 · number_theory

Problema original de Grigoriy Nazarov, del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El emperador Adriano sacrifica un rebaño de n carneros, con n impar,
repartiéndolo por igual entre cierto número de dioses. Teón de Esmirna
quiere que ese número sea impar y tenga un número impar de divisores
positivos. Hallar el mayor número de dioses así.

## Entrada

Un entero impar n (1 ≤ n ≤ 10¹⁸ − 1).

## Salida

El mayor número de dioses que sirve.

## Ejemplos

### Ejemplo 1

Entrada:

```
45
```

Salida:

```
9
```

## Solución

Un número tiene una cantidad impar de divisores exactamente cuando es
un cuadrado perfecto: los divisores se emparejan como k y m/k, y solo un
cuadrado tiene un divisor emparejado consigo mismo. Todo divisor de un n
impar es impar, así que la respuesta es el mayor cuadrado que divide a
n, el producto de p^(2⌊e/2⌋) sobre las potencias de primos p^e de n.

Se extraen los primos impares p mientras p³ ≤ n, con n disminuyendo por
el camino. Lo que queda no tiene factores primos hasta su raíz cúbica,
así que es 1, un primo, un producto de dos primos o el cuadrado de un
primo, y solo el último aporta un cuadrado: se comprueba con una raíz
cuadrada entera exacta. La división de prueba da como mucho 10⁶ pasos,
y la solución en Python solo prueba los primos de una criba.
`O(n^(1/3))`.

En el ejemplo 45 = 3²·5, así que la respuesta es 9.

Trampas:

- el cuadrado de un primo grande, como (10⁹ − 63)², queda tras la
  división de prueba y hay que reconocerlo igualmente;
- la raíz cuadrada en coma flotante de un número cercano a 10¹⁸ puede
  equivocarse en uno; se corrige con comprobaciones enteras.

Las respuestas coinciden con una búsqueda directa en cien números
pequeños y con una implementación aceptada independiente en primos
grandes, productos de dos primos grandes, cuadrados de primos grandes y
productos de muchos primos pequeños.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1854_number_theory.cpp](1854_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^(1/3)) | AC | 0.015 s | 128 KB |
| [1854_number_theory.go](1854_number_theory.go) | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 1160 KB |
| [1854_number_theory.java](1854_number_theory.java) | Java 1.8 | number_theory | O(n^(1/3)) | AC | 0.093 s | 488 KB |
| [1854_number_theory.py](1854_number_theory.py) | Python 3.12 x64 | number_theory | O(n^(1/3)) | AC | 0.171 s | 1968 KB |
| [1854_number_theory.rs](1854_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.062 s | 224 KB |
