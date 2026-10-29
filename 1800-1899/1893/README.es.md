# 1893. A380

[Timus 1893](https://acm.timus.ru/problem.aspx?space=1&num=1893) · dificultad 60 · implementation

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Clasificar un asiento válido mediante su número de fila y su letra.
La distribución depende de la fila:

| Filas | Letras de asientos en orden | Pasillos entre |
| --- | --- | --- |
| 1–2 | A B C D | A/B y C/D |
| 3–20 | A B C D E F | B/C y D/E |
| 21–65 | A B C D E F G H J K | C/D y G/H |

El primer y el último asiento de cada fila están junto a una ventana.
Los asientos a ambos lados de un pasillo están junto a ese pasillo.
Escribir `window` si está junto a una ventana; en otro caso, `aisle`
si está junto a un pasillo, o `neither` para los demás asientos.
La clasificación de ventana tiene prioridad.

Los límites son 1 segundo y 64 MB.

## Entrada

Un identificador de asiento: el número de fila seguido inmediatamente
por su letra mayúscula, por ejemplo `3C`. La fila está entre 1 y 65
y la letra es válida para esa fila. Las filas de clase económica
omiten la letra I.

## Salida

Escribir una sola palabra: `window`, `aisle` o `neither`.

## Evaluación

Las salidas se comparan como secuencias de tokens.

## Ejemplos

### Ejemplo 1

Entrada:

```
3C
```

Salida:

```
aisle
```

### Ejemplo 2

Entrada:

```
64A
```

Salida:

```
window
```

### Ejemplo 3

Entrada:

```
21F
```

Salida:

```
neither
```

## Solución

La fila es el número antes del último carácter, y el asiento es la
última letra. El avión tiene tres disposiciones, y cada una fija qué
asientos dan a una ventana y cuáles a un pasillo:

| Filas | `window` | `aisle` | `neither` |
| --- | --- | --- | --- |
| 1–2 | A D | B C | ninguno |
| 3–20 | A F | B C D E | ninguno |
| 21–65 | A K | C D G H | B E F J |

En las filas 1–2 los asientos A y D tocan una ventana y un pasillo; la
ventana tiene prioridad, así que son `window`. `O(1)`.

Detalles a tener en cuenta:

- la disposición cambia después de las filas 2 y 20;
- en las filas 21–65 no hay asiento I.

## Soluciones optimizadas

La solución optimizada en C++ lee el asiento con `scanf("%d%c")` e
imprime con `puts` en lugar de usar `iostream` y `std::string`: 120 KB
en lugar de 348 KB. Las disposiciones son las mismas.

La solución optimizada en Java lee el asiento byte a byte, las cifras
dan la fila y el byte siguiente la letra, en lugar de leer una cadena:
0.109 s en lugar de 0.156 s y 380 KB en lugar de 1580 KB.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1893_implementation.cpp](1893_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 348 KB | 11291153 |
| [1893_implementation.go](1893_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1104 KB | 11291155 |
| [1893_implementation.java](1893_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1580 KB | 11291159 |
| [1893_implementation.py](1893_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 468 KB | 11291157 |
| [1893_implementation.rs](1893_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB | 11291163 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1893_implementation_optimized.cpp](1893_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 120 KB | 11303647 |
| [1893_implementation_optimized.java](1893_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 380 KB | 11303785 |
