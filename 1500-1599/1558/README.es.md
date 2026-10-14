# 1558. Números periódicos

[Timus 1558](https://acm.timus.ru/problem.aspx?space=1&num=1558) · dificultad 865 · math

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número periódico (a₁…aₖ)b₁…bₘ tiene infinitas cifras a la izquierda:
el bloque a₁…aₖ repetido sin fin y, en el extremo bajo, b₁…bₘ. Hay que
sumar dos de estos números dados con periodos de la misma longitud
k ≤ 9 y sin parte no periódica, cifra a cifra desde el extremo bajo y
con acarreos como siempre. La suma se imprime con el periodo más corto
y, entre esas, con la parte no periódica más corta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Dos líneas, cada una con un número de la forma (a₁…aₖ).

## Salida

La suma en la misma notación.

## Ejemplos

### Ejemplo 1

Entrada:

```
(234)
(342)
```

Salida:

```
(576)
```

## Solución

Se leen ambos periodos como números A y B de k cifras y se suman,
S = A + B. Si S < 10ᵏ, ningún bloque acarrea y la suma es S repetido,
escrito con k cifras. Si no, el bloque más bajo es S − 10ᵏ y pasa un
acarreo; cada bloque por encima recibe ese acarreo, vale S + 1 − 10ᵏ y
también pasa un acarreo. Así que la suma es el bloque P = S + 1 − 10ᵏ
repetido sin fin sobre el único bloque S − 10ᵏ.

Queda la forma más corta. El periodo más corto de la parte infinita es
el menor divisor d de k para el que P está formado por k/d copias de sus
primeras d cifras. Luego la parte no periódica se recorta desde arriba:
bajando desde el primer bloque de P, una cifra sigue en la parte
periódica mientras sea igual a la cifra d posiciones más arriba. Las
cifras que quedan debajo forman la parte no periódica más corta, y el
periodo se lee justo encima de ellas, lo que puede rotar el bloque:
999909 + 099000 da (100989)09 (prueba gen4). Los resultados se
contrastaron con una suma directa de 200 cifras en 1500 pares
aleatorios.

Detalles a tener en cuenta:

- la parte no periódica puede acortarse: (111) + (999) es (1)0, y
  (5) + (5) también es (1)0 (pruebas 09, 02);
- los ceros a la izquierda forman parte del periodo, como en (0100)
  (prueba 10);
- una suma de solo nueves, como (454545) + (545454), no tiene ningún
  acarreo y es simplemente (9) (prueba 08).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1558_math.cpp](1558_math.cpp) | G++ 13.2 x64 | math | O(k^2) | AC | 0.015 s | 380 KB |
| [1558_math.go](1558_math.go) | Go 1.14 x64 | math | O(k^2) | AC | 0.031 s | 1036 KB |
| [1558_math.java](1558_math.java) | Java 1.8 | math | O(k^2) | AC | 0.109 s | 468 KB |
| [1558_math.py](1558_math.py) | Python 3.12 x64 | math | O(k^2) | AC | 0.093 s | 556 KB |
| [1558_math.rs](1558_math.rs) | Rust 1.75 x64 | math | O(k^2) | AC | 0.046 s | 220 KB |
