# 2126. Gana el equipo rojo: coeficientes trinomiales centrales módulo un primo

[Timus 2126](https://acm.timus.ru/problem.aspx?space=1&num=2126) · dificultad 1598 · math, combinatorics

Problema original de Alexander Zimin, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada una de n personas se une de forma independiente al equipo rojo, al
azul o mira, cada opción con probabilidad 1/3. Gana el equipo más
numeroso. Con t la probabilidad de que gane el rojo, imprimir t · 3ⁿ
módulo un primo p, es decir, el número de las 3ⁿ elecciones en que el
rojo es mayor. Los límites son 1 segundo y 64 MB.

## Entrada

n y p, 1 ≤ n ≤ 10¹⁸, 5 ≤ p < 10⁶, p primo.

## Salida

Ese número módulo p.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 5
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
5 7
```

Salida:

```
5
```

## Solución

Intercambiar los colores muestra que rojo y azul ganan igual de a
menudo, así que la respuesta es (3ⁿ − D) / 2, donde D cuenta los
empates. Se da a cada persona el peso x por rojo, 1 por mirar y x⁻¹ por
azul: D es el término constante de (x + 1 + x⁻¹)ⁿ, el coeficiente
trinomial central Tₙ. Dividir entre 2 es multiplicar por (p + 1) / 2.

Como (1 + x + x²)ᵖ ≡ 1 + xᵖ + x²ᵖ módulo p, estos coeficientes cumplen
una propiedad de Lucas: Tₙ es el producto de T_d sobre las cifras d de n
en base p. Las cifras son menores que p < 10⁶, y Tₖ sigue la recurrencia

(k + 1) T_{k+1} = (2k + 1) Tₖ + 3k T_{k−1}.

Para no dividir en cada paso, los programas llevan Fₖ = k! · Tₖ, que
cumple F_{k+1} = (2k + 1) Fₖ + 3k² F_{k−1}, y dividen una sola vez por
los factoriales al final; las cifras están ordenadas, así que una pasada
llega a todas. Una cifra mayor que (p − 1) / 2 se refleja primero con
T_{p−1−d} ≡ (−3)^{(p−1)/2 − d} T_d (mod p), así que la pasada nunca
supera (p − 1) / 2. 3ⁿ sale de la exponenciación rápida. La recurrencia
requiere O(p) operaciones; la exponenciación modular añade O(log p + log n),
por lo que el trabajo total es O(p + log n).

En el primer ejemplo T₅ = 51, 3⁵ = 243 y (243 − 51) / 2 = 96 ≡ 1 módulo 5.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2126_math_combinatorics.cpp](2126_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(p + log n) | AC | 0.015 s | 396 KB |
| [2126_math_combinatorics.go](2126_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(p + log n) | AC | 0.046 s | 1124 KB |
| [2126_math_combinatorics.java](2126_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(p + log n) | AC | 0.109 s | 456 KB |
| [2126_math_combinatorics.py](2126_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(p + log n) | AC | 0.140 s | 544 KB |
| [2126_math_combinatorics.rs](2126_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(p + log n) | AC | 0.046 s | 232 KB |
