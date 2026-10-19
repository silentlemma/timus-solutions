# 1948. El primer retorno imposible

[Timus 1948](https://acm.timus.ru/problem.aspx?space=1&num=1948) · difficulty 1217 · math

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elegir un real x. En el segundo i+1, i=0,1,…, el desplazamiento con signo
en una recta es a(x+i)²+b(x+i)+c. Hallar el menor entero positivo k para
el cual ningún x real hace cero la suma de los primeros k desplazamientos.
Cada k permite un x distinto; no se prohíben retornos anteriores.
Límites: 1 segundo y 64 MB.

## Entrada

t, 1≤t≤1000, seguido de t ternas enteras a,b,c.
0<a<10⁹, |b|,|c|<10⁹; los límites absolutos son estrictos.

## Salida

Un k por terna. El enunciado exige `Infinity` si no existe o supera 10¹⁸.
Con los límites dados eso es imposible, como se demuestra abajo; todas
las respuestas son enteras.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
2
1 -2 1
1 1 -6
```

```
2
9
```

## Solución

La suma es una cuadrática en x con coeficiente principal ak>0. Completar
el cuadrado usando la media de los índices 0,…,k−1:

Σ_{i=0}^{k−1} f(x+i)
= ak·(x+(k−1)/2+b/(2a))²
+ k·(a(k²−1)/12+c−b²/(4a)).

Existe una raíz real exactamente cuando el mínimo es no positivo.
Por tanto es posible retornar si y solo si

k² ≤ 1 + 3b²/a² − 12c/a.

El lado derecho es fijo. Para evitar redondeos de coma flotante en
cuadrados exactos y productos enormes, calcular pisos enteros anidados:

s = floor(3b²/a) − 12c.

Si s<0, la cantidad real 3b²/a−12c pertenece a [s,s+1) y es negativa;
ni k=1 funciona y la respuesta es 1. En otro caso s≥0, y definimos

T = 1 + floor(s/a).

Para m entero y a entero positivo,
floor((z−m)/a)=floor((floor(z)−m)/a). Tomando z=3b²/a y m=12c resulta
T=floor(1+3b²/a²−12c/a). Un cuadrado entero cumple la desigualdad
original exactamente cuando k²≤T. La respuesta es floor(sqrt(T))+1,
también si T es un cuadrado perfecto.

Python usa raíz cuadrada entera exacta. Los otros lenguajes buscan
binariamente el primer k en [1,2000000000] con k²>T. El predicado es
monótono y el extremo derecho siempre lo cumple, por lo que se obtiene
el primer segundo imposible. El mínimo exacto y las equivalencias de
redondeo prueban el algoritmo.

O(t log U) tiempo, U=2000000000, con hasta 31 iteraciones por caso.
El núcleo aritmético usa O(1) espacio; guardar entrada o salida requiere
O(t). La raíz entera exacta de Python también satisface esta cota.

x es real, no entero. Fallar exige k²>T estrictamente; la igualdad aún
permite una raíz doble. El signo de b desaparece al elevar al cuadrado.
s<0 da respuesta 1. Evitar productos de 32 bits y no exigir un único x
que funcione simultáneamente para todos los tiempos.

## Notas por lenguaje

Usar enteros con signo de 64 bits para coeficientes, productos y límites.
3b²≤2999999994000000003, s≤3000000005999999991 y
T≤3000000005999999992. Los cuadrados de búsqueda no exceden
4000000000000000000<2⁶³−1. Comprobar s<0 antes de la segunda división
para que truncar coincida con floor; el primer numerador no es negativo.
No formar a²k² ni usar raíces flotantes. Los enteros e isqrt de Python son exactos.

Como a≥1, la cota real de k² no supera
1+3·999999999²+12·999999999=3000000005999999992<2000000000².
Siempre existe k≤2000000000<10¹⁸; no hace falta rama `Infinity`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1948_math.cpp](1948_math.cpp) | G++ 13.2 x64 | math | O(t log U) | AC | 0.015 s | 444 KB |
| [1948_math.go](1948_math.go) | Go 1.14 x64 | math | O(t log U) | AC | 0.031 s | 1156 KB |
| [1948_math.java](1948_math.java) | Java 1.8 | math | O(t log U) | AC | 0.078 s | 500 KB |
| [1948_math.py](1948_math.py) | Python 3.12 x64 | math | O(t log U) | AC | 0.078 s | 908 KB |
| [1948_math.rs](1948_math.rs) | Rust 1.75 x64 | math | O(t log U) | AC | 0.015 s | 284 KB |
