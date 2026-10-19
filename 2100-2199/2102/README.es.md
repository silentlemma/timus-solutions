# 2102. Exactamente veinte factores primos

[Timus 2102](https://acm.timus.ru/problem.aspx?space=1&num=2102) · dificultad 147 · number_theory

Problema original de Vladimir Leskov, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Decir si en la factorización de n los exponentes suman exactamente 20,
es decir, si n es producto de exactamente 20 primos contados con
multiplicidad. Los límites son 2 segundos y 64 MB.

## Entrada

n, 1 ≤ n ≤ 10¹⁸.

## Salida

`Yes` o `No`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
No
```

### Ejemplo 2

Entrada:

```
1048576
```

Salida:

```
Yes
```

### Ejemplo 3

Entrada:

```
10000000000
```

Salida:

```
Yes
```

## Solución

Se divide n entre cada d de 2 a B = 2·10⁶ mientras d² ≤ n, contando los
factores primos quitados. Si el bucle se detiene porque d² supera lo que
queda, el resto es 1 o un primo y aporta 0 o 1. Si no, el resto es al
menos B² = 4·10¹², así que la parte quitada es a lo sumo 10¹⁸ / B²,
menos de 2¹⁸, es decir, menos de 18 factores hasta ahora; el resto no
tiene factores menores que B y es a lo sumo 10¹⁸ < B³, así que aporta a
lo sumo dos. El total no puede llegar a 20, y la respuesta es No. El
trabajo es O(min(sqrt n, B)).

En el tercer ejemplo 10¹⁰ = 2¹⁰ · 5¹⁰ tiene 20 factores primos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2102_number_theory.cpp](2102_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 124 KB |
| [2102_number_theory.go](2102_number_theory.go) | Go 1.14 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.046 s | 1120 KB |
| [2102_number_theory.java](2102_number_theory.java) | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.156 s | 1636 KB |
| [2102_number_theory.py](2102_number_theory.py) | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.484 s | 428 KB |
| [2102_number_theory.rs](2102_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 232 KB |
