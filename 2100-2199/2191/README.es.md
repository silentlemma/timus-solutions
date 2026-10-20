# 2191. Escribir una poligonal como suma con signos de exactamente N valores absolutos

[Timus 2191](https://acm.timus.ru/problem.aspx?space=1&num=2191) · dificultad 1765 · math, constructive

Problema original de Valentin Zuev y Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función lineal a trozos viene dada por N vértices (xᵢ, yᵢ) con xᵢ
crecientes. Escribirla en [x₁, x_N] como
±|a₁x + b₁| ± … ± |a_N x + b_N| con exactamente N términos, con el
formato de los ejemplos. Los límites son 3 segundos y 256 MB.

## Entrada

N, 2 ≤ N ≤ 10⁵, y luego los N vértices con coordenadas enteras de valor
absoluto hasta 10⁵.

## Salida

La expresión en una línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 0
2 1
```

Salida:

```
|1x-1|+|0x+0|
```

### Ejemplo 2

Entrada:

```
2
0 1
1 2
```

Salida:

```
|1x-0|+|0x+1|
```

### Ejemplo 3

Entrada:

```
3
-1 1
0 -1
1 0
```

Salida:

```
|1.5x-0|-|0.5x+0.5|-|0x+0.5|
```

## Solución

Sea sᵢ la pendiente del i-ésimo segmento. En un vértice interior xᵢ la
pendiente pasa de sᵢ₋₁ a sᵢ, y el término cᵢ |x − xᵢ| con
cᵢ = (sᵢ − sᵢ₋₁) / 2 hace justo ese quiebre, porque su pendiente salta
2cᵢ allí. Los N − 2 vértices interiores usan N − 2 términos, y en
[x₁, x_N] lo que queda es una función lineal, escrita con los dos
restantes:

- α |x − x₁| vale α(x − x₁) en el intervalo. A la izquierda de todos los
  quiebres los términos de quiebre tienen pendiente
  −Σcᵢ = −(s_last − s₁) / 2, así que α = (s₁ + s_last) / 2 recupera la
  primera pendiente.
- Una constante β, escrita como |0x + β| con el signo de β delante, fija
  el valor en x₁: β = y₁ − Σ cᵢ (xᵢ − x₁).

Esa suma parece una mezcla de muchas fracciones, pero la suma por partes
convierte Σ (sᵢ − sᵢ₋₁)(xᵢ − x₁) en
s_last (x_{N−1} − x₁) − (y_{N−1} − y₁), porque cada sⱼ por el ancho de
su segmento es simplemente su subida. Así, los numeradores de cᵢ y α son
sumas o diferencias de dos productos de diferencias de coordenadas, y
sus denominadores son el doble de un producto de dos diferencias de
coordenadas. El numerador de la ordenada bᵢ = −cᵢ xᵢ necesita otro factor
de coordenada. Cada diferencia de coordenadas tiene valor absoluto de
a lo sumo 2·10⁵, por lo que ese numerador tiene valor absoluto de a lo
sumo 8·10¹⁵; la aritmética entera para construir los coeficientes cabe
en 64 bits con signo.

Cuidado (pruebas 13–14): las pendientes grandes cerca de los límites de
coordenadas requieren enteros intermedios de 64 bits, incluido el factor
adicional xᵢ al calcular las ordenadas.

Cada fracción se convierte por división entera, truncando a 18
decimales y sin ceros finales, así que la expresión se desvía a lo sumo
unos 10⁻¹⁸ por coeficiente. Redondear antes las pendientes dejaría que
los errores se acumularan a lo largo de la línea.

En el tercer ejemplo las pendientes son −2 y 1, así que el quiebre en 0
es 1.5|x|, α = −0.5 y β = 1 − 1.5 = −0.5.

Esto cuesta O(N) con 18 dígitos por número.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2191_math_constructive.cpp](2191_math_constructive.cpp) | G++ 13.2 x64 | math, constructive | O(N) | AC | 0.234 s | 5020 KB |
| [2191_math_constructive.go](2191_math_constructive.go) | Go 1.14 x64 | math, constructive | O(N) | AC | 0.093 s | 14532 KB |
| [2191_math_constructive.java](2191_math_constructive.java) | Java 1.8 | math, constructive | O(N) | AC | 0.218 s | 22016 KB |
| [2191_math_constructive.py](2191_math_constructive.py) | Python 3.12 x64 | math, constructive | O(N) | AC | 0.593 s | 28096 KB |
| [2191_math_constructive.rs](2191_math_constructive.rs) | Rust 1.75 x64 | math, constructive | O(N) | AC | 0.062 s | 9732 KB |
