# 1672. Moscas droide

[Timus 1672](https://acm.timus.ru/problem.aspx?space=1&num=1672) · dificultad 8499 · geometry

Problema original de Dmitry Ivankov, del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N moscas flotan en puntos enteros distintos del espacio. Hay que hallar
un cubo que las contenga a todas con al menos una mosca en cada cara, e
imprimir tres vectores unitarios a lo largo de sus aristas. Ese cubo
siempre existe.

## Entrada

N (2 ≤ N ≤ 100) y luego las coordenadas de las moscas, enteros de valor
absoluto a lo sumo 100.

## Salida

Tres vectores unitarios a lo largo de las aristas del cubo, con la mayor
precisión posible.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
0 1 1
1 0 1
1 1 0
1 1 2
1 2 1
2 1 1
```

Salida:

```
1 0 0
0 1 0
0 0 1
```

### Ejemplo 2

Entrada:

```
2
1 0 0
-1 0 0
```

Salida:

```
0.577350269 0.211324865 -0.788675135
0.577350269 0.577350269 0.577350269
0.577350269 -0.788675135 0.211324865
```

Se acepta cualquier cubo válido.

## Solución

Para un vector unitario u, la anchura w(u) es la mayor menos la menor
proyección de una mosca sobre u. La caja mínima según un triedro
ortonormal e₁, e₂, e₃ toca moscas en sus seis caras. Es un cubo si y solo
si w(e₁) = w(e₂) = w(e₃).

Primero comprobar los ejes coordenados: sus anchuras enteras son exactas
y, si coinciden, el triedro ya da el cubo.

Para puntos colineales, incluido N = 2, w(u) = L·|cos|. Se construyen
directamente tres ejes que forman arccos(1/√3) con la recta. Si no:

1. Hallar la dirección del diámetro n_max. Para n_min usar la normal si
   los puntos son coplanarios, o la mejor de S = 1500 direcciones de la
   esfera, refinada con pequeños giros. Solo es una dirección inicial.
2. Mover el tercer eje por un círculo máximo de n_min a n_max. En cada
   posición, bisecar un cuarto de vuelta de los dos primeros ejes para
   igualar sus anchuras. Una bisección exterior intenta igualar la tercera.
   Comprobar el resultado: la raíz interior seleccionada puede saltar.
3. Si falla, usar un disco de cuaterniones con vértices de borde
   (1,0,0,0), (−1/2,1/2,1/2,1/2), (−1/2,−1/2,−1/2,−1/2) y centro
   (0,1/√2,−1/√2,0). Normalizar los cuaterniones interpolados y calcular
   F = (w(e₁) − w(e₃), w(e₂) − w(e₃)). En el borde los ejes se permutan
   cíclicamente: F tiene índice no nulo alrededor del origen, salvo que
   ya se haya encontrado un triedro válido.
4. Dividir el disco en tres triángulos, conservar uno con índice no nulo
   y subdividirlo en cuatro mediante puntos medios normalizados. El índice
   es aditivo, así que un hijo sigue encerrando un cero. Para recorrer una
   arista con seguridad, subdividirla hasta garantizar que una coordenada
   de F conserva su signo: su variación no supera 4D veces la cuerda de
   los cuaterniones, siendo D el diámetro. Entonces es válido el ángulo
   entre los extremos. La subdivisión también detecta ceros en aristas.
   Solo terminar cuando la diferencia de anchuras no supere 10⁻¹⁰D.

Con límites fijos para las bisecciones y búsquedas locales, el tiempo es
`O(N² + N(S + K))`, donde K cuenta las muestras adaptativas del índice.
Solo se guardan el triángulo actual y la pila recursiva de aristas, sin
una malla creciente. Cada resultado de la búsqueda se verifica; normalizar los
cuaterniones mantiene la ortogonalidad.

Detalles a tener en cuenta:

- los puntos colineales necesitan su triedro directo y los coplanarios
  dan una normal exacta (pruebas 02, 05, 06);
- las raíces pueden saltar, y refinar las mejores celdas o aplicar giros
  locales puede atascarse con residuo positivo (prueba 17); hay que
  conservar un índice no nulo, sin confiar en un mínimo numérico;
- los ángulos de los extremos pueden omitir una vuelta completa o un
  cero en la arista; la subdivisión necesita una cota de variación;
- el comprobador usa una tolerancia relativa de anchuras de 10⁻⁶ y
  acepta cualquier triedro ortonormal que la satisfaga.

Los 16 archivos de entrada y 9 casos del generador pasan el comprobador.
Otras 1000 entradas aleatorias pequeñas pasan la verificación independiente
con el oráculo constructivo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1672_geometry.cpp](1672_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2 + N(S + K)) | AC | 0.015 s | 244 KB |
| [1672_geometry.go](1672_geometry.go) | Go 1.14 x64 | geometry | O(N^2 + N(S + K)) | AC | 0.046 s | 1204 KB |
| [1672_geometry.java](1672_geometry.java) | Java 1.8 | geometry | O(N^2 + N(S + K)) | AC | 0.156 s | 4976 KB |
| [1672_geometry.py](1672_geometry.py) | Python 3.12 x64 | geometry | O(N^2 + N(S + K)) | AC | 1.125 s | 1816 KB |
| [1672_geometry.rs](1672_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2 + N(S + K)) | AC | 0.046 s | 280 KB |
