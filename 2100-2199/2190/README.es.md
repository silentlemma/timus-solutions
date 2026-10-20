# 2190. Menos movimientos de rocas para dejar los montones en proporción

[Timus 2190](https://acm.timus.ru/problem.aspx?space=1&num=2190) · dificultad 1229 · math, sorting

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N montones de sᵢ rocas. Un minuto añade o quita una sola roca.
Hallar el menor tiempo tras el cual los montones siguen la proporción
p₁ : … : p_N sin estar todos vacíos. Los límites son 2 segundos y
256 MB.

## Entrada

N, 2 ≤ N ≤ 10⁵, y luego s₁ … s_N y p₁ … p_N, todos entre 1 y 10⁹.

## Salida

El menor número de minutos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
21 34
2 3
```

Salida:

```
2
```

## Solución

Se dividen todos los pᵢ entre su máximo común divisor y se obtiene qᵢ.
Un conjunto no vacío de montones en esa proporción es exactamente
k · qᵢ con k ≥ 1 entero, así que la respuesta es el mínimo sobre k de

cost(k) = Σ |sᵢ − k qᵢ| = Σ qᵢ · |sᵢ / qᵢ − k|.

Es una suma de distancias de k a los puntos sᵢ / qᵢ con pesos qᵢ, una
función convexa cuyo mínimo real está en una mediana ponderada: se
ordenan los cocientes, comparando a / b con c / d como a · d frente a
c · b en 64 bits, y se toma el primer cociente donde el peso acumulado
llega a la mitad del total. El mejor entero es el suelo de ese cociente
o uno más, y el suelo se omite si es cero. Los dos candidatos distan a
lo sumo 1 del mínimo real, así que cada coste es menor que
cost(1) + Σqᵢ ≤ 2 · 10¹⁴ y cabe en 64 bits.

En el ejemplo los cocientes son 10.5 y 11.33, el segundo lleva peso 3 de
5 y es la mediana, y k = 11 da 22 y 33 con coste 1 + 1.

La ordenación da O(N log N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2190_math_sorting.cpp](2190_math_sorting.cpp) | G++ 13.2 x64 | math, sorting | O(N log N) | AC | 0.203 s | 1564 KB |
| [2190_math_sorting.go](2190_math_sorting.go) | Go 1.14 x64 | math, sorting | O(N log N) | AC | 0.078 s | 5848 KB |
| [2190_math_sorting.java](2190_math_sorting.java) | Java 1.8 | math, sorting | O(N log N) | AC | 0.140 s | 2732 KB |
| [2190_math_sorting.py](2190_math_sorting.py) | Python 3.12 x64 | math, sorting | O(N log N) | AC | 0.875 s | 24836 KB |
| [2190_math_sorting.rs](2190_math_sorting.rs) | Rust 1.75 x64 | math, sorting | O(N log N) | AC | 0.062 s | 5304 KB |
