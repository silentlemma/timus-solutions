# 1420. División compleja entera

[Timus 1420](https://acm.timus.ru/problem.aspx?space=1&num=1420) · dificultad 1771 · math

Problema original de Evgeny Krokhalev, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para complejos con partes enteras, una división de a entre b con resto
es cualquier par (q, r) de tales números con b·q + r = a y |r| < |b|.
Dados a y b (todas las partes como mucho 10⁶ en valor absoluto), hay
que contar los resultados posibles.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las partes real e imaginaria de a en la primera línea, las de b en la
segunda.

## Salida

El número de resultados.

## Ejemplos

### Ejemplo 1

Entrada:

```
12 0
0 5
```

Salida:

```
2
```

## Solución

El resto queda fijado por q, así que se cuentan los complejos enteros q
con |a − b·q| < |b|. Si b = 0 nada es más corto que 0 y la respuesta es
0. Si no, dividiendo entre |b| queda |a / b − q| < 1: q está en el disco
unidad abierto alrededor de a / b, así que es uno de los 3 × 3 puntos
alrededor de (⌊Re a/b⌋, ⌊Im a/b⌋), de los que como mucho cuatro caben.

Con a / b = (x + y·i) / |b|², donde x = Re a·Re b + Im a·Im b e
y = Im a·Re b − Re a·Im b, la división redondeando hacia abajo da el
centro exacto de la cuadrícula de candidatos. Cada candidato se prueba
como |a − b·q|² < |b|² en enteros de 64 bits (de precisión arbitraria en
Python): las partes del resto no pasan de unas pocas veces |b|, así que
nada desborda y no hace falta coma flotante. `O(1)`.

Detalles a tener en cuenta:

- la división entre cero no tiene ningún resultado (pruebas 04, 05);
- un cociente a distancia exactamente 1 no cuenta, así que un a / b
  entero da un solo resultado (pruebas 02, 07);
- la división debe redondear hacia menos infinito con partes negativas
  (pruebas 10, 11, 12).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1420_math.cpp](1420_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB |
| [1420_math.go](1420_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1080 KB |
| [1420_math.java](1420_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 1568 KB |
| [1420_math.py](1420_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 416 KB |
| [1420_math.rs](1420_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 216 KB |
