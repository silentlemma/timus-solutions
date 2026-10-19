# 2098. Pagar en efectivo o pagar más por el seguro

[Timus 2098](https://acm.timus.ru/problem.aspx?space=1&num=2098) · dificultad 325 · math

Problema original de Denis Dublennykh, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tras un pequeño accidente un conductor puede pagar b rublos en efectivo,
o declararlo y dejar que pague el seguro. El seguro cuesta c ahora y
sube d cada año, así que los próximos k años cuestan c + d, c + 2d, …,
c + kd; tras un accidente declarado esos k pagos son un p por ciento
más caros. Decir qué opción es más barata (Insurance en caso de empate)
y por cuánto. Los límites son 1 segundo y 64 MB.

## Entrada

b (hasta 10⁵), después c y d (hasta 10⁴) y después k y p (hasta 100).

## Salida

`Cash` o `Insurance` y después el ahorro con error absoluto o relativo
de a lo sumo 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
10000
5000 1000
3 50
```

Salida:

```
Cash
500.00
```

### Ejemplo 2

Entrada:

```
15000
2500 1000
4 25
```

Salida:

```
Insurance
10000.00
```

## Solución

Las dos opciones pagan el seguro normal S = k·c + d·k(k + 1)/2 de los
próximos k años. El efectivo añade b y la declaración añade S·p/100.
Comparar 100·b con S·p mantiene todo en enteros (a lo sumo unos 5·10⁹),
y su diferencia dividida entre 100 es el ahorro, impreso de forma exacta
con dos decimales.

En el primer ejemplo S = 21000, así que declarar cuesta 10500 más y el
efectivo 10000 más: Cash, por 500.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2098_math.cpp](2098_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 136 KB |
| [2098_math.go](2098_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1080 KB |
| [2098_math.java](2098_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1744 KB |
| [2098_math.py](2098_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 424 KB |
| [2098_math.rs](2098_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 228 KB |
