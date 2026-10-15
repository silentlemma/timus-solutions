# 1669. Palabra universal

[Timus 1669](https://acm.timus.ru/problem.aspx?space=1&num=1669) · dificultad 1390 · bitmask

Problema original de Ivan Burmistrov (preparado por Alex Samsonov), del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una palabra sobre las primeras N letras es universal si cada ordenación
de esas N letras, cada una usada una vez, es una subsecuencia suya. Hay
que decidir si la palabra dada es universal.

## Entrada

N (1 ≤ N ≤ 26) y luego una palabra de longitud L ≤ 300 con letras
minúsculas de entre las N primeras.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
abacaba
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
3
abcba
```

Salida:

```
NO
```

## Solución

Un orden fijo de letras es subsecuencia exactamente cuando, tomando cada
letra siguiente en su primera aparición tras la anterior, se logra
recorrer la palabra. Así que para un conjunto S de letras sea reach(S)
hasta dónde llega esta inserción voraz con el peor orden de S. El peor
orden termina con alguna letra c tras el peor orden de las demás:

reach(S) = máximo sobre c en S de after(c, reach(S \ {c})),

donde after(c, p) es la posición justo después de la primera c en p o
más adelante. La palabra es universal exactamente cuando reach de las N
letras no se sale de la palabra. Si algún conjunto falla, falla también
cualquier superconjunto suyo, porque un adversario puede empezar por él.

- Las máscaras en orden creciente listan cada subconjunto antes que sus
  superconjuntos, así que la tabla se llena de abajo arriba y solo crece
  lo necesario: la primera máscara que falla termina con `NO`.
- Antes, una cota rápida: se haya colocado lo que sea, las k letras
  restantes tienen k siguientes apariciones distintas, así que la más
  lejana avanza al menos k posiciones. Una palabra universal necesita
  entonces N + (N − 1) + … + 1 letras, y con N ≥ 25 siempre es `NO`.

Detalles a tener en cuenta:

- una tabla completa de 2²⁴ entradas de 16 bits ocupa 32 MiB;
  la tabla crece a medida que se recorren las máscaras;
- el zigzag a…q, p…a, b…q, … sobre 17 letras es universal en 273
  posiciones y hace contar los 2¹⁷ subconjuntos (prueba 06);
- una palabra universal en las primeras 17 letras aún puede carecer
  de la subsecuencia rb (prueba 08).

Las respuestas coinciden con una comprobación exhaustiva de todos los
órdenes en 500 entradas pequeñas aleatorias y con una implementación
aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1669_bitmask.cpp](1669_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(L + 2^N N) | AC | 0.015 s | 1196 KB |
| [1669_bitmask.go](1669_bitmask.go) | Go 1.14 x64 | bitmask | O(L + 2^N N) | AC | 0.031 s | 4180 KB |
| [1669_bitmask.java](1669_bitmask.java) | Java 1.8 | bitmask | O(L + 2^N N) | AC | 0.109 s | 1580 KB |
| [1669_bitmask.py](1669_bitmask.py) | Python 3.12 x64 | bitmask | O(L + 2^N N) | AC | 0.718 s | 6764 KB |
| [1669_bitmask.rs](1669_bitmask.rs) | Rust 1.75 x64 | bitmask | O(L + 2^N N) | AC | 0.046 s | 1268 KB |
