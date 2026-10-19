# 1981. Diagonales agrupadas por dirección

[Timus 1981](https://acm.timus.ru/problem.aspx?space=1&num=1981) · dificultad 444 · math, combinatorics

Problema original de Grigory Nazarov, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un polígono regular de `n` vértices, cuente las diagonales con al
menos otra diagonal paralela y, por separado, las que tienen al menos
una diagonal perpendicular. Una diagonal une vértices no adyacentes. Se
cuentan las diagonales que cumplen la condición; una misma diagonal
puede pertenecer a ambos resultados.

El tamaño entero cumple `4≤n≤100000`. Tiempo: 0,5 segundos; memoria: 64 MB.

## Entrada

Un entero `n`.

## Salida

Dos enteros: primero la cantidad para paralelismo y después para
perpendicularidad.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

Entrada:

```
4
```

Salida:

```
0 2
```

## Solución

Numere los vértices `0,…,n−1` alrededor de la circunferencia. La cuerda
entre `i,j` tiene dirección `π(i+j)/n+π/2`, módulo `π`. Por tanto, su
clase de dirección no orientada es `r=(i+j) mod n`.

Cuente primero las diagonales por clase. Si `n` es impar, entre las `n`
soluciones ordenadas de `i+j≡r` hay una con extremos repetidos. Quedan
`(n−1)/2` pares no ordenados distintos, de los cuales exactamente uno es
un lado. Cada clase contiene `d=(n−3)/2` diagonales. Si `d≥2`, las `n d`
diagonales tienen pareja paralela; en otro caso, ninguna.

Para `n` par, sea `h=n/2`. Hay `h` clases de cada paridad. Una clase par
tiene dos soluciones ordenadas con extremos repetidos y ningún lado,
dejando `h−1` diagonales. Una clase impar no tiene extremos repetidos,
pero incluye dos lados, dejando `h−2`. Cada tamaño `d` aporta `d` si
`d≥2`, y cero en otro caso. Sume los dos aportes y multiplique por `h`.
Los polígonos pequeños quedan cubiertos por esos mismos tamaños.

Las direcciones perpendiculares difieren en `n/2` clases. Esto es
imposible para `n` impar, cuyo segundo resultado es cero. Si `n` y `h`
son pares, la clase pareja conserva paridad y tiene el mismo tamaño
positivo. Si `h` es impar, entonces `h≥3` y ambos tamaños son positivos.
Así, toda diagonal de un polígono con `n` par tiene una perpendicular, y
el resultado es el total `n(n−3)/2`.

La identidad de direcciones asigna cada diagonal a exactamente una
clase. La condición sobre su tamaño equivale a disponer de otra diagonal
paralela; el desplazamiento de `n/2` caracteriza las parejas
perpendiculares. Esto demuestra ambos recuentos.

En el cuadrado del ejemplo, cada una de las dos direcciones contiene una
sola diagonal, por lo que ninguna tiene pareja paralela. Son
perpendiculares entre sí, dando `0 2`.

Tiempo `O(1)` y memoria adicional `O(1)`. Use aritmética de 64 bits: la
respuesta máxima `4 999 850 000` supera incluso un entero sin signo de
32 bits.

Trampas:

- Una clase de tamaño uno no aporta diagonales al resultado de paralelismo.
- Excluya lados y extremos repetidos al contar cuerdas.
- Las direcciones se toman módulo `π`; orientaciones opuestas pertenecen
  a la misma clase.
- Se cuentan diagonales, no pares no ordenados de diagonales.
- Promueva el tipo antes de multiplicar; los productos intermedios
  también superan 32 bits.

## Notas por lenguaje

Python usa enteros exactos. C++, Go y Java usan valores con signo de 64
bits en todas las fórmulas; Rust usa `u64`. Los programas enviados no
usan trigonometría.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1981_math.cpp](1981_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 440 KB |
| [1981_math.go](1981_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1100 KB |
| [1981_math.java](1981_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 448 KB |
| [1981_math.py](1981_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 460 KB |
| [1981_math.rs](1981_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB |
