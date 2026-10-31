# 1711. Nombres en clave

[Timus 1711](https://acm.timus.ru/problem.aspx?space=1&num=1711) · dificultad 135 · greedy

Problema original de Alex Samsonov, preparado por Igor Chevdar, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los n problemas tiene tres nombres en clave candidatos, y
los problemas de un conjunto van en orden alfabético de sus nombres.
Hay que elegir un nombre por problema para que los problemas queden en
un orden dado, o informar de que no se puede.

## Entrada

n (1 ≤ n ≤ 16), luego n líneas con los tres nombres de cada problema:
letras latinas minúsculas, a lo sumo 20 por nombre, todos distintos. La
última línea es el orden pedido, una permutación de 1 … n.

## Salida

Los nombres elegidos en el orden pedido, uno por línea, o IMPOSSIBLE.
Se acepta cualquier elección válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
11
cipher grille kamkohob
names codenames codes
newtests rejudge timus
size volume summit
watchmen braineater twosides
solution random yesorno
keywords subversion commands
bosses shooting shaitan
game strategy playgame
mnemonic palindromes bestname
eligibility rectangle rules
2 1 7 10 9 6 11 3 8 4 5
```

Salida:

```
codenames
grille
keywords
mnemonic
playgame
random
rectangle
rejudge
shaitan
volume
watchmen
```

### Ejemplo 2

Entrada:

```
3
problems in the
first sample are
ordered not randomly
1 2 3
```

Salida:

```
IMPOSSIBLE
```

## Solución

Se recorre el orden pedido y a cada problema se le da el menor de sus
nombres que va después del nombre elegido anterior. Si no hay ninguno,
la respuesta es IMPOSSIBLE.

Esta elección voraz es segura. Supongamos que existe una elección
válida y comparémosla con la voraz problema a problema. Por inducción,
el nombre voraz nunca va después del válido: el nombre válido del
siguiente problema va después del válido anterior, y por tanto también
después del voraz anterior. Así que es un candidato, y la elección
voraz no es mayor que él. Por eso el recorrido voraz nunca se atasca.
`O(n)` comparaciones de cadenas cortas.

Trampas:

- los nombres se comparan como cadenas, así que un prefijo va antes:
  «code» antes de «codenames»;
- la línea del orden da los números de problema según su lugar en el
  conjunto, no el lugar de cada problema;
- se acepta cualquier respuesta válida, así que las pruebas usan un
  comprobador.

El comprobador verifica que cada nombre pertenezca a su problema y que
los nombres crezcan. Las respuestas coinciden con una implementación
aceptada independiente en 600 conjuntos aleatorios.

## Soluciones optimizadas

La solución optimizada en C++ lee con `scanf` en un arreglo fijo de
16 × 3 nombres de 21 bytes cada uno, suficiente para n ≤ 16 y 20 letras
más el cero final, en lugar de un vector de vectores de `std::string`
leídos con `iostream`. En lugar de ordenar los tres nombres de cada
problema, los recorre con `strcmp` buscando el menor que va después de
la elección anterior, guarda solo punteros a los nombres elegidos y los
imprime con `puts`: {1711_greedy_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1711_greedy_optimized.cpp`: reducción de tiempo +51.61%; reducción de
  memoria +74.75%; base: `1711_greedy.cpp`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1711_greedy.go](1711_greedy.go).
- [1711_greedy.java](1711_greedy.java).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1711_greedy.cpp](1711_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.031 s | 396 KB | 11304067 |
| [1711_greedy.go](1711_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.062 s | 1148 KB | 11289207 |
| [1711_greedy.java](1711_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 516 KB | 11289209 |
| [1711_greedy.py](1711_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.093 s | 492 KB | 11304068 |
| [1711_greedy.rs](1711_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 236 KB | 11289213 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1711_greedy_optimized.cpp](1711_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 100 KB | 11304441 |
