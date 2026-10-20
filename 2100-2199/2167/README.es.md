# 2167. La menor clave XOR que convierte un número en primo

[Timus 2167](https://acm.timus.ru/problem.aspx?space=1&num=2167) · dificultad 493 · bitmask, number_theory

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada uno de los T números a menores que 2²⁰, hallar la menor clave
no negativa k tal que a XOR k sea primo. Los límites son 2 segundos y
256 MB.

## Entrada

T, 1 ≤ T ≤ 10⁵, y luego los números, 0 ≤ a ≤ 1 048 575.

## Salida

La menor clave de cada número.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
5
6
1
```

Salida:

```
0
1
2
```

## Solución

Para un a fijo, la clave k = a XOR p está en biyección con el primo p,
así que hay que hallar el primo p que minimiza a XOR p. Las claves
menores que 2²⁰ ya alcanzan todos los primos menores que 2²⁰, entre
ellos el 2, y un primo mayor necesitaría una clave de al menos 2²⁰, así
que solo importan los primos menores que 2²⁰.

El XOR es menor cuanto más bits altos de p coinciden con a. Se criban
los primos menores que 2²⁰ y se construye, para cada j, una tabla que
dice si algún primo empieza por un prefijo dado de j bits; cada tabla es
el OR de pares de entradas de la siguiente. Una consulta elige los bits
de p desde arriba: conserva el bit de a si algún primo tiene ese prefijo
más largo, y toma el otro bit si no. Son 20 pasos por número tras una
preparación de O(2²⁰).

En el ejemplo 5 es primo, 6 XOR 1 = 7 y 1 XOR 2 = 3.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2167_bitmask_number_theory.cpp](2167_bitmask_number_theory.cpp) | G++ 13.2 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.109 s | 2300 KB |
| [2167_bitmask_number_theory.go](2167_bitmask_number_theory.go) | Go 1.14 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.031 s | 3080 KB |
| [2167_bitmask_number_theory.java](2167_bitmask_number_theory.java) | Java 1.8 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.140 s | 4904 KB |
| [2167_bitmask_number_theory.py](2167_bitmask_number_theory.py) | Python 3.12 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.671 s | 16692 KB |
| [2167_bitmask_number_theory.rs](2167_bitmask_number_theory.rs) | Rust 1.75 x64 | bitmask, number_theory | O(2^20 + 20 T) | AC | 0.031 s | 4172 KB |
