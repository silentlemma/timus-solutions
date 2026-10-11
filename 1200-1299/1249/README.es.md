# 1249. ¿Son rectángulos todas las zonas oscuras?

[Timus 1249](https://acm.timus.ru/problem.aspx?space=1&num=1249) · dificultad 220 · implementation

Problema original de Nikita Shamgunov y Leonid Volkov, del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da una imagen de N × M ceros y unos (N, M ≤ 3000). Hay que decidir si
cada zona conexa de unos (casillas unidas por un lado) es un rectángulo de
lados paralelos a los ejes.

Límite de tiempo: 2.5 segundos. Límite de memoria: 4 MB.

## Entrada

N y M, y luego N líneas de M dígitos separados por espacios.

## Salida

`Yes` o `No`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
0 1
1 1
```

Salida:

```
No
```

### Ejemplo 2

Entrada:

```
3 3
0 0 1
1 1 0
1 1 0
```

Salida:

```
Yes
```

## Solución

Una zona no es un rectángulo justo cuando tiene en algún sitio una
esquina interior, y una esquina interior es una ventana de 2 × 2 con
exactamente tres casillas oscuras. Al revés, si ninguna ventana tiene
tres casillas oscuras, cada zona es un rectángulo: recorriendo su borde
nunca se puede girar hacia dentro. Así que toda la comprobación es que
ninguna ventana de 2 × 2 tenga exactamente tres unos.

La verdadera restricción es la memoria: la imagen tiene hasta 9 millones
de casillas y el texto de entrada unos 18 MB, frente a un límite de 4 MB.
Una ventana solo necesita dos filas, así que el programa guarda la fila
anterior y la actual, lee la entrada como un flujo y se detiene en la
primera ventana mala. Tiempo `O(N·M)`, memoria `O(M)`.

Detalles a tener en cuenta:

- leer toda la entrada de golpe, o guardar la imagen, rompe el límite de
  4 MB;
- dos zonas que solo se tocan por una esquina están bien: esa ventana
  tiene dos casillas oscuras (el segundo ejemplo).

La regla se comparó con la búsqueda de cada zona y la comprobación de que
llena su caja envolvente, en 400 imágenes pequeñas aleatorias.

## Notas por lenguaje

- Python lee una línea cada vez, la convierte en un entero usado como
  conjunto de bits y encuentra una ventana mala con operaciones de bits:
  un número impar de bits a uno entre los cuatro, con al menos dos.
- Java y Rust leen la entrada byte a byte con un búfer pequeño.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1249_implementation.cpp](1249_implementation.cpp) | G++ 13.2 x64 | implementation | O(N·M) | AC | 0.531 s | 208 KB |
| [1249_implementation.go](1249_implementation.go) | Go 1.14 x64 | implementation | O(N·M) | AC | 0.093 s | 1096 KB |
| [1249_implementation.java](1249_implementation.java) | Java 1.8 | implementation | O(N·M) | AC | 0.156 s | 452 KB |
| [1249_implementation.py](1249_implementation.py) | Python 3.12 x64 | implementation | O(N·M) | AC | 0.218 s | 1532 KB |
| [1249_implementation.rs](1249_implementation.rs) | Rust 1.75 x64 | implementation | O(N·M) | AC | 0.031 s | 224 KB |
