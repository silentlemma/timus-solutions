# 1362. Compañeros de clase 2

[Timus 1362](https://acm.timus.ru/problem.aspx?space=1&num=1362) · dificultad 442 · dp

Problema original de Evgeny Krokhalev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una agencia de N ≤ 100 000 empleados es un árbol: todos salvo el
director tienen exactamente un jefe. Tanya tiene una noticia, y quien
la conoce puede llamar a su jefe o a uno de sus subordinados directos;
una llamada dura un minuto, y cada persona hace una sola llamada a la
vez. Hay que imprimir el menor número de minutos hasta que toda la
agencia lo sepa. Es la versión en árbol de
[1323](../1323/README.es.md).

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas: la línea K enumera los subordinados del empleado K y
termina en 0. La última línea tiene el número de Tanya.

## Salida

El menor número de minutos.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
2 3 0
4 5 7 0
6 9 0
0
0
8 10 0
0
0
0
0
2
```

Salida:

```
5
```

## Solución

Las llamadas van hacia arriba y hacia abajo, así que el jefe es un
vecino más. Se enraíza el árbol en Tanya; entonces la noticia entra en
cada subárbol una sola vez, por su raíz.

Sea time(v) los minutos que v necesita para avisar a todo su subárbol
tras conocer la noticia. Si v llama a sus hijos en cierto orden, el
hijo i-ésimo se entera en el minuto i y termina en i + time(hijo). El
mejor orden llama primero al subárbol más lento: se ordenan los tiempos
de los hijos de mayor a menor t₁ ≥ t₂ ≥ …, y time(v) = max(tᵢ + i).
Intercambiar dos vecinos que no siguen este orden nunca empeora el resultado, lo que
lo demuestra.

El árbol se recorre en anchura y los tiempos se calculan desde las
hojas hacia arriba, así que ni una cadena de 100 000 necesita
recursión. `O(N log N)`.

Detalles a tener en cuenta:

- el director no siempre es la raíz: si Tanya es subordinada, la noticia sube y
  luego baja por otras ramas (pruebas 03 y 04);
- una cadena de 100 000 es demasiado profunda para la recursión en la
  mayoría de los lenguajes (prueba generada 2);
- una estrella de 100 000 necesita 99 999 minutos, una llamada cada vez
  (prueba generada 3).

Las respuestas se compararon con una búsqueda sobre todas las formas de
llamar, minuto a minuto, en 400 árboles aleatorios de hasta 8
empleados.

## Soluciones optimizadas

C++, Go y Rust conservan la llamada primero al subárbol más lento. Cada empleado guarda jefe original, primer hijo y siguiente hermano; enumeran vecinos no dirigidos sin contenedores por vértice ni objetos duplicados por arista. Un orden BFS plano y padres enraízan en el informador; su jefe original es otro vecino y el director puede ser distinto. Se procesa al revés, reuniendo tiempos de hijos en un prefijo reutilizado, ordenando de mayor a menor y tomando max(time[i]+i+1). Las hojas requieren cero. Identificadores y tiempos caben en 32 bits: un horario secuencial termina en N−1 minutos. Tiempo O(N log N), árbol O(N), sin recorrido recursivo. C++ y Go leen en flujo; Rust guarda la entrada y usa O(N+bytes de entrada). Se conservan las bases; Java y Python reutilizan las admitidas.

El envío aceptado en Rust 1.75 x64 tarda 0.046 s frente a 0.031 s de la base y usa 3 948 KB frente a 15320 KB.

Las implementaciones base aceptadas [1362_dp.java](1362_dp.java), [1362_dp.py](1362_dp.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Java guarda el árbol en arreglos planos y lee la entrada byte a byte;
  Go también la lee byte a byte.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1362_dp.cpp](1362_dp.cpp) | G++ 13.2 x64 | dp | O(N log N) | AC | 0.171 s | 8896 KB | 11285481 |
| [1362_dp.go](1362_dp.go) | Go 1.14 x64 | dp | O(N log N) | AC | 0.093 s | 17784 KB | 11285489 |
| [1362_dp.java](1362_dp.java) | Java 1.8 | dp | O(N log N) | AC | 0.093 s | 6848 KB | 11285508 |
| [1362_dp.py](1362_dp.py) \* | Python 3.12 x64 | dp | O(N log N) | AC | 0.468 s | 33988 KB | 11285503 |
| [1362_dp.rs](1362_dp.rs) | Rust 1.75 x64 | dp | O(N log N) | AC | 0.031 s | 15320 KB | 11285514 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1362_dp_optimized.cpp](1362_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N log N) | AC | 0.015 s | 2824 KB | 11315122 |
| [1362_dp_optimized.go](1362_dp_optimized.go) \* | Go 1.14 x64 | dp | O(N log N) | AC | 0.015 s | 4256 KB | 11315125 |
| [1362_dp_optimized.rs](1362_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(N log N) | AC | 0.046 s | 3948 KB | 11315130 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
