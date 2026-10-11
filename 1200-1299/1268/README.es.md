# 1268. El pequeño Chu

[Timus 1268](https://acm.timus.ru/problem.aspx?space=1&num=1268) · dificultad 728 · number_theory

Problema original de Pavel Atnashev, del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El pequeño Chu despierta K, K², K³, … días después de nacer y nunca
debe ver dos veces el mismo día de la semana; una semana tiene N días,
N primo (2 < N < 65 536), y K es como mucho una semana. Para cada uno de
T ≤ 6553 valores de N, hay que imprimir el K que da más despertares; el
ejemplo muestra que se espera el mayor de esos K.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

T, luego T primos N.

## Salida

K para cada N, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
5
7
11
```

Salida:

```
2
3
5
8
```

## Solución

El día de la semana del i-ésimo despertar es K^i mod N. Estos valores
se repiten con el orden multiplicativo de K módulo N, así que el máximo
de despertares, N − 1, lo da una raíz primitiva. La respuesta es la
mayor raíz primitiva módulo N.

Un número g es raíz primitiva justo cuando g^((N−1)/q) ≠ 1 mod N para
cada primo q que divide N − 1. Se factoriza N − 1 con una criba de
menores factores primos hasta 65 536 y se prueban g = N − 1, N − 2, …
hasta que uno pase. Las raíces primitivas son una buena parte de los
residuos, así que se prueban pocos candidatos, cada uno con unas pocas
potencias rápidas. Los N repetidos se responden desde una tabla. Más o
menos `O(L log log L + T · k log N)` para el límite L de la criba y k
candidatos.

Detalles a tener en cuenta:

- cualquier raíz primitiva mantiene distintos los días, pero se espera
  la mayor (en el ejemplo, 8 para N = 11 y no 2);
- el límite de tiempo es un cuarto de segundo para hasta 6553
  consultas, así que conviene factorizar N − 1 con la criba y no
  probando divisores cada vez (pruebas 04, 05);
- cuando N − 1 es potencia de dos, basta una sola potencia de prueba
  (prueba 06).

Las respuestas se compararon con listar las potencias de cada candidato
para cada primo menor que 3000.

## Notas por lenguaje

- Todos los lenguajes construyen la misma criba y guardan una tabla de
  respuestas por N.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1268_number_theory.cpp](1268_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 708 KB |
| [1268_number_theory.go](1268_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.031 s | 2440 KB |
| [1268_number_theory.java](1268_number_theory.java) | Java 1.8 | number_theory | O(L log log L + T · k log N) | AC | 0.093 s | 2884 KB |
| [1268_number_theory.py](1268_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.109 s | 4508 KB |
| [1268_number_theory.rs](1268_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L + T · k log N) | AC | 0.015 s | 1420 KB |
