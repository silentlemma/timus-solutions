# 1672. Moscas droide

[Timus 1672](https://acm.timus.ru/problem.aspx?space=1&num=1672) · dificultad 10739 · geometry

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

Se acepta cualquier cubo válido; para el primer ejemplo esta solución
imprime otros vectores.

## Solución

Para un vector unitario u, la anchura w(u) es la mayor menos la menor
proyección de una mosca sobre u. La caja más pequeña con aristas según
un triedro ortogonal e₁, e₂, e₃ toca moscas en todas sus caras, y es un
cubo exactamente cuando w(e₁) = w(e₂) = w(e₃).

Las moscas en una recta (incluye N = 2) tienen w(u) = L·|cos|, así que
tres ejes a ángulo arccos(1/√3) de la recta dan un cubo; se escriben
directamente. Si no:

1. n_max es la dirección entre las dos moscas más alejadas, donde
   ninguna anchura es mayor. n_min es la dirección de anchura mínima: la
   normal de un enjambre plano o, si no, la mejor de 1500 direcciones
   repartidas por la esfera, pulida con pequeños giros.
2. Los triedros considerados tienen el tercer eje n(t) en el arco de
   círculo máximo de n_min (t = 0) a n_max (t = 1) y los dos primeros
   girados φ a su alrededor. Un cuarto de vuelta intercambia los dos
   primeros ejes, así que w(e₁) − w(e₂) cambia de signo en [0, π/2] y
   una bisección halla φ(t) con las dos primeras anchuras iguales.
3. En t = 0 la tercera anchura es la menor de todas y en t = 1 la mayor,
   así que una bisección en t para w(e₃) = w(e₁) da el cubo.

La raíz φ(t) no siempre es única, y entonces la bisección puede caer en
un salto. El resultado se comprueba y, si falla, se busca en todo el
cuadrado (t, φ): la curva de las dos primeras anchuras iguales lo cruza
de t = 0 a t = 1 y a lo largo de ella la tercera anchura va de la menor
a la mayor, así que dentro hay un cubo. Una rejilla de 80 × 80 de las
diferencias de anchura al cuadrado se refina alrededor de sus cuatro
mejores celdas con catorce rondas de rejillas locales 5 veces más finas.
Al final, pequeños giros del triedro sobre sus propios ejes dejan las
anchuras al nivel del error de redondeo. `O(N · (S + G²))` para S
direcciones en la esfera y una rejilla G × G.

Detalles a tener en cuenta:

- las moscas en una recta o en un plano dan la dirección más estrecha
  exacta, y la recta necesita su propio triedro (pruebas 02, 05, 06);
- las búsquedas locales paran tras un número fijo de pasadas, pues
  mejoras diminutas podrían alargarlas mucho;
- el comprobador acepta cualesquiera vectores unitarios ortogonales con
  anchuras iguales hasta 10⁻⁶.

En 474 enjambres generados (aleatorios, planos, en una recta, cerca de
una esfera, largos y finos) todas las respuestas pasan el comprobador;
uno de cada veinte, más o menos, necesitó buscar en el cuadrado.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1672_geometry.cpp](1672_geometry.cpp) | G++ 13.2 x64 | geometry | O(N (S + G^2)) | AC | 0.015 s | 408 KB |
| [1672_geometry.go](1672_geometry.go) | Go 1.14 x64 | geometry | O(N (S + G^2)) | AC | 0.078 s | 1828 KB |
| [1672_geometry.java](1672_geometry.java) | Java 1.8 | geometry | O(N (S + G^2)) | AC | 0.234 s | 6628 KB |
| [1672_geometry.py](1672_geometry.py) | Python 3.12 x64 | geometry | O(N (S + G^2)) | AC | 0.968 s | 2488 KB |
| [1672_geometry.rs](1672_geometry.rs) | Rust 1.75 x64 | geometry | O(N (S + G^2)) | AC | 0.031 s | 628 KB |
