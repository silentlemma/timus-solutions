# 1924. Un juego de signos con paridad invariable

[Timus 1924](https://acm.timus.ru/problem.aspx?space=1&num=1924) · difficulty 39 · math

Problema original de folclore, del concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los enteros de 1 a n están en orden. Dos equipos alternan colocando
un signo + o − en un espacio aún libre entre enteros consecutivos. El primero,
`black`, desea un resultado par; `grimy` desea uno impar. Ambos juegan
óptimamente y black empieza. Determinar quién gana. Para n=1 no hay
espacios y la expresión vale 1. Límites: 1 segundo y 64 MB.

## Entrada

Un entero n, 1≤n≤50.

## Salida

Escribir exactamente `black` si gana el objetivo par; en otro caso `grimy`.

## Evaluación

Se compara exactamente el único token, escrito en minúsculas.

## Ejemplos

```
1
```

```
grimy
```

```
4
```

```
black
```

## Solución

Cambiar + por − delante de x cambia el resultado en −2x, que es par.
Toda expresión completa tiene por ello la misma paridad que la suma
positiva S=n(n+1)/2. Ni los espacios elegidos, ni los signos, ni el orden
afectan al ganador. Imprimir black si S es par y grimy si es impar.
La fórmula también cubre n=1 sin jugadas.

El argumento abarca todas las expresiones finales, así que ninguna
estrategia óptima puede alterar la conclusión; no hace falta buscar jugadas.

O(1) tiempo y O(1) espacio auxiliar.

Restar un impar sigue aportando paridad impar. No simular turnos ni
decidir por el equipo que juega al final. La ausencia de espacios en n=1
no produce empate. Dividir el producto antes de comprobar paridad.

## Notas por lenguaje

Las cinco versiones usan enteros y división exacta por 2. n(n+1) no supera
2550 y la suma no supera 1275, de modo que bastan tipos enteros ordinarios.
Python y Rust leen texto; C++, Go y Java usan entrada estándar para un entero.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1924_math.cpp](1924_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 380 KB |
| [1924_math.go](1924_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1100 KB |
| [1924_math.java](1924_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1616 KB |
| [1924_math.py](1924_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 396 KB |
| [1924_math.rs](1924_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB |
