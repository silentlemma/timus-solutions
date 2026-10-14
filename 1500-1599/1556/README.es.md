# 1556. Disparo múltiple en el nivel secreto de las vacas

[Timus 1556](https://acm.timus.ru/problem.aspx?space=1&num=1556) · dificultad 8030 · geometry

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Vasya está en un punto del plano entre N vacas (N ≤ 50000), discos de
un mismo radio R (0.4 ≤ R ≤ 2) que no se intersecan ni se tocan entre
sí y no contienen ni tocan a Vasya. Vasya elige una dirección principal y
dispara K flechas a la vez
(2 ≤ K ≤ 16); la flecha i (desde 0) vuela por un rayo con ángulo
Aᵢ = arctan(i/(K − 1) − 1/2) respecto a la dirección principal. Un rayo
que cruza o toca una vaca la alcanza. Tras cada impacto la flecha sigue
volando con probabilidad P % (0 ≤ P ≤ 100) y se detiene en caso
contrario, y tras el quinto impacto se detiene con seguridad. Hay que
hallar una dirección principal con el mayor número esperado de impactos
en total.

Límite de tiempo: 5 segundos. Límite de memoria: 64 MB.

## Entrada

N, K, P y R, luego las coordenadas de Vasya y luego las de los N centros
de las vacas; todas las coordenadas son reales de valor absoluto no mayor
que 25000.

## Salida

La línea `The best shot at (x;y) gives Vasya E average hits.`, donde
(x, y) es la dirección principal como vector unitario con al menos 10
decimales y E es la esperanza con 4 decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5 40 1.0
-2.0 1
0 2.0
3 2.0
4 -3
```

Salida:

```
The best shot at (0.8944271910;0.4472135955) gives Vasya 5.8000 average hits.
```

## Solución

Se traslada Vasya al origen. Un rayo con ángulo θ alcanza una vaca con
centro a distancia d en la dirección c exactamente cuando θ dista de c
como mucho asin(R/d), extremos incluidos. La flecha i vuela en φ + Aᵢ
para la dirección principal φ, así que alcanza la vaca cuando φ está en
el mismo intervalo girado hacia atrás en Aᵢ. Todos los impactos tienen la
misma probabilidad de seguir, así que solo importa el número m de vacas
en el rayo: la flecha suma 0 si m = 0 y, en otro caso,
1 + q + … + q^(min(m, 5) − 1) con q = P/100.

La suma sobre las flechas solo cambia en los 2NK extremos de estos
intervalos. Los extremos se ordenan una vez; cada flecha ve la misma
lista ordenada, solo que rotada, así que las K listas se mezclan en una
vuelta al círculo (con un montículo en Python y comparando las K cabezas
en los demás lenguajes), empezando por los intervalos que ya contienen
φ = 0. Cada ángulo de evento es un candidato en el que los intervalos que
entran ya cuentan y los que salen aún cuentan, y cada tramo abierto entre
eventos es un candidato con los contadores ya actualizados; en caso de
empate gana el punto medio del tramo, más seguro de imprimir que una
dirección tangente. Cada evento agrupa extremos a no más de 10⁻¹² del primero.

Las sumas se guardan como enteros en unidades de 1/100⁴, así que las
comparaciones son exactas. Un verificador acepta cualquier dirección cuya
puntuación
iguale la mejor esperanza con un margen de 10⁻⁴; los resultados se
contrastaron con un programa independiente.

Detalles a tener en cuenta:

- la fórmula de Aᵢ es una imagen en el enunciado original, y el ejemplo
  confirma arctan(i/(K − 1) − 1/2); los desplazamientos son simétricos,
  así que da igual hacia qué lado se midan;
- tocar cuenta, así que el mejor disparo puede ser una única dirección
  tangente: en el ejemplo 5.8 solo se alcanza ahí, con 4.4 y 4.8 a cada
  lado;
- los intervalos cerca de la dirección del eje x pasan por 2π
  (pruebas 02, 06);
- una flecha suma como mucho cinco impactos por muchas vacas que haya en
  el rayo (prueba 03), y con P = 0 cada flecha suma como mucho 1
  (prueba 04);
- una vaca en la esquina lejana del cuadrado mide solo unos 10⁻⁵ de
  ángulo (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1556_geometry.cpp](1556_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N + N K^2) | AC | 0.718 s | 2044 KB |
| [1556_geometry.go](1556_geometry.go) | Go 1.14 x64 | geometry | O(N log N + N K^2) | AC | 0.843 s | 5792 KB |
| [1556_geometry.java](1556_geometry.java) | Java 1.8 | geometry | O(N log N + N K^2) | AC | 0.484 s | 15164 KB |
| [1556_geometry.py](1556_geometry.py) | Python 3.12 x64 | geometry | O(N log N + N K log K) | AC | 3.671 s | 25528 KB |
| [1556_geometry.rs](1556_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N + N K^2) | AC | 0.281 s | 7480 KB |
