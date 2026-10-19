# 1838. El golpe del samurái

[Timus 1838](https://acm.timus.ru/problem.aspx?space=1&num=1838) · dificultad 721 · math

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
- 2sₙ llega a 2·10⁹, que no cabe en enteros de 32 bits.

Las respuestas coinciden con un recuento de los cortes que hacen caer
una parte sobre una malla fina en unos cientos de tallos pequeños y con
una implementación aceptada independiente en las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1838_math.cpp](1838_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.093 s | 984 KB |
| [1838_math.go](1838_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.078 s | 3324 KB |
| [1838_math.java](1838_math.java) | Java 1.8 | math | O(n) | AC | 0.093 s | 1300 KB |
| [1838_math.py](1838_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.171 s | 11024 KB |
| [1838_math.rs](1838_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 2668 KB |
