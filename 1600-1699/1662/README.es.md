# 1662. La cabra en el huerto 6

[Timus 1662](https://acm.timus.ru/problem.aspx?space=1&num=1662) · dificultad 4622 · geometry

Problema original de Alex Samsonov, del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un bancal de coles es un polígono convexo. Hay que clavar una estaca
fuera de él y atar a ella una cabra con una cuerda de longitud R y un
cabrito con una cuerda de longitud r, de modo que la cabra alcance todos
los puntos del bancal y el cabrito ningún punto interior. Hay que
imprimir un lugar para la estaca, redondeado a 10⁻⁶, o `No solution`.

## Entrada

N (3 ≤ N ≤ 50), luego los N vértices del polígono en orden, enteros de
valor absoluto a lo sumo 1000, y luego r y R (1 ≤ r < R ≤ 1000).

## Salida

Las coordenadas de la estaca, o `No solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
0 1
1 1
1 0
1 3
```

Salida:

```
0.500000 -1.000000
```

### Ejemplo 2

Entrada:

```
3
0 0
0 14
2 7
8 10
```

Salida:

```
No solution
```

Se acepta cualquier lugar válido; para el primer ejemplo esta solución
imprime otro.

## Solución

La cabra alcanza todo el bancal exactamente cuando alcanza cada vértice,
así que la estaca debe estar en A, la intersección de los discos de radio
R alrededor de los vértices. El cabrito no alcanza el interior
exactamente cuando la estaca está a al menos r del bancal, es decir,
fuera del interior de B, el bancal ensanchado en r (su borde son las
aristas desplazadas r hacia fuera unidas por arcos de radio r alrededor
de los vértices). Tanto A como B son convexos.

Si algún punto de A queda fuera del interior de B, también queda fuera
algún punto del borde de A: basta alejarse de B cruzando una recta que
separe el punto de él hasta salir de A. La parte del borde de A fuera de
B se compone de trozos, y cada trozo o es el borde entero o termina donde
el borde de A cruza el borde de B. Así que basta con probar:

- las esquinas de A, donde se cortan dos circunferencias de radio R;
- los puntos donde una circunferencia de radio R corta una arista
  desplazada r;
- los puntos donde una circunferencia de radio R corta una de radio r
  alrededor de un vértice.

Cada candidato se comprueba directamente, con una tolerancia de 10⁻⁷: a
lo sumo R de cada vértice, fuera del bancal y a al menos r de cada
arista. Se imprime el primero que pasa. `O(N³)`.

Detalles a tener en cuenta:

- la respuesta puede ser un único punto donde todo va justo, por ejemplo
  donde se cortan tres circunferencias de radio R (prueba 03), o a
  exactamente r de una arista y exactamente R de un vértice (prueba 04);
  una búsqueda que solo prueba las esquinas de A y los puntos medios de
  sus arcos se pierde los del segundo tipo;
- los vértices pueden ir en cualquier sentido, lo que decide qué lado de
  una arista es el exterior;
- el comprobador acepta cualquier lugar que cumpla las condiciones con
  margen 10⁻⁵.

En entradas aleatorias, y con el menor R entero que admite un lugar para
muchos polígonos, las respuestas coinciden con una implementación
aceptada independiente sobre si existe un lugar, salvo el caso exacto de
la prueba 04, donde el lugar hallado aquí se comprobó que es válido.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1662_geometry.cpp](1662_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^3) | AC | 0.015 s | 216 KB |
| [1662_geometry.go](1662_geometry.go) | Go 1.14 x64 | geometry | O(N^3) | AC | 0.015 s | 1128 KB |
| [1662_geometry.java](1662_geometry.java) | Java 1.8 | geometry | O(N^3) | AC | 0.140 s | 1120 KB |
| [1662_geometry.py](1662_geometry.py) | Python 3.12 x64 | geometry | O(N^3) | AC | 0.093 s | 852 KB |
| [1662_geometry.rs](1662_geometry.rs) | Rust 1.75 x64 | geometry | O(N^3) | AC | 0.031 s | 272 KB |
