# 1582. Casas de apuestas

[Timus 1582](https://acm.timus.ru/problem.aspx?space=1&num=1582) · dificultad 123 · math

Problema original de Sergey Pupyrev, preparado por Vladimir Yakovlev, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un partido tiene tres resultados con las mejores cuotas k₁, k₂ y k₃
(0.01 … 100): una apuesta de x al resultado correcto paga k·x, y una
errada no paga nada. Hay que repartir apuestas por un total de
1000 libras entre los tres resultados para recuperar lo máximo en el
peor caso, e imprimir esa cantidad redondeada al entero más cercano.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k₁, k₂ y k₃.

## Salida

El pago garantizado, redondeado.

## Ejemplos

### Ejemplo 1

Entrada:

```
3.5 3.5 3.5
```

Salida:

```
1167
```

### Ejemplo 2

Entrada:

```
1.25 10.0 5.75
```

Salida:

```
931
```

## Solución

Se apuesta xᵢ al resultado i, con x₁ + x₂ + x₃ = 1000; el resultado i
paga kᵢ·xᵢ. Para garantizar un pago P, cada resultado debe pagar al
menos P, así que xᵢ ≥ P / kᵢ, y sumar las tres desigualdades da
1000 ≥ P·(1/k₁ + 1/k₂ + 1/k₃). Las apuestas xᵢ = P / kᵢ alcanzan esa
cota, así que el mayor pago garantizado es

P = 1000 / (1/k₁ + 1/k₂ + 1/k₃).

Se lee cada decimal exactamente como a / 10ˢ. Partiendo de N = 1 y
D = 0, para cada cuota se actualiza D = D·a + N·10ˢ y luego N = N·a.
Así, P = 1000·N / D. Con enteros de precisión arbitraria, se busca
por búsqueda binaria el mayor entero m que cumple
2·1000·N ≥ (2m − 1)·D; las mitades exactas se redondean hacia arriba
sin errores de coma flotante. La respuesta no supera ⌊1000·100 / 3⌋,
por lo que la búsqueda tiene un número constante de pasos. Para L
dígitos decimales de entrada (tras expandir cualquier exponente),
el tiempo es `O(L^2)` y el espacio es `O(L)`.

Detalles a tener en cuenta:

- con cuotas mayores que 3, el pago garantizado supera lo apostado, como
  en el primer ejemplo;
- una mitad exacta redondea hacia arriba: las cuotas 2, 10 y 25 dan
  1562.5 y la respuesta 1563, mientras que `printf("%.0f")` redondearía
  al par e imprimiría 1562 (prueba 08);
- la coma flotante binaria puede reducir ligeramente una mitad exacta:
  las cuotas 0.02, 0.02 y 0.03 dan exactamente 7.5 y la respuesta 8
  (prueba 10). La precisión decimal no está limitada, así que se usa
  aritmética exacta en lugar de sumar un epsilon.

## Soluciones optimizadas

La solución optimizada en Java lee las tres cuotas con `BufferedReader`
y `StringTokenizer` en lugar de un `Scanner`, y se ahorra sus
expresiones regulares y datos de configuración regional. La aritmética
sigue siendo exacta, con las cuotas en `BigDecimal` y las comparaciones
en `BigInteger`, así que solo se abarata la lectura de la entrada:
{1582_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1582_math_optimized.java`: reducción de tiempo +14.68%; reducción de
  memoria +57.08%; base: `1582_math.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1582_math.go](1582_math.go).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1582_math.cpp](1582_math.cpp) | G++ 13.2 x64 | math | O(L^2) | AC | 0.031 s | 388 KB | 11304410 |
| [1582_math.go](1582_math.go) | Go 1.14 x64 | math | O(L^2) | AC | 0.031 s | 1192 KB | 11298030 |
| [1582_math.java](1582_math.java) | Java 1.8 | math | O(L^2) | AC | 0.109 s | 1780 KB | 11304013 |
| [1582_math.py](1582_math.py) | Python 3.12 x64 | math | O(L^2) | AC | 0.078 s | 532 KB | 11304014 |
| [1582_math.rs](1582_math.rs) | Rust 1.75 x64 | math | O(L^2) | AC | 0.046 s | 212 KB | 11304419 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1582_math_optimized.java](1582_math_optimized.java) | Java 1.8 | math | O(L^2) | AC | 0.093 s | 764 KB | 11304379 |
