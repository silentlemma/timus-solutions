# 1190. ¿Puede ser honesta una etiqueta de chocolate con algunos porcentajes?

[Timus 1190](https://acm.timus.ru/problem.aspx?space=1&num=1190) · dificultad 338 · greedy

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

`1 ≤ N ≤ 5000`. Los nombres son distintos, tienen de 1 a 16 caracteres y
solo contienen letras inglesas, guiones o guiones bajos. Las proporciones
impresas son enteros de 1 a 10000 y se garantiza que aparecen en orden no
creciente, incluso entre ingredientes con proporciones desconocidas.

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

La entrada garantiza que las proporciones impresas ya están en orden no
creciente; las dos pasadas siguientes dependen de esta condición.

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
  mínima por encima del 100% (prueba `06`);
- las proporciones impresas crecientes incumplen las restricciones de
  entrada y no son un contraejemplo al método de dos pasadas;
- sin valores impresos por encima, una proporción desconocida puede llegar
  al 100%, no solo hasta el primer valor impreso;
- una etiqueta sin ningún valor impreso siempre es honesta, pues
  `N ≤ 5000` proporciones de al menos 1 caben en 10000.

Las respuestas se compararon con un oráculo exacto de programación dinámica
en 2000 etiquetas aleatorias y las seis pruebas guardadas; también se
comprobaron los casos generados.

## Soluciones optimizadas

C++ y Go procesan cada tramo de proporciones desconocidas al leer la siguiente proporción publicada. Esta da su límite inferior y la anterior da el superior. El tramo final tiene límite inferior uno. Solo se conservan su longitud, la proporción anterior y dos límites de la suma total, con espacio auxiliar constante.

Las implementaciones base aceptadas [1190_greedy.java](1190_greedy.java), [1190_greedy.py](1190_greedy.py), [1190_greedy.rs](1190_greedy.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes hacen dos pasadas, una desde cada extremo, guardando
  el valor impreso más cercano.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1190_greedy.cpp](1190_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.031 s | 432 KB | 11283432 |
| [1190_greedy.go](1190_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 1336 KB | 11283435 |
| [1190_greedy.java](1190_greedy.java) \* | Java 1.8 | greedy | O(N) | AC | 0.171 s | 6296 KB | 11283438 |
| [1190_greedy.py](1190_greedy.py) \* | Python 3.12 x64 | greedy | O(N) | AC | 0.062 s | 1372 KB | 11283437 |
| [1190_greedy.rs](1190_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.015 s | 448 KB | 11283442 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1190_greedy_optimized.cpp](1190_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.015 s | 108 KB | 11310618 |
| [1190_greedy_optimized.go](1190_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 908 KB | 11310591 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
