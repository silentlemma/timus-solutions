# 1861. Cementerio en Deyja

[Timus 1861](https://acm.timus.ru/problem.aspx?space=1&num=1861) · dificultad 1004 · dp

Problema original de Mikhail Rubinchik, del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una inscripción de n caracteres está en parte borrada: un "?" marca una
letra que no se puede leer. Restaurando las letras borradas de la mejor
manera, ¿cuántas veces como mucho puede aparecer en la inscripción un
nombre dado de m letras? Las apariciones pueden solaparse, y las letras
de distinta caja son distintas.

## Entrada

La inscripción (letras y "?") y el nombre (letras), 1 ≤ m ≤ n ≤ 1000.

## Salida

El mayor número posible de apariciones.

## Ejemplos

### Ejemplo 1

Entrada:

```
R?la?dDefe?tedHi?Br?t?erArc?i??ld
Archibald
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
Arch?????rchibaldIronfist
Archibald
```

Salida:

```
1
```

## Solución

Se eligen las posiciones donde empiezan copias del nombre. Una copia
cabe en j cuando cada letra del nombre cae sobre la misma letra o sobre
un "?". Dos copias a distancia d < m se solapan y concuerdan
exactamente cuando d es un periodo del nombre, es decir, cuando el
nombre desplazado d coincide consigo mismo; las copias a distancia m o
más no se tocan.

Un conjunto de copias es coherente en cuanto cada copia concuerda con la
siguiente. Para tres copias j₁ < j₂ < j₃, toda posición común a la
primera y la tercera cae también dentro de la segunda, así que la
concordancia pasa por la cadena. De ahí una DP sobre la última copia:
best[j] es uno más que el mayor de best[k] con k ≤ j − m y de
best[j − d] para los periodos d del nombre. Los periodos salen de la
función de prefijos: son m − b para los bordes b del nombre. Con como
mucho m periodos y n − m + 1 posiciones la DP da como mucho
m(n − m) ≤ n²/4 pasos. La solución en Python halla las posiciones que
caben con un solo AND de máscaras de bits desplazadas, una por letra.
`O(n·m)`.

En el segundo ejemplo caben copias en las posiciones 0 y 8, pero 8 no es
un periodo de "Archibald", así que solo se puede escribir una de ellas.

Trampas:

- basta la coherencia de copias vecinas; no hace falta seguir las
  letras restauradas;
- un "?" puede ser cualquier letra, también una que no está en el
  nombre;
- "A" y "a" son letras distintas.

Las respuestas coinciden con probar todas las restauraciones en
cuatrocientas inscripciones cortas y con una implementación aceptada
independiente en las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1861_dp.cpp](1861_dp.cpp) | G++ 13.2 x64 | dp | O(n m) | AC | 0.015 s | 400 KB |
| [1861_dp.go](1861_dp.go) | Go 1.14 x64 | dp | O(n m) | AC | 0.031 s | 1112 KB |
| [1861_dp.java](1861_dp.java) | Java 1.8 | dp | O(n m) | AC | 0.125 s | 628 KB |
| [1861_dp.py](1861_dp.py) | Python 3.12 x64 | dp | O(n m) | AC | 0.109 s | 576 KB |
| [1861_dp.rs](1861_dp.rs) | Rust 1.75 x64 | dp | O(n m) | AC | 0.046 s | 240 KB |
