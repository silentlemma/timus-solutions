# 1685. Ortografía

[Timus 1685](https://acm.timus.ru/problem.aspx?space=1&num=1685) · dificultad 183 · strings

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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1685_strings.cpp](1685_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 388 KB |
| [1685_strings.go](1685_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1228 KB |
| [1685_strings.java](1685_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1672 KB |
| [1685_strings.py](1685_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 536 KB |
| [1685_strings.rs](1685_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.062 s | 248 KB |
