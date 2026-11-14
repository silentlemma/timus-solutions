# 1838. El golpe del samurái

[Timus 1838](https://acm.timus.ru/problem.aspx?space=1&num=1838) · dificultad 720 · math

Problema original de Denis Dublennykh, del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tallo de bambú de longitud l descansa sobre n apoyos. Se corta en
un punto en dos partes, y una parte cae salvo que su centro de masas
quede entre dos apoyos bajo ella. Hallar la longitud total de los
puntos donde un corte hace caer al menos una parte, redondeada hacia
arriba.

## Entrada

l y n (3 ≤ l ≤ 10⁹, 2 ≤ n ≤ 10⁵), luego las n posiciones distintas de
los apoyos en orden creciente, todas estrictamente entre 0 y l. El
tallo entero está estable.

## Salida

La longitud total de los puntos donde cae una parte, redondeada hacia
arriba.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
1 2 3 4
```

Salida:

```
4
```

## Solución

Sea el corte en x entre los apoyos sᵢ y sᵢ₊₁. La parte izquierda
[0, x] descansa sobre s₁, …, sᵢ y se sostiene cuando su centro x/2
está en [s₁, sᵢ]; la derecha [x, l] descansa sobre sᵢ₊₁, …, sₙ y se
sostiene cuando (x + l)/2 está en [sᵢ₊₁, sₙ]. Así, en este hueco ambas
se sostienen para x en

[max(sᵢ, 2s₁, 2sᵢ₊₁ − l), min(sᵢ₊₁, 2sₙ − l, 2sᵢ)],

y un corte a la izquierda de s₁ o a la derecha de sₙ siempre hace caer
una parte. Sumando las longitudes seguras de los n − 1 huecos y
restándolas de l se obtiene la respuesta. Todos los extremos son
enteros, así que el redondeo nunca la cambia. `O(n)`.

En el ejemplo solo es seguro el hueco (2, 3): allí el centro izquierdo
x/2 está entre 1 y 2, y el derecho (x + 5)/2 entre 3 y 4. Así que se
pintan 4 de las 5 unidades.

Trampas:

- una parte necesita dos apoyos debajo, así que un corte antes del
  segundo apoyo siempre hace caer la parte izquierda;
- los puntos sueltos, como un corte justo sobre un apoyo, no tienen
  longitud y no importan;
- 2sₙ es menor que 2·10⁹ y cabe en enteros de 32 bits con signo.

Las respuestas coinciden con un recuento de los cortes que hacen caer
una parte sobre una malla fina en unos cientos de tallos pequeños y con
una implementación aceptada independiente en las pruebas grandes.

## Soluciones optimizadas

Las versiones optimizadas usan el primer y el último apoyo para acotar los cortes que deben examinarse. Dejan de recorrer los intervalos cuando el extremo izquierdo alcanza el límite superior.

Python 3.12 x64, envío 11319948. Tiempo 0,156 → 0,156 s, memoria 10892 → 8196 KB.

Rust 1.75 x64, envío 11319998. Tiempo 0,015 → 0,015 s, memoria 2664 → 596 KB.

Go 1.14 x64, envío 11320023. Tiempo 0,078 → 0,031 s, memoria 3336 → 1320 KB.

G++ 13.2 x64, envío 11320066. Tiempo 0,093 → 0,015 s, memoria 968 → 520 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321963 · Java 1.8 №11321964 · Python 3.12 x64 №11321965 · Rust 1.75 x64 №11321966 · Go 1.14 x64 №11322291.

Java 1.8, envío 11322007. Tiempo 0,109 → 0,125 s, memoria 1268 → 828 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1838_math.cpp](1838_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.093 s | 968 KB | 11321963 |
| [1838_math.go](1838_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.078 s | 3336 KB | 11322291 |
| [1838_math.java](1838_math.java) | Java 1.8 | math | O(n) | AC | 0.109 s | 1268 KB | 11321964 |
| [1838_math.py](1838_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.156 s | 10892 KB | 11321965 |
| [1838_math.rs](1838_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 2664 KB | 11321966 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1838_math_optimized.py](1838_math_optimized.py) \* | Python 3.12 x64 | math | O(n) | AC | 0.156 s | 8196 KB | 11319948 |
| [1838_math_optimized.rs](1838_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 596 KB | 11319998 |
| [1838_math_optimized.go](1838_math_optimized.go) \* | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1320 KB | 11320023 |
| [1838_math_optimized.cpp](1838_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 520 KB | 11320066 |
| [1838_math_optimized.java](1838_math_optimized.java) \* | Java 1.8 | math | O(n) | AC | 0.125 s | 828 KB | 11322007 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
