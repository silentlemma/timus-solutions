# 1042. Cambiar cada válvula un número impar de veces

[Timus 1042](https://acm.timus.ru/problem.aspx?space=1&num=1042) · dificultad 810 · math

Problema original de Evgeny Shtykov, del V Campeonato por Equipos de Programación de la Universidad Estatal de los Urales, octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` válvulas, todas cerradas, y `N` técnicos (`1 ≤ N ≤ 250`). Cada
técnico es responsable de un conjunto no vacío de válvulas y, cuando se le
llama, cambia cada válvula del conjunto (abierta ↔ cerrada). Los conjuntos
son independientes: el conjunto de ningún técnico es la diferencia
simétrica de los conjuntos de otros técnicos. Elige técnicos de modo que
al final todas las válvulas queden abiertas. Imprime los números en orden
creciente, la lista más corta si hay varias, o `No solution`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas: la línea `i` enumera las válvulas del técnico `i`
y termina con `-1`.

## Salida

Los números de los técnicos elegidos en orden creciente, o `No solution`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 2 -1
2 3 4 -1
2 -1
4 -1
```

Salida:

```
1 2 3
```

### Ejemplo 2

Entrada:

```
3
2 3 -1
1 2 -1
3 -1
```

Salida:

```
2 3
```

## Solución

Llamar dos veces a un técnico no cambia nada, así que cada técnico se
llama una vez o ninguna: una incógnita `x_t` en GF(2). La válvula `v`
queda abierta cuando se cambia un número impar de veces:

```text
suma de x_t sobre los técnicos t con v en su conjunto = 1 (mod 2), para cada v
```

Son `N` ecuaciones lineales con `N` incógnitas sobre GF(2). La
independencia de los conjuntos significa que la matriz es invertible: el
sistema tiene exactamente una solución. Así que es la única y también la
más corta, y `No solution` nunca ocurre con una entrada válida (las
soluciones lo comprueban de todos modos).

Se resuelve por eliminación de Gauss–Jordan con las filas como conjuntos
de bits: para cada columna se busca una fila con un 1, se sube y se suma
(XOR) a todas las demás filas con un 1 en esa columna. Con palabras de 64
bits, una operación de fila son unos 4 XOR, así que toda la eliminación es
`O(N^3 / 64)`.

Detalles a tener en cuenta:

- todas las válvulas empiezan cerradas, así que el lado derecho son todo
  unos;
- la ecuación de una válvula reúne a los técnicos que la tienen: la matriz
  es la traspuesta de las listas de la entrada;
- la lista de un técnico termina con `-1`, no con el final de la línea.

## Notas por lenguaje

- **C++**: `std::bitset`; **Go**, **Java**, **Rust**: arreglos de palabras
  de 64 bits.
- **Python**: cada ecuación es un único entero usado como máscara de bits,
  así que una operación de fila es un solo `^`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1042_math.cpp](1042_math.cpp) | G++ 13.2 x64 | math | O(N^3 / 64) | AC | 0.046 s | 204 KB |
| [1042_math.go](1042_math.go) | Go 1.14 x64 | math | O(N^3 / 64) | AC | 0.046 s | 2156 KB |
| [1042_math.java](1042_math.java) | Java 1.8 | math | O(N^3 / 64) | AC | 0.125 s | 516 KB |
| [1042_math.py](1042_math.py) | Python 3.12 x64 | math | O(N^3 / 64) | AC | 0.109 s | 5716 KB |
| [1042_math.rs](1042_math.rs) | Rust 1.75 x64 | math | O(N^3 / 64) | AC | 0.046 s | 764 KB |
