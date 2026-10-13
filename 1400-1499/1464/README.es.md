# 1464. Iluminación

[Timus 1464](https://acm.timus.ru/problem.aspx?space=1&num=1464) · dificultad 2749 · geometry

Problema original de Dmitry Ivankov (idea de Alexander Ipatov), del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una habitación es un polígono simple de N vértices (3 ≤ N ≤ 50000)
dados en sentido antihorario, con coordenadas de 0 a 1000 y como mucho
cuatro decimales. Una lámpara cuelga en un punto estrictamente interior.
Hay que hallar el área de la parte de la habitación que ilumina la
lámpara, es decir, el área visible desde ella, con al menos dos decimales.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

La lámpara, N y luego los N vértices.

## Salida

El área iluminada.

## Ejemplos

### Ejemplo 1

Entrada:

```
1.0 1.0
6
0 0
3 0
3 2
2 2
2 3
0 3
```

Salida:

```
8.00
```

## Solución

Se mira la habitación desde la lámpara. Se ordenan los vértices por
dirección y se juntan las direcciones iguales; como la lámpara está
dentro, direcciones consecutivas distan menos de media vuelta. Entre dos
direcciones consecutivas no se ve ningún vértice, así que en ese hueco
la región iluminada termina en una sola arista, la más cercana que lo
cruza, y el hueco aporta el triángulo entre la lámpara y esa arista,
cortado por los dos rayos.

Una arista, vista desde la lámpara, cubre una serie de huecos
consecutivos (una arista vista de canto no cubre ninguno ni tapa nada).
Los huecos se ponen en un árbol de segmentos y cada arista se añade a
los O(log N) nodos que forman su serie. Cada nodo guarda solo la más
cercana de sus aristas: dos aristas que cubren los mismos huecos nunca se
cruzan, así que una comparación a lo largo de un rayo por el primer
hueco del nodo decide para todos sus huecos. La arista más cercana de
cada hueco está entonces entre los nodos de su camino a la raíz.
`O(N log N)`.

Todas las coordenadas se leen exactas como enteros en unidades de
10⁻⁴, así que la unión de direcciones y la orientación de las aristas se
deciden sin redondeo; la coma flotante se usa para ángulos,
intersecciones con rayos y áreas.

Detalles a tener en cuenta:

- vértices alineados con la lámpara y aristas que apuntan directo a
  ella (pruebas 07, 13, gen3);
- entrantes profundos y peines con regiones parcialmente ocultas (pruebas 04, gen2);
- recorrer todas las aristas para cada hueco es demasiado lento para
  50000 vértices.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1464_geometry.cpp](1464_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.109 s | 6232 KB |
| [1464_geometry.go](1464_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.140 s | 13688 KB |
| [1464_geometry.java](1464_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.250 s | 9068 KB |
| [1464_geometry.py](1464_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 1.531 s | 38272 KB |
| [1464_geometry.rs](1464_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 9092 KB |
