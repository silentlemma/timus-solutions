# 1352. Primos de Mersenne

[Timus 1352](https://acm.timus.ru/problem.aspx?space=1&num=1352) · dificultad 132 · number_theory

Problema original de Vladimir Yakovlev, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un primo de Mersenne es un primo de la forma 2^p − 1. Dadas T
consultas, cada una con un número N ≤ 38, hay que imprimir el exponente
p del N-ésimo primo de Mersenne en orden creciente.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

T, luego T líneas con N.

## Salida

T líneas con los exponentes.

## Ejemplos

### Ejemplo 1

Entrada:

```
13
18
32
24
21
19
34
27
33
20
30
28
29
22
```

Salida:

```
3217
756839
19937
9689
4253
1257787
44497
859433
4423
132049
86243
110503
9941
```

## Solución

Ningún programa puede hallar estos primos en un segundo: el exponente
38 es 6 972 593, y comprobar un solo número de ese tamaño exige muchísimo
cálculo. El orden de los primeros 38 primos de Mersenne se estableció
hace tiempo, así que las soluciones guardan la lista de sus exponentes
como una tabla constante y responden cada consulta con un acceso por
índice. `O(T)`.

Detalles a tener en cuenta:

- N cuenta desde 1: el primer primo de Mersenne es 2² − 1 = 3, con
  exponente 2 (prueba 03);
- todos los exponentes caben en enteros de 32 bits.

Las primeras 22 entradas se comprobaron con la prueba de Lucas–Lehmer
para todos los exponentes primos hasta 10 000; el resto viene de la
lista publicada y coincide con el ejemplo y con los valores que cita el
enunciado.

## Notas por lenguaje

- Python guarda la tabla como una sola cadena partida en palabras, así
  que las respuestas se imprimen sin volver a convertirlas en números.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1352_number_theory.cpp](1352_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T) | AC | 0.001 s | 128 KB |
| [1352_number_theory.go](1352_number_theory.go) | Go 1.14 x64 | number_theory | O(T) | AC | 0.031 s | 1084 KB |
| [1352_number_theory.java](1352_number_theory.java) | Java 1.8 | number_theory | O(T) | AC | 0.078 s | 444 KB |
| [1352_number_theory.py](1352_number_theory.py) | Python 3.12 x64 | number_theory | O(T) | AC | 0.062 s | 324 KB |
| [1352_number_theory.rs](1352_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T) | AC | 0.001 s | 216 KB |
