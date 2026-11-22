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

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. El comprobador del repositorio exige dos líneas no vacías, cada una una permutación de 1..N que empieza en1. Cierra el recorrido al primer destino, suma productos de ciudades vecinas y compara con el coste mínimo o máximo de referencia; cualquier óptimo empatado es válido.

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

`1535_constructive_optimized.py`. Conserva los recorridos mínimo/máximo exactos, generando ciudades por índice/paridad sin almacenar rutas completas. Convierte y une lotes B=512 de etiquetas en vez de codificar/actualizar bytearray por número. No cambian espacios, primera ciudad ni centro para N par. O(N) operaciones aritméticas, O(N log N) trabajo decimal y O(B log N) cadenas temporales con B fijo. El checker admite cualquier recorrido óptimo; conserva la construcción base.

Accepted exacto CPython 3.12 #11326668: 0.078 s / 840 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 1/33, memoria 1/33. Por debajo de 1024 KB, admisión estricta solo por tiempo.

- `1535_constructive_optimized.py`: 0.078 s / 840 KB; base didáctica conservada `1535_constructive.py` (Python 3.12 x64): 0.109 s / 8752 KB; cambio de tiempo -28.4%; cambio de memoria -90.4%.

Frente a `1535_constructive.py`: tiempo 0.109 s → 0.187 s; memoria 8752 KB → 3 184 KB.

`1535_constructive_optimized.java`. Conserva ambas construcciones extremales demostradas, generando ciudades directamente sin used[], listas con objetos, ciclo, sublistas copiadas ni cadenas completas. El recorrido mínimo emite pares de extremos alternos y la ciudad central restante si procede; el máximo, impares ascendentes y pares descendentes. Los mismos bucles cubren N=2. Cada línea empieza en uno e incluye todas las ciudades una vez. Tiempo O(N) para números acotados y espacio auxiliar O(1) aparte de búferes fijos; conserva la construcción didáctica con listas.

Frente a `1535_constructive.java`: tiempo 0.140 s → 0.109 s; memoria 11176 KB → 504 KB.

C++, Go y Rust indexan el mismo ciclo de dos brazos sin guardar marcas, brazos, ciclo, rotación ni cadenas. Sea q=⌊(N−1)/2⌋. Emitir 1,N y aₖ=k+1 para k impar o N−k para k par, k=1…q. Si N>2 es par, queda el centro 2⌊N/4⌋+1. Terminar con bₖ=k para k impar o N−k+1 para k par, k=q…2; b₁=1 ya está primero. Para N=2 se emite 1,2. Es exactamente la construcción anterior sin almacenarla. El máximo conserva impares ascendentes y pares descendentes. Bloques de 8192 bytes dan tiempo O(N) y espacio extra O(1). Se conservan bases; Java/Python reutilizan las admitidas. Una DP exacta independiente verifica ambos extremos hasta N=14 como regresión; la reducción Supnick en la explicación sencilla demuestra la optimalidad general.

El envío aceptado en Rust 1.75 x64 tarda 0.046 s frente a 0.031 s de la base y usa 232 KB frente a 4376 KB.

Las bases Accepted conservadas [1535_constructive.rs](1535_constructive.rs) pasan también diez primeros o 15% superior en las métricas exigidas de la comparación guardada. Se reutilizan sin duplicados; conserva las demás bases. El asterisco indica la meta propia del lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1535_constructive_optimized.java`: puesto de tiempo 2/18 y de memoria 1/18 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1535_constructive_optimized.java](1535_constructive_optimized.java) \* | Java 1.8 | constructive | O(N) | AC | 0.109 s | 504 KB | 11325038 |
| [1535_constructive_optimized.py](1535_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N log N) output time; O(B log N) temporary space | AC | 0.078 s | 840 KB | 11326668 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
