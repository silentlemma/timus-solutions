# 2217. Llegar a un palíndromo ordenando subcadenas de una cadena binaria

[Timus 2217](https://acm.timus.ru/problem.aspx?space=1&num=2217) · dificultad 549 · prefix_sums

Problema original de Timofey Imaev, de la clasificatoria del Campeonato Regional de los Urales ICPC 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En una cadena binaria S de longitud N se puede ordenar en orden no
decreciente cualquier subcadena, tantas veces como se quiera. ¿Puede
convertirse en palíndromo? Los límites son 1 segundo y 256 MB.

## Entrada

N, 1 ≤ N ≤ 10⁵, y luego S.

## Salida

YES o NO.

## Ejemplos

### Ejemplo 1

Entrada:

```
12
010110110100
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
1
1
```

Salida:

```
YES
```

### Ejemplo 3

Entrada:

```
2
10
```

Salida:

```
NO
```

## Solución

Ordenar una subcadena solo mueve ceros a la izquierda, y se puede hacer
con un intercambio adyacente "10" → "01" cada vez. Así una cadena T con
las mismas cuentas es alcanzable exactamente cuando cada prefijo de T
tiene al menos tantos ceros como el mismo prefijo de S.

Un palíndromo tiene tantos ceros en sus primeros k caracteres como en
los últimos k. Para un palíndromo alcanzable P, los primeros k
caracteres de P tienen al menos tantos ceros como los de S, y los
últimos k como mucho tantos como los de S, porque los ceros solo salen
del final. Así para todo k hasta N / 2:

ceros en los últimos k caracteres de S ≥ ceros en los primeros k.

Además, con N par los ceros se emparejan, así que su número debe ser
par; con N impar el carácter central se encarga de la paridad. Estas dos
condiciones también bastan. Sean Z el total de ceros, m = floor(N / 2),
h = floor(Z / 2), y A(k), B(k) las cuentas de ceros en los primeros y
últimos k caracteres de S. Las condiciones implican A(k) ≤ h para
k ≤ m y B(m) ≥ h. Elegimos la primera mitad de P con
Q(k) = min(B(k), h) ceros en cada prefijo de longitud k. Esta cuenta
empieza en cero, aumenta como máximo uno por carácter y termina en h.
Reflejamos esta mitad y, si N es impar, usamos un cero en el centro
exactamente cuando Z es impar. Como A(k) ≤ Q(k) ≤ B(k), ambas mitades
cumplen las restricciones de alcanzabilidad y este palíndromo es alcanzable.

Un recorrido desde ambos extremos guarda la diferencia acumulada de las
dos cuentas de ceros y responde NO cuando se vuelve negativa.

Trampa (test 12): el emparejamiento por sí solo no garantiza que un
objetivo sea alcanzable. Para S = "1001", la respuesta es YES porque
S ya es un palíndromo, pero "0110", con los ceros lo más a la izquierda
que permite el emparejamiento, es inalcanzable: sus dos primeros
caracteres contienen menos ceros que los de S.

En el tercer ejemplo "10" tiene un cero, una cuenta impar con longitud
par, así que la respuesta es NO.

Esto cuesta O(N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2217_prefix_sums.cpp](2217_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 436 KB |
| [2217_prefix_sums.go](2217_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 1552 KB |
| [2217_prefix_sums.java](2217_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 996 KB |
| [2217_prefix_sums.py](2217_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.093 s | 388 KB |
| [2217_prefix_sums.rs](2217_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.031 s | 244 KB |
