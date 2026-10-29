# 2035. Dividir un total bajo dos cotas superiores

[Timus 2035](https://acm.timus.ru/problem.aspx?space=1&num=2035) · dificultad 78 · math

Problema original de Kirill Borozdin, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados enteros `X,Y,C`, con `0 ≤ X,Y,C ≤ 1000000000`, encuentra cualquier
pareja entera `A,B` tal que `0 ≤ A ≤ X`, `0 ≤ B ≤ Y` y `A+B=C`.
Límites: 0,5 segundos y 64 MB.

## Entrada

Una línea `X Y C`, una sola instancia sin cantidad inicial de pruebas.

## Salida

Cualquier pareja válida `A B` o la palabra exacta `Impossible` si no existe.
La pareja `0 0` es válida cuando `C=0`.

## Evaluación

Un comprobador verifica ambos límites y la suma; `Impossible` solo se
acepta si no existe ninguna pareja. Se acepta cualquier pareja válida.

## Ejemplos

```
2 7 5
```

```
2 3
```

```
9 15 100
```

```
Impossible
```

## Solución

Se toma A lo mayor posible, A = min(X, C), y B = C − A. Si B ≤ Y, el
par sirve; si no, no sirve ninguno, porque cualquier otro A es menor y
solo hace mayor a B. `O(1)`.

Detalles a tener en cuenta:

- tomar A = X sin limitarlo por C puede dejar B negativo;
- se admiten sumandos cero, y se acepta cualquier par válido.

## Soluciones optimizadas

La solución optimizada en C++ analiza los tres números a mano con
`getchar` en lugar de `iostream`: 100 KB en lugar de 400 KB, con el
mismo tiempo.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2035_math.cpp](2035_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 400 KB | 11293165 |
| [2035_math.go](2035_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1088 KB | 11293168 |
| [2035_math.java](2035_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 492 KB | 11303531 |
| [2035_math.py](2035_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB | 11293171 |
| [2035_math.rs](2035_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11293174 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2035_math_optimized.cpp](2035_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 100 KB | 11303670 |
