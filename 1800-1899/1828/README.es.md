# 1828. Aproximación por una progresión

[Timus 1828](https://acm.timus.ru/problem.aspx?space=1&num=1828) · dificultad 478 · math

Problema original de Alexey Samsonov, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados los enteros a₁, …, aₙ, hallar la progresión aritmética b₁, …, bₙ,
no necesariamente entera, que minimiza Σ(aᵢ − bᵢ)².

## Entrada

n (2 ≤ n ≤ 10⁴), luego a₁, …, aₙ, cada uno de valor absoluto no mayor
que 10⁴.

## Salida

El primer término y la diferencia, con error absoluto o relativo de
como mucho 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 6 10 15
```

Salida:

```
0.400 4.900
```

### Ejemplo 2

Entrada:

```
4
-2 -2 -2 -2
```

Salida:

```
-2 0
```

## Solución

Una progresión es bᵢ = b + d·xᵢ con xᵢ = i − 1, así que se trata de la
recta de mínimos cuadrados ajustada a los puntos (xᵢ, aᵢ). Igualar a cero las
derivadas respecto de b y d da las ecuaciones normales, cuya solución
es

d = (n·Σxa − Σx·Σa) / (n·Σx² − (Σx)²),  b = (Σa − d·Σx) / n.

Las cuatro sumas son enteros que caben en 64 bits (n·Σxa queda por
debajo de 10¹⁶). Después C++, Go, Java y Rust usan coma flotante;
Python conserva fracciones exactas hasta la salida. El denominador
vale n²(n² − 1)/12, nunca 0 para n ≥ 2. `O(n)`.

Para el primer ejemplo x̄ = 1.5 y ā = 7.75; Σ(x − x̄)(a − ā) = 24.5 y
Σ(x − x̄)² = 5, así que d = 4.9 y b = 7.75 − 4.9·1.5 = 0.4.

Trampas:

- la progresión se ajusta a las posiciones 0 … n − 1, no solo a los
  valores: la media no basta;
- Σx² ronda 3·10¹¹ y n·Σx² ronda 3·10¹⁵, más allá de 32 bits;
- el primer término es b₁, el valor en la primera posición, no la
  ordenada en otro origen.

## Soluciones optimizadas

C++/Go/Java/Rust acumulan solo A=Σaᵢ y B=Σ(i−1)aᵢ. Las mismas ecuaciones dan first=((4n−2)A−6B)/(n(n+1)) y step=(12B−6(n−1)A)/(n(n²−1)), sin acumular Σx² ni restar coeficientes ya redondeados. Numeradores bajo10¹³ en magnitud y denominadores bajo10¹²; división larga entera genera nueve decimales y redondea según el resto doble. Cada resto por diez queda bajo10¹³: cabe en64 bits con signo. Error de formato hasta0.5·10⁻⁹. Tiempo O(n), espacio O(1), E/S acotada sin formateadores flotantes. Se conservan bases; Python reutiliza la admitida.

Las implementaciones base aceptadas [1828_math.py](1828_math.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1828_math.cpp](1828_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 120 KB | 11328311 |
| [1828_math.go](1828_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1256 KB | 11290410 |
| [1828_math.java](1828_math.java) | Java 1.8 | math | O(n) | AC | 0.093 s | 964 KB | 11328312 |
| [1828_math.py](1828_math.py) \* | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 1936 KB | 11328313 |
| [1828_math.rs](1828_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 536 KB | 11328314 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1828_math_optimized.cpp](1828_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 68 KB | 11315311 |
| [1828_math_optimized.go](1828_math_optimized.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 332 KB | 11315314 |
| [1828_math_optimized.java](1828_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.109 s | 388 KB | 11315307 |
| [1828_math_optimized.rs](1828_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 44 KB | 11315315 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
