# 1220. Mil pilas en tres cuartos de megabyte

[Timus 1220](https://acm.timus.ru/problem.aspx?space=1&num=1220) · dificultad 279 · implementation

Problema original de Pavel Atnashev, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que ejecutar hasta `10⁵` operaciones sobre 1000 pilas: `PUSH A B`
pone el número `B ≤ 10⁹` en la pila `A`, y `POP A` quita la cima de la
pila `A` y la imprime. Cada `POP` encuentra su pila no vacía. El límite
de memoria es de solo 0,75 MB.

Límite de tiempo: 0.5 segundos. Límite de memoria: 0.75 MB.

## Entrada

`N` y luego las operaciones, una por línea.

## Salida

El valor de cada `POP`, uno por línea, en orden.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
PUSH 1 100
PUSH 1 200
PUSH 2 300
PUSH 2 400
POP 2
POP 1
POP 2
```

Salida:

```
400
200
300
```

## Solución

Guardar cada valor con un puntero al que tiene debajo ocuparía unos
600 KB para `10⁵` valores, demasiado cerca del límite contando el propio
programa, y un arreglo aparte por pila desperdiciaría espacio en las
vacías.

Así que cada pila es una cadena de bloques de 10 valores, el bloque más
nuevo primero, y cada bloque recuerda el siguiente bloque más antiguo de
la misma pila. El tamaño de la pila dice cuán lleno está su bloque más
nuevo, así que no hace falta un contador por bloque: apilar en un bloque
lleno (o en una pila vacía) toma un bloque de una lista libre, y
desapilar hasta vaciar el bloque más nuevo lo devuelve. Solo el bloque
más nuevo de cada pila puede estar a medias, así que nunca hay más de
`10⁵/10 + 1000` bloques en uso, unos 460 KB en total. Unos búferes fijos
pequeños para leer y escribir hacen rápidas la entrada y la salida sin
gastar mucha memoria. `O(N)`.

Detalles a tener en cuenta:

- la biblioteca de flujos de C++ ya cuesta bastante memoria por sí sola,
  así que el programa lee y escribe con `fread` y `fwrite`;
- un bloque debe devolverse en cuanto se vacía, o una pila que crece y
  mengua una y otra vez agotaría la reserva;
- bastan números de bloque de 16 bits, porque hay menos de 32.768
  bloques.

La salida se comparó con una simulación sencilla con listas en todas las
pruebas, incluidas 100.000 operaciones de varios tipos.

## Notas por lenguaje

- Timus solo acepta este problema en C, C++ y Pascal, así que solo se da
  la solución en C++.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1220_implementation.cpp](1220_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 540 KB |
