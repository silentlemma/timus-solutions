# 2223. Cuántas llamadas hace una suma con XOR y acarreo

[Timus 2223](https://acm.timus.ru/problem.aspx?space=1&num=2223) · dificultad 936 · bitmask

Problema original de Vadim Barinov, del Campeonato de los Urales 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La función recursiva f(x, y) devuelve x cuando y = 0 y si no llama a
f(x xor y, (x and y) << 1), con enteros sin límite. Para X e Y
positivos dados en binario con hasta 10⁶ dígitos, imprimir el número de
llamadas que hace f(X, Y), o "infinity". Los límites son 1 segundo y
256 MB.

## Entrada

X e Y en binario, 1 ≤ X, Y < 2^1000000.

## Salida

El número de llamadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
1011
100
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
101
1
```

Salida:

```
3
```

## Solución

Es una suma por propagación repetida del acarreo: x xor y es la suma
sin acarreos y (x and y) << 1 es el acarreo. La suma x + y nunca cambia
y ambos argumentos siguen siendo no negativos, así que la recursión
siempre termina, y "infinity" nunca ocurre con estas entradas.

Un acarreo nace en un bit donde ambos números tienen un 1, y cada
llamada siguiente lo sube un bit, mientras el bit de arriba sea 1 en
exactamente uno de los números. Se detiene en el primer bit igual en
ambos: dos ceros lo absorben, y dos unos son donde nace otro acarreo.
Así el número de rondas con acarreo no nulo es la longitud de la cadena
más larga formada por un 1 común seguido de una racha de bits distintos
por encima, contando el bit común.

Un recorrido desde el bit más alto guarda la longitud de la racha actual
de bits distintos; en cada 1 común cierra una cadena de esa longitud más
uno, y cada bit igual reinicia la racha. La respuesta es la cadena más
larga más 2, por la primera llamada y por la última con y = 0.

En el segundo ejemplo 101 + 1 tiene un 1 común en el bit más bajo y el
bit de encima es 0 en ambos, así que la cadena tiene longitud 1 y hay
3 llamadas.

Esto cuesta O(L) para L dígitos binarios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2223_bitmask.cpp](2223_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(L) | AC | 0.015 s | 3580 KB |
| [2223_bitmask.go](2223_bitmask.go) | Go 1.14 x64 | bitmask | O(L) | AC | 0.093 s | 8124 KB |
| [2223_bitmask.java](2223_bitmask.java) | Java 1.8 | bitmask | O(L) | AC | 0.203 s | 11272 KB |
| [2223_bitmask.py](2223_bitmask.py) | Python 3.12 x64 | bitmask | O(L) | AC | 0.171 s | 5580 KB |
| [2223_bitmask.rs](2223_bitmask.rs) | Rust 1.75 x64 | bitmask | O(L) | AC | 0.046 s | 2960 KB |
