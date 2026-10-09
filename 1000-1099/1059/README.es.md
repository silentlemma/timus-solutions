# 1059. El programa postfijo más corto para un polinomio

[Timus 1059](https://acm.timus.ru/problem.aspx?space=1&num=1059) · dificultad 677 · math

Problema original de la Academia Estatal de Aviación de Rybinsk.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Escribe la expresión más corta en notación polaca inversa que calcule el
polinomio `a0·x^N + a1·x^(N−1) + … + aN` para cualesquiera coeficientes y
cualquier `x` (`1 ≤ N ≤ 1000`). La expresión puede usar las operaciones
`+` y `*`, la letra `X` para el argumento y el número `i` para el
coeficiente `ai`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

La expresión, un elemento por línea.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
0
X
*
1
+
```

### Ejemplo 2

Entrada:

```
3
```

Salida:

```
0
X
*
1
+
X
*
2
+
X
*
3
+
```

## Solución

El esquema de Horner `(((a0·x + a1)·x + a2)·x + …)·x + aN` escrito en
forma postfija es `0` y luego `X * i +` para `i = 1 … N`: `4N + 1`
elementos.

No existe nada más corto. Todos los coeficientes deben aparecer, lo que
son `N + 1` operandos. No hay manera de copiar un valor, así que `X` debe
aparecer al menos `N` veces: una expresión con `k` apariciones de `X`
tiene grado como mucho `k`. Una expresión postfija con `m` operandos tiene
exactamente `m − 1` operaciones binarias, así que hacen falta al menos
`(2N + 1) + 2N = 4N + 1` elementos. `O(N)`.

Detalles a tener en cuenta:

- el coeficiente `ai` se escribe como el número `i`, no como `ai`;
- el orden de los elementos importa para la comprobación: el esquema
  empieza con `0 X *`, como en el ejemplo.

## Notas por lenguaje

- Todos los lenguajes imprimen las mismas líneas; con `N = 1000` son 4001
  líneas, así que la salida va por un búfer.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1059_math.cpp](1059_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 128 KB |
| [1059_math.go](1059_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1084 KB |
| [1059_math.java](1059_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 1588 KB |
| [1059_math.py](1059_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 356 KB |
| [1059_math.rs](1059_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 232 KB |
