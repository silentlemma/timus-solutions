# 1095. Reordenar cifras para obtener un múltiplo de 7

[Timus 1095](https://acm.timus.ru/problem.aspx?space=1&num=1095) · dificultad 580 · number_theory

Problema original de Dmitry Filimonenkov, del USU Open Collegiate Programming Contest, marzo de 2001, Senior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de `N` enteros positivos (`1 ≤ N ≤ 10000`, de hasta 20 cifras)
contiene cada una de las cifras 1, 2, 3 y 4. Reordena las cifras de cada
número para que el resultado sea divisible entre 7, o imprime 0 si es
imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` números, uno por línea.

## Salida

Un múltiplo de 7 formado con las cifras de cada número, uno por línea.

## Evaluación

Se acepta cualquier reordenación adecuada. El comprobador verifica que
cada respuesta usa exactamente las cifras de su número, no empieza por 0
y es divisible entre 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1234
531234
```

Salida:

```
3241
531342
```

## Solución

Se saca del número un 1, un 2, un 3 y un 4. Se escriben primero las demás
cifras no nulas en cualquier orden, luego las cuatro cifras clave en
algún orden y al final todos los ceros. Los ceros del final multiplican
el número por una potencia de 10, lo que no cambia la divisibilidad
entre 7, y el número no puede empezar por cero. Para un principio con
resto `r` módulo 7, el número es `r · 10⁴ + p` módulo 7 para el orden `p`
de las cifras clave, y los 24 órdenes de 1, 2, 3, 4 dan los siete restos
módulo 7 (`1234 ≡ 2`, `1243 ≡ 4`, `1324 ≡ 1`, `2134 ≡ 6`, `2143 ≡ 1`,
`3124 ≡ 2`, `3241 ≡ 0`, `4123 ≡ 0`, `1342 ≡ 5`, …). Así que uno de ellos
siempre sirve, y 0 nunca es la respuesta. `O(N · L)` para `L` cifras.

Detalles a tener en cuenta:

- un número de 20 cifras no cabe en enteros de 64 bits, así que el resto
  se calcula cifra a cifra (Python usa directamente enteros grandes);
- los ceros del principio podrían quedar delante si el principio está
  vacío, por eso todos los ceros van al final;
- solo se saca una copia de cada cifra clave; las demás se quedan en el
  principio.

El comprobador verifica las cifras y la divisibilidad de cada respuesta
con enteros grandes.

## Notas por lenguaje

- C++ recorre los órdenes con `std::next_permutation`; Go, Java y Rust
  los construyen recursivamente; Python usa `itertools.permutations`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1095_number_theory.cpp](1095_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N·L) | AC | 0.031 s | 668 KB |
| [1095_number_theory.go](1095_number_theory.go) | Go 1.14 x64 | number_theory | O(N·L) | AC | 0.031 s | 4712 KB |
| [1095_number_theory.java](1095_number_theory.java) | Java 1.8 | number_theory | O(N·L) | AC | 0.140 s | 7436 KB |
| [1095_number_theory.py](1095_number_theory.py) | Python 3.12 x64 | number_theory | O(N·L) | AC | 0.171 s | 2740 KB |
| [1095_number_theory.rs](1095_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N·L) | AC | 0.046 s | 944 KB |
