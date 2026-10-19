# 2021. Retrasar la Certeza del Ganador

[Timus 2021](https://acm.timus.ru/problem.aspx?space=1&num=2021) · dificultad 462 · sorting

Problema original de Oleg Dolgorukov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos equipos tienen `n` participantes cada uno, con puntuaciones enteras
predeterminadas de 0 a 6. Organice `n` rondas, con una persona de cada
equipo por ronda y cada participante exactamente una vez. Las dos
puntuaciones de la ronda se anuncian simultáneamente. Gana el equipo de
mayor suma final; si las sumas coinciden, hay empate. El público solo
conoce los límites de puntuación.

Elija ambos órdenes para retrasar al máximo la primera ronda en que los
resultados anunciados garanticen un equipo ganador. Tras `k` rondas, con
`r=n−k` restantes y diferencia `d`, hay victoria garantizada si y solo si
`|d| > 6r`. La igualdad todavía permite un empate. Si no se garantiza una
victoria antes, todo el resultado se conoce al terminar la última ronda.

Se cumple `2 ≤ n ≤ 1 000`, con puntuaciones entre 0 y 6.
Límites: 1 segundo y 64 MB.

## Entrada

La primera línea contiene `n`; la segunda y la tercera, los `n` puntos de
cada equipo. Sus participantes se numeran independientemente de 1 a `n`
en el orden de entrada.

## Salida

Imprima `n` líneas con los dos índices de la ronda, primero del primer
equipo y luego del segundo. Cada columna debe ser una permutación completa.
Se admite cualquier orden globalmente óptimo.

## Evaluación

Un comprobador verifica ambas permutaciones, reproduce las puntuaciones
y acepta cualquier orden cuya primera ronda decisiva sea la más tardía
posible.

## Ejemplos

```
5
0 1 4 3 6
6 5 1 3 0
```

```
5 1
1 5
4 4
2 3
3 2
```

## Solución

Compare las **sumas finales**, independientes del orden. Si gana el primer
equipo, ordene sus participantes por puntos crecientes y los del segundo por
puntos decrecientes. Si gana el segundo, intercambie las direcciones. En
empate sirve cualquier orden; el programa ordena ambos crecientemente.
Conserve los índices originales y empareje ambas listas por posición.

Suponga que el primero gana por una diferencia final `D>0`. Tras cualquier
prefijo con `r` rondas pendientes, sea `R` la diferencia que añadirán quienes
quedan. Cada ronda aporta de −6 a 6, luego `R≤6r` y
`d=D−R≥D−6r>−6r`. El equipo que acabará perdiendo nunca puede tener una
victoria garantizada en ningún orden. Solo importa la barrera superior `d>6r`.

Para cada longitud `k`, el orden creciente del primero toma la menor
suma posible de sus primeros `k` resultados; el decreciente del segundo
toma la mayor suma rival. Juntos minimizan `d(k)` entre **todos** los
órdenes y para cada `k` a la vez. Si esta programación garantiza
victoria por primera vez en `k<n`, cualquier otra tiene una diferencia
al menos igual en esa ronda y ya garantiza victoria. Ninguna puede
retrasarla más. Llegar a la última ronda ya consigue el máximo retraso
posible. El otro ganador es simétrico.

Cuando `D=0`, todo prefijo cumple `d=−R`, de donde `|d|≤6r`. Ningún orden
garantiza ganador antes de revelarse el empate final, así que todos son
óptimos. Una gran ventaja temporal del futuro perdedor no causa certeza
prematura: las puntuaciones reales restantes impiden rebasar la barrera.

En el ejemplo las sumas finales son 14 y 15. Las primeras cuatro parejas
mostradas dan los mismos puntos a ambos equipos y la última da 4 frente a 5.
El ganador solo se conoce en la quinta ronda, lo que es óptimo.

Ordenar dos listas de índices cuesta `O(n log n)` tiempo y `O(n)` espacio.
Las sumas y diferencias tienen magnitud máxima 6 000; bastan enteros ordinarios.

Trampas:

- Determinar las direcciones con las sumas finales, no con la ventaja actual.
- Usar `|d| > 6r` estrictamente: la igualdad todavía permite empate.
- Anunciar ambos puntos juntos y usar cada índice una vez en su propio equipo.
- Emitir índices originales desde uno, no puntos ni posiciones ordenadas.
- Admitir cualquier óptimo, incluidos todos los órdenes cuando empatan
  los totales.

## Notas por lenguaje

Las cinco versiones ordenan por `(puntos, índice)` e invierten al futuro
perdedor. El desempate por índice solo hace determinista la salida. C++ y
Go usan ordenación por comparaciones; Python, claves; Rust, claves de tupla;
Java 8 ordena índices encapsulados con un comparador.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2021_sorting.cpp](2021_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 472 KB |
| [2021_sorting.go](2021_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.015 s | 1252 KB |
| [2021_sorting.java](2021_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 2812 KB |
| [2021_sorting.py](2021_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.093 s | 764 KB |
| [2021_sorting.rs](2021_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.015 s | 340 KB |
