# 1535. El hobbit, o Historia de una ida y de una vuelta

[Timus 1535](https://acm.timus.ru/problem.aspx?space=1&num=1535) · dificultad 497 · constructive

Problema original de Alexander Ipatov, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Bilbo sale de la ciudad 1, visita una vez cada una de las ciudades
2 … N y vuelve a la ciudad 1 (2 ≤ N ≤ 50000). Entrar en la ciudad P
desde la ciudad Q cuesta P·Q monedas de oro. Hay que escribir un orden
de visita de coste total mínimo y otro de coste total máximo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

Dos líneas con N números cada una, empezando por 1: el orden más barato
y el más caro. Se acepta cualquier orden óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
1 4 2 3
1 3 4 2
```

## Solución

El coste del ciclo suma productos de vecinos, incluida la arista final
de vuelta a 1. Sea D(i,j)=N²−ij, matriz no negativa y simétrica.
Para i<j<k<l,

(Dᵢⱼ+Dₖₗ)−(Dᵢₖ+Dⱼₗ)=(k−j)(i−l)<0,

(Dᵢₖ+Dⱼₗ)−(Dᵢₗ+Dⱼₖ)=(j−i)(k−l)<0.

Son las desigualdades de Supnick. El ciclo D mínimo recorre primero los
impares en orden ascendente y luego los pares en orden descendente. El
ciclo D máximo alterna dos ramas. Cada coste D es N³ menos la suma
original de productos, por lo que estos ciclos maximizan y minimizan
dicha suma, respectivamente. [Teoremas de ciclos extremos](https://doi.org/10.1016/S0166-218X(99)00148-1)

Para el máximo, emitir 1, 3, 5, … y luego los pares en orden descendente
hasta 2. Para el mínimo, comenzar en N, con q=⌊(N−1)/2⌋. Para k=1…q,
una rama toma aₖ=k+1 si k es impar y N−k si es par. La otra toma bₖ=k
si k es impar y N−k+1 si es par. Unir N, a₁, …, a_q, el único valor
central sin usar si N es par, y b_q, …, b₁. El centro para N par vale
2⌊N/4⌋+1. Rotar el ciclo para comenzar en 1. Al leerlo al revés se obtiene
el ciclo D máximo 1, N−1, 3, N−3, …, N−2, 2, N, lo que prueba el mínimo
original. Para N=2 y N=3 el conjunto de aristas no dirigidas es único.

Los programas sencillos guardan brazos y rotan el ciclo, con O(N)
tiempo y espacio auxiliar. Los rápidos distintos generan los mismos
índices directamente con búferes de salida acotados.

Ambas líneas empiezan en 1. El coste incluye la arista de cierre y cada
ciudad se imprime una sola vez.

## Soluciones optimizadas

C++, Go y Rust indexan el mismo ciclo de dos brazos sin guardar marcas, brazos, ciclo, rotación ni cadenas. Sea q=⌊(N−1)/2⌋. Emitir 1,N y aₖ=k+1 para k impar o N−k para k par, k=1…q. Si N>2 es par, queda el centro 2⌊N/4⌋+1. Terminar con bₖ=k para k impar o N−k+1 para k par, k=q…2; b₁=1 ya está primero. Para N=2 se emite 1,2. Es exactamente la construcción anterior sin almacenarla. El máximo conserva impares ascendentes y pares descendentes. Bloques de 8192 bytes dan tiempo O(N) y espacio extra O(1). Se conservan bases; Java/Python reutilizan las admitidas. Una DP exacta independiente verifica ambos extremos hasta N=14 como regresión; la reducción Supnick en la explicación sencilla demuestra la optimalidad general.

El envío aceptado en Rust 1.75 x64 tarda 0.046 s frente a 0.031 s de la base y usa 232 KB frente a 4376 KB.

Las implementaciones base aceptadas [1535_constructive.java](1535_constructive.java), [1535_constructive.py](1535_constructive.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1535_constructive.cpp](1535_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1700 KB | 11287470 |
| [1535_constructive.go](1535_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 7060 KB | 11287471 |
| [1535_constructive.java](1535_constructive.java) \* | Java 1.8 | constructive | O(N) | AC | 0.140 s | 11176 KB | 11287473 |
| [1535_constructive.py](1535_constructive.py) \* | Python 3.12 x64 | constructive | O(N) | AC | 0.109 s | 8752 KB | 11287472 |
| [1535_constructive.rs](1535_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 4376 KB | 11287474 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1535_constructive_optimized.cpp](1535_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 100 KB | 11315377 |
| [1535_constructive_optimized.go](1535_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 936 KB | 11315379 |
| [1535_constructive_optimized.rs](1535_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 232 KB | 11315380 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
