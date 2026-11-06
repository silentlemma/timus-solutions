# 1692. Banderas para las provincias

[Timus 1692](https://acm.timus.ru/problem.aspx?space=1&num=1692) · dificultad 380 · constructive

Problema original de Igor Chevdar, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Diseñar tantas banderas como sea posible con n colores de modo que
cada dos banderas compartan un color, pero ningún color aparezca en
tres o más banderas.

## Entrada

n (3 ≤ n ≤ 1000).

## Salida

El número de banderas k y luego cada bandera como su número de colores
seguido de los colores. Se acepta cualquier diseño válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
3
2 1 2
2 1 3
2 2 3
```

## Solución

Cada uno de los k(k − 1)/2 pares de banderas necesita un color común.
Un color que está en a lo sumo dos banderas es común a un par como
mucho, así que pares distintos usan colores distintos y
k(k − 1)/2 ≤ n.

La cota se alcanza: se numeran los pares de banderas y se da a cada par
un color propio, puesto solo en esas dos banderas. Cada bandera lleva
entonces k − 1 colores, dos banderas cualesquiera comparten el color de
su par y ningún color está en más de dos banderas. Se toma el mayor k
con k(k − 1)/2 ≤ n; los colores sobrantes no se usan. `O(n)` de salida.

Trampas:

- no hace falta usar los colores sobrantes (test 04);
- el diseño del ejemplo es uno de muchos, así que un verificador
  valida las banderas en vez de comparar texto.

El verificador comprueba la cantidad, los rangos, los colores comunes
de cada par y la regla de a lo sumo dos; las respuestas de una
implementación aceptada independiente lo pasan para todo n hasta 300.

## Soluciones optimizadas

Go y Rust generan cada bandera directamente con los índices de las demás. Para a < b con índices desde cero entre k banderas, el color es a(2k−a−1)/2 + b−a. El primer término cuenta los pares anteriores y el segundo sitúa el actual. Así, cada color aparece exactamente en sus dos banderas sin guardar una matriz de colores por pareja. Ambas versiones usan búferes fijos de bytes para entrada y salida, sin Scanner ni conversiones de cadenas.

Las implementaciones base aceptadas [1692_constructive.cpp](1692_constructive.cpp), [1692_constructive.java](1692_constructive.java), [1692_constructive.py](1692_constructive.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1692_constructive.cpp](1692_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 232 KB | 11288948 |
| [1692_constructive.go](1692_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.046 s | 1152 KB | 11288949 |
| [1692_constructive.java](1692_constructive.java) \* | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1796 KB | 11288952 |
| [1692_constructive.py](1692_constructive.py) \* | Python 3.12 x64 | constructive | O(n) | AC | 0.078 s | 464 KB | 11288950 |
| [1692_constructive.rs](1692_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 264 KB | 11288953 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1692_constructive_optimized.go](1692_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 780 KB | 11311145 |
| [1692_constructive_optimized.rs](1692_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 180 KB | 11311155 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
