# 1886. Viaje 2

[Timus 1886](https://acm.timus.ru/problem.aspx?space=1&num=1886) · dificultad 2046 · dp

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Denis está en el aeropuerto 1 en el instante 0 y debe llegar al
aeropuerto n. Cada vuelo sale de a hacia b en el instante t y dura f
minutos, pero con probabilidad p% llega d minutos tarde. Denis compra
cada billete solo tras aterrizar, hace los transbordos al instante y
elige los vuelos para llegar seguro a n con el menor tiempo esperado de
llegada. Hay que escribir ese tiempo esperado, o "Fail" si no puede
asegurar la llegada.

## Entrada

n y m (2 ≤ n ≤ 100 000, 1 ≤ m ≤ 100 000) y luego m vuelos a, b, t, f, p,
d (1 ≤ t, f, d ≤ 10⁹, 1 ≤ p ≤ 99).

## Salida

El tiempo esperado de llegada con error de como mucho 10⁻⁶, o "Fail".

## Ejemplos

### Ejemplo 1

Entrada:

```
4 5
1 4 10 10 90 20
1 2 5 5 50 5
2 4 15 10 50 5
2 3 1 14 10 1
3 4 15 1 50 1
```

Salida:

```
27.500
```

### Ejemplo 2

Entrada:

```
2 1
2 1 20 19 50 1
```

Salida:

```
Fail
```

## Solución

Sea E(a, T) la mejor llegada esperada para quien está en el aeropuerto
a en el instante T: E(n, T) = T, y si no, el mínimo sobre los vuelos que
salen de a en T o después de (1 − p)·E(b, t + f) + p·E(b, t + f + d).
Un vuelo con algún resultado que lleve al infinito no sirve, porque la
llegada debe ser segura. Las dos llegadas son posteriores a la salida,
así que los vuelos se tratan desde la salida más tardía hacia atrás.
Cuando se trata un vuelo, todos los vuelos a los que su pasajero podría
enlazar ya se conocen. Para cada aeropuerto se guardan sus vuelos
tratados en ese orden con un mínimo acumulado: E(a, T) es el mínimo
acumulado en el último vuelo que sale en T o después, hallado por
búsqueda binaria. La respuesta es E(1, 0). `O(m log m)`.

En el primer ejemplo el vuelo directo 1 → 4 da 0.1·20 + 0.9·40 = 38
minutos. Volar 1 → 2 aterriza a las 10 o a las 15, ambas a tiempo para
el vuelo 2 → 4 de las 15, que aterriza a las 25 o a las 30: 27.5
minutos.

Trampas:

- un vuelo solo vale si tanto la llegada puntual como la retrasada
  siguen llevando con seguridad al aeropuerto n;
- se puede tomar un vuelo que sale justo en el instante de llegada;
- los vuelos que salen del aeropuerto n no importan: Denis se detiene
  al llegar;
- los tiempos llegan a unos 3·10⁹ por vuelo, más que un entero de 32
  bits;
- la solución en Python guarda los vuelos en arreglos numéricos planos y
  omite las salidas inalcanzables y dominadas: 14 MB en el juez, donde
  una versión anterior con tuplas y listas ocupaba 65 MB en la prueba
  15.

Las respuestas coinciden con un cálculo por la definición en 3000
horarios pequeños aleatorios, y con una implementación aceptada
independiente en los grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1886_dp.cpp](1886_dp.cpp) | G++ 13.2 x64 | dp | O(m log m) | AC | 0.312 s | 12500 KB |
| [1886_dp.go](1886_dp.go) | Go 1.14 x64 | dp | O(m log m) | AC | 0.140 s | 15964 KB |
| [1886_dp.java](1886_dp.java) | Java 1.8 | dp | O(m log m) | AC | 0.234 s | 18828 KB |
| [1886_dp.py](1886_dp.py) | Python 3.12 x64 | dp | O(m log m) | AC | 0.546 s | 13932 KB |
| [1886_dp.rs](1886_dp.rs) | Rust 1.75 x64 | dp | O(m log m) | AC | 0.093 s | 24620 KB |
