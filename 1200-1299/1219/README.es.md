# 1219. Un millón de letras sin letra, par ni trío demasiado frecuente

[Timus 1219](https://acm.timus.ru/problem.aspx?space=1&num=1219) · dificultad 121 · constructive

Problema original de Pavel Atnashev y Leonid Volkov, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que imprimir 1.000.000 de letras latinas minúsculas de modo que cada
letra aparezca como mucho 40.000 veces, cada dos letras consecutivas como
mucho 2.000 veces y cada tres letras consecutivas como mucho 100 veces.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

No hay entrada.

## Salida

Una línea con las letras.

## Evaluación

Se acepta cualquier secuencia que cumpla los tres límites.

## Ejemplos

No hay entrada, y el enunciado no da ninguna salida de ejemplo.

## Solución

Se reparten el millón de letras de la forma más uniforme posible. Hay 26
letras, `26² = 676` pares y `26³ = 17.576` tríos, así que un reparto
perfecto da unas 38.462, 1.479 y 57 apariciones, todo dentro de los
límites.

Una secuencia de De Bruijn de orden 3 sobre 26 letras es un ciclo de
17.576 letras en el que cada trío aparece exactamente una vez como tres
letras consecutivas, dando la vuelta al ciclo. Repetirla seguida deja
cada ventana de tres letras como una ventana del ciclo, así que tras unas
57 copias cada trío aparece 56 o 57 veces, cada par 26 veces más y cada
letra 676 veces más: aquí como mucho 38.532, 1.482 y 57. El ciclo sale de
la construcción clásica que une en orden lexicográfico las palabras de
Lyndon cuya longitud divide a 3. `O(L)` para `L = 10⁶`.

Detalles a tener en cuenta:

- las ventanas que pasan de una copia a la siguiente son ventanas
  cíclicas de la secuencia, así que no rompen el equilibrio;
- una secuencia aleatoria probablemente también pasaría, pero su trío más
  frecuente rondaría las 90 apariciones, cerca del límite.

La salida se comprobó con los tres límites, y las cifras de arriba son
sus máximos reales.

## Notas por lenguaje

- Todos los lenguajes generan el ciclo con la misma construcción
  recursiva y escriben la línea entera de una vez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1219_constructive.cpp](1219_constructive.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.001 s | 1184 KB |
| [1219_constructive.go](1219_constructive.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.015 s | 2624 KB |
| [1219_constructive.java](1219_constructive.java) | Java 1.8 | constructive | O(L) | AC | 0.062 s | 8868 KB |
| [1219_constructive.py](1219_constructive.py) | Python 3.12 x64 | constructive | O(L) | AC | 0.078 s | 3224 KB |
| [1219_constructive.rs](1219_constructive.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.001 s | 2404 KB |
