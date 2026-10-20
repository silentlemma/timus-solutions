# 2130. Un número coherente con las respuestas de divisibilidad

[Timus 2130](https://acm.timus.ru/problem.aspx?space=1&num=2130) · dificultad 961 · math, number_theory

Problema original de Kirill Borozdin y Nikita Sivukhin, preparado por Vladimir Leskov, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un entero oculto x está entre 1 y 10¹². Cada una de las n jugadas dice
si x es divisible por algún dᵢ. Tras cada jugada, imprimir cualquier
número del mismo rango que concuerde con todas las respuestas hasta ese
momento, o −1 si no existe. Se acepta cualquier número así. Los límites
son 2.5 segundos y 256 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, y luego n pares dᵢ, tᵢ con 1 ≤ dᵢ ≤ 10⁶; tᵢ = 1
significa "sí".

## Salida

Un número adecuado o −1 tras cada jugada.

## Evaluación

Un comprobador decide en cada jugada si existe un número adecuado y
verifica cada número impreso con las respuestas hasta ese momento.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10 1
5 0
100500 0
```

Salida:

```
100500
-1
-1
```

### Ejemplo 2

Entrada:

```
6
2 1
5 0
3 1
1 1
5 1
100500 0
```

Salida:

```
12
12
12
12
-1
-1
```

### Ejemplo 3

Entrada:

```
6
1000000 1
999999 1
2 0
999998 1
999997 1
999996 1
```

Salida:

```
999999000000
999999000000
-1
-1
-1
-1
```

## Solución

Todo número válido es múltiplo de L, el mínimo común múltiplo de los
divisores con respuesta "sí". El propio L es el mejor candidato: si
existe un x válido, L divide a x, y un divisor d con respuesta "no" no
divide a x, así que tampoco divide a L. Por tanto la respuesta es L
cuando L ≤ 10¹² y ningún divisor "no" divide a L, y −1 en otro caso; una
vez es −1 sigue siéndolo, porque las respuestas solo añaden condiciones.

Un divisor "no" nuevo se comprueba una vez con el L actual. Un "sí" que
no cambia L no cambia nada, y un cambio de L al menos lo duplica, así que
L cambia unas 40 veces como mucho antes de pasar de 10¹². Solo entonces
se vuelven a comprobar todos los divisores "no" guardados, lo que deja
el trabajo total en O(40 n).

En el segundo ejemplo 2 y 3 dan L = 6, pero 5 es un divisor "no" y el
"sí" posterior para 5 hace L = 30, divisible por 5, así que la respuesta
pasa a ser −1; el ejemplo imprime 12, otro múltiplo de 6.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2130_math_number_theory.cpp](2130_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(n log X) | AC | 0.062 s | 1220 KB |
| [2130_math_number_theory.go](2130_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(n log X) | AC | 0.046 s | 7616 KB |
| [2130_math_number_theory.java](2130_math_number_theory.java) | Java 1.8 | math, number_theory | O(n log X) | AC | 0.125 s | 8892 KB |
| [2130_math_number_theory.py](2130_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(n log X) | AC | 0.343 s | 18092 KB |
| [2130_math_number_theory.rs](2130_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(n log X) | AC | 0.031 s | 4564 KB |
