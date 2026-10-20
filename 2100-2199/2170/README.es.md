# 2170. Tiempo para mezclar zumo por parejas en bloques alineados de potencia de dos

[Timus 2170](https://acm.timus.ru/problem.aspx?space=1&num=2170) · dificultad 1404 · dp, prefix_sums

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

2ᴺ recipientes tienen un litro cada uno a temperaturas tᵢ. Una consulta
toma los 2ᵖ recipientes desde l y los mezcla por rondas, vertiendo cada
segundo recipiente en su vecino izquierdo; una pareja se vierte en cuanto
sus dos partes se han estabilizado. Mezclar volúmenes V₁, V₂ a t₁, t₂ da
t = (V₁t₁ + V₂t₂) / (V₁ + V₂) y tarda (|t − t₁| V₁ + |t − t₂| V₂)
segundos. Responder Q consultas así. Los límites son 3 segundos y
512 MB.

## Entrada

N y Q, 1 ≤ N ≤ 18, 1 ≤ Q ≤ 10⁵, las temperaturas, 0 ≤ tᵢ ≤ 10⁵, y luego
las consultas l, p con l + 2ᵖ − 1 ≤ 2ᴺ.

## Salida

El tiempo de cada consulta.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
1 2 3 4
2 1
1 2
```

Salida:

```
1.0
5.0
```

## Solución

Las mezclas siempre unen dos mitades de igual volumen V. Entonces t es su
media, y el tiempo es V |t₁ − t₂|, la diferencia absoluta de las
cantidades de calor V t₁ y V t₂, es decir, de las sumas de las
temperaturas originales de las dos mitades. Ambas mitades se terminan de
forma independiente, así que un bloque de tamaño 2ᵖ que empieza en l
tarda

T(l, p) = max(T(l, p − 1), T(l + 2ᵖ⁻¹, p − 1)) + |S(izquierda) − S(derecha)|,

con T(l, 0) = 0 y S de sumas prefijas. Las consultas pueden empezar en
cualquier sitio, así que la tabla se rellena para cada inicio y cada p:
N · 2ᴺ valores, unos 4.7 millones, cada uno en O(1). Los tiempos son
enteros, y cada consulta es una búsqueda en la tabla.

En el ejemplo el bloque 1 … 4 mezcla primero (1, 2) y (3, 4) en 1 segundo
cada uno, y luego las mitades con sumas 3 y 7 en 4 más, 5 en total.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2170_dp_prefix_sums.cpp](2170_dp_prefix_sums.cpp) | G++ 13.2 x64 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.125 s | 36892 KB |
| [2170_dp_prefix_sums.go](2170_dp_prefix_sums.go) | Go 1.14 x64 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.046 s | 50324 KB |
| [2170_dp_prefix_sums.java](2170_dp_prefix_sums.java) | Java 1.8 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.265 s | 44600 KB |
| [2170_dp_prefix_sums.py](2170_dp_prefix_sums.py) | PyPy 3.10 x64 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.421 s | 62776 KB |
| [2170_dp_prefix_sums.rs](2170_dp_prefix_sums.rs) | Rust 1.75 x64 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.062 s | 43200 KB |
