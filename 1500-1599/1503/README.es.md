# 1503. Polinomio

[Timus 1503](https://acm.timus.ru/problem.aspx?space=1&num=1503) · dificultad 1709 · math

Problema original de Den Raskovalov, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado un polinomio a0·x^N + a1·x^(N−1) + … + aN de grado N (1 ≤ N ≤ 5)
con coeficientes enteros (−100 ≤ ai ≤ 100, a0 ≠ 0), hay que escribir
todas sus raíces reales en orden creciente, repitiendo cada una tantas
veces como su multiplicidad, con precisión 10⁻⁶.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los coeficientes a0, a1, …, aN, uno por línea.

## Salida

Las raíces reales, una por línea; nada si no hay ninguna.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1
-2
1
```

Salida:

```
1
1
```

## Solución

Las raíces simples son fáciles: en ellas el polinomio cambia de signo,
y entre dos raíces vecinas de la derivada es monótono, así que cambia
de signo como mucho una vez. Las raíces de la derivada se hallan igual,
de forma recursiva; con ellas se corta el intervalo
|x| < 1 + max |ai / a0| (todas las raíces están dentro) y se biseca
cada trozo con signos distintos en los extremos.

Una raíz de multiplicidad par no cambia el signo, y una múltiple impar
es difícil de fijar numéricamente, así que primero se quitan las raíces
múltiples de forma exacta. Una raíz racional p/q tiene p divisor de aN
y q divisor de a0; cada candidata se prueba con aritmética entera
(q^N·f(p/q) = 0) y se saca con división sintética entre q·x − p, que
deja coeficientes enteros. Después, una raíz repetida es irracional y
su conjugada también se repite, así que el resto tiene como factor el
cuadrado de un trinomio cuadrático irracional. Con grado como mucho 5 y
sin raíces racionales, eso solo pasa si el resto es exactamente
a0·(x² + b·x + d)² de grado 4. Comparando coeficientes (ahora a0, …, a4 son los del resto), con
u = 4·a0 y e = u·a2 − a1², ocurre cuando 2·a1·e = a3·u² y e² = a4·u³, y entonces
las raíces dobles son (−a1 ± √(a1² − 2e)) / u. Lo que queda solo tiene
raíces simples para la bisección. En total, unos cientos de
evaluaciones.

Detalles a tener en cuenta:

- una raíz doble solo toca el eje, así que buscar cambios de signo la
  pierde (prueba 01, el ejemplo);
- una raíz puede tener multiplicidad 5 (prueba 02);
- las raíces repetidas pueden ser irracionales (pruebas 03, 06, gen3);
- sin raíces reales la salida queda vacía (prueba 04);
- con a0 ≠ ±1 hay raíces racionales fraccionarias (pruebas 05, 07);
- la raíz 0 no sirve para la búsqueda de divisores (todo p divide a 0),
  así que primero se quitan los términos independientes nulos
  (prueba 08);
- cinco raíces simples solo se separan con las raíces de la derivada
  entre ellas (prueba 09);
- las raíces se comparan con tolerancia, así que las pruebas usan un
  comprobador (todas las pruebas).

## Notas por lenguaje

La solución en C++ biseca en `long double` pero imprime un `double`: el
`printf` de MinGW que usa G++ en Windows puede imprimir mal `long double`.
La solución en Python trabaja de forma exacta con `Fraction` todo el
tiempo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1503_math.cpp](1503_math.cpp) | G++ 13.2 x64 | math | O(N^2 * STEPS) | AC | 0.031 s | 220 KB |
| [1503_math.go](1503_math.go) | Go 1.14 x64 | math | O(N^2 * STEPS) | AC | 0.031 s | 1136 KB |
| [1503_math.java](1503_math.java) | Java 1.8 | math | O(N^2 * STEPS) | AC | 0.125 s | 1148 KB |
| [1503_math.py](1503_math.py) | Python 3.12 x64 | math | O(N^2 * STEPS) | AC | 0.140 s | 1144 KB |
| [1503_math.rs](1503_math.rs) | Rust 1.75 x64 | math | O(N^2 * STEPS) | AC | 0.046 s | 268 KB |
