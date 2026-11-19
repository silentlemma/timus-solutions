# 1370. Mago

[Timus 1370](https://acm.timus.ru/problem.aspx?space=1&num=1370) · dificultad 89 · implementation

Problema original de Stanislav Vasiliev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una rueda lleva N cifras en el borde, 11 ≤ N ≤ 1000, y una ventanilla
muestra 10 seguidas, al principio de la 1.ª a la 10.ª. Cada chasquido
gira la rueda una cifra, así que tras un chasquido la ventanilla muestra
de la 2.ª a la 11.ª. Dados M chasquidos (1 ≤ M ≤ 32 767), hay que imprimir las
10 cifras de la ventanilla.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego las N cifras, una por línea.

## Salida

Las 10 cifras de la ventanilla, con sus ceros a la izquierda.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
12 7
1
2
3
4
5
6
7
8
9
0
7
7
```

Salida:

```
8907712345
```

## Solución

Tras M chasquidos la ventanilla empieza en la cifra M (contando desde
0), y la rueda da la vuelta, así que la respuesta son las cifras
(M + i) mod N para i = 0 … 9. `O(1)` tras leer la entrada.

Detalles a tener en cuenta:

- M puede ser muchas veces mayor que N (prueba 05);
- la ventanilla puede pasar de la última cifra a la primera (ejemplo);
- la respuesta se imprime como cifras, con sus ceros a la izquierda
  (prueba 03).

## Soluciones optimizadas

La solución optimizada en Java analiza los números a mano en lugar de
`Scanner`, guarda las cifras como bytes y escribe las diez cifras de la
ventana como un solo arreglo de bytes: 0.093 s en lugar de 0.125 s y
340 KB en lugar de 1892 KB.

La solución optimizada en C++ lee las cifras como caracteres en un
arreglo fijo e imprime diez de ellas con `putchar`, sin convertirlas en
números y sin `std::string`: 120 KB en lugar de 196 KB, con el mismo
tiempo.

`1370_implementation_optimized.py`. Reduce el giro a start=M mod N. Al leer el dígito i lo guarda solo si offset=(i-start) mod N es menor que diez, en esa posición de salida. Con N>=11 los diez índices son distintos y se rellenan una vez. Mantiene vueltas y ceros iniciales sin guardar la rueda. Tiempo O(N) y diez bytes de salida. Usa un bytearray de diez posiciones y el analizador por bloques de 65536 bytes. Conserva almacenamiento de bloque y tokens, pero no una lista de N dígitos; solo decodifica los diez bytes de respuesta. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1370_implementation.py`: tiempo 0.062 s → 0.14 s; memoria 404 KB → 244 KB.

`1370_implementation_optimized.rs`. Reduce el giro a start=M mod N. Al leer el dígito i lo guarda solo si offset=(i-start) mod N es menor que diez, en esa posición de salida. Con N>=11 los diez índices son distintos y se rellenan una vez. Mantiene vueltas y ceros iniciales sin guardar la rueda. Tiempo O(N) y diez bytes de salida. Usa un arreglo fijo de diez bytes y estado numérico O(1); emite dígitos ASCII sin String de salida. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1370_implementation.rs`: tiempo 0.015 s → 0.015 s; memoria 244 KB → 52 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1370_implementation_optimized.py`: puesto de tiempo 170/179 y de memoria 1/179 en esta muestra comparable.

`1370_implementation_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1370_implementation.cpp](1370_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11285595 |
| [1370_implementation.go](1370_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB | 11285596 |
| [1370_implementation.java](1370_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 1892 KB | 11285599 |
| [1370_implementation.py](1370_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 404 KB | 11285597 |
| [1370_implementation.rs](1370_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 244 KB | 11285600 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1370_implementation_optimized.cpp](1370_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 120 KB | 11303744 |
| [1370_implementation_optimized.java](1370_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 340 KB | 11303603 |
| [1370_implementation_optimized.py](1370_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N) | AC | 0.14 s | 244 KB | 11325069 |
| [1370_implementation_optimized.rs](1370_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 52 KB | 11324865 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
