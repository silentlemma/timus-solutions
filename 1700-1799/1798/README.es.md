# 1798. Círculo de fuego. Versión 2

[Timus 1798](https://acm.timus.ru/problem.aspx?space=1&num=1798) · dificultad 2105 · geometry

Problema original de Alexander Ipatov; una versión del problema 1490 con un radio mayor.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un suelo está cubierto de losas de 1 × 1, y un círculo de fuego de
radio R tiene su centro en una esquina común de cuatro losas. Una losa
se daña si tiene al menos dos puntos en común con el círculo de fuego.
Contar las losas dañadas.

## Entrada

R, un entero de 1 a 10⁹.

## Salida

El número de losas dañadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
16
```

### Ejemplo 2

Entrada:

```
4
```

Salida:

```
60
```

## Solución

Como muestran los ejemplos, el fuego cubre todo el disco. En el primer
cuadrante, la losa [x, x + 1] × [y, y + 1] comparte más de un punto con
el disco exactamente cuando su esquina más cercana está estrictamente
dentro: x² + y² ≤ R² − 1 = n. Así que la respuesta es 4 veces el número
de puntos de red con x, y ≥ 0 en el disco x² + y² ≤ n.

Por simetría respecto a la diagonal basta sumar g(x) = ⌊√(n − x²)⌋ en
las columnas x = 0 … m, con m = ⌊√(n/2)⌋, ya que ahí la circunferencia
no es más empinada que 45°. Son unas 0,7·10⁹ columnas, demasiadas para
visitarlas. En su lugar se camina desde la columna m hacia la izquierda
por la envolvente convexa superior de los puntos de red del disco. A lo
largo de una arista (a, b) de la envolvente, a columnas a la izquierda
y b filas arriba con gcd(a, b) = 1, cada columna vale el suelo de la
recta de la arista, así que las a columnas suman de una vez
a·y + (a − 1)(b − 1)/2 + b. La arista siguiente se halla con una
búsqueda en el árbol de Stern–Brocot entre la última dirección que
salió del disco y otra que queda dentro. La búsqueda se detiene cuando,
desde un punto mediante exterior, los pasos en la dirección interior
suben al menos tan rápido como la circunferencia, pues entonces ningún
punto interior puede quedar entre ambas direcciones. La envolvente
tiene unos R^(2/3) vértices, así que para R = 10⁹ el recorrido da
alrededor de un millón de pasos. Después el primer cuadrante contiene
2·(Σ g(x) − m(m + 1)/2) + m + 1 puntos: la parte sobre la diagonal dos
veces y la diagonal una. `O(R^(2/3))`.

En el segundo ejemplo n = 15 y m = 2; las columnas 0, 1, 2 tienen
alturas 3, 3, 3, así que el cuadrante contiene 2·(9 − 3) + 3 = 15
puntos y la respuesta es 60.

Trampas:

- una losa que toca la circunferencia solo en una esquina no se daña,
  de ahí la desigualdad estricta y n = R² − 1;
- la respuesta ronda π·10¹⁸, cerca del límite de los enteros de 64 bits
  con signo;
- la prueba de pendiente multiplica números cercanos a 10¹⁸ por
  cuadrados de longitudes de aristas, lo que requiere 128 bits:
  __int128, i128, bits.Mul64, o en Java doubles con una comprobación
  exacta con BigInteger cuando ambos lados están cerca.

Para cada radio hasta 4000 la suma por columnas coincide con una suma
directa, y la versión en Go coincide con una implementación aceptada
independiente en todos los radios hasta 600 y en radios grandes hasta
10⁹, entre ellos múltiplos de hipotenusas pitagóricas. La solución en
Python corre en PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1798_geometry.cpp](1798_geometry.cpp) | G++ 13.2 x64 | geometry | O(R^(2/3)) | AC | 0.031 s | 928 KB |
| [1798_geometry.go](1798_geometry.go) | Go 1.14 x64 | geometry | O(R^(2/3)) | AC | 0.046 s | 2516 KB |
| [1798_geometry.java](1798_geometry.java) | Java 1.8 | geometry | O(R^(2/3)) | AC | 0.218 s | 2672 KB |
| [1798_geometry.py](1798_geometry.py) | PyPy 3.10 x64 | geometry | O(R^(2/3)) | AC | 0.312 s | 3536 KB |
| [1798_geometry.rs](1798_geometry.rs) | Rust 1.75 x64 | geometry | O(R^(2/3)) | AC | 0.031 s | 1060 KB |
