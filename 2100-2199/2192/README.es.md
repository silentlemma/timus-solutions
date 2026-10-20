# 2192. Una ruta por el bosque donde cada sendero paga más por las setas

[Timus 2192](https://acm.timus.ru/problem.aspx?space=1&num=2192) · dificultad 927 · graphs

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un bosque tiene N claros y M senderos de un solo sentido sin ciclos; el
sendero i tiene sᵢ setas y wᵢ bayas. El día j una seta se vende a aⱼ y
una baya a bⱼ. Para cada uno de los Q días, decir si alguna ruta del
claro 1 al claro N cumple aⱼ sᵢ > bⱼ wᵢ en cada sendero que recorre. Los
límites son 2 segundos y 256 MB.

## Entrada

N, M y Q, 2 ≤ N ≤ 10⁵, 1 ≤ M, Q ≤ 10⁵. Luego M líneas uᵢ vᵢ sᵢ wᵢ con
números de claro hasta 10⁵ y 1 ≤ sᵢ, wᵢ ≤ 10⁹, y Q líneas aⱼ bⱼ,
1 ≤ aⱼ, bⱼ ≤ 10⁹. Ningún par de claros está unido por dos senderos.

## Salida

YES o NO para cada día.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 3
1 2 2 4
2 3 3 9
1 3 10 50
58 9
60 23
61 9
```

Salida:

```
YES
NO
YES
```

## Solución

La condición en un sendero es sᵢ / wᵢ > bⱼ / aⱼ, así que una ruta sirve
un día exactamente cuando su menor cociente sᵢ / wᵢ supera bⱼ / aⱼ. Los
días solo necesitan un número del bosque: el mayor valor posible del
menor cociente entre todas las rutas de 1 a N.

Como los senderos no forman ciclos, este valor de cuello de botella es
una programación dinámica en un orden topológico hallado con el
algoritmo de Kahn: best(1) es infinito, y un sendero u → v ofrece a v el
valor min(best(u), s / w), del que v se queda con el mayor. Los cocientes
se guardan como numerador y denominador y se comparan multiplicando en
cruz, lo que no pasa de 10¹⁸; el infinito es 1 / 0. Los números de claro
pueden superar N, así que los arreglos se dimensionan por L, el máximo
de N y todos los números.

Un día es YES cuando N es alcanzable y aⱼ · s > bⱼ · w para el mejor
cociente s / w, y la desigualdad estricta hace que un empate sea NO.

En el ejemplo el sendero directo tiene cociente 1 / 5 y la ruta por 2
tiene min(1 / 2, 1 / 3) = 1 / 3, así que el cuello de botella es 1 / 3.
Los días comparan con él 9 / 58, 23 / 60 y 9 / 61, y solo 23 / 60 es
demasiado grande.

El orden y las consultas cuestan O(L + M + Q).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2192_graphs.cpp](2192_graphs.cpp) | G++ 13.2 x64 | graphs | O(L + M + Q) | AC | 0.453 s | 10692 KB |
| [2192_graphs.go](2192_graphs.go) | Go 1.14 x64 | graphs | O(L + M + Q) | AC | 0.125 s | 15996 KB |
| [2192_graphs.java](2192_graphs.java) | Java 1.8 | graphs | O(L + M + Q) | AC | 0.140 s | 10520 KB |
| [2192_graphs.py](2192_graphs.py) | Python 3.12 x64 | graphs | O(L + M + Q) | AC | 0.500 s | 77964 KB |
| [2192_graphs.rs](2192_graphs.rs) | Rust 1.75 x64 | graphs | O(L + M + Q) | AC | 0.078 s | 28904 KB |
