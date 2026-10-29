# 2023. Pasos entre tres destinos

[Timus 2023](https://acm.timus.ru/problem.aspx?space=1&num=2023) · dificultad 40 · implementation

Problema original de Alex Samsonov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres destinos ocupan las posiciones consecutivas 0, 1 y 2 de una línea.
Cada etiqueta pertenece a un único destino según esta tabla completa:

| Posición | Etiquetas |
| --- | --- |
| 0 | Alice, Ariel, Aurora, Phil, Peter, Olaf, Phoebus, Ralph, Robin |
| 1 | Bambi, Belle, Bolt, Mulan, Mowgli, Mickey, Silver, Simba, Stitch |
| 2 | Dumbo, Genie, Jiminy, Kuzko, Kida, Kenai, Tarzan, Tiana, Winnie |

Procesa `n` etiquetas en el orden dado, empezando en la posición 0. Ir a
una posición adyacente cuesta un paso; procesar una etiqueta en su
destino no cuesta pasos. Calcula el total. El recorrido termina en el
último destino, sin obligación de volver a la posición 0. Las etiquetas
pueden repetirse. Límites: `1 ≤ n ≤ 1000`, 1 segundo, 64 MB.

## Entrada

La primera línea contiene `n`. Cada una de las siguientes `n` líneas
contiene una etiqueta de la tabla con la grafía y las mayúsculas
indicadas. Su orden es el de procesamiento. Las etiquetas solo tienen
letras y su longitud no supera siete.

## Salida

Un entero: el número total de pasos, entre 0 y `2n`, ambos incluidos.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
4
Aurora
Tiana
Ariel
Mulan
```

```
5
```

## Solución

Se busca la posición de cada etiqueta en la tabla y se camina hasta
ella: ir de la posición p a la q cuesta |p − q| pasos. Se suman estas
distancias, empezando en la posición 0. `O(n)`.

En el ejemplo las posiciones son 0 → 0 → 2 → 0 → 1, y los pasos
0 + 2 + 2 + 1 = 5.

Detalles a tener en cuenta:

- el recorrido empieza en la posición 0, antes de la primera etiqueta;
- después de la última etiqueta no hay que volver.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Java) leen la entrada byte a byte y no
guardan nombres. La única mayúscula de una etiqueta es la primera, y las
primeras letras distinguen las posiciones: A, P, O y R indican la
posición 0, B, M y S la posición 1, todas las demás la posición 2. Las
cifras de `n` no contienen mayúsculas, así que cada mayúscula de la
entrada empieza la etiqueta siguiente. C++: 100 KB en lugar de 400 KB,
con el mismo tiempo; Java: 0.078 s en lugar de 0.140 s y 344 KB en lugar
de 1964 KB.

La solución optimizada en Rust recorre la entrada byte a byte buscando
mayúsculas, como las de C++ y Java, en lugar de leer los nombres y
buscarlos en una tabla: 232 KB en lugar de 424 KB, con el mismo tiempo.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2023_implementation.cpp](2023_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 400 KB | 11303356 |
| [2023_implementation.go](2023_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1156 KB | 11303357 |
| [2023_implementation.java](2023_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1964 KB | 11303358 |
| [2023_implementation.py](2023_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 400 KB | 11303359 |
| [2023_implementation.rs](2023_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 424 KB | 11303360 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2023_implementation_optimized.cpp](2023_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 100 KB | 11303660 |
| [2023_implementation_optimized.java](2023_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.078 s | 344 KB | 11303663 |
| [2023_implementation_optimized.rs](2023_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 232 KB | 11303793 |
