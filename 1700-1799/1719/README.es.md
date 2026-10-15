# 1719. Mata al jefe Shaitán

[Timus 1719](https://acm.timus.ru/problem.aspx?space=1&num=1719) · dificultad 1444 · geometry

Problema original de Alexander Ipatov, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un jugador está en el origen y cuatro jefes en puntos dados, sin tres
en una recta. Un disparo recorre una recta entera en ambos sentidos y
mata a todos los jefes que hay en ella. Con solo dos disparos, hallar
el camino más corto que le permite matar a los cuatro.

## Entrada

Cuatro líneas con las coordenadas enteras de los jefes, de valor
absoluto hasta 10000.

## Salida

El camino más corto, con un error de a lo sumo 10⁻⁵.

## Ejemplos

### Ejemplo 1

Entrada:

```
-2 0
2 0
-2 4
2 4
```

Salida:

```
2.0000000000
```

## Solución

No hay tres jefes en una recta, así que cada disparo mata exactamente a
dos. Eso da tres maneras de repartir los jefes en las dos rectas L₁ y
L₂, y dos órdenes de disparo. El jugador camina hasta un punto P de L₁,
dispara a lo largo de ella, luego camina en línea recta hasta el punto
más cercano de L₂ y dispara de nuevo.

Sea P = A + t·u en L₁, con u la dirección unitaria. El camino es
entonces f(t) = √((t − t₀)² + h²) + |k·t + m|. Aquí t₀ es la
proyección del origen sobre L₁ y h su distancia a L₁. El segundo
término es la distancia de P a L₂: k = n·u para la normal unitaria n de
L₂, con |k| ≤ 1. Ambos términos son convexos, así que el mínimo está en
un quiebre o donde la pendiente se anula:

- t₀, cuando L₂ es paralela a L₁ (k = 0);
- el cruce de las rectas, t = −m/k, donde el segundo término se quiebra;
- t₀ ± k·h/√(1 − k²), donde la pendiente del primer término, que va de
  −1 a 1, cancela ±k.

Evaluar f en estos pocos puntos y tomar el menor da el mínimo exacto,
sin búsqueda. `O(1)`.

Trampas:

- el jugador puede estar sobre un jefe o empezar en una de las rectas:
  la respuesta puede ser 0 (test 02);
- con rectas perpendiculares |k| = 1, y basta comprobar el punto de
  intersección para hallar el mínimo;
- el disparo va en ambos sentidos de la recta, así que el jugador no
  necesita colocarse más allá de los jefes.

Las respuestas coinciden con una implementación aceptada independiente,
que usa búsqueda ternaria, en 900 casos aleatorios. Entre ellos hay
rectas casi paralelas lejos del origen.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1719_geometry.cpp](1719_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 204 KB |
| [1719_geometry.go](1719_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1136 KB |
| [1719_geometry.java](1719_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1808 KB |
| [1719_geometry.py](1719_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 720 KB |
| [1719_geometry.rs](1719_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 276 KB |
