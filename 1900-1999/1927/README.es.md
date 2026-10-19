# 1927. Área común de dos franjas infinitas

[Timus 1927](https://acm.timus.ru/problem.aspx?space=1&num=1927) · difficulty 1062 · geometry

Original problem from Ural Regional School Programming Contest 2012 | by Artyom Averin.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de dos segmentos no nulos es una sección transversal perpendicular
de una franja infinita. La franja reúne todas las rectas perpendiculares al
segmento que pasan por sus puntos y se extienden en ambos sentidos.
Calcular el área común; imprimir −1 si es infinita. Límites: 1 segundo, 64 MB.

## Entrada

Dos líneas de cuatro enteros x1 y1 x2 y2: extremos de cada segmento.
Coordenadas entre −1000 y 1000 inclusive. Los extremos de cada segmento
son distintos y pueden aparecer en cualquier orden.

## Salida

Un área real, o −1 si es infinita. Franjas disjuntas o que solo se tocan
en una recta tienen área cero, aunque esa recta sea ilimitada.

## Evaluación

Un token numérico; error absoluto O relativo de como máximo 10^−6.

## Ejemplos

```
0 0 2 0
0 0 0 2
```

```
4
```

## Solución

Sean A,B y C,D los extremos; v=B−A y w=D−C son normales. La primera
franja contiene los puntos X con v·X entre v·A y v·B; la segunda usa
w·C y w·D. Ordenar los límites cuando haga falta.

Calcular el determinante entero Δ=vx wy−vy wx. Si Δ≠0, la transformación
lineal invertible X↦(v·X,w·X) convierte la intersección en un rectángulo
de lados v·(B−A)=|v|² y w·(D−C)=|w|². Multiplica áreas por |Δ|, por lo
que el área original es |v|²|w|²/|Δ|. Así queda probada la fórmula finita;
trasladar cualquiera de los segmentos no cambia su valor.

Si Δ=0, proyectar ambos segmentos sobre la misma normal v. Ordenar los
intervalos v·A,v·B y v·C,v·D. Sean L el mayor límite inferior y R el
menor superior. Si L<R, un ancho común positivo se prolonga infinitamente:
el área es infinita. Si L>R no hay intersección; si L=R solo queda una
recta, de área cero. Estos dos casos producen 0. Las posibilidades son
exhaustivas, lo que demuestra la corrección.

O(1) tiempo y espacio: siempre se leen ocho enteros.

Las franjas son completas, no rayos ni medias franjas. Comprobar paralelismo
exactamente, sin epsilon: determinante ±1 da un área enorme pero finita.
Una recta de contacto ilimitada tiene área cero. Proyectar los dos segmentos
con el MISMO vector, incluso al invertir extremos. Usar normas al cuadrado;
no hacen falta raíces cuadradas ni trigonometría.

## Notas por lenguaje

C++, Go, Java y Rust usan enteros con signo de 64 bits antes de multiplicar.
Cada componente vectorial tiene módulo ≤2000, cada norma al cuadrado
≤8 000 000 y su producto ≤64 000 000 000 000. El producto es menor que
2^46 y se representa exactamente en doble precisión. El determinante tiene
módulo ≤8 000 000 y, si no es cero, al menos 1. Predicados enteros, una
sola división flotante y diez decimales cumplen la tolerancia.
Python mantiene enteros exactos hasta dividir; Java imprime con Locale.US.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1927_geometry.cpp](1927_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 452 KB |
| [1927_geometry.go](1927_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1100 KB |
| [1927_geometry.java](1927_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1796 KB |
| [1927_geometry.py](1927_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 544 KB |
| [1927_geometry.rs](1927_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 256 KB |
