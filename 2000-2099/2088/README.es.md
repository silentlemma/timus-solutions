# 2088. Probabilidad de ganar eligiendo el mejor color tras un reparto a ciegas

[Timus 2088](https://acm.timus.ru/problem.aspx?space=1&num=2088) · dificultad 5162 · dp, combinatorics

Problema original de Eugene Kurpilyansky.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una baraja tiene cartas de colores 0 … k; el color 0 es un comodín.
Sasha toma algunas cartas conocidas y luego recibe t cartas al azar del
resto. Conociendo la mano, elige un color c ≥ 1 que maximiza la
probabilidad de ganar; después se abren y cartas al azar del mazo
restante, y Sasha gana si su mano tiene al menos x cartas más de los
colores 0 y c que las abiertas. Hallar la probabilidad de que Sasha gane
módulo 10⁹ + 7. Los límites son 2 segundos y 256 MB.

## Entrada

k ≤ 100 y t ≤ 100, las cantidades c₀ … c_k de cada color en la baraja (a
lo sumo 100 cartas), las cantidades s₀ … s_k que toma Sasha, y después
x e y.

## Salida

La probabilidad p/q como p·q⁻¹ módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1
1 2 0 1
0 1 0 0
1 2
```

Salida:

```
666666672
```

### Ejemplo 2

Entrada:

```
2 3
6 5 3
2 2 0
5 3
```

Salida:

```
176428573
```

## Solución

Tras las cartas conocidas quedan rᵢ cartas del color i, R en total, y
D = R − t siguen en el mazo tras el reparto a ciegas. Si la mano tiene h
cartas de los colores 0 y c, el mazo tiene u = c₀ + c_c − h de ellas, las
abiertas siguen una ley hipergeométrica, y Sasha gana cuando entre las y
abiertas hay a lo sumo h − x de los colores 0 y c. Así que el número de
aperturas ganadoras, de C(D, y), es
W(u, h − x) = Σ_{j ≤ h−x} C(u, j) C(D − u, y − j), una tabla calculada
una vez.

El reparto a ciegas da z comodines y dᵢ cartas del color i, con
Σ dᵢ = t − z; tiene C(r₀, z) Π C(rᵢ, dᵢ) variantes equiprobables. Para un
z fijo la puntuación del color i solo depende de dᵢ, y la respuesta
necesita la suma sobre todos los repartos de la puntuación máxima. Esa
suma se reúne por umbrales: todos los pares (color, dᵢ > 0) se ordenan
por puntuación y se mantiene un polinomio P(X) = Π Fᵢ(X), donde Fᵢ suma
C(rᵢ, d) X^d sobre los d permitidos hasta ahora (d = 0 siempre está
permitido, y además da la puntuación base: el máximo sobre los colores
de la puntuación con dᵢ = 0). Permitir un par más (i, d) convierte Fᵢ en
Fᵢ + C(rᵢ, d) X^d, así que P crece en C(rᵢ, d) X^d · P / Fᵢ; la división
es exacta porque Fᵢ empieza por 1. El aumento del coeficiente de
X^{t−z} cuenta los repartos cuya mejor puntuación acaba de pasar a ser
esta, y cada uno se suma con esa puntuación. Los conteos se reducen
módulo 10⁹ + 7 y el resultado se divide entre C(R, t) C(D, y). El trabajo es O(t · k · t²) en el peor caso, mínimo con
estos límites.

En el primer ejemplo con cualquier mano la mejor elección es el color 1,
y dos de las tres manos equiprobables ganan, así que la respuesta es
2/3.

## Notas por lenguaje

Las puntuaciones se comparan de forma exacta; llegan a C(100, 50) ≈ 10²⁹.
C++ y Rust las guardan en enteros sin signo de 128 bits, Go y Java en
enteros grandes, y Python en sus propios enteros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2088_dp_combinatorics.cpp](2088_dp_combinatorics.cpp) | G++ 13.2 x64 | dp, combinatorics | O(t^3 k) | AC | 0.015 s | 672 KB |
| [2088_dp_combinatorics.go](2088_dp_combinatorics.go) | Go 1.14 x64 | dp, combinatorics | O(t^3 k) | AC | 0.031 s | 2368 KB |
| [2088_dp_combinatorics.java](2088_dp_combinatorics.java) | Java 1.8 | dp, combinatorics | O(t^3 k) | AC | 0.125 s | 2536 KB |
| [2088_dp_combinatorics.py](2088_dp_combinatorics.py) | Python 3.12 x64 | dp, combinatorics | O(t^3 k) | AC | 0.093 s | 1268 KB |
| [2088_dp_combinatorics.rs](2088_dp_combinatorics.rs) | Rust 1.75 x64 | dp, combinatorics | O(t^3 k) | AC | 0.046 s | 476 KB |
