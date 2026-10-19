# 1950. Área atravesada por un canal finito

[Timus 1950](https://acm.timus.ru/problem.aspx?space=1&num=1950) · difficulty 2085 · geometry

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Partir del triángulo A=(0,0), B=(10,0), C=(10,10) y del canal finito AF,
con F=(x,y) estrictamente interior. Trazar la altura a la hipotenusa para
dividir el triángulo rectángulo isósceles en dos mitades congruentes.
La mitad sin F queda como parcela final y se repite en la que contiene F.
Si F está en la altura nueva, parar y dejar ambas mitades como finales;
en otro caso los tamaños pueden disminuir indefinidamente.

Una parcela sirve si su frontera tiene exactamente dos puntos distintos
en común con AF. Sumar las áreas útiles, despreciando un resto suficientemente
pequeño si hace falta. Límites: 1 segundo y 64 MB.

## Entrada

Coordenadas decimales reales x,y, con hasta tres cifras decimales y
0<y<x<10 estrictamente.

## Salida

Un área total con error absoluto o relativo no mayor que 10⁻³.

## Evaluación

La respuesta se compara con error absoluto o relativo 10⁻³.

## Ejemplos

```
8.125 4.375
```

```
29.6875
```

## Solución

Representar el triángulo por el ángulo recto R y los extremos P,Q de la
hipotenusa. Al inicio R=B, P=A, Q=C y área=50. El pie de la altura es
H=(P+Q)/2. Todas las aristas y alturas son horizontales, verticales o de
pendiente ±1; AF tiene pendiente estrictamente entre 0 y 1. Nunca coincide
con una arista. La mitad descartada no contiene extremos de AF en su
interior: atravesarla produce dos puntos de frontera, tocar un vértice no.

Tomar n=(sign(H_y−R_y),−sign(H_x−R_x)) y definir
v(T)=n·(T−R), w(T)=x·T_y−y·T_x. La mitad descartada sirve exactamente
cuando w(R),w(H) tienen signos estrictamente opuestos, y v(A),v(F)
tienen signos opuestos o v(F)=0. La primera condición sitúa el cruce en
el interior de RH, sin sus extremos; la segunda lo restringe al segmento
finito AF, permitiendo F. Usar el rayo incluiría parcelas más allá de F.

Sumar media área cuando se cumplan las condiciones. Si v(F)=0, terminar:
F estaba dentro del padre, así que está dentro de la altura; una mitad
contiene el canal entrante y la otra solo toca F. Cuenta exactamente una.
En otro caso, comparar v(F),v(P): con igual signo conservar (H,P,R),
con distinto signo (H,R,Q), cuyo primer vértice es el nuevo ángulo recto.
Dividir el área entre dos y continuar.

Prueba por inducción: el triángulo actual convexo contiene la parte final
de AF hasta F. Su mitad descartada contiene canal interior exactamente
cuando esa parte cruza internamente la altura, expresado por los dos
tests de signos. Solo esa mitad queda final en este paso; las contribuciones
de la conservada se resuelven después. La regla de parada exacta trata
ambas mitades, contando una vez cada parcela útil.

Leer milésimas enteras fx,fy y multiplicar las coordenadas geométricas por
S=2³⁰. Inicialmente R=(10000S,0), P=(0,0), Q=(10000S,10000S), F=(fxS,fyS).
Hacer hasta 30 cortes. Tras d puntos medios, los vértices siguen siendo
múltiplos de 10000·2^(30−d), así que puntos y signos son enteros exactos.
Para w usar fx,fy originales, no F escalado.

Coordenadas ≤10737418240000, componentes normales −1,0,1 y expresiones
del rayo de valor absoluto <2.15·10¹⁷: todo cabe en enteros con signo de
64 bits. Comparar signos directamente; multiplicar valores de lado o hacer
un producto cruzado general de puntos escalados podría desbordar.

Las áreas parciales son fracciones binarias exactas. Tras 30 cortes queda
como máximo 50/2³⁰≈4.657·10⁻⁸, cota de toda contribución omitida. Diez
decimales añaden hasta 5·10⁻¹¹. Para 30 pasos, tiempo y espacio O(1);
con precisión ε como parámetro, tiempo O(log(1/ε)) y espacio O(1).

El canal es finito. Tocar un extremo de la altura no aporta área descartada,
pero F sobre ella sí es un extremo de frontera. El nuevo ángulo está en H.
No usar epsilon para lados, multiplicar valores de signos ni afirmar que
la truncación de un proceso infinito da una suma total exacta.

## Notas por lenguaje

C++, Go, Java y Rust usan coordenadas y productos enteros con signo de
64 bits; Python usa enteros. Solo áreas y salida usan coma flotante.
Completar la parte decimal a tres cifras evita decisiones por redondeo
binario de entrada. El operando izquierdo del desplazamiento debe ser de 64 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1950_geometry.cpp](1950_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 432 KB |
| [1950_geometry.go](1950_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1164 KB |
| [1950_geometry.java](1950_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1080 KB |
| [1950_geometry.py](1950_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 728 KB |
| [1950_geometry.rs](1950_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 268 KB |
