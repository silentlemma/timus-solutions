# 1685. Ortografía

[Timus 1685](https://acm.timus.ru/problem.aspx?space=1&num=1685) · dificultad 184 · strings

Problema original de Eugene Krokhalev, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto se cifra escribiendo su carácter central (el número
(1 + n) div 2 de n), luego cifrando la parte a su izquierda y después
la parte a su derecha. Dada la línea cifrada, recuperar el texto.

## Entrada

Una línea de a lo sumo 20000 caracteres: letras latinas, espacios y
signos de puntuación.

## Salida

El texto original.

## Ejemplos

### Ejemplo 1

Entrada:

```
kyaVs alisse uop.
```

Salida:

```
Vasya likes soup.
```

### Ejemplo 2

Entrada:

```
gtorhoprahy
```

Salida:

```
orthography
```

## Solución

El cifrado recorre las posiciones del texto en un orden fijo: el centro
de un rango, luego el rango izquierdo, luego el derecho. Ese orden solo
depende de n, así que se reproduce y se coloca el i-ésimo carácter
cifrado en la i-ésima posición visitada. Con rangos lo..hi numerados
desde 0, el centro es (lo + hi) div 2. Una pila explícita sustituye la
recursión, aunque su profundidad es solo de unos log n. `O(n)`.

Trampas:

- la línea puede empezar o acabar con espacios, que son caracteres del
  texto: solo se quita el salto de línea;
- el texto puede contener varios espacios seguidos (test 05).

Las respuestas coinciden con una implementación aceptada independiente
y devuelven la salida del cifrador a textos aleatorios.

## Soluciones optimizadas

La solución optimizada en C++ lee la línea con `fgets` en un búfer
estático de 20003 bytes, suficiente para 20000 caracteres, un retorno de
carro, un salto de línea y el cero final, y llena un arreglo estático de
salida de 20000 bytes que imprime con `fwrite`, en lugar de
`std::string` e `iostream`. Reproduce el orden con recursión simple
sobre intervalos semiabiertos en lugar de un vector de pares, ya que la
profundidad es como mucho unos 15 niveles para 20000 caracteres:
{1685_strings_optimized.cpp}.

La solución optimizada en Java reproduce el orden con recursión simple
sobre intervalos semiabiertos, de como mucho unos 15 niveles para
20000 caracteres, en lugar de un `ArrayDeque` que reserva dos rangos
`int[]` por cada carácter: {1685_strings_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1685_strings_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +71.13%; base: `1685_strings.cpp`.

- `1685_strings_optimized.java`: reducción de tiempo +14.68%; reducción
  de memoria +60.05%; base: `1685_strings.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1685_strings.go](1685_strings.go).
- [1685_strings.rs](1685_strings.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1685_strings.cpp](1685_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 388 KB | 11288861 |
| [1685_strings.go](1685_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1228 KB | 11288862 |
| [1685_strings.java](1685_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1672 KB | 11288864 |
| [1685_strings.py](1685_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 536 KB | 11288863 |
| [1685_strings.rs](1685_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.062 s | 248 KB | 11288865 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1685_strings_optimized.cpp](1685_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 112 KB | 11307312 |
| [1685_strings_optimized.java](1685_strings_optimized.java) \* | Java 1.8 | strings | O(n) | AC | 0.093 s | 668 KB | 11307316 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
