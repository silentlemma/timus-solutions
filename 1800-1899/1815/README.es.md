# 1815. Granja en San Andreas

[Timus 1815](https://acm.timus.ru/problem.aspx?space=1&num=1815) · dificultad 4204 · geometry

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan tres ciudades y el precio por kilómetro de una carretera desde
cada una. Poner una granja en cualquier punto del plano de modo que el
precio total de las tres carreteras rectas hasta ella, la suma
ponderada de distancias, sea mínimo, e imprimir ese precio con error
absoluto o relativo de como mucho 10⁻⁹. Hay hasta 10⁴ casos.

## Entrada

t (1 ≤ t ≤ 10⁴), luego para cada caso tres líneas con coordenadas de
ciudades (enteros de valor absoluto hasta 1000) y una línea con los
tres precios (de 1 a 1000).

## Salida

El menor precio total de cada caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0
1 0
0 1
1 1 1
-3 0
3 5
0 -1
7 9 8
```

Salida:

```
1.9318516526
81.1600672826
```

## Solución

Es el problema de Fermat–Torricelli ponderado, y la precisión pedida
descarta búsquedas iterativas, que se arrastran cerca de una ciudad.
Tiene respuesta exacta.

El coste es convexo. Una ciudad v es el mejor lugar cuando el tirón de
las demás, la suma de sus pesos por los vectores unitarios desde v hacia
ellas, no es más largo que el peso total que hay en v; las ciudades en
un mismo punto suman allí sus pesos.

Si ninguna ciudad cumple, el mejor punto M está dentro, donde los tres
vectores unitarios ponderados se anulan, y su coste tiene forma
cerrada. Se construye el punto Q al otro lado de BC respecto a A con
|BQ| : |CQ| : |BC| = w₃ : w₂ : w₁. La desigualdad de Ptolomeo para M,
B, Q, C da w₂|MB| + w₃|MC| ≥ w₁|MQ| para todo M, así que el coste es al
menos w₁(|MA| + |MQ|) ≥ w₁|AQ|. Como el óptimo está dentro, se da la
igualdad, y la respuesta es w₁|AQ|. Una tolerancia diminuta en la
prueba de ciudades evita dividir por cero justo en la frontera, donde
ambas fórmulas coinciden. `O(1)` por caso.

En el primer ejemplo todos los precios son 1 y todos los ángulos son
menores de 120°, así que la respuesta es el punto de Fermat clásico,
con distancia total (1 + √3)/√2 ≈ 1,93185.

Trampas:

- la iteración de Weiszfeld puede pararse en una ciudad si cae
  exactamente sobre ella, por ejemplo cuando las ciudades están en una
  recta y su centro es una de ellas;
- dos o tres ciudades pueden coincidir;
- los pesos no tienen por qué formar un triángulo; entonces gana
  directamente la ciudad de mayor peso.

Las respuestas coinciden con una búsqueda local fina desde el centro en
3000 casos aleatorios con ciudades coincidentes, alineadas y generales.
También coinciden con una implementación aceptada independiente en
todas partes, salvo en casos alineados en que su iteración empieza en
una ciudad y se queda allí.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1815_geometry.cpp](1815_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) per case | AC | 0.156 s | 168 KB |
| [1815_geometry.go](1815_geometry.go) | Go 1.14 x64 | geometry | O(1) per case | AC | 0.062 s | 1588 KB |
| [1815_geometry.java](1815_geometry.java) | Java 1.8 | geometry | O(1) per case | AC | 0.234 s | 6304 KB |
| [1815_geometry.py](1815_geometry.py) | Python 3.12 x64 | geometry | O(1) per case | AC | 0.265 s | 10052 KB |
| [1815_geometry.rs](1815_geometry.rs) | Rust 1.75 x64 | geometry | O(1) per case | AC | 0.015 s | 1304 KB |
