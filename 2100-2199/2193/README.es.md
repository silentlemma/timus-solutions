# 2193. La mejor rima: longitud del sufijo dividida a la mitad por cada diferencia

[Timus 2193](https://acm.timus.ru/problem.aspx?space=1&num=2193) · dificultad 1660 · strings

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos palabras riman en una longitud de sufijo L con la puntuación L / 2ᵏ,
donde k es el número de posiciones en que difieren sus últimas L letras,
y su rima es la mejor puntuación sobre todo L. Dadas N palabras y Q
consultas "u v c", hallar la rima de las palabras u y v tras cortar c
letras del final de ambas. Se aceptan respuestas con error 10⁻⁶. Los
límites son 3 segundos y 256 MB.

## Entrada

N y Q, 2 ≤ N ≤ 10⁵, 1 ≤ Q ≤ 10⁵, luego N palabras de letras minúsculas
de longitud total hasta 10⁶, y luego las Q consultas con
0 ≤ c < min(|s_u|, |s_v|).

## Salida

La puntuación de cada consulta.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 7
fate
cmake
stake
cfake
cmate
1 2 0
2 3 0
1 4 0
2 5 0
1 5 0
1 4 1
2 5 2
```

Salida:

```
1.5
3
2
2.5
3
1.5
3
```

## Solución

Se alinean las dos palabras por el final. Para un número fijo k de
diferencias conviene el sufijo más largo, así que los candidatos son las
longitudes justo antes de la (k + 1)-ésima diferencia contando desde el
corte, con puntuación L / 2ᵏ. La primera diferencia puede estar justo en
el corte, pero entonces k = 1 ya puntúa al menos 1/2, mientras que
k ≥ 18 puntúa menos de 10⁵ / 2¹⁸ < 1/2. Así cada consulta mira a lo
sumo 18 diferencias.

Las consultas se agrupan por su par de palabras, y cada par construye
una vez las posiciones de diferencia de sus finales alineados: los
lenguajes compilados comparan las letras directamente, y Python hace XOR
de las dos palabras leídas como enteros grandes y busca los bytes no
nulos. Luego una consulta salta de diferencia en diferencia desde su
corte y se detiene cuando ni toda la longitud restante dividida por la
siguiente potencia de dos puede superar la mejor puntuación. Números de
palabra iguales o finales idénticos dan de inmediato toda la longitud
restante.

Las puntuaciones se guardan exactas como múltiplos de 2⁻¹⁸ y se
imprimen como decimales exactos.

En el ejemplo "fate" y "cmake" terminan en "fate" y "make"; con una
diferencia el sufijo "ate" frente a "ake" da 3/2 = 1.5, la mejor.

Un par cuesta la longitud de su palabra más corta, en total a lo sumo
unas 2 · 10⁸ letras sobre todos los pares distintos, y una consulta
O(18).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2193_strings.cpp](2193_strings.cpp) | G++ 13.2 x64 | strings | O(L sqrt Q + 18 Q) | AC | 0.531 s | 5344 KB |
| [2193_strings.go](2193_strings.go) | Go 1.14 x64 | strings | O(L sqrt Q + 18 Q) | AC | 0.625 s | 15792 KB |
| [2193_strings.java](2193_strings.java) | Java 1.8 | strings | O(L sqrt Q + 18 Q) | AC | 0.734 s | 17408 KB |
| [2193_strings.py](2193_strings.py) | Python 3.12 x64 | strings | O(L sqrt Q + 18 Q) | AC | 2.187 s | 61240 KB |
| [2193_strings.rs](2193_strings.rs) | Rust 1.75 x64 | strings | O(L sqrt Q + 18 Q) | AC | 0.390 s | 15092 KB |
