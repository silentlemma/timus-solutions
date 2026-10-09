# 1071. La menor base en la que tachar cifras convierte x en y

[Timus 1071](https://acm.timus.ru/problem.aspx?space=1&num=1071) · dificultad 624 · math

Problema original de Dmitry Filimonenkov, del Ural State University Personal Contest Online, febrero de 2001, Students Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan dos enteros `1 ≤ y < x ≤ 1 000 000`. Halla la menor base `b ≥ 2`
en la que las cifras de `y` se pueden obtener de las cifras de `x` tachando
algunas, o imprime `No solution` si no existe tal base.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`x` e `y` en una línea.

## Salida

La base, o `No solution`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
127 16
```

Salida:

```
3
```

## Solución

Las bases se dividen en tres rangos.

- `b > x`: `x` es una sola cifra e `y` es otra distinta, así que nada
  funciona.
- `b² ≤ x`: como mucho mil bases. Se escriben ambos números en base `b` y
  se comprueba de forma voraz que las cifras de `y` aparecen en orden entre
  las de `x`.
- `b² > x` y `b ≤ x`: `x` tiene exactamente dos cifras, `x div b` y
  `x mod b`, e `y < x` debe ser una de ellas.
  - `x div b = y` para `b` desde `⌊x/(y+1)⌋ + 1` hasta `⌊x/y⌋`, así que la
    menor base así en este rango se conoce enseguida.
  - `x mod b = y` significa que `b` divide a `x − y` y `b > y`, así que se
    toma el menor divisor de `x − y` suficientemente grande; los divisores
    se recorren por parejas hasta `√(x − y)`.

Las bases pequeñas se prueban primero, así que la primera coincidencia ahí
es la respuesta; si no, la respuesta es el menor de los dos candidatos del
último rango. `O(√x · log x)`.

Detalles a tener en cuenta:

- la respuesta puede ser enorme, por ejemplo 465379 para `932318 1560`,
  así que una búsqueda que se detiene en la base 10 o 36 es incorrecta;
- probar todas las bases hasta `x` con una conversión completa es bastante
  rápido en un lenguaje compilado, pero casi todas caen en el rango de dos
  cifras, y tratarlo con aritmética hace rápido a cualquier lenguaje;
- una cifra es menor que la base: para la cifra baja es la condición
  `b > y`, y para la alta se cumple sola porque `b² > x`.

Las respuestas se comprobaron con una fuerza bruta sobre todas las bases y
una prueba general de subsecuencia, para todos los pares con `x < 700` y
para pares grandes aleatorios.

## Notas por lenguaje

- C++ y Java calculan `b · b` en 64 bits en la condición del bucle; Go y
  Rust usan enteros de 64 bits en todo el programa.
- Python comprueba la subsecuencia con el modismo `d in it` sobre un solo
  iterador, que avanza por las cifras de `x`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1071_math.cpp](1071_math.cpp) | G++ 13.2 x64 | math | O(√x · log x) | AC | 0.015 s | 188 KB |
| [1071_math.go](1071_math.go) | Go 1.14 x64 | math | O(√x · log x) | AC | 0.031 s | 1192 KB |
| [1071_math.java](1071_math.java) | Java 1.8 | math | O(√x · log x) | AC | 0.125 s | 1636 KB |
| [1071_math.py](1071_math.py) | Python 3.12 x64 | math | O(√x · log x) | AC | 0.062 s | 572 KB |
| [1071_math.rs](1071_math.rs) | Rust 1.75 x64 | math | O(√x · log x) | AC | 0.031 s | 232 KB |
