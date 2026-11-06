# 1350. Comedor

[Timus 1350](https://acm.timus.ru/problem.aspx?space=1&num=1350) · dificultad 384 · implementation

Problema original de Pavel Egorov, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un menú tiene N ≤ 100 productos, y la comida del día se hace con M
distintos de ellos, sin saber cuáles. La comen K + 1 ≤ 101 estudiantes;
de cada uno se conocen los productos que le son peligrosos. El primer
estudiante comió y quedó bien. Para cada uno de los otros K hay que
imprimir `YES` si la comida es sin duda inofensiva para esa persona,
`NO` si sin duda contiene algo peligroso para ella, y `MAYBE` si puede
ser cualquiera de las dos cosas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y los N nombres de producto, luego K, luego K + 1 bloques: una
cantidad y otros tantos productos peligrosos, el primer bloque para el
primer estudiante. La entrada acaba con M.

## Salida

K líneas con `YES`, `NO` o `MAYBE`.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
Rafinad
Kefir
Pastila
Smetana
Chokolade
Kljukva
Imbir
3
3
Rafinad
Kefir
Imbir
1
Rafinad
3
Kefir
Kljukva
Smetana
2
Imbir
Smetana
3
```

Salida:

```
YES
NO
MAYBE
```

## Solución

Como el primer estudiante quedó bien, ninguno de sus productos
peligrosos está en la comida: la comida son M productos del resto, el
conjunto seguro S. Para otro estudiante con productos peligrosos D:

- si M = 0, o ningún producto de S está en D, toda comida posible es
  inofensiva: `YES`;
- si fuera de D hay menos de M productos de S, toda comida de M
  productos tiene que tomar alguno de D: `NO`;
- si no, una comida puede evitar D y otra incluirlo: `MAYBE`.

`O(N · K)` en promedio; C++: `O(N · K · log N)`.

Detalles a tener en cuenta:

- con M = 0 no se come nada y todos quedan bien (prueba 02);
- los nombres distinguen mayúsculas: `Milk` y `milk` son dos productos
  (prueba 04);
- los productos peligrosos fuera de S no importan, porque no pueden
  estar en la comida.

Las respuestas se compararon con probar todas las comidas posibles en
400 comedores aleatorios de hasta 6 productos.

## Soluciones optimizadas

Las versiones compactas asignan un índice a cada alimento del menú. C++ y Rust lo buscan en un vector ordenado, y Go en una tabla hash. Rust reutiliza el mismo búfer para cada palabra de la entrada. Un vector guarda el último estudiante que mencionó cada alimento para contar una sola vez los nombres repetidos. Tras excluir los alimentos peligrosos para el primer estudiante, se conserva solo el número de alimentos peligrosos elegibles para cada otro estudiante. Esos recuentos bastan cuando se lee el tamaño de la comida.

Las implementaciones base aceptadas [1350_implementation.java](1350_implementation.java), [1350_implementation.py](1350_implementation.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Las cinco soluciones cuentan los productos de S dentro y fuera de D.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1350_implementation.cpp](1350_implementation.cpp) | G++ 13.2 x64 | implementation | O(N·K·log N) | AC | 0.062 s | 1344 KB | 11285155 |
| [1350_implementation.go](1350_implementation.go) | Go 1.14 x64 | implementation | O(N·K) | AC | 0.031 s | 2156 KB | 11285156 |
| [1350_implementation.java](1350_implementation.java) \* | Java 1.8 | implementation | O(N·K) | AC | 0.140 s | 6524 KB | 11285160 |
| [1350_implementation.py](1350_implementation.py) \* | Python 3.12 x64 | implementation | O(N·K) | AC | 0.078 s | 2240 KB | 11285157 |
| [1350_implementation.rs](1350_implementation.rs) | Rust 1.75 x64 | implementation | O(N·K) | AC | 0.015 s | 1560 KB | 11285161 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1350_implementation_optimized.cpp](1350_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(N·K·log N) | AC | 0.015 s | 424 KB | 11310451 |
| [1350_implementation_optimized.go](1350_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(N·K) expected | AC | 0.031 s | 944 KB | 11310453 |
| [1350_implementation_optimized.rs](1350_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N·K·log N) | AC | 0.015 s | 192 KB | 11310869 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
