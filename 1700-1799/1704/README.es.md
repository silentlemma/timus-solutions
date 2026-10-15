# 1704. Demodulación

[Timus 1704](https://acm.timus.ru/problem.aspx?space=1&num=1704) · dificultad 2965 · math

Problema original de Pavel Atnashev, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto se envió bit a bit, ocho bits por carácter empezando por el
menor y t muestras por bit. La muestra k de un bit es un nivel
desconocido más una amplitud desconocida por sin(2πk/t) para un uno o
sin(4πk/t) para un cero, más ruido. Dadas las n muestras, recuperar el
texto.

## Entrada

n y t (0 < n ≤ 10000, 5 ≤ t ≤ 1000, n múltiplo de 8t), y luego n
muestras entre 0 y 1 con a lo sumo cinco decimales, en una o varias
líneas.

## Salida

El texto: letras latinas, dígitos, signos de puntuación y espacios. Se
decodifica de forma única.

## Ejemplos

### Ejemplo 1

Entrada:

```
40 5
0.3 0.8 0.6 0.4 0.2
0.5 0.6 0.3 0.9 0.4
0.4 0.8 0.3 0.8 0.2
0.3 0.6 0.1 0.7 0.2
0.7 0.7 0.1 0.7 0.1
0.5 0.8 0.7 0.3 0.2
0.4 0.8 0.2 0.8 0.2
0.5 0.8 0.3 0.8 0.2
```

Salida:

```
!
```

## Solución

En un número entero de periodos, sin(2πk/t) y sin(4πk/t) suman cero y
son ortogonales: la suma de sus productos para k = 0 … t − 1 es 0
cuando t ≥ 5. Así que para las t muestras de un bit se calcula la
correlación con ambas ondas, es decir, las sumas de muestra × onda. El
nivel constante no aporta nada a ninguna suma. La onda enviada aporta
su amplitud por t/2 a su propia suma y nada a la otra, y el ruido solo
lo difumina. El bit es la onda con la suma mayor, y los caracteres se
montan desde su bit menor. `O(n)`.

Trampas:

- el nivel y la amplitud son desconocidos, pero no hace falta
  estimarlos: el nivel se cancela y la amplitud solo escala;
- los bits de un carácter van desde el menor: las muestras del ejemplo
  dan 10000100, que es 33, el código de !;
- las muestras pueden repartirse entre las líneas de cualquier forma
  (test 05).

Las respuestas coinciden con una implementación aceptada independiente
sobre la salida del codificador del enunciado con niveles, amplitudes y
ruido aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1704_math.cpp](1704_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 296 KB |
| [1704_math.go](1704_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1312 KB |
| [1704_math.java](1704_math.java) | Java 1.8 | math | O(n) | AC | 0.078 s | 616 KB |
| [1704_math.py](1704_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 1364 KB |
| [1704_math.rs](1704_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 580 KB |
