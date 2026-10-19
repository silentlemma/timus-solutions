# 2083. Una suma ponderada de potencias de una permutación por ciclos

[Timus 2083](https://acm.timus.ru/problem.aspx?space=1&num=2083) · dificultad 2654 · math

Problema original de Denis Dublennykh.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da una permutación p de 1 … n. La fila t de una matriz A de m × n es
p aplicada t veces: A[t][j] = pᵗ(j) (la primera fila es la propia p).
Calcular el vector q × A para un q dado de longitud m, es decir,
v[j] = q₁ p(j) + q₂ p²(j) + … + q_m pᵐ(j). Los límites son 4 segundos y
256 MB.

## Entrada

m y n, 2 ≤ m, n ≤ 5·10⁴, después p(1) … p(n) y después q₁ … q_m,
0 ≤ qᵢ ≤ 10⁹.

## Salida

Las n componentes de q × A.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4
3 2 4 1
3 5 8
```

Salida:

```
37 32 41 50
```

## Solución

Se descompone p en ciclos. En un ciclo c₀, c₁, …, c_{L−1} con
p(c_s) = c_{s+1} (índices módulo L), pᵗ(c_s) = c_{(s+t) mod L}. Se
pliega q por el resto de t módulo L: Q[r] es la suma de q_t sobre
t ≡ r (mod L). Entonces v[c_s] = Σ_r Q[r] · c_{(s+r) mod L}, una
correlación cíclica de longitud L. El pliegue solo depende de L, y los
ciclos tienen a lo sumo unas √(2n) longitudes distintas, así que los
pliegues cuestan O(m √n).

Una correlación es un producto de polinomios: Q invertido por el ciclo
escrito dos veces da v[c_s] como coeficiente s + L − 1. Los valores
llegan a 5·10⁴ · 5·10⁴ · 10⁹ = 2.5·10¹⁸, así que el producto debe ser
exacto. C++, Go, Java y Rust usan una transformada teórico-numérica
módulo tres primos (998244353, 167772161, 469762049) y recomponen los
coeficientes con el método de Garner; el resultado es menor que 2⁶³, así
que la aritmética de 64 bits con desbordamiento lo da exacto. Python
empaqueta cada sucesión en un solo entero grande, diez bytes por número,
multiplica los dos enteros y relee los coeficientes, ya que ninguno se
sale de sus diez bytes. Los ciclos cortos (hasta 32) se suman
directamente. Los productos suman O(n log n) con NTT y O(n^(log₂ 3)) con
la multiplicación de Karatsuba de Python.

En el ejemplo p es el ciclo 1 → 3 → 4 → 1 más el punto fijo 2, y
v[2] = (3 + 5 + 8) · 2 = 32.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2083_math.cpp](2083_math.cpp) | G++ 13.2 x64 | math | O(n log n + m sqrt n) | AC | 0.593 s | 12432 KB |
| [2083_math.go](2083_math.go) | Go 1.14 x64 | math | O(n log n + m sqrt n) | AC | 0.734 s | 19740 KB |
| [2083_math.java](2083_math.java) | Java 1.8 | math | O(n log n + m sqrt n) | AC | 1.500 s | 16236 KB |
| [2083_math.py](2083_math.py) | Python 3.12 x64 | math | O(n^(log₂ 3) + m sqrt n) | AC | 2.781 s | 27692 KB |
| [2083_math.rs](2083_math.rs) | Rust 1.75 x64 | math | O(n log n + m sqrt n) | AC | 0.593 s | 12824 KB |
