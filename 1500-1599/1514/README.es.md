# 1514. Parque nacional

[Timus 1514](https://acm.timus.ru/problem.aspx?space=1&num=1514) · dificultad 1753 · geometry

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N árboles (3 ≤ N ≤ 50000) están en puntos enteros con coordenadas de
valor absoluto hasta 10⁶; varios árboles pueden compartir un punto. Hay
que elegir tres árboles distintos cuyo triángulo tenga el menor
perímetro; un triángulo de área cero también cuenta. Se escribe el
perímetro con al menos cuatro cifras decimales y los números de los
tres árboles.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego las coordenadas de los N árboles.

## Salida

El menor perímetro y luego los números de los tres árboles en
cualquier orden. Se acepta cualquier terna óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
0 0
1 1
3 0
0 3
3 3
```

Salida:

```
6.6503
1 2 3
```

## Solución

Divide y vencerás, como para el par de puntos más cercano. Se ordenan
los árboles por x, se resuelven las mitades izquierda y derecha, y sea
d el mejor perímetro hasta ahora. Cada lado de un triángulo mide como
mucho la mitad de su perímetro, así que un triángulo mejor tiene sus
tres árboles a menos de d/2 entre sí. Por tanto, un triángulo mejor con
árboles a ambos lados de la línea divisoria está en la franja de ancho
d/2 a cada lado: se ordena la franja por y y, para cada árbol, se
prueban los pares de árboles por encima a menos de d/2 de altura,
reduciendo el límite cada vez que d mejora. El argumento de
empaquetado del par más cercano acota el número de esos árboles, así
que cada nivel cuesta una ordenación y el total es `O(N log² N)`. Los
trozos de hasta 8 árboles se comprueban terna a terna.

Detalles a tener en cuenta:

- tres árboles en un mismo punto dan perímetro 0 (prueba 03, gen7);
- los triángulos degenerados cuentan, así que árboles en una recta dan
  el doble de la distancia entre los extremos (pruebas 02, 06, gen2,
  gen3);
- cuando todos los árboles comparten x, cada árbol cae en cada franja
  y solo el límite en y mantiene el trabajo pequeño (gen2);
- 50000 árboles dan unas 2·10¹³ ternas, demasiadas para probarlas todas
  (gen1);
- puede haber muchas ternas empatadas, así que las pruebas usan un
  comprobador (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1514_geometry.cpp](1514_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log^2 N) | AC | 0.109 s | 1024 KB |
| [1514_geometry.go](1514_geometry.go) | Go 1.14 x64 | geometry | O(N log^2 N) | AC | 0.078 s | 6540 KB |
| [1514_geometry.java](1514_geometry.java) | Java 1.8 | geometry | O(N log^2 N) | AC | 0.515 s | 8444 KB |
| [1514_geometry.py](1514_geometry.py) | Python 3.12 x64 | geometry | O(N log^2 N) | AC | 0.890 s | 16368 KB |
| [1514_geometry.rs](1514_geometry.rs) | Rust 1.75 x64 | geometry | O(N log^2 N) | AC | 0.062 s | 3348 KB |
