# 1149. Escribir una expresión anidada de senos

[Timus 1149](https://acm.timus.ru/problem.aspx?space=1&num=1149) · dificultad 61 · strings

Problema original de Vladimir Gladkov, del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda de prueba.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sea `Aₙ = sin(1−sin(2+sin(3−…sin(n)…)))`, con los signos alternando menos
y más, y `S_N = (…((A₁+N)A₂+N−1)A₃+…+2)A_N+1`. Para `1 ≤ N ≤ 200`, imprime
el texto de `S_N` exactamente como en el ejemplo, sin espacios.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

La expresión `S_N`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
((sin(1)+3)sin(1-sin(2))+2)sin(1-sin(2+sin(3)))+1
```

## Solución

Solo se pide el texto; no se calcula nada. `Aₙ` es `sin(1`, luego para
cada `k` siguiente el signo (menos tras un número impar, más tras uno par)
y `sin(k`, y al final `n` paréntesis de cierre. `S_N` empieza con `N − 1`
paréntesis de apertura; luego, para `i` de 1 a `N`, contiene `Aᵢ`, un más,
el número `N − i + 1` y un paréntesis de cierre tras cada parte menos la
última. La salida tiene unos `4·N²` caracteres, 165 mil para `N = 200`,
construidos en una sola cadena. `O(N²)`.

Detalles a tener en cuenta:

- el signo tras `k` depende de `k`, no de la profundidad del seno;
- la última parte `A_N+1` no lleva paréntesis de cierre;
- para `N = 1` la respuesta es simplemente `sin(1)+1`;
- no hay espacios en ningún sitio.

Las respuestas se compararon en todas las pruebas con una segunda
construcción que envuelve la expresión de dentro hacia fuera, `(S)Aᵢ+…`,
con `Aᵢ` construido por recursión.

## Soluciones optimizadas

La solución optimizada en C++ usa `scanf`, `printf` y `putchar` en
lugar de `iostream` e imprime la expresión por partes en lugar de
construirla en un `std::string`, así que la respuesta larga nunca está
entera en memoria: 128 KB en lugar de 768 KB.

La solución optimizada en Java escribe la expresión directamente en un
búfer de bytes de 4 KB en lugar de construir cadenas, y analiza el
número byte a byte en lugar de usar `Scanner`: 0.046 s en lugar de
0.125 s y 372 KB en lugar de 4356 KB. La solución optimizada en Python
escribe las piezas a medida que las construye y forma cada seno
prolongando la parte inicial del anterior: 384 KB en lugar de 780 KB,
con el mismo tiempo.

## Notas por lenguaje

- La solución sencilla en Python une partes; las demás soluciones
  sencillas usan cadenas o búferes.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1149_strings.cpp](1149_strings.cpp) | G++ 13.2 x64 | strings | O(N²) | AC | 0.015 s | 768 KB | 11280016 |
| [1149_strings.go](1149_strings.go) | Go 1.14 x64 | strings | O(N²) | AC | 0.015 s | 2976 KB | 11280150 |
| [1149_strings.java](1149_strings.java) | Java 1.8 | strings | O(N²) | AC | 0.125 s | 4356 KB | 11280213 |
| [1149_strings.py](1149_strings.py) | Python 3.12 x64 | strings | O(N²) | AC | 0.046 s | 780 KB | 11280177 |
| [1149_strings.rs](1149_strings.rs) | Rust 1.75 x64 | strings | O(N²) | AC | 0.015 s | 636 KB | 11280243 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1149_strings_optimized.cpp](1149_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(N²) | AC | 0.015 s | 128 KB | 11303572 |
| [1149_strings_optimized.java](1149_strings_optimized.java) | Java 1.8 | strings | O(N²) | AC | 0.046 s | 372 KB | 11303716 |
| [1149_strings_optimized.py](1149_strings_optimized.py) | Python 3.12 x64 | strings | O(N²) | AC | 0.062 s | 384 KB | 11303717 |
