# 1904. Reversing Absolute Folds

[Timus 1904](https://acm.timus.ru/problem.aspx?space=1&num=1904) · difficulty 478 · math, sorting

Original problem by Alexander Ipatov, from Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para una entrada real x, aplica k operaciones en orden, reemplazando el
valor actual y por |y−aᵢ|. Describe todas las entradas cuyo resultado final
es como máximo 1 mediante intervalos cerrados, ordenados y disjuntos,
con extremos enteros. x puede ser negativo. Límites: 1 segundo y 64 MB.

## Entrada

Primero k, con 1 ≤ k ≤ 10. Después k referencias enteras a₁,…,aₖ en
orden de procesamiento, con −1000 ≤ aᵢ ≤ 1000.

## Salida

El número de intervalos, seguido de un par l ≤ r por línea en orden
creciente. Se permiten puntos aislados; imprime 0 para el conjunto vacío.
Incluye los extremos cuyo valor final es exactamente 1.

## Evaluación

El modo `tokens` compara exactamente las componentes conexas ordenadas.
Los intervalos solapados o que comparten extremo se fusionan.

## Ejemplos

```
3
0 4 2
```

```
4
-7 -5
-3 -1
1 3
5 7
```

## Solución

Invierte las operaciones desde el rango final aceptado [0,1]. Si una
salida debe estar en [l,r], elimina el intervalo si r < 0; de lo contrario,
recorta l a max(l,0), pues un valor absoluto no es negativo.
La preimagen completa de `z = |y−a|` es

`[a−r, a−l] ∪ [a+l, a+r]`.

Genera ambas ramas para cada intervalo, ordena y fusiona intersecciones,
incluidos extremos compartidos. Repite para aₖ,aₖ₋₁,…,a₁. Cada salida
invertida es no negativa, por lo que ese recorte es necesario. Tras la
última inversión conserva las entradas originales negativas: no recortes
el conjunto final a valores no negativos.

El invariante afirma que la unión actual contiene exactamente los valores
que pasan el sufijo ya invertido. Las dos ramas reflejadas son todas las
soluciones de una restricción absoluta. Intersectar la salida con [0,∞)
solo elimina imposibles; ordenar y fusionar conserva la unión. Por inducción,
al invertir toda la cadena se obtienen exactamente las entradas buscadas.

Referencias y extremos iniciales son enteros. Trasladar, reflejar, recortar
en cero y unir mantiene extremos enteros. Toda entrada válida cumple
`|x| ≤ 1 + Σ|aᵢ| ≤ 10001`, por lo que bastan enteros de 32 bits con signo.

Cada paso como máximo duplica los intervalos. Hay a lo sumo `2^k`
candidatos; al ordenar cada nivel, el tiempo es `O(k·2^k)` y el espacio
`O(2^k)`. k ≤ 10 es pequeño. Una unión vacía permanece vacía.

En el ejemplo, invertir a₃=2 da [1,3]; invertir a₂=4 da [1,3] y [5,7].
Invertir a₁=0 añade sus reflejos negativos y produce los cuatro intervalos.

## Notas por lenguaje

Las cinco fuentes ordenan por extremo izquierdo y luego derecho. Python
usa CPython 3.12. Lee referencias con signo. Java solo modifica el extremo
derecho de un intervalo combinado recién construido.

Fusiona si el siguiente extremo izquierdo no supera el derecho anterior;
el dominio es real. Conserva puntos aislados. Una referencia negativa
puede impedir toda salida intermedia: [0,−2] no acepta nada y [2,−1]
solo acepta x=2.

Las respuestas coinciden con evaluar la cadena hacia delante en 4025
casos, 1725 de ellos con respuesta vacía y 915 con puntos aislados; las
pruebas más grandes tienen 512 intervalos separados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1904_math_sorting.cpp](1904_math_sorting.cpp) | G++ 13.2 x64 | math, sorting | O(k 2^k) | AC | 0.015 s | 436 KB |
| [1904_math_sorting.go](1904_math_sorting.go) | Go 1.14 x64 | math, sorting | O(k 2^k) | AC | 0.031 s | 1252 KB |
| [1904_math_sorting.java](1904_math_sorting.java) | Java 1.8 | math, sorting | O(k 2^k) | AC | 0.140 s | 2764 KB |
| [1904_math_sorting.py](1904_math_sorting.py) | Python 3.12 x64 | math, sorting | O(k 2^k) | AC | 0.093 s | 540 KB |
| [1904_math_sorting.rs](1904_math_sorting.rs) | Rust 1.75 x64 | math, sorting | O(k 2^k) | AC | 0.015 s | 260 KB |
