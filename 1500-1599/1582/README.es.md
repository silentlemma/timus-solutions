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

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

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

`1582_math_optimized.py`. Mantiene el pago racional exacto y redondea directamente como floor((2*1000*numerator+denominator)/(2*denominator)), sin búsqueda binaria. Analiza notación decimal/científica desde bytes, elimina ceros de relleno antes de las potencias y construye los coeficientes enteros en grupos de nueve cifras. La agrupación evita el límite de conversión del coeficiente sin perder precisión ni redondeo de mitad hacia arriba. El Accepted registrado corresponde a PyPy 3.10. El exponente aún usa int(): un exponente con relleno excesivo de ceros puede alcanzar el límite de conversión en CPython; no se afirma compatibilidad irrestricta con ese caso. I es el tamaño de entrada y D el de los operandos normalizados; espacio O(I+D), con coste aritmético dependiente de D. Los coeficientes positivos y los tres resultados se conservan; vacía la salida antes de salir.

Frente a `1582_math.py`: tiempo 0.078 s → 0.109 s; memoria 532 KB → 292 KB.

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

`1582_math_optimized.cpp`. Conserva aritmética racional exacta y redondeo de mitades hacia arriba, sin epsilon de coma flotante. Guarda enteros no negativos en dígitos u32 de base 10^9 y normaliza ceros iniciales/finales y escala científica antes de formar los arreglos. Acumula N,D para P=1000N/D y busca binariamente la respuesta redondeada acotada con 2000N >= (2m-1)D y productos por factores pequeños. Las mitades exactas suben. Si B es la longitud de entrada cruda y Q la precisión decimal normalizada de las cuotas y sus productos, el trabajo escolar es O(B+Q²), con O(B+Q) almacenamiento. El búfer de cifras crudas aún cuesta O(B); los ceros de relleno no se expanden en grandes arreglos de dígitos.

Frente a `1582_math.cpp`: tiempo 0.031 s → 0.015 s; memoria 388 KB → 156 KB.

`1582_math_optimized.rs`. Conserva aritmética racional exacta y redondeo de mitades hacia arriba, sin epsilon de coma flotante. Guarda enteros no negativos en dígitos u32 de base 10^9 y normaliza ceros iniciales/finales y escala científica antes de formar los arreglos. Acumula N,D para P=1000N/D y busca binariamente la respuesta redondeada acotada con 2000N >= (2m-1)D y productos por factores pequeños. Las mitades exactas suben. Si B es la longitud de entrada cruda y Q la precisión decimal normalizada de las cuotas y sus productos, el trabajo escolar es O(B+Q²), con O(B+Q) almacenamiento. El búfer de cifras crudas aún cuesta O(B); los ceros de relleno no se expanden en grandes arreglos de dígitos.

Frente a `1582_math.rs`: tiempo 0.046 s → 0.015 s; memoria 212 KB → 64 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1582_math_optimized.cpp`: puesto de tiempo 1/103 y de memoria 7/103 en esta muestra comparable.

`1582_math_optimized.py`: puesto de tiempo 23/34 y de memoria 1/34 en esta muestra comparable.

`1582_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1582_math_optimized.cpp](1582_math_optimized.cpp) | G++ 13.2 x64 | math | O(B+Q²) | AC | 0.015 s | 156 KB | 11325058 |
| [1582_math_optimized.rs](1582_math_optimized.rs) | Rust 1.75 x64 | math | O(B+Q²) | AC | 0.015 s | 64 KB | 11325102 |
| [1582_math_optimized.py](1582_math_optimized.py) \* | PyPy 3.10 x64 | math | Exact integer arithmetic; O(I+D) storage | AC | 0.109 s | 292 KB | 11325490 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
