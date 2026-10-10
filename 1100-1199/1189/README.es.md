# 1189. Pares X + Y = N donde Y es X con un dígito tachado

[Timus 1189](https://acm.timus.ru/problem.aspx?space=1&num=1189) · dificultad 500 · math

Problema original de Vladimir Lelyukh y Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado `10 ≤ N ≤ 10⁹`, hay que hallar todos los pares `X + Y = N` donde `X`
tiene al menos dos dígitos y ningún cero inicial, e `Y` es `X` con un
dígito tachado, escrito con un dígito menos que `X` (así que puede empezar
por ceros). Se imprime su número y los pares en orden creciente de `X`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

El número de pares y luego líneas `X + Y = N`.

## Ejemplos

### Ejemplo 1

Entrada:

```
302
```

Salida:

```
5
251 + 51 = 302
275 + 27 = 302
276 + 26 = 302
281 + 21 = 302
301 + 01 = 302
```

## Solución

Se tacha de `X` el dígito `d` en la posición `k` (contando desde la
derecha y desde 0). Escribiendo `X = (10a + d)·10ᵏ + b` con `b < 10ᵏ`,
resulta `Y = a·10ᵏ + b` y

`X + Y = (11a + d)·10ᵏ + 2b = N`.

Así que `2b` es congruente con `N` módulo `10ᵏ`. Como `2b < 2·10ᵏ`, es
`N mod 10ᵏ` o eso más `10ᵏ`, y debe ser par con `b < 10ᵏ`. El resto,
`(N − 2b)/10ᵏ`, es `11a + d`, que da `a` y `d` al dividir entre 11; el
resto de la división debe ser un dígito de verdad, no 10. Se guarda `X`
si tiene al menos dos dígitos y empieza por un dígito no nulo, es decir,
`a > 0` o `d > 0`. Como mucho dos candidatos por posición, `O(log N)` en
total.

Detalles a tener en cuenta:

- el mismo par puede salir de tachar dígitos iguales distintos, como en
  `11 + 1 = 12`, así que los candidatos van a un conjunto;
- `Y` se imprime con exactamente un dígito menos que `X`, con ceros
  iniciales, como en `301 + 01`;
- el resto `d` de la división entre 11 puede ser 10, que no es un dígito.

Las respuestas se compararon con una búsqueda directa sobre todos los `X`
para cada `N` hasta 1199 y para 150 `N` aleatorios hasta 200000, y con una
solución escrita aparte en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes imprimen `Y` con un ancho tomado de la longitud de
  `X` y relleno de ceros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1189_math.cpp](1189_math.cpp) | G++ 13.2 x64 | math | O(log N) | AC | 0.015 s | 188 KB |
| [1189_math.go](1189_math.go) | Go 1.14 x64 | math | O(log N) | AC | 0.031 s | 1124 KB |
| [1189_math.java](1189_math.java) | Java 1.8 | math | O(log N) | AC | 0.109 s | 1872 KB |
| [1189_math.py](1189_math.py) | Python 3.12 x64 | math | O(log N) | AC | 0.093 s | 448 KB |
| [1189_math.rs](1189_math.rs) | Rust 1.75 x64 | math | O(log N) | AC | 0.015 s | 236 KB |
