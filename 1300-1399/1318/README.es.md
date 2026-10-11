# 1318. Logaritmo

[Timus 1318](https://acm.timus.ru/problem.aspx?space=1&num=1318) · dificultad 1393 · bitmask

Problema original con idea de Nikita Shamgunov, preparado por Nikita Shamgunov y Anton Botov, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados N ≤ 5000 números A₀, …, A_{N−1} de 128 bits, hay que calcular la
suma de ⌊log₁₀(A_k xor A_j)⌋ sobre todos los pares ordenados k, j de 0
a N − 1, tomando el logaritmo de 0 como 0.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La primera línea tiene N. Cada una de las N líneas siguientes tiene
cuatro números de 0 a 2³² − 1, las palabras de 32 bits de A_k de la más
alta a la más baja: A_k = 2⁹⁶ · a₁ + 2⁶⁴ · a₂ + 2³² · a₃ + a₄.

## Salida

La suma.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0 0 2324
0 2332 0 0
```

Salida:

```
44
```

## Solución

⌊log₁₀ x⌋ es la cantidad de potencias 10¹, 10², … que no superan x. Una
potencia de diez con menos bits que x siempre es menor que x, y como
10 > 2, como mucho una potencia tiene exactamente tantos bits como x.
Así, una tabla indexada por la longitud en bits L da la cantidad de
potencias más cortas, y la única potencia de longitud L, si existe,
necesita una sola comparación. Cada par k < j cuesta un xor, una
longitud en bits y como mucho una comparación, y la suma sobre pares
ordenados es el doble de la suma sobre k < j, ya que la diagonal da 0.
`O(N²)`, unos 12.5 millones de pares.

Detalles a tener en cuenta:

- los pares son ordenados, así que el ejemplo cuenta 22 dos veces
  (prueba 01);
- un xor de exactamente 10³⁸ tiene logaritmo 38 y 10³⁸ − 1 tiene 37
  (prueba 06), y el mayor xor, 2¹²⁸ − 1, sigue dando 38 (prueba 05);
- las palabras se deben leer sin signo: 4 294 967 295 no cabe en un
  entero de 32 bits con signo;
- la suma no supera 5000 · 4999 · 38 ≈ 9.5 · 10⁸, que aún cabe en
  32 bits, pero un contador de 64 bits no cuesta nada.

## Notas por lenguaje

- C++ y Rust usan un entero nativo de 128 bits; Go y Java guardan cada
  número como dos mitades de 64 bits y las comparan sin signo.
- En Python los 12.5 millones de pares tardarían varios segundos, así
  que trabaja con los números ordenados. En un rango que comparte los
  bits por encima de cierto bit t, todos los pares que cruzan la
  división en t tienen un xor cuyo bit más alto es t, de modo que
  comparten las potencias más cortas. Cuando una potencia de diez tiene
  t como bit más alto, los pares que la alcanzan se cuentan bajando por
  ambas mitades bit a bit, como en un trie binario, y los grupos muy
  pequeños se comprueban par a par. Esto tarda unos 0.2 segundos, y los
  resultados se compararon con una suma directa sobre todos los pares
  en 800 conjuntos aleatorios pequeños.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1318_bitmask.cpp](1318_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(N^2) | AC | 0.062 s | 280 KB |
| [1318_bitmask.go](1318_bitmask.go) | Go 1.14 x64 | bitmask | O(N^2) | AC | 0.093 s | 1420 KB |
| [1318_bitmask.java](1318_bitmask.java) | Java 1.8 | bitmask | O(N^2) | AC | 0.328 s | 2368 KB |
| [1318_bitmask.py](1318_bitmask.py) | Python 3.12 x64 | bitmask | O(N log N) | AC | 0.093 s | 2268 KB |
| [1318_bitmask.rs](1318_bitmask.rs) | Rust 1.75 x64 | bitmask | O(N^2) | AC | 0.093 s | 588 KB |
