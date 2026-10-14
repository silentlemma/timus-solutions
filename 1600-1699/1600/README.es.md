# 1600. El aeropuerto

[Timus 1600](https://acm.timus.ru/problem.aspx?space=1&num=1600) · dificultad 552 · geometry

Problema original de Vladimir Yakovlev, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hasta 500 objetos vuelan en línea recta a velocidad constante en el
espacio; todos empiezan a más distancia entre sí que una distancia
crítica d. Hay que hallar el primer momento en que algún par se acerca a
distancia d, e imprimir `ALARM!` y luego el tiempo con tres decimales y
el par, u `OK` si eso nunca ocurre. Si en ese momento se acercan varios
pares, se puede imprimir cualquiera.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y d, y luego la posición y la velocidad de cada objeto, seis números.

## Salida

`OK`, o `ALARM!` y luego el tiempo y los números de los dos objetos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1.0
1.0 1.0 -1.0 0.0 0.0 10.0
0.0 0.0 4.0 2.0 0.0 0.0
```

Salida:

```
ALARM!
0.500 1 2
```

## Solución

Visto desde un objeto del par, el otro se mueve por la recta p + v·t,
donde p y v son las diferencias de posiciones y velocidades. Están a
distancia d cuando |p + v·t|² = d², una ecuación cuadrática:
(v·v)t² + 2(p·v)t + (p·p − d²) = 0. Con velocidades iguales o
discriminante negativo, el par nunca se acerca. Si no, la raíz menor es
el momento en que la distancia llega por primera vez a d; como todos los
pares empiezan separados, una raíz negativa significa que se alejan. El
momento más temprano entre todos los pares es la respuesta: `O(n²)`,
unos 125000 pares.

Las pruebas usan un verificador que acepta cualquier par que se acerque
en el momento correcto, con el redondeo a tres decimales. Los tiempos se
contrastaron con una bisección sobre la distancia antes del máximo
acercamiento.

Detalles a tener en cuenta:

- un par que solo toca la distancia d en su máximo acercamiento también
  da la alarma: el discriminante es entonces exactamente 0 (prueba 04);
- con una velocidad relativa diminuta el tiempo puede ser grande, casi
  10⁶ segundos en la prueba 07, así que no hay que acotarlo de antemano;
- con el semidiscriminante, b = p·v y b² − a·c, no hace falta arrastrar
  el factor 4.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1600_geometry.cpp](1600_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.015 s | 272 KB |
| [1600_geometry.go](1600_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.015 s | 1156 KB |
| [1600_geometry.java](1600_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.109 s | 1068 KB |
| [1600_geometry.py](1600_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.156 s | 928 KB |
| [1600_geometry.rs](1600_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.062 s | 328 KB |
