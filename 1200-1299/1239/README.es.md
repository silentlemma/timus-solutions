# 1239. Un rayo a través del mayor número de esferas

[Timus 1239](https://acm.timus.ru/problem.aspx?space=1&num=1239) · dificultad 3112 · geometry

Problema original de Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2002–2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cañón en el origen dispara un rayo hacia el octante x, y, z ≥ 0. Hay
N fantasmas (0 ≤ N ≤ 100), bolas de centro entero (X, Y, Z),
1 ≤ X, Y, Z ≤ 10 000, y radio entero 1 ≤ R ≤ min(X, Y, Z); el rayo mata a
cada fantasma que toca, aunque sea en un solo punto. Hay que hallar
cuántos fantasmas puede matar un solo rayo, y cuáles.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego cada fantasma como `X Y Z R`.

## Salida

El número de fantasmas y luego sus números en cualquier orden.

## Evaluación

Puede haber varios grupos óptimos, así que el verificador acepta
cualquiera: la cantidad debe ser igual a la cantidad máxima, los números
distintos, y debe existir un rayo que toque a todos los fantasmas
listados. El verificador busca ese rayo con decimales de 50 cifras.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1200 1200 3900 300
160 160 820 60
```

Salida:

```
2
1 2
```

### Ejemplo 2

Entrada:

```
13
1200 1200 3900 300
160 160 820 60
100 10 10 10
10 100 10 10
10 10 100 10
10 10 10 10
50 50 50 10
100 100 75 20
100 75 100 20
75 100 100 20
3000 4000 7000 2600
100 1000 1000 50
1000 100 1000 100
```

Salida:

```
5
6 7 9 10 11
```

## Solución

Desde el cañón, un fantasma de centro C es un cono circular: un rayo en
la dirección d lo toca justo cuando `d·C ≥ L·|d|`, donde
`L = √(|C|² − R²)` es la longitud de una tangente desde el origen. En la
esfera de direcciones cada fantasma es un casquete, y se busca un punto
cubierto por el mayor número de casquetes.

Los casquetes que contienen un punto óptimo se cortan en una región
convexa. O esa región es un solo casquete, y entonces su centro está en
todos, o tiene una esquina donde los contornos de dos casquetes se cortan
o se tocan. Así que basta probar la dirección de cada centro y los puntos
donde se encuentran dos contornos, `O(N²)` candidatos, y contar los
casquetes que contienen cada uno. `O(N³)`.

Los contornos de los casquetes i y j se encuentran en los vectores
unitarios `d = (a·C_i + b·C_j ± c·C_i×C_j)` con `d·C_i = L_i` y
`d·C_j = L_j`. Con `g = C_i·C_j` y `det = |C_i|²|C_j|² − g²`,

```text
a·det = L_i|C_j|² − L_j·g,   b·det = L_j|C_i|² − L_i·g,   c² = Q / det²,
Q = det − L_i²|C_j|² − L_j²|C_i|² + 2g·L_i·L_j
```

Toda la dificultad es la precisión: el primer ejemplo solo funciona porque
los dos conos se tocan exactamente, y un toque basta. Por eso todo lo que
se puede decidir con enteros se decide así:

- el centro del casquete i está en el casquete k cuando
  `(C_i·C_k)² ≥ L_k²·|C_i|²`, todo entero;
- los contornos se encuentran cuando Q ≥ 0, donde Q es un entero más
  `2g·√(L_i²L_j²)`; su signo sale de comparar cuadrados con enteros de
  128 bits, así que un toque da exactamente Q = 0 y un solo punto;
- cuando Q, `a·det` y `b·det` son diferencias de números casi iguales, se
  calculan con el conjugado, `x − y = (x² − y²)/(x + y)`, con el
  numerador exacto.

Solo la última prueba, si un tercer casquete contiene el punto candidato,
usa una tolerancia, y sobre una cantidad cuyos términos son exactos hasta
unos 10⁻¹⁵, así que un 10⁻⁹ relativo es seguro.

Detalles a tener en cuenta:

- los conos iguales de fantasmas escalados, como `(1200, 1200, 3900, 300)`
  y `(2400, 2400, 7800, 600)`, dan det = 0 y ningún punto de la pareja,
  pero sus puntos con otros casquetes siguen contando a los dos
  (prueba 09);
- una copia un poco más estrecha debe fallar el punto de contacto
  (prueba 08);
- sin fantasmas la respuesta es 0 y una lista vacía.

Las respuestas se compararon con la misma búsqueda hecha con decimales de
80 cifras en 600 casos pequeños aleatorios, muchos formados por copias
escaladas y reflejadas.

## Notas por lenguaje

- C++ y Rust usan enteros de 128 bits para los signos exactos, Go
  `math/big` y Java `BigInteger`; los enteros de Python ya son exactos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1239_geometry.cpp](1239_geometry.cpp) | G++ 13.2 x64 | geometry | O(N³) | AC | 0.031 s | 252 KB |
| [1239_geometry.go](1239_geometry.go) | Go 1.14 x64 | geometry | O(N³) | AC | 0.031 s | 3908 KB |
| [1239_geometry.java](1239_geometry.java) | Java 1.8 | geometry | O(N³) | AC | 0.125 s | 3728 KB |
| [1239_geometry.py](1239_geometry.py) | Python 3.12 x64 | geometry | O(N³) | AC | 0.187 s | 1132 KB |
| [1239_geometry.rs](1239_geometry.rs) | Rust 1.75 x64 | geometry | O(N³) | AC | 0.015 s | 296 KB |
