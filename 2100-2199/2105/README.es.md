# 2105. Encuentros de dos ciclistas en sentidos opuestos

[Timus 2105](https://acm.timus.ru/problem.aspx?space=1&num=2105) · dificultad 206 · math

Problema original de Nikita Sivukhin, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos niños recorren un camino circular de longitud L en sentidos
opuestos con velocidades v_A y v_B, saliendo juntos, durante T segundos;
a veces uno de ellos se detiene un rato. Un encuentro es un momento en
que están en el mismo punto sin haberlo estado justo antes. Contar los
encuentros. Los límites son 1 segundo y 64 MB.

## Entrada

L ≤ 10⁹, T ≤ 10⁶, v_A, v_B ≤ 10³ y después n ≤ 10⁵ paradas: quién,
inicio y duración; las paradas de un mismo niño no se solapan.

## Salida

El número de encuentros.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 10 2 1
3
1 1 1
1 2 2
2 2 1
```

Salida:

```
2
```

## Solución

Yendo en sentidos opuestos, los dos están en el mismo punto exactamente
cuando la distancia recorrida entre ambos es múltiplo de L. Esa
distancia nunca decrece y empieza en 0, así que cada múltiplo kL con
k ≥ 1 hasta la distancia final se alcanza una vez y cuenta como un
encuentro, aunque los dos se queden quietos allí un rato; el comienzo
no cuenta. Las paradas de un niño no se solapan, así que cada uno rueda
T menos la suma de sus paradas, y la respuesta es
⌊(v_A · ride_A + v_B · ride_B) / L⌋, calculada en enteros de 64 bits.

En el ejemplo Alice rueda 7 segundos y Bob 9, juntos 2 · 7 + 9 = 23
metros en un camino de 10: dos encuentros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2105_math.cpp](2105_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 136 KB |
| [2105_math.go](2105_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.015 s | 1084 KB |
| [2105_math.java](2105_math.java) | Java 1.8 | math | O(n) | AC | 0.171 s | 472 KB |
| [2105_math.py](2105_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.062 s | 440 KB |
| [2105_math.rs](2105_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 216 KB |
