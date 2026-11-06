# 1651. Subcadena más corta

[Timus 1651](https://acm.timus.ru/problem.aspx?space=1&num=1651) · dificultad 346 · dp

Problema original de Vladimir Yakovlev (idea de Magaz Asanov), del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un camino p en un grafo dirigido se da por su lista de n vértices. Hay que
hallar un camino q con los mismos vértices primero y último cuyas
aristas sean aristas de p tomadas en el mismo orden, con el menor número
de aristas posible.

## Entrada

n (2 ≤ n ≤ 100000) y luego n números de vértice de 1 a 10000; dos números
vecinos nunca coinciden.

## Salida

Los vértices de q separados por espacios; q puede ser un solo vértice.

## Ejemplos

### Ejemplo 1

Entrada:

```
9
1 2 7 3 2
8 4 8 5
```

Salida:

```
1 2 8 5
```

## Solución

La posición i de la lista significa «en el vértice pᵢ, con las aristas de
p desde la i-ésima disponibles». Desde ahí q puede tomar cualquier arista
posterior que salga de pᵢ, es decir, una arista (pⱼ, pⱼ₊₁) con j ≥ i y
pⱼ = pᵢ, y seguir desde la posición j + 1. Llegar al último vértice en
cualquier sitio termina q, pues seguir solo añadiría aristas.

Así, dp[i] = 0 si pᵢ es el último vértice y, si no,
dp[i] = 1 + min dp[j + 1] sobre j ≥ i con pⱼ = pᵢ. Recorriendo de
derecha a izquierda, una tabla indexada por vértice guarda ese mínimo del
sufijo, así que cada posición cuesta O(1); recordar la j elegida
reconstruye q desde la posición 0. Si el primer y el último vértice
coinciden, q es ese único vértice. `O(n)`.

Entre caminos igual de cortos el programa conserva el salto más tardío de
cada vértice. Así las cinco soluciones dan el mismo resultado, pero cualquier
camino óptimo es válido. El comprobador verifica los extremos, el orden de
las aristas y la longitud mínima, calculada de forma independiente al
recorrer las aristas de izquierda a derecha.

Detalles a tener en cuenta:

- un camino cerrado se reduce a su único vértice (prueba 03);
- deben aceptarse distintas listas óptimas de vértices (prueba gen3);
- q solo puede pasar por el último vértice al final, así que parar en la
  primera llegada es correcto;
- el destino del salto es la posición tras la arista elegida, j + 1, no j.

La solución en Python y el comprobador se verificaron por enumeración
exhaustiva de subconjuntos de aristas en 2000 caminos pequeños aleatorios
y 1155 casos exhaustivos.

## Soluciones optimizadas

Las versiones en C++ y Go aplican la misma recurrencia por sufijos con una variable para la distancia en la posición siguiente. Para cada posición solo se guarda el salto elegido. Los vértices y las distancias caben en 16 bits: si un recorrido mínimo visitara dos veces un vértice, se podría omitir el tramo entre ambas visitas y las aristas restantes conservarían el orden de entrada. Si coinciden los extremos, no hace falta la tabla de saltos. El tiempo sigue siendo O(n).

Las implementaciones base aceptadas [1651_dp.java](1651_dp.java), [1651_dp.py](1651_dp.py), [1651_dp.rs](1651_dp.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1651_dp.cpp](1651_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.062 s | 1448 KB | 11288521 |
| [1651_dp.go](1651_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.078 s | 4176 KB | 11288522 |
| [1651_dp.java](1651_dp.java) | Java 1.8 | dp | O(n) | AC | 0.125 s | 2188 KB | 11288524 |
| [1651_dp.py](1651_dp.py) \* | Python 3.12 x64 | dp | O(n) | AC | 0.156 s | 16708 KB | 11288523 |
| [1651_dp.rs](1651_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.031 s | 3840 KB | 11288525 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1651_dp_optimized.cpp](1651_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 732 KB | 11310342 |
| [1651_dp_optimized.go](1651_dp_optimized.go) \* | Go 1.14 x64 | dp | O(n) | AC | 0.015 s | 2072 KB | 11310392 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
