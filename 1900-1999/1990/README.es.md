# 1990. El segmento horizontal más ancho que atraviesa un corredor

[Timus 1990](https://acm.timus.ru/problem.aspx?space=1&num=1990) · dificultad 1061 · geometry, sorting

Problema original de Denis Dublennykh, preparado por Egor Shchelkonogov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos polilíneas que no se cruzan ni se tocan delimitan un corredor por
izquierda y derecha. Sus alturas aumentan estrictamente; comparten las
alturas inicial y final. Un segmento horizontal parte de cualquier
posición válida inferior y debe llegar arriba mediante un camino
continuo. Puede trasladarse en cualquier dirección, conservando su
orientación horizontal y permaneciendo entre las paredes. Se permite
tocar las paredes.

Hay obstáculos puntuales, posiblemente fuera del corredor. Pueden tocar
los extremos del segmento, pero no pertenecer a su interior estricto.
Calcule la máxima anchura que admite un recorrido.

Cada pared tiene entre 2 y 100000 vértices; hay `0≤q≤100000` obstáculos.
Las coordenadas son enteras de valor absoluto como máximo `10⁹`. Los
obstáculos están ordenados por altura no decreciente; sus `x` dentro de
una altura son arbitrarias. Tiempo: 1 segundo; memoria: 64 MB.

## Entrada

El número `n` de vértices izquierdos y sus pares `x y`; luego `m` y los
vértices derechos; finalmente `q` y los obstáculos. Los vértices de cada
pared tienen `y` estrictamente creciente. En todo el intervalo común, la
pared izquierda permanece estrictamente a la izquierda de la derecha.

## Salida

Un real: la anchura máxima viable.

## Evaluación

Los números se comparan con error absoluto o relativo 10⁻⁶.

## Ejemplos

Entrada:

```
2
0 0
5 10
3
5 0
10 5
10 10
1
6 5
```

Salida:

```
4.0
```

A altura 5 las paredes están en 2.5 y 10. El obstáculo en 6 deja huecos
de 3.5 y 4. El resto del corredor tiene anchura al menos 5, por lo que
el óptimo es 4.

## Solución

Sean `L(y)<R(y)` las paredes. Sin obstáculos, la cota es
`C=min_y(R(y)−L(y))`. Entre alturas consecutivas de la unión de
vértices, ambas paredes son afines; su diferencia también y alcanza su
mínimo en un extremo. Evalúe todos los vértices izquierdos frente a la
pared derecha y viceversa. El índice de la arista opuesta solo avanza,
por lo que los dos barridos cuestan `O(n+m)`.

Para cada altura de obstáculos dentro del intervalo vertical, ordene las
`x`, descarte los puntos fuera de `[L(y),R(y)]` e incluya las paredes
como extremos. Sea `G(y)` el mayor hueco entre coordenadas consecutivas.
El segmento cabe en ese nivel exactamente cuando su anchura no supera
`G(y)`. Los duplicados añaden huecos cero; los puntos sobre una pared no
restringen más. Si no queda ningún punto interior, basta la restricción
de paredes ya incluida en `C`.

La respuesta es `min(C, min_y G(y))`. Los puntos de distintas alturas
carecen de extensión vertical y no forman por sí solos una barrera
continua; sus cotas se pueden tratar por separado. Procese un grupo por
altura y adelante dos cursores sobre las paredes.

### Suficiencia de las condiciones locales

Cualquier recorrido continuo de abajo arriba atraviesa cada altura
intermedia, aunque retroceda verticalmente. Por ello todas las cotas de
paredes y huecos son necesarias.

Para demostrar suficiencia, tome todas las alturas de vértices y
obstáculos. En cada evento elija una posición válida del segmento de
anchura `w`; su extremo izquierdo `a` cumple `L(y)≤a≤R(y)−w`. Entre
eventos consecutivos no hay obstáculos y ambas paredes son afines.
Interpole linealmente los extremos elegidos: las desigualdades se
conservan por combinación convexa en toda la franja. Se obtiene un
camino continuo creciente en altura. Las posiciones en los eventos ya
son seguras. Como se permite tocar paredes y extremos de obstáculos, las
igualdades y la anchura óptima también son viables.

### Interpolación estable

No interpole primero dos coordenadas flotantes grandes para restarlas
después. Frente al vértice `(x,y)` y la arista `(aₓ,aᵧ),(bₓ,bᵧ)`,
calcule en enteros el numerador `(aₓ−x)(bᵧ−y)+(bₓ−x)(y−aᵧ)` y divida al
final por `bᵧ−aᵧ`. Cambie el signo al evaluar vértices derechos contra
la pared izquierda.

En una altura de obstáculos represente cada pared por `N/D`, con
`N=aₓ(bᵧ−y)+bₓ(y−aᵧ)` y `D=bᵧ−aᵧ>0`. Compruebe pertenencia mediante
productos enteros. Los huecos extremos son `(x·D−N)/D` y `(N−x·D)/D`;
los interiores son enteros. Para el último vértice use denominador 1. La
cancelación ocurre antes de convertir a coma flotante.

Los pesos no negativos suman como máximo `2·10⁹`. El numerador de un
hueco tiene valor absoluto como máximo `4·10¹⁸`, y el de una coordenada
`2·10¹⁸`. Los productos y diferencias usados caben en enteros con signo
de 64 bits. No multiplique cruzadamente las fracciones de ambas paredes,
pues necesitaría otra cota. Convierta únicamente el hueco completo a
double e imprima 12 decimales.

## Notas por lenguaje

Con `k_y` puntos por altura, tiempo `O(n+m+q+Σ k_y log(k_y+1))`, a lo
sumo `O(n+m+q log(q+1))`. Las paredes y el mayor grupo de tamaño `K`
ocupan `O(n+m+K)`. No hace falta ordenar globalmente. Go y Rust retienen
además `I` bytes de entrada: memoria real `O(n+m+K+I)`. Las otras
versiones leen por flujo.

Java usa heapsort sobre un arreglo primitivo para garantizar `O(k log
k)`, entrada por búfer de bytes y productos `long`. C++, Go y Rust ya
usan 64 bits antes de multiplicar; Python tiene enteros exactos. Cero
obstáculos, puntos iniciales o finales, alturas externas y `x`
desordenadas se rigen por las mismas reglas. Una alternativa es buscar
binariamente la anchura comprobando intervalos viables, con barridos
repetidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1990_geometry.cpp](1990_geometry.cpp) | G++ 13.2 x64 | geometry | O(n+m+q log(q+1)) | AC | 0.109 s | 3164 KB |
| [1990_geometry.go](1990_geometry.go) | Go 1.14 x64 | geometry | O(n+m+q log(q+1)) | AC | 0.046 s | 20820 KB |
| [1990_geometry.java](1990_geometry.java) | Java 1.8 | geometry | O(n+m+q log(q+1)) | AC | 0.171 s | 8564 KB |
| [1990_geometry.py](1990_geometry.py) | Python 3.12 x64 | geometry | O(n+m+q log(q+1)) | AC | 0.625 s | 28596 KB |
| [1990_geometry.rs](1990_geometry.rs) | Rust 1.75 x64 | geometry | O(n+m+q log(q+1)) | AC | 0.031 s | 12468 KB |
