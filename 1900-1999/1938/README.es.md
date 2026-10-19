# 1938. Un triángulo equilátero sobre tres rectas

[Timus 1938](https://acm.timus.ru/problem.aspx?space=1&num=1938) · difficulty 4554 · geometry

Original problem from Open Ural FU Championship 2012 | by Olga Soboleva.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elegir un punto sobre cada una de tres rectas infinitas distintas para
formar un triángulo equilátero. Se garantiza una respuesta adecuada.
Límites: 1 segundo, 64 MB.

## Entrada

Tres líneas con cuatro enteros x₁,y₁,x₂,y₂: dos puntos distintos de
cada recta. Las coordenadas pertenecen a [−1000,1000]; las rectas son
distintas por parejas. Pueden ser paralelas o concurrentes; los puntos
buscados pueden estar fuera de los segmentos que las definen.

## Salida

Tres pares, uno por línea: el punto i corresponde a la recta i.
Cada coordenada tiene valor absoluto de hasta 10⁸. La distancia a la
recta asignada es como máximo 10⁻⁶, toda separación entre puntos al
menos 10⁻⁶ y la diferencia entre lados mayor y menor hasta 10⁻⁶.
Todas las tolerancias son absolutas. Cualquier respuesta válida sirve.

## Evaluación

Un comprobador verifica las tres condiciones de arriba con las
tolerancias indicadas; se acepta cualquier triángulo así.

## Ejemplos

```
0 -1 1 0
0 -1 -1 0
0 -1 0 1
```

```
1 0
-1 0
0 1.7320508
```

```
3 1 4 1
-2 -1 -4 -1
-4 0 4 0
```

```
0 1
0 -1
1.7320508 0
```

## Solución

Sean Q+t·u y Z+s·v las rectas 2 y 3. Elegir A en la primera. Para una
rotación R de +60° o−60° se busca P₃−A=R(P₂−A). Rotar la segunda
recta alrededor de A da T=A+R(Q−A), D=Ru. Se intersecta con la tercera.
Con Δ=Z−T y det=cross(D,v), los parámetros son

t=cross(Δ,v)/det, s=cross(Δ,D)/det.

Devolver A,Q+t·u,Z+s·v. Los puntos pertenecen explícitamente a sus
rectas, y P₃−A=R(P₂−A) prueba lados iguales: una rotación de 60°
conserva longitud y su cuerda tiene la misma longitud.

Dos elecciones garantizan estabilidad. Primero elegir el extremo de
la primera recta con mayor |cross(u,extremo−Q)|, evaluado con enteros.
Ambas áreas no pueden ser cero porque las rectas 1 y 2 son distintas.
Así A queda fuera de la segunda. El área entera no nula es al menos 1,
por lo que |P₂−A|≥1/|u|≥1/(2000√2)>10⁻⁶ y no hay colapso.

Segundo, usar el mayor |cross(Ru,v)| entre las dos orientaciones.
Si θ es el ángulo de u a v, los determinantes normalizados son
sin(θ−60°),sin(θ+60°). Su media cuadrática es
¼sin²θ+¾cos²θ=¼+½cos²θ≥¼. El elegido tiene magnitud al menos
|u||v|/2, evitando intersecciones casi paralelas en toda configuración.

También se acotan las coordenadas. Con M=1000, las normas de los
anclajes de entrada son≤√2M; entonces |T|≤3√2M y |Δ|≤4√2M.
La cota del determinante da |t||u|≤2|Δ| y |s||v|≤2|Δ|. Ambos puntos
nuevos tienen norma≤9√2M<13000, muy por debajo de 10⁸. Estas escalas
mantienen pequeños los errores de doble precisión con tolerancia
absoluta. Se imprimen 15 decimales.

Tiempo y espacio O(1): siempre hay tres rectas y un número fijo de
operaciones aritméticas.

El primer extremo puede ser la intersección común y causar triángulo
nulo. Una sola orientación puede producir denominador casi cero y
coordenadas enormes. Respetar la asociación de puntos y rectas. Invertir
extremos no cambia validez. Las rectas continúan fuera de sus segmentos.

## Notas por lenguaje

El área para elegir extremo se calcula con enteros antes de convertir:
long long en C++, int64 en Go, long en Java, i64 en Rust y enteros
Python. Rotaciones y parámetros usan double/float64/f64. Java fija
Locale.US. Todos imprimen tres líneas de dos coordenadas y salto final.
No hace falta búsqueda numérica.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1938_geometry.cpp](1938_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 448 KB |
| [1938_geometry.go](1938_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1132 KB |
| [1938_geometry.java](1938_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 988 KB |
| [1938_geometry.py](1938_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 848 KB |
| [1938_geometry.rs](1938_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 280 KB |
