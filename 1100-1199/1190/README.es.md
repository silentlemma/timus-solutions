# 1190. ¿Puede ser honesta una etiqueta de chocolate con algunos porcentajes?

[Timus 1190](https://acm.timus.ru/problem.aspx?space=1&num=1190) · dificultad 339 · greedy

Problema original de Leonid Volkov, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una etiqueta enumera `N ≤ 5000` ingredientes en orden no creciente de su
proporción; algunas proporciones están impresas, en centésimas de punto
porcentual. Cada proporción real es un entero de 1 a 10000 centésimas, y
todas suman exactamente 100%. Hay que decidir si existen proporciones
reales que respeten el orden y todos los valores impresos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego, para cada ingrediente, su nombre, `0`, o `1` y su proporción.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
Water 0
Cocoa-butter 0
Cocoa-powder 1 4000
Lecithin 0
```

Salida:

```
NO
```

## Solución

Como las proporciones nunca crecen al bajar por la lista, un ingrediente
sin valor impreso vale al menos el siguiente valor impreso por debajo (o
1 si no lo hay) y como mucho el último valor impreso por encima (o
10000). Los valores impresos son fijos. Tomar cada proporción en su
mínimo da una lista no creciente válida con la menor suma, y en su máximo
la de mayor suma.

Toda suma intermedia también se alcanza: partiendo de la lista mínima, se
sube la primera proporción de uno en uno hasta su máximo, luego la
segunda, y así sucesivamente; la lista sigue siendo no creciente todo el
tiempo y la suma crece de uno en uno. Así que la respuesta es `YES`
exactamente cuando la suma mínima es como mucho 10000 y la máxima al
menos 10000. `O(N)`.

Detalles a tener en cuenta:

- una proporción desconocida vale al menos 1, lo que puede llevar la suma
  mínima por encima del 100%;
- sin valores impresos por encima, una proporción desconocida puede llegar
  al 100%, no solo hasta el primer valor impreso;
- una etiqueta sin ningún valor impreso siempre es honesta, pues
  `N ≤ 5000` proporciones de al menos 1 caben en 10000.

Las respuestas se compararon con una solución escrita aparte en 300
etiquetas aleatorias y en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes hacen dos pasadas, una desde cada extremo, guardando
  el valor impreso más cercano.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1190_greedy.cpp](1190_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.031 s | 432 KB |
| [1190_greedy.go](1190_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 1336 KB |
| [1190_greedy.java](1190_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.171 s | 6296 KB |
| [1190_greedy.py](1190_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.062 s | 1372 KB |
| [1190_greedy.rs](1190_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.015 s | 448 KB |
