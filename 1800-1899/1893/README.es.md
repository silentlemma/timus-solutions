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

El último carácter es la letra; los dígitos anteriores forman el
número de fila. Elegir uno de los tres intervalos y usar esta tabla:

| Filas | `window` | `aisle` | `neither` |
| --- | --- | --- | --- |
| 1–2 | A D | B C | ninguno |
| 3–20 | A F | B C D E | ninguno |
| 21–65 | A K | C D G H | B E F J |

Los conjuntos se deducen de los extremos de cada fila y de los vecinos
de cada pasillo. En las filas 1–2, A y D están tanto junto a una ventana
como junto a un pasillo; la prioridad de ventana produce la tabla.
Así, cada letra válida recibe la clasificación requerida.

El número de comprobaciones y el tamaño de la entrada están acotados
por constantes, así que el tiempo y la memoria adicional son `O(1)`.

En los ejemplos, la fila 3 tiene un pasillo entre B y C, por lo que
`3C` es `aisle`. El asiento `64A` está junto a la ventana izquierda.
`21F` está en el interior del bloque central entre los pasillos y no
toca ninguno, por lo que es `neither`.

Trampas:

- la distribución cambia entre las filas 2/3 y 20/21;
- la letra de la ventana derecha cambia de D a F y después a K;
- no hay asiento I en las filas 21–65;
- comprobar las ventanas antes que los pasillos, sobre todo A y D en filas 1–2.

Las respuestas coinciden con un modelo aparte de la distribución de la
cabina en los 566 asientos válidos.

## Notas por lenguaje

Las cinco versiones interpretan como fila los dígitos anteriores a la
última letra ASCII y usan la misma clasificación de tamaño fijo. Go y
Rust pueden indexar por bytes: la entrada válida solo contiene dígitos
decimales y una letra inglesa mayúscula.

Java lee este único token corto con `Scanner`. No hacen falta una rutina
especial de entrada rápida ni enteros grandes; las búsquedas de pertenencia
solo recorren los conjuntos fijos de letras de asiento.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1893_implementation.cpp](1893_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 348 KB |
| [1893_implementation.go](1893_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1104 KB |
| [1893_implementation.java](1893_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1580 KB |
| [1893_implementation.py](1893_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 468 KB |
| [1893_implementation.rs](1893_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB |
