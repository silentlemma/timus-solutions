# 1707. El secreto del Hipnosapo

[Timus 1707](https://acm.timus.ru/problem.aspx?space=1&num=1707) · dificultad 1900 · fenwick

Problema original de Dmitry Ivankov, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los estados son los números 0 … n − 1. Cada una de las m leyes produce
los estados de los ojos (sᵢ, tᵢ) = ((s₀ + iΔs) mod n,
(t₀ + iΔt) mod n) para i = 0 … k − 1. Cada uno de los p experimentos
produce, con la misma clase de regla, q estados del aparato
(aⱼ, bⱼ, cⱼ, dⱼ). Para un estado del aparato, xⱼ = 1 si algún estado
de los ojos tiene s entre aⱼ y bⱼ y t entre cⱼ y dⱼ, con los extremos
incluidos, y xⱼ = 0 en otro caso.

## Entrada

n y m (1 ≤ n ≤ 5000, 1 ≤ m ≤ 1000), luego m líneas s₀ t₀ Δs Δt k
(0 ≤ s₀, t₀, |Δs|, |Δt| ≤ n − 1, 1 ≤ k ≤ 567). Después p
(1 ≤ p ≤ 345) y p líneas a₀ b₀ c₀ d₀ Δa Δb Δc Δd q, con las mismas
cotas para inicios y pasos y 1 ≤ q ≤ 345.

## Salida

Una línea por experimento: para q ≤ 20 los dígitos x₀ … x_{q−1} sin
espacios, para q > 20 el número (Σ 7ʲ xⱼ) mod 200904040963.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
0 1 0 0 1
1 2 0 0 1
2 0 0 0 1
5
0 0 1 1 0 0 0 0 5
1 1 0 0 0 0 0 0 3
0 1 0 0 0 0 0 0 345
1 2 1 1 0 0 0 1 4
1 2 1 1 0 0 0 1 3
```

Salida:

```
11111
000
0
0110
011
```

## Solución

Los estados de los ojos son a lo sumo 567000 puntos de la cuadrícula
n × n, y cada estado del aparato pregunta si un rectángulo con lados
paralelos a los ejes contiene alguno. Se responde contando: si C(x, y)
es el número de puntos con s ≤ x y t ≤ y, el rectángulo
[a, b] × [c, d] contiene
C(b, d) − C(a − 1, d) − C(b, c − 1) + C(a − 1, c − 1) puntos, y una
esquina con una coordenada negativa cuenta 0.

Todas las esquinas se conocen de antemano, así que se responden fuera
de línea. Se recorre t de 0 a n − 1: se añaden los puntos de la fila t
a un árbol de Fenwick sobre s y se lee C(x, t) para cada esquina de esa
fila como suma de prefijo del árbol. Una tabla completa de C ocuparía
25 millones de contadores, demasiada memoria, mientras que el recorrido
guarda solo el árbol y un contador por esquina. Con P puntos y
Q = 4 · Σq esquinas el tiempo es `O((P + Q) log n + n)`.

Trampas:

- los pasos pueden ser negativos, así que los restos deben llevarse a
  0 … n − 1;
- los extremos de un intervalo pueden venir en cualquier orden,
  incluido aⱼ > bⱼ;
- el hash pone x₀ en la potencia más baja, 7⁰;
- la solución en Python guarda puntos y esquinas en arreglos compactos,
  ordenados por fila con un ordenamiento por conteo: las listas de
  objetos enteros llegan aquí a unos 77 MB, por encima del límite de
  64 MB.

Las respuestas coinciden con una implementación aceptada independiente
en leyes y experimentos aleatorios sobre cuadrículas pequeñas, en los
tamaños máximos y en pocas leyes lentas con rectángulos estrechos,
donde se mezclan ceros y unos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1707_fenwick.cpp](1707_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((P + Q) log n + n) | AC | 0.078 s | 14752 KB |
| [1707_fenwick.go](1707_fenwick.go) | Go 1.14 x64 | fenwick | O((P + Q) log n + n) | AC | 0.093 s | 40324 KB |
| [1707_fenwick.java](1707_fenwick.java) | Java 1.8 | fenwick | O((P + Q) log n + n) | AC | 0.187 s | 20128 KB |
| [1707_fenwick.py](1707_fenwick.py) | Python 3.12 x64 | fenwick | O((P + Q) log n + n) | AC | 3.046 s | 19836 KB |
| [1707_fenwick.rs](1707_fenwick.rs) | Rust 1.75 x64 | fenwick | O((P + Q) log n + n) | AC | 0.062 s | 24072 KB |
