# 2123. Formas de formar una masa con dos pesas de cada tipo de crecimiento rápido

[Timus 2123](https://acm.timus.ru/problem.aspx?space=1&num=2123) · dificultad 1040 · dp

Problema original de Alexey Danilyuk, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n tipos de pesas con masas a₁ … aₙ, cada tipo al menos el doble de
pesado que el anterior, y dos pesas de cada tipo. Contar las formas de
formar exactamente la masa W; dos formas difieren si difiere el número
de pesas de algún tipo. Los límites son 4 segundos y 256 MB.

## Entrada

n y W, 1 ≤ n ≤ 60, 0 ≤ W ≤ 4 · 10¹⁸, y luego a₁ … aₙ con 1 ≤ a₁,
2aᵢ ≤ aᵢ₊₁ y aₙ ≤ 10¹⁸.

## Salida

El número de formas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 100
2 5 10 21 49
```

Salida:

```
3
```

## Solución

Se escribe el número de pesas del tipo i como 1 + xᵢ con
xᵢ ∈ {−1, 0, 1}. Con S el total de las masas, una forma es una elección
de xᵢ con Σ xᵢ aᵢ = W − S. Cambiar todos los signos lleva las soluciones
de un valor a las de su opuesto, así que basta contar las
representaciones de r = |W − S| (y con W > 2S no hay ninguna).

Se va del tipo más pesado hacia abajo, guardando los restos alcanzables
con su número de formas. Antes de usar el tipo i, un resto r tiene que
cubrirse con los tipos 1 … i, así que r ≤ Sᵢ, la suma de a₁ … aᵢ. Elegir
xᵢ convierte r en r o en r − aᵢ, y por la misma simetría de signos
r − aᵢ puede sustituirse por |r − aᵢ|; r + aᵢ nunca es lo bastante
pequeño, porque los tipos más ligeros suman menos que aᵢ. Con estas
condiciones de crecimiento solo todos los xᵢ = 0 dan 0, así que un resto
0 es una forma y pasa directamente a la respuesta.

Los restos se guardan ordenados. Quedarse conserva el orden, r − aᵢ con
r > aᵢ también, y aᵢ − r con r ≤ aᵢ lo invierte, así que la lista
siguiente es una mezcla de tres flujos ordenados, sumando los restos
iguales. Cada tipo al menos divide por dos la cota de los restos y a lo
sumo duplica un número de formas, así que un resto y su cuenta caben
juntos en una palabra de 64 bits. El número de restos puede crecer como
los números de Fibonacci, pero está limitado por Sᵢ + 1 y cabe en los
límites.

En el ejemplo las tres formas son 2 · 5 + 2 · 10 + 21 + 49, 2 + 2 · 49
y 2 · 2 + 5 + 2 · 21 + 49.

## Notas por lenguaje

La solución en Python guarda los restos como bitsets por bloques de
masas, con los números de formas en planos de bits binarios, así que un
paso son unos pocos desplazamientos y máscaras y una suma bit a bit.
Cuando los tipos más ligeros forman una cadena exacta de duplicación
u, 2u, 4u, …, el número de formas de terminar con ellos es un recuento
hiperbinario, un término de la sucesión diatómica de Stern, que se
calcula directamente en lugar de desplegar la cadena.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2123_dp.cpp](2123_dp.cpp) | G++ 13.2 x64 | dp | O(n R), R the largest number of residuals | AC | 0.031 s | 564 KB |
| [2123_dp.go](2123_dp.go) | Go 1.14 x64 | dp | O(n R), R the largest number of residuals | AC | 0.046 s | 1292 KB |
| [2123_dp.java](2123_dp.java) | Java 1.8 | dp | O(n R), R the largest number of residuals | AC | 0.109 s | 620 KB |
| [2123_dp.py](2123_dp.py) | Python 3.12 x64 | dp | O(n R), R the largest number of residuals | AC | 0.078 s | 1304 KB |
| [2123_dp.rs](2123_dp.rs) | Rust 1.75 x64 | dp | O(n R), R the largest number of residuals | AC | 0.031 s | 360 KB |
